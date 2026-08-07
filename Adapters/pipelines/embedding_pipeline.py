# %% [setup]
# embedding_pipeline.py
# Generates embeddings for the unified dataset from multiple models.
#
# Zero-downtime design:
#   - Each batch is written atomically to its own Parquet shard (os.replace)
#   - A per-model checkpoint.json tracks completed batch indices
#   - On restart: sorted df order is stable → same batch indices → checkpoint skip
#   - SIGINT / SIGTERM: current batch completes, then exits cleanly
#   - API retries: exponential backoff + jitter, respects Retry-After on 429
#
# Output layout:
#   AI/data/embeddings/{model_key}/batches/batch_{i:09d}.parquet  ← shards
#   AI/data/embeddings/{model_key}.parquet                         ← merged model file
#   AI/data/embeddings/embeddings.parquet                          ← final wide table
#   AI/data/embeddings/{model_key}_checkpoint.json                 ← resume state
#
# .env:
#   OPENROUTER_API_KEY=sk-or-v1-...

import json
import logging
import os
import random
import re
import signal
import time
from pathlib import Path

import httpx
import numpy as np
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from dotenv import load_dotenv
from fastembed import TextEmbedding

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger(__name__)

BASE = Path(__file__).parent.parent  # AI/
DATA_DIR = BASE / "data"
UNIFIED_PATH = DATA_DIR / "unified_dataset.parquet"
EMBED_DIR = DATA_DIR / "embeddings"
EMBED_DIR.mkdir(parents=True, exist_ok=True)

OPENROUTER_KEY = os.environ.get("OPENROUTER_API_KEY", "")
OPENROUTER_URL = "https://openrouter.ai/api/v1/embeddings"

# %% [model config]
# Each entry drives one full embedding run over the unified dataset.
# Adjust batch_size to match your API tier / memory.
#
# Cost estimate at current OpenRouter pricing (~Jul 2026):
# Cost at full corpus (92.9M tokens):
#   ada-002          : $0.10/M  → ~$9.29
#   te3-small        : $0.02/M  → ~$1.86
#   qwen3-emb-8b     : $0.01/M  → ~$0.93
#   bge-m3           : $0.01/M  → ~$0.93
#   me5-large        : $0.01/M  → ~$0.93
#   pplx-embed-1     : $0.004/M → ~$0.37
#   nemotron-1b-free : free
#   fastembed-*      : free (local CPU/ONNX)
#   ─────────────────────────────────────
#   total (paid)     :           ~$14.31

EMBEDDING_MODELS: dict[str, dict] = {
    # ── OpenRouter API models ────────────────────────────────────────────────
    "ada-002": {
        "type": "openrouter",
        "model_id": "openai/text-embedding-ada-002",
        "dim": 1536,
        "batch_size": 96,
        "max_chars": 30_000,  # 8k token context
        "price_per_m_tokens": 0.10,
        "role": "mandatory source, fixed constraint",
    },
    "te3-small": {
        "type": "openrouter",
        "model_id": "openai/text-embedding-3-small",
        "dim": 1536,
        "batch_size": 96,
        "max_chars": 30_000,  # 8k token context
        "price_per_m_tokens": 0.02,
        "role": "primary pair, real-world Ada migration path",
    },
    "qwen3-emb-8b": {
        "type": "openrouter",
        "model_id": "qwen/qwen3-embedding-8b",
        "dim": 4096,
        "batch_size": 32,
        "max_chars": 25_000,
        "price_per_m_tokens": 0.01,
        "role": "closed-to-open, avoid-lock-in story",
    },
    "bge-m3": {
        "type": "openrouter",
        "model_id": "baai/bge-m3",
        "dim": 1024,
        "batch_size": 96,
        "max_chars": 30_000,  # 8k token context
        "price_per_m_tokens": 0.01,
        "role": "open-source target",
    },
    "me5-large": {
        "type": "openrouter",
        "model_id": "intfloat/multilingual-e5-large",
        "dim": 1024,
        "batch_size": 96,
        "max_chars": 1_800,  # 512 token context limit → ~1.8k chars
        "price_per_m_tokens": 0.01,
        "role": "open-open control pair when paired with bge-m3",
    },
    "pplx-embed-1": {
        "type": "openrouter",
        "model_id": "perplexity/pplx-embed-v1-0.6b",
        "dim": 1024,
        "batch_size": 96,
        "max_chars": 120_000,  # 32k token context
        "price_per_m_tokens": 0.004,
        "role": "cheapest addition, lightweight low-latency baseline",
    },
    "nemotron-1b-free": {
        "type": "openrouter",
        "model_id": "nvidia/llama-nemotron-embed-vl-1b-v2:free",
        "dim": 2048,
        "batch_size": 32,  # free tier, be conservative
        "max_chars": 30_000,
        "price_per_m_tokens": 0.0,
        "role": "free tier — multimodal image/text bi-encoder, not a like-for-like text comparison",
    },
    # ── Local fastembed (ONNX, no API key, no cost) ──────────────────────────
    "fastembed-bge-small": {
        "type": "fastembed",
        "model_id": "BAAI/bge-small-en-v1.5",
        "dim": 384,
        "batch_size": 256,  # power-of-2 for best ONNX throughput
        "max_chars": 8_000,
        "price_per_m_tokens": 0.0,
        "role": "local baseline, fastest inference",
    },
    # "fastembed-bge-large": {
    #     "type": "fastembed",
    #     "model_id": "BAAI/bge-large-en-v1.5",
    #     "dim": 1024,
    #     "batch_size": 64,
    #     "max_chars": 8_000,
    #     "price_per_m_tokens": 0.0,
    #     "role": "local high-quality baseline",
    # },
}

# Retry settings (OpenRouter only — network / server errors)
MAX_RETRIES = 6
BACKOFF_BASE = 1.5  # seconds; doubles each attempt, capped at 90s


# %% [graceful shutdown]
_SHUTDOWN = False


def _on_shutdown(sig, _frame):
    global _SHUTDOWN
    log.warning("Shutdown signal — finishing current batch then stopping cleanly.")
    _SHUTDOWN = True


signal.signal(signal.SIGINT, _on_shutdown)
signal.signal(signal.SIGTERM, _on_shutdown)


# %% [checkpoint helpers]


def _cp_path(model_key: str) -> Path:
    return EMBED_DIR / f"{model_key}_checkpoint.json"


def load_checkpoint(model_key: str) -> set[int]:
    """Returns the set of batch start-indices already completed."""
    p = _cp_path(model_key)
    if p.exists():
        return set(json.loads(p.read_text()).get("completed_batches", []))
    return set()


def save_checkpoint(model_key: str, completed: set[int]) -> None:
    """Atomically update checkpoint (POSIX rename = crash-safe)."""
    p = _cp_path(model_key)
    tmp = p.with_suffix(".tmp")
    tmp.write_text(json.dumps({"completed_batches": sorted(completed)}, indent=2))
    tmp.replace(p)


# %% [batch I/O helpers]


def _batch_dir(model_key: str) -> Path:
    d = EMBED_DIR / model_key / "batches"
    d.mkdir(parents=True, exist_ok=True)
    return d


def flush_batch(
    model_key: str,
    start_idx: int,
    ids: list[int],
    vecs: list[np.ndarray],
) -> None:
    """Atomically write one batch shard. Safe to call after any crash."""
    # ── Pre-flight validation ────────────────────────────────────────────────
    if not vecs:
        raise RuntimeError(f"[{model_key}] flush_batch called with empty vecs at idx {start_idx}")
    if len(ids) != len(vecs):
        raise RuntimeError(
            f"[{model_key}] ID/vec count mismatch: {len(ids)} ids vs {len(vecs)} vecs"
        )
    shapes = {v.shape for v in vecs}
    if len(shapes) > 1:
        raise RuntimeError(
            f"[{model_key}] Inconsistent embedding shapes in batch: {shapes}. "
            "API returned vectors of different dimensions."
        )
    if vecs[0].ndim != 1:
        raise RuntimeError(
            f"[{model_key}] Expected 1-D embedding vectors, got shape {vecs[0].shape}"
        )

    col = f"{model_key}-EMBEDDING"

    # Stack into (batch, dim) — raises ValueError immediately if shapes differ
    mat = np.stack(vecs).astype(np.float32)
    dim = mat.shape[1]

    # FixedSizeList encodes dim in the schema: wrong-sized vector raises here,
    # not silently at query/training time.
    emb_arr = pa.FixedSizeListArray.from_arrays(
        pa.array(mat.ravel(), type=pa.float32()), dim
    )

    # Sanity-check: zero nulls before touching disk
    if emb_arr.null_count != 0:
        raise RuntimeError(
            f"[{model_key}] BUG: {emb_arr.null_count} null embeddings produced "
            f"before write at batch idx {start_idx}. Aborting flush."
        )

    table = pa.table({"ID": pa.array(ids, type=pa.int64()), col: emb_arr})
    path = _batch_dir(model_key) / f"batch_{start_idx:09d}.parquet"
    tmp = path.with_suffix(".tmp.parquet")
    pq.write_table(table, tmp)
    tmp.replace(path)  # atomic on POSIX


def merge_model_batches(model_key: str) -> Path | None:
    """Stream-concatenate all batch shards into one model-level Parquet."""
    shards = sorted(_batch_dir(model_key).glob("batch_*.parquet"))
    if not shards:
        log.warning(f"[{model_key}] No batch shards found — skipping merge")
        return None

    out_path = EMBED_DIR / f"{model_key}.parquet"
    tmp = out_path.with_suffix(".tmp.parquet")

    writer = None
    for shard in shards:
        table = pq.read_table(shard)
        if writer is None:
            writer = pq.ParquetWriter(tmp, table.schema)
        writer.write_table(table)
    if writer:
        writer.close()

    tmp.replace(out_path)
    log.info(f"[{model_key}] Merged {len(shards)} shards → {out_path.name}")
    return out_path


# %% [openrouter embed]


def _backoff_secs(attempt: int) -> float:
    return min(BACKOFF_BASE * (2**attempt) + random.uniform(0, 0.5), 90.0)


def _truncate_to_token_budget(texts: list[str], requested: int, budget: int = 290_000) -> list[str]:
    """Proportionally shorten every text so the batch stays under the token budget.
    Applies an extra 15% safety margin because character-to-token ratios are not
    perfectly uniform — dense segments have more tokens per char than the average."""
    ratio = (budget / requested) * 0.85
    return [t[: max(50, int(len(t) * ratio))] for t in texts]


def embed_openrouter(texts: list[str], model_id: str, _trunc: int = 0) -> list[np.ndarray]:
    """Embed a batch via OpenRouter with retry/backoff. Raises on exhaustion."""
    headers = {
        "Authorization": f"Bearer {OPENROUTER_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com/queryn/queryn",
    }
    payload = {"model": model_id, "input": texts, "encoding_format": "float"}

    for attempt in range(MAX_RETRIES):
        if _SHUTDOWN:
            raise RuntimeError("Shutdown requested mid-retry")
        try:
            r = httpx.post(OPENROUTER_URL, headers=headers, json=payload, timeout=120.0)

            if r.status_code == 429:
                wait = float(r.headers.get("Retry-After", _backoff_secs(attempt)))
                log.warning(
                    f"429 rate-limited — waiting {wait:.1f}s [attempt {attempt + 1}/{MAX_RETRIES}]"
                )
                time.sleep(wait)
                continue

            if r.status_code >= 500:
                wait = _backoff_secs(attempt)
                log.warning(
                    f"{r.status_code} server error — waiting {wait:.1f}s [attempt {attempt + 1}/{MAX_RETRIES}]"
                )
                time.sleep(wait)
                continue

            # Non-retryable client errors: convert to RuntimeError immediately
            # so run_pipeline's handler catches them cleanly and checkpoints are preserved.
            if r.status_code == 402:
                msg = r.json().get("error", {}).get("message", "insufficient credits")
                raise RuntimeError(f"OpenRouter credits exhausted (402): {msg}")
            if 400 <= r.status_code < 500:
                raise RuntimeError(
                    f"Non-retryable client error {r.status_code} for {model_id}: {r.text[:200]}"
                )

            r.raise_for_status()
            body = r.json()
            if "data" not in body:
                err_msg = str(body.get("error", {}).get("message", ""))
                # OpenRouter returns HTTP 200 with an error body for token-limit violations.
                # Every model uses a different message format; we handle them all here.
                #
                # "requested" regexes — how many tokens were actually sent:
                _m_req       = re.search(r"Requested (\d+) tokens", err_msg)          # ada/te3 batch (old)
                _m_ctx       = re.search(r"you requested (\d+) tokens", err_msg)      # ada/te3 per-text (old)
                _m_got       = re.search(r"got (\d+)", err_msg)                        # pplx: "got N, maximum is M"
                _m_input_exc = re.search(r"Input length (\d+) exceeds", err_msg)      # nemotron per-text
                # "budget" regexes — what the model's limit actually is:
                _m_limit     = re.search(r"maximum context length is (\d+)", err_msg) # ada/te3 per-text (old)
                _m_req_size  = re.search(r"maximum request size is (\d+) tokens", err_msg)  # te3 batch (new)
                _m_input_len = re.search(r"maximum input length is (\d+) tokens", err_msg)  # te3 per-text (new)
                _m_max_is    = re.search(r"maximum is (\d+)", err_msg)                # pplx: "maximum is M"
                _m_max_tok   = re.search(r"maximum allowed token size (\d+)", err_msg)      # nemotron per-text
                _is_token_error = any(phrase in err_msg for phrase in (
                    "max_tokens_per_request",
                    "maximum context length",
                    "maximum request size",
                    "maximum input length",
                    "Input total size exceeds",
                    "exceeds maximum allowed token size",
                ))
                if _is_token_error:
                    if _trunc >= 3:
                        raise RuntimeError(
                            f"Still over token limit after {_trunc} truncations for {model_id}: {err_msg[:200]}"
                        )
                    # When the error only reports the limit (not how many were sent),
                    # assume +500 tokens over — gives ~30% cut with the 0.85 safety margin.
                    _req_match      = _m_req or _m_ctx or _m_got or _m_input_exc
                    _per_text_limit = _m_limit or _m_input_len or _m_max_tok
                    requested = (
                        int(_req_match.group(1))
                        if _req_match else
                        int(_per_text_limit.group(1)) + 500
                        if _per_text_limit else
                        310_000
                    )
                    budget = (
                        int(_m_limit.group(1))    - 100    if _m_limit    else
                        int(_m_input_len.group(1)) - 100   if _m_input_len else
                        int(_m_max_tok.group(1))  - 100    if _m_max_tok  else
                        int(_m_req_size.group(1)) - 10_000 if _m_req_size else
                        int(_m_max_is.group(1))   - 10_000 if _m_max_is   else
                        290_000
                    )
                    log.warning(
                        f"Token limit hit ({requested:,} tokens, budget {budget:,}) "
                        f"[attempt {_trunc + 1}/3] — trimming texts and retrying"
                    )
                    return embed_openrouter(
                        _truncate_to_token_budget(texts, requested, budget),
                        model_id,
                        _trunc=_trunc + 1,
                    )
                raise RuntimeError(
                    f"Unexpected response from OpenRouter (no 'data' key): {body}"
                )
            items = sorted(body["data"], key=lambda x: x["index"])
            return [np.array(item["embedding"], dtype=np.float32) for item in items]

        except (
            httpx.TimeoutException,
            httpx.NetworkError,
            httpx.RemoteProtocolError,
        ) as e:
            wait = _backoff_secs(attempt)
            log.warning(
                f"Network error: {e} — waiting {wait:.1f}s [attempt {attempt + 1}/{MAX_RETRIES}]"
            )
            time.sleep(wait)

    raise RuntimeError(f"Exhausted {MAX_RETRIES} retries for {model_id}")


# %% [fastembed embed]

_FE_CACHE: dict[str, TextEmbedding] = {}


def _get_fastembed(model_id: str) -> TextEmbedding:
    if model_id not in _FE_CACHE:
        log.info(
            f"Loading fastembed model {model_id} (first run downloads ~100 MB to ~/.cache)…"
        )
        _FE_CACHE[model_id] = TextEmbedding(model_name=model_id)
        log.info(f"  {model_id} ready")
    return _FE_CACHE[model_id]


def embed_fastembed(
    texts: list[str],
    model_id: str,
    batch_size: int,
) -> list[np.ndarray]:
    model = _get_fastembed(model_id)
    return [
        np.array(v, dtype=np.float32) for v in model.embed(texts, batch_size=batch_size)
    ]


# %% [per-model pipeline]


def run_pipeline(model_key: str, df: pd.DataFrame) -> None:
    cfg = EMBEDDING_MODELS[model_key]
    mtype = cfg["type"]
    model_id = cfg["model_id"]
    batch_size = cfg["batch_size"]
    max_chars = cfg["max_chars"]

    if mtype == "openrouter" and not OPENROUTER_KEY:
        log.error(f"[{model_key}] OPENROUTER_API_KEY not set — skipping")
        return

    log.info(f"[{model_key}] Starting — model: {model_id}")

    # Stable sort: same ID order on every restart → same batch boundaries
    df = df.sort_values("ID").reset_index(drop=True)

    # Pre-load fastembed model before the loop (avoids download overhead in batch 0)
    if mtype == "fastembed":
        _get_fastembed(model_id)

    completed = load_checkpoint(model_key)
    total = len(df)
    total_batches = (total + batch_size - 1) // batch_size
    log.info(f"[{model_key}] {len(completed)}/{total_batches} batches already done")

    for i in range(0, total, batch_size):
        if _SHUTDOWN:
            log.warning(
                f"[{model_key}] Stopping at batch {i // batch_size + 1}/{total_batches}"
            )
            break

        if i in completed:
            continue  # already done — skip without re-embedding

        batch_df = df.iloc[i : i + batch_size]
        ids = batch_df["ID"].tolist()
        # Truncate to model context limit before sending
        texts = [t[:max_chars] for t in batch_df["TEXT"].tolist()]
        batch_num = i // batch_size + 1

        log.info(f"[{model_key}] Batch {batch_num}/{total_batches} ({len(ids)} texts)…")

        try:
            if mtype == "openrouter":
                vecs = embed_openrouter(texts, model_id)
            elif mtype == "fastembed":
                vecs = embed_fastembed(texts, model_id, batch_size)
            else:
                raise ValueError(f"Unknown model type: {mtype}")

            # 1. Flush batch shard to disk (atomic)
            flush_batch(model_key, i, ids, vecs)
            # 2. Mark as completed (atomic checkpoint update)
            completed.add(i)
            save_checkpoint(model_key, completed)

            log.info(f"[{model_key}] Batch {batch_num}/{total_batches} — flushed ✓")

        except RuntimeError as e:
            # Non-retryable failure after all backoff exhausted.
            # Checkpoint NOT updated → this batch will retry on next run.
            log.error(f"[{model_key}] Batch {batch_num} failed permanently: {e}")
            log.error(
                f"[{model_key}] Stopping — re-run script to resume from batch {batch_num}"
            )
            break

    done_rows = min(len(completed) * batch_size, total)
    log.info(f"[{model_key}] Pipeline done — {done_rows:,}/{total:,} rows embedded")


# %% [run all models]
try:
    df_unified = pd.read_parquet(UNIFIED_PATH)
except Exception as _load_err:
    log.error(
        f"Failed to load unified dataset: {_load_err}\n"
        "  The file is likely corrupted (e.g. from a prior RAM-overflow crash).\n"
        "  Fix: re-run dataset_generator.py to regenerate it, then restart this script.\n"
        "  Your embedding shards are intact — checkpoints will skip completed batches."
    )
    raise SystemExit(1)
log.info(f"Unified dataset loaded: {len(df_unified):,} rows")

for _model_key in EMBEDDING_MODELS:
    if _SHUTDOWN:
        log.warning("Stopped before starting next model.")
        break
    run_pipeline(_model_key, df_unified)

if _SHUTDOWN:
    log.warning("Interrupted — skipping merge, validate, and final table build. Re-run to continue.")
    raise SystemExit(0)


# %% [merge batch shards per model]
log.info("Merging batch shards per model…")
for _model_key in EMBEDDING_MODELS:
    merge_model_batches(_model_key)


# %% [validate shard health — run any time to check progress]
# Reads every shard file and reports null counts + schema.
# NOTE: Parquet viewer apps (e.g. "Parquet Reader") cannot display
#       fixed_size_list<element: float>[N] columns — they show NULL.
#       Use this cell to verify data is actually correct.
print("=" * 60)
for _model_key in EMBEDDING_MODELS:
    _bd = _batch_dir(_model_key)
    _shards = sorted(_bd.glob("batch_*.parquet"))
    if not _shards:
        print(f"[{_model_key}]  no shards yet")
        continue
    _total_null = 0
    _total_rows = 0
    for _s in _shards:
        _t = pq.read_table(str(_s))
        _col = f"{_model_key}-EMBEDDING"
        _c = _t.column(_col)
        _total_null += _c.null_count
        _total_rows += len(_t)
        if _c.null_count:
            print(f"  [!] {_s.name}: {_c.null_count} NULLS  type={_c.type}")
    _status = "✓" if _total_null == 0 else f"⚠ {_total_null} nulls"
    _first = pq.read_table(str(_shards[0])).column(f"{_model_key}-EMBEDDING")
    print(f"[{_model_key}]  {len(_shards)} shards  {_total_rows} rows  {_status}  type={_first.type}  first_val[:3]={_first[0].as_py()[:3]}")
print("=" * 60)


# %% [build final wide embeddings table]
# Output: embeddings.parquet — columns: ID | {model}-EMBEDDING …
# Only COMPLETE models (all rows present, zero nulls) are merged.
# Partial models are reported and skipped — re-run the pipeline to finish them.
#
# RAM strategy: model files are opened with memory_map=True (OS pages data from
# disk on demand, can evict pages under pressure) and written in row groups of
# _CHUNK rows. Peak physical RAM ≈ _CHUNK × N_models × max_dim × 4 bytes (~100 MB).
log.info("Building final wide embeddings table…")

_ref_table  = pq.read_table(UNIFIED_PATH, columns=["ID"])
_total_rows = len(_ref_table)
_ref_ids    = _ref_table.column("ID")

_complete: list[str] = []
_partial:  list[str] = []
_missing:  list[str] = []

for _model_key in EMBEDDING_MODELS:
    _p = EMBED_DIR / f"{_model_key}.parquet"
    if not _p.exists():
        _missing.append(_model_key)
    elif pq.read_metadata(str(_p)).num_rows == _total_rows:
        _complete.append(_model_key)
    else:
        _partial.append(_model_key)

if _missing:
    log.warning(f"  no merged file (not started yet): {_missing}")
if _partial:
    log.warning(f"  incomplete (re-run pipeline to finish): {_partial}")
if not _complete:
    log.error("No fully-complete model files found — run the pipeline first.")
else:
    # Open each model file memory-mapped and validate before touching disk.
    _model_tables: dict[str, pa.Table] = {}
    for _model_key in _complete:
        _t   = pq.read_table(str(EMBED_DIR / f"{_model_key}.parquet"), memory_map=True).sort_by("ID")
        _col = f"{_model_key}-EMBEDDING"
        _emb = _t.column(_col)

        if not _t.column("ID").equals(_ref_ids):
            log.error(
                f"  [{_model_key}] ID mismatch with unified dataset "
                "(dataset was regenerated?) — skipping"
            )
            continue
        if _emb.null_count:
            log.error(
                f"  [{_model_key}] {_emb.null_count:,} null embeddings in model file — "
                "delete its checkpoint + shard dir and re-run"
            )
            continue

        _model_tables[_model_key] = _t
        log.info(f"  {_model_key}: {len(_t):,} rows  type={_emb.type}  ✓")

    if _model_tables:
        final_path = EMBED_DIR / "embeddings.parquet"
        tmp = final_path.with_suffix(".tmp.parquet")

        _CHUNK = 2_000  # rows per write call; adjust down if RAM is still tight
        _writer: pq.ParquetWriter | None = None
        for _start in range(0, _total_rows, _CHUNK):
            _end = min(_start + _CHUNK, _total_rows)
            _chunk_cols: dict = {"ID": _ref_ids[_start:_end]}
            for _mk, _mt in _model_tables.items():
                _chunk_cols[f"{_mk}-EMBEDDING"] = _mt.column(f"{_mk}-EMBEDDING")[_start:_end]
            _chunk = pa.table(_chunk_cols)
            if _writer is None:
                _writer = pq.ParquetWriter(str(tmp), _chunk.schema)
            _writer.write_table(_chunk)
        if _writer:
            _writer.close()
        tmp.replace(final_path)

        # Validate via metadata only — avoids loading the full wide table into RAM.
        _meta   = pq.read_metadata(str(final_path))
        _schema = pq.read_schema(str(final_path))
        log.info(f"Final wide table → {final_path}")
        log.info(f"  rows   : {_meta.num_rows:,}")
        for _f in _schema:
            if "EMBEDDING" in _f.name:
                log.info(f"  {_f.name}: type={_f.type}  ✓")
