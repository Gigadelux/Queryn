# Embedding Pipeline — Operational Guide

A hands-on reference for running, monitoring, resuming, and troubleshooting
`AI/embedding_pipeline.py`.

---

## Directory layout

```
AI/
├── embedding_pipeline.py          ← the script
├── data/
│   ├── unified_dataset.parquet    ← input (written by dataset_generator.py)
│   └── embeddings/
│       ├── {model}/
│       │   └── batches/
│       │       ├── batch_000000000.parquet   ← atomic shard (96 rows)
│       │       ├── batch_000000096.parquet
│       │       └── …
│       ├── {model}_checkpoint.json           ← completed batch indices
│       ├── {model}.parquet                   ← merged model file
│       └── embeddings.parquet                ← final wide table (all models)
```

---

## Prerequisites

```bash
# .env in repo root or AI/
OPENROUTER_API_KEY=sk-or-v1-...

pip install httpx numpy pandas pyarrow fastembed python-dotenv
```

---

## How to run

```bash
cd AI/
python embedding_pipeline.py
```

The script runs all six cells in sequence (see below).
Stop it at any time with **Ctrl-C** — the current batch finishes cleanly,
then the script exits without running merge or final-build.
Re-run the same command to resume; completed batches are skipped.

---

## What happens step by step

### Cell 1 — Load unified dataset
Reads `data/unified_dataset.parquet` into a DataFrame.
If the file is corrupted (e.g. from a prior RAM-overflow crash), the script
prints a clear error and exits. Fix: regenerate with `dataset_generator.py`.

### Cell 2 — Per-model embedding loop (`run_pipeline`)

For each model in `EMBEDDING_MODELS`:

1. **Sort by ID** — guarantees the same batch boundaries on every restart.
2. **Load checkpoint** — `{model}_checkpoint.json` contains the set of
   already-completed batch start-indices. Those batches are skipped instantly.
3. **Batch loop** — for each batch of `batch_size` rows:
   - Truncate texts to `max_chars` (hard char limit before sending).
   - Call the embedding API (OpenRouter) or local ONNX model (fastembed).
   - If the API returns a token-limit error (HTTP 200 with error body):
     proportionally shorten all texts and retry up to 3 times.
   - If the call fails permanently: log the error and break out of the loop.
     The checkpoint is **not** updated, so the batch retries on the next run.
   - On success: write shard atomically (`batch_{i:09d}.tmp.parquet` →
     rename → `batch_{i:09d}.parquet`), then update the checkpoint.

### Cell 3 — Merge shards per model
Concatenates all `batches/batch_*.parquet` shards for each model into a
single `{model}.parquet`. Streaming write — only one shard in RAM at a time.

### Cell 4 — Validate shard health
Reads every shard and prints null counts and embedding type. Use this any
time to check progress without running the full pipeline.

### Cell 5 — Build final wide table
Joins all **complete** model files (exactly N rows, zero nulls) into
`embeddings.parquet` with columns `ID | ada-002-EMBEDDING | te3-small-EMBEDDING | …`.

**RAM-safe**: model files are opened with `memory_map=True` (OS manages pages,
can evict under pressure) and written in row groups of 2 000 rows.
Peak physical RAM ≈ 100 MB regardless of dataset size or number of models.
Validation uses metadata only — the final file is never fully loaded.

---

## Resuming after interruption

```bash
python embedding_pipeline.py
```

That's it. The script detects completed batches via checkpoint files and skips
them. Models that are fully done are also skipped.

If you interrupted mid-batch, that batch's shard was not written (atomic
rename was not reached), so it will be re-embedded on the next run.

---

## Monitoring progress

**While running** — watch the log output:
```
[ada-002] Batch 3191/3642 (96 texts)…
[ada-002] Batch 3191/3642 — flushed ✓
```

**After stopping** — run the validate cell standalone:
```bash
python - <<'EOF'
from pathlib import Path
import pyarrow.parquet as pq

EMBED_DIR = Path("AI/data/embeddings")
for model_dir in sorted(EMBED_DIR.iterdir()):
    bd = model_dir / "batches"
    if not bd.is_dir():
        continue
    shards = sorted(bd.glob("batch_*.parquet"))
    rows = sum(len(pq.read_metadata(str(s)).row_groups) * pq.read_metadata(str(s)).row_group(0).num_rows for s in shards)
    print(f"{model_dir.name:25s}  {len(shards)} shards")
EOF
```

Or use `read_chunks.py` to inspect one embedding per shard file:
```bash
python AI/read_chunks.py ada-002
```

---

## Token limit errors (automatic — no action needed)

OpenRouter can reject batches or individual texts that exceed the model's
token window. The pipeline catches all known error message formats:

| Error message contains | Meaning | Action |
|---|---|---|
| `max_tokens_per_request` | Batch total > 300 k tokens | Proportionally shorten all texts |
| `maximum request size is N` | Same, new format | Same |
| `maximum context length is N` | Single text > model window | Same |
| `maximum input length is N` | Same, new format | Same |

Up to 3 truncation attempts per batch, each cutting texts to ~79–83% of the
previous length. If still over limit after 3 tries, the batch fails permanently
and will retry from scratch on the next run.

---

## Common errors and fixes

### `OSError: Couldn't deserialize thrift`
The `unified_dataset.parquet` footer is corrupted (most likely from a prior
RAM-overflow crash that killed a write mid-flight).

Fix:
```bash
python AI/dataset_generator.py   # regenerate the input file
python AI/embedding_pipeline.py  # resume — shards + checkpoints are intact
```

### `80 GB swap / RAM overflow`
The final wide table builder previously loaded all model embeddings into RAM
simultaneously. This is now fixed — see Cell 5 above (chunked row-group writes).

If you still see high RAM during the embedding loop itself: reduce `batch_size`
in `EMBEDDING_MODELS` for the model that's causing it. fastembed models in
particular can buffer large ONNX tensors; halving `batch_size` halves peak ONNX
memory.

### `Batch N failed permanently: Still over token limit after 3 truncations`
The text is so token-dense (e.g. minified JS, dense tables) that even at ~50%
length it still exceeds the model window. Options:
- Increase `max_chars` truncation before sending (lower in the loop at
  `texts = [t[:max_chars] for t in …]`).
- Skip the model for this domain and document the gap.

### Merge runs on Ctrl-C (old behavior — now fixed)
Previously, the merge and final-build cells ran even after a Ctrl-C interrupt.
Now: if `_SHUTDOWN` is True after the model loop, the script exits cleanly
before any post-processing.

### `ID mismatch with unified dataset`
`unified_dataset.parquet` was regenerated after some embedding shards were
written, changing the IDs. Fix: delete all embedding data and start fresh.
```bash
rm -rf AI/data/embeddings/
python AI/embedding_pipeline.py
```

---

## Running only specific cells

The script is structured as `%%`-delimited cells, so you can copy any cell
into a standalone script or run it in a Jupyter/VS Code notebook.

Useful standalone runs:
- **Validate only**: copy the `[validate shard health]` cell.
- **Merge only**: call `merge_model_batches("ada-002")` after importing the helpers.
- **Final build only**: copy the `[build final wide embeddings table]` cell.
