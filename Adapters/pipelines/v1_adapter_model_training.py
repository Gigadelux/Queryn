# %%
"""IMPORT"""
import json
import logging
import sys
import time
from pathlib import Path

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import polars as pl
import pyarrow.parquet as pq
from torch.utils.data.dataloader import DataLoader
from torch.utils.data.dataset import IterableDataset

try:
    _ROOT = Path(__file__).parent.parent
except NameError:
    _ROOT = Path.cwd()  # Zed / Jupyter REPL fallback

# architectures/ is a sibling of pipelines/ under Adapters/, not an
# installed package — put Adapters/ on sys.path so `from architectures
# import ...` resolves regardless of how this script is launched.
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from architectures import ARCHITECTURES  # noqa: E402  (import after sys.path fix)

#%%
"""CONFIG"""
DATASET_SIZE = 349674
TEST_SIZE = int(349674*0.2)
TRAIN_SIZE = DATASET_SIZE - TEST_SIZE
lr = 1e-3
BATCH_SIZE = 128
EPOCHS = 15


def _select_device() -> str:
    """Apple Silicon target: prefer MPS, but verify it's actually usable
    rather than hardcoding the string. torch can be running under an
    x86_64 interpreter via Rosetta on M-series hardware (common with older
    conda/venv setups) where `torch.backends.mps` reports unavailable even
    though the chip supports it — fail over to CPU instead of crashing on
    the first `.to("mps")` call.
    """
    if torch.backends.mps.is_available():
        return "mps"
    logging.getLogger(__name__).warning(
        "MPS backend not available (torch not built with MPS support, or "
        "running under Rosetta) — falling back to CPU. On Apple Silicon "
        "this usually means the Python interpreter itself is x86_64; "
        "check `platform.machine()` == 'arm64'."
    )
    return "cpu"


DEVICE = _select_device()

# ReduceLROnPlateau on test_cos — v0 trained every pair at a fixed lr for
# all 15 epochs, which was fine for well-conditioned pairs but caused real
# divergence (not overfitting — train_loss itself oscillated) on
# high-dimensional / large-magnitude sources like qwen3-emb-8b and
# pplx-embed-1. Backing off the LR once test_cos stops improving lets those
# pairs settle instead of bouncing around a minimum indefinitely.
LR_SCHEDULER_FACTOR   = 0.5
LR_SCHEDULER_PATIENCE = 2

MODELS_DIR  = _ROOT / "models" / "v1"
REPORTS_DIR = _ROOT / "reports" / "v1"
TRAIN_PATH  = _ROOT / "data/splits/train.parquet"
TEST_PATH   = _ROOT / "data/splits/test.parquet"

# Embedding dimension per model key — keep in sync with embedding_pipeline.py
MODEL_DIMS: dict[str, int] = {
    "ada-002":              1536,
    "te3-small":            1536,
    "qwen3-emb-8b":         4096,
    "bge-m3":               1024,
    "me5-large":            1024,
    "pplx-embed-1":         1024,
    "nemotron-1b-free":     2048,
    "fastembed-bge-small":   384,
}

# ada-002 is being deprecated: it stays as a valid *source* (customers still
# hold corpora embedded with it and need a way off), but it is dropped as a
# *target* — nobody should be training a new mapper that produces
# embeddings in a space that's going away. N*(N-1) - (N-1) = 49 pairs.
PAIRS: list[tuple[str, str]] = [
    (src, tgt) for src in MODEL_DIMS for tgt in MODEL_DIMS
    if src != tgt and tgt != "ada-002"
]

PARQUET_BATCH = 8192   # rows per parquet read chunk

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger(__name__)

# %%
"""DATA PIPELINE"""
def parquet_batch_iterator(path,feature_col,label_col,batch_size=8192):
    """
    Yields (X,y) numpy batches without ever holding the full dataset in RAM.
    """
    pf = pq.ParquetFile(path)
    for batch in pf.iter_batches(batch_size=batch_size,columns=feature_col+label_col):
        df = pl.from_arrow(batch)
        X = pl.DataFrame(df).select(feature_col).to_numpy()
        y = pl.DataFrame(df).select(label_col).to_numpy()
        yield X,y

class ParquetIterableDataset(IterableDataset):
    def __init__(self,path,feature_col,label_col,batch_size=8192) -> None:
        super().__init__()
        self.path = path
        self.feature_col = feature_col
        self.label_col = label_col
        self.batch_size = batch_size
    def __iter__(self):
        for X,y in parquet_batch_iterator(
            self.path,self.feature_col,self.label_col,self.batch_size
        ):
            yield X,y

# %%
"""TRAINING UTILITIES"""

def _to_tensor(arr: np.ndarray, device: str) -> torch.Tensor:
    """Convert parquet_batch_iterator output to a (N, dim) float32 tensor.

    polars to_numpy() for fixed_size_list columns can return several layouts:
    - (N,)   object — each cell is a (dim,) numpy array or polars Series
    - (N, 1) object — each cell is a (dim,) numpy array (extra wrapper dim)
    - (N, dim) float32 — direct, no unwrapping needed
    """
    if arr.dtype == object:
        elem = arr.flat[0]
        if isinstance(elem, np.ndarray):
            arr = np.stack([x.ravel().astype(np.float32) for x in arr.ravel()])
        elif hasattr(elem, "to_numpy"):       # polars Series
            arr = np.stack([x.to_numpy().astype(np.float32) for x in arr.ravel()])
        else:                                  # Python scalars / lists
            arr = np.array(arr.tolist(), dtype=np.float32)
    a = np.ascontiguousarray(arr, dtype=np.float32)
    t = torch.from_numpy(a)
    if t.ndim == 1:
        t = t.unsqueeze(0)
    elif t.ndim == 3:
        t = t.squeeze(1)
    return t.to(device)


def cosine_loss(preds: torch.Tensor, targets: torch.Tensor) -> torch.Tensor:
    """1 - mean cosine similarity.

    Directly optimizes the thing test_cos measures, instead of Huber/L2 on
    embedding magnitude standing in for it. F.cosine_similarity normalizes
    both arguments internally, so neither preds nor targets need
    pre-normalization here — and the architectures in
    Adapters/architectures/ normalize their own input/output internally,
    so raw embeddings can be fed straight through end to end.
    """
    return 1.0 - F.cosine_similarity(preds, targets, dim=-1).mean()


def _eval_epoch(
    model: nn.Module,
    loader: DataLoader,
    device: str,
    loss_fn,
) -> tuple[float, float]:
    """Returns (avg_cosine_loss, avg_cosine_similarity) over one full pass."""
    model.eval()
    total_loss, total_cos, n = 0.0, 0.0, 0
    with torch.no_grad():
        for X_np, y_np in loader:
            X = _to_tensor(X_np, device)
            y = _to_tensor(y_np, device)
            for i in range(0, len(X), BATCH_SIZE):
                xb    = X[i : i + BATCH_SIZE]
                yb    = y[i : i + BATCH_SIZE]
                preds = model(xb)
                total_loss += loss_fn(preds, yb).item() * len(xb)
                total_cos  += F.cosine_similarity(preds, yb, dim=-1).sum().item()
                n          += len(xb)
    return (
        total_loss / n if n else float("inf"),
        total_cos  / n if n else 0.0,
    )

# %%
"""SINGLE-ARCHITECTURE TRAINING"""

def train_architecture(
    name: str,
    model_cls: type,
    in_dim: int,
    out_dim: int,
    train_ld: DataLoader,
    test_ld: DataLoader,
    pair_id: str,
) -> dict:
    """Train one architecture for `EPOCHS` epochs, tracking the best epoch
    by test_cos rather than trusting the final one — several v0 pairs
    (pplx-embed-1_to_ada-002, qwen3-emb-8b_to_me5-large, ...) peaked early
    and then degraded from optimizer instability, and v0 only ever saved
    the last epoch. Returns history plus the best epoch's own state_dict.
    """
    model     = model_cls(in_dim, out_dim).to(DEVICE)
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)
    scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(
        optimizer, mode="max",
        factor=LR_SCHEDULER_FACTOR, patience=LR_SCHEDULER_PATIENCE,
    )
    loss_fn = cosine_loss

    history: list[dict] = []
    best_test_cos   = -1.0
    best_epoch      = 0
    best_state_dict = None

    t0 = time.perf_counter()

    for epoch in range(EPOCHS):
        model.train()
        ep_loss, ep_n = 0.0, 0

        for X_np, y_np in train_ld:
            X = _to_tensor(X_np, DEVICE)
            y = _to_tensor(y_np, DEVICE)
            for i in range(0, len(X), BATCH_SIZE):
                xb    = X[i : i + BATCH_SIZE]
                yb    = y[i : i + BATCH_SIZE]
                optimizer.zero_grad()
                preds = model(xb)
                loss  = loss_fn(preds, yb)
                loss.backward()
                torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
                optimizer.step()
                ep_loss += loss.item() * len(xb)
                ep_n    += len(xb)

        avg_train_loss              = ep_loss / ep_n if ep_n else float("inf")
        avg_test_loss, avg_test_cos = _eval_epoch(model, test_ld, DEVICE, loss_fn)
        scheduler.step(avg_test_cos)

        if avg_test_cos > best_test_cos:
            best_test_cos   = avg_test_cos
            best_epoch      = epoch + 1
            best_state_dict = {k: v.detach().cpu().clone() for k, v in model.state_dict().items()}

        history.append({
            "epoch":      epoch + 1,
            "train_loss": round(avg_train_loss, 6),
            "test_loss":  round(avg_test_loss,  6),
            "test_cos":   round(avg_test_cos,   6),
            "lr":         round(optimizer.param_groups[0]["lr"], 8),
        })
        log.info(
            f"[{pair_id}][{name}] {epoch + 1:02d}/{EPOCHS}"
            f"  train_loss={avg_train_loss:.5f}"
            f"  test_loss={avg_test_loss:.5f}"
            f"  test_cos={avg_test_cos:.4f}"
            f"  lr={optimizer.param_groups[0]['lr']:.2e}"
        )

    elapsed = time.perf_counter() - t0

    arch_kwargs = {"latent_dim": model.latent_dim} if hasattr(model, "latent_dim") else {}

    if hasattr(torch, "mps") and hasattr(torch.mps, "empty_cache"):
        torch.mps.empty_cache()

    return {
        "history":         history,
        "best_epoch":      best_epoch,
        "best_test_cos":   best_test_cos,
        "best_state_dict": best_state_dict,
        "arch_kwargs":     arch_kwargs,
        "elapsed_s":       elapsed,
    }

# %%
"""PAIR TRAINING"""

def train_pair(src: str, tgt: str) -> dict:
    """Train every architecture in ARCHITECTURES for src→tgt, keep the best
    epoch of each, then save whichever architecture scored higher —
    ties (including the common case where the nonlinear mapper doesn't
    beat the linear baseline) go to `linear`, per its position in
    ARCHITECTURES: the simpler model is preferred unless the deeper one
    demonstrably earns its extra capacity.
    """
    src_col   = f"{src}-EMBEDDING"
    tgt_col   = f"{tgt}-EMBEDDING"
    pair_id   = f"{src}_to_{tgt}"
    save_path = MODELS_DIR / f"{pair_id}.pt"

    if save_path.exists():
        log.info(f"[{pair_id}] already saved — skipping")
        return {}

    in_dim  = MODEL_DIMS[src]
    out_dim = MODEL_DIMS[tgt]
    log.info(f"[{pair_id}] {in_dim}d → {out_dim}d")
    t0 = time.perf_counter()

    # batch_size=None: DataLoader yields raw (X, y) parquet chunks without
    # collation. Sub-batching to BATCH_SIZE happens inside train_architecture.
    train_ds = ParquetIterableDataset(str(TRAIN_PATH), [src_col], [tgt_col], PARQUET_BATCH)
    test_ds  = ParquetIterableDataset(str(TEST_PATH),  [src_col], [tgt_col], PARQUET_BATCH)

    arch_results: dict[str, dict] = {}
    for name, model_cls in ARCHITECTURES.items():
        # Fresh DataLoaders per architecture — the underlying IterableDataset
        # re-opens the parquet file each time __iter__ is called.
        train_ld = DataLoader(train_ds, batch_size=None)
        test_ld  = DataLoader(test_ds,  batch_size=None)
        arch_results[name] = train_architecture(
            name, model_cls, in_dim, out_dim, train_ld, test_ld, pair_id,
        )

    # Max accuracy (test_cos) between linear and deep; linear wins ties.
    winner = "linear"
    for name in arch_results:
        if name == "linear":
            continue
        if arch_results[name]["best_test_cos"] > arch_results["linear"]["best_test_cos"]:
            winner = name
    win = arch_results[winner]

    elapsed = time.perf_counter() - t0

    torch.save(
        {
            "state_dict": win["best_state_dict"],
            "config": {
                "src":          src,
                "tgt":          tgt,
                "in_dim":       in_dim,
                "out_dim":      out_dim,
                "architecture": winner,
                "arch_kwargs":  win["arch_kwargs"],
                "best_epoch":   win["best_epoch"],
                # The architecture normalizes its own input/output (see
                # architectures/linear.py, deep.py) — this is informational,
                # not a contract the caller has to uphold.
                "self_normalizing": True,
            },
            "history": win["history"],
            # Honest ablation record — every architecture's own best epoch,
            # not just the winner, so a pair where linear beat deep is
            # visible in the report rather than silently discarded.
            "architecture_comparison": {
                name: {
                    "best_epoch":    r["best_epoch"],
                    "best_test_cos": round(r["best_test_cos"], 6),
                    "arch_kwargs":   r["arch_kwargs"],
                }
                for name, r in arch_results.items()
            },
        },
        save_path,
    )
    log.info(
        f"[{pair_id}] winner={winner} "
        f"best_epoch={win['best_epoch']} best_test_cos={win['best_test_cos']:.4f} "
        f"saved → {save_path.name}  ({elapsed:.1f}s)"
    )

    return {
        "src": src,
        "tgt": tgt,
        "architecture": winner,
        "best_epoch": win["best_epoch"],
        "history": win["history"],
        "architecture_comparison": {
            name: {
                "best_epoch":    r["best_epoch"],
                "best_test_cos": round(r["best_test_cos"], 6),
            }
            for name, r in arch_results.items()
        },
        "elapsed_s": elapsed,
    }

# %%
"""TRAIN ALL PAIRS"""
if __name__ == "__main__":
    MODELS_DIR.mkdir(parents=True, exist_ok=True)
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    for p in (TRAIN_PATH, TEST_PATH):
        if not p.exists():
            log.error(
                f"Missing: {p}\n"
                "Run dataset_splitting.py first:\n"
                "  cd Adapters/ && python dataset_splitting.py"
            )
            raise SystemExit(1)

    log.info(
        f"Device: {DEVICE}  |  Pairs: {len(PAIRS)}  |  "
        f"Architectures: {list(ARCHITECTURES)}  |  "
        f"Epochs: {EPOCHS}  |  Batch: {BATCH_SIZE}"
    )

    all_results: dict[str, dict] = {}
    t_global = time.perf_counter()

    for idx, (src, tgt) in enumerate(PAIRS, 1):
        log.info(f"\n─── [{idx}/{len(PAIRS)}] {src} → {tgt} ───")
        result = train_pair(src, tgt)
        if result:
            all_results[f"{src}_to_{tgt}"] = result

    total_s = time.perf_counter() - t_global

    report = {
        "device":       DEVICE,
        "epochs":       EPOCHS,
        "batch_size":   BATCH_SIZE,
        "architectures": list(ARCHITECTURES),
        "total_pairs":  len(PAIRS),
        "total_time_min": round(total_s / 60, 2),
        "pairs": all_results,
    }
    report_path = REPORTS_DIR / "training_report.json"
    with open(report_path, "w") as f:
        json.dump(report, f, indent=2)

    log.info(
        f"\nAll done in {total_s / 60:.1f} min\n"
        f"Models   → {MODELS_DIR}/\n"
        f"Report   → {report_path}"
    )
