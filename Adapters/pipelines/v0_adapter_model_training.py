# %%
"""IMPORT"""
import json
import logging
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

#%%
"""CONFIG"""
DATASET_SIZE = 349674
TEST_SIZE = int(349674*0.2)
TRAIN_SIZE = DATASET_SIZE - TEST_SIZE
lr = 1e-3
BATCH_SIZE = 128
EPOCHS = 15
DEVICE = "mps"

try:
    _ROOT = Path(__file__).parent.parent
except NameError:
    _ROOT = Path.cwd()  # Zed / Jupyter REPL fallback

MODELS_DIR  = _ROOT / "models"
REPORTS_DIR = _ROOT / "reports"
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

# All directed pairs: N*(N-1) = 56
PAIRS: list[tuple[str, str]] = [
    (src, tgt) for src in MODEL_DIMS for tgt in MODEL_DIMS if src != tgt
]

HIDDEN_DIM_CAP = 2048   # caps hidden size for qwen3 pairs
PARQUET_BATCH  = 8192   # rows per parquet read chunk

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
"""LINEAR MODEL"""
def linearModel(input,output):
    return nn.Linear(input,output)

# %%
"""DEEP NEURAL NET MODEL"""
class DeepModel(nn.Module):
    def __init__(self,input,hidden_dim,output) -> None:
        super().__init__()
        self.model= nn.Sequential(
            nn.Linear(input,hidden_dim),
            nn.GELU(),
            nn.Linear(hidden_dim,output),
        )
        self.optimizer = torch.optim.Adam(self.model.parameters(),lr=lr)
        self.loss_fn = nn.HuberLoss()
    def forward(self,x):
        y = self.model.forward(x)
        return y

def train(model:DeepModel,loader):
    model.train()
    for epoch in range(EPOCHS):
        running_loss = 0.0
        n_batches = 0
        for xb,yb in loader:
            xb,yb = xb.to(DEVICE),yb.to(DEVICE)
            model.optimizer.zero_grad()
            preds = model(xb)
            loss = model.loss_fn(preds,yb)
            loss.backward()
            model.optimizer.step()
            running_loss += loss.item()
            n_batches+=1

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


def _eval_epoch(
    model: DeepModel,
    loader: DataLoader,
    device: str,
) -> tuple[float, float]:
    """Returns (avg_huber_loss, avg_cosine_similarity) over one full pass."""
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
                total_loss += model.loss_fn(preds, yb).item() * len(xb)
                total_cos  += F.cosine_similarity(preds, yb, dim=-1).sum().item()
                n          += len(xb)
    return (
        total_loss / n if n else float("inf"),
        total_cos  / n if n else 0.0,
    )

# %%
"""PAIR TRAINING"""

def train_pair(src: str, tgt: str) -> dict:
    """Train a DeepModel mapper for src→tgt, save to models/, return metrics."""
    src_col   = f"{src}-EMBEDDING"
    tgt_col   = f"{tgt}-EMBEDDING"
    pair_id   = f"{src}_to_{tgt}"
    save_path = MODELS_DIR / f"{pair_id}.pt"

    if save_path.exists():
        log.info(f"[{pair_id}] already saved — skipping")
        return {}

    in_dim  = MODEL_DIMS[src]
    out_dim = MODEL_DIMS[tgt]
    hidden  = min(max(in_dim, out_dim), HIDDEN_DIM_CAP)
    log.info(f"[{pair_id}] {in_dim}d → {out_dim}d  hidden={hidden}")
    t0 = time.perf_counter()

    model = DeepModel(in_dim, hidden, out_dim).to(DEVICE)

    # batch_size=None: DataLoader yields raw (X, y) parquet chunks without collation.
    # Sub-batching to BATCH_SIZE happens in the inner loop below.
    train_ds = ParquetIterableDataset(str(TRAIN_PATH), [src_col], [tgt_col], PARQUET_BATCH)
    test_ds  = ParquetIterableDataset(str(TEST_PATH),  [src_col], [tgt_col], PARQUET_BATCH)
    train_ld = DataLoader(train_ds, batch_size=None)
    test_ld  = DataLoader(test_ds,  batch_size=None)

    history: list[dict] = []

    for epoch in range(EPOCHS):
        model.train()
        ep_loss, ep_n = 0.0, 0

        for X_np, y_np in train_ld:
            X = _to_tensor(X_np, DEVICE)
            y = _to_tensor(y_np, DEVICE)
            for i in range(0, len(X), BATCH_SIZE):
                xb    = X[i : i + BATCH_SIZE]
                yb    = y[i : i + BATCH_SIZE]
                model.optimizer.zero_grad()
                preds = model(xb)
                loss  = model.loss_fn(preds, yb)
                loss.backward()
                torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
                model.optimizer.step()
                ep_loss += loss.item() * len(xb)
                ep_n    += len(xb)

        avg_train_loss             = ep_loss / ep_n if ep_n else float("inf")
        avg_test_loss, avg_test_cos = _eval_epoch(model, test_ld, DEVICE)

        history.append({
            "epoch":      epoch + 1,
            "train_loss": round(avg_train_loss, 6),
            "test_loss":  round(avg_test_loss,  6),
            "test_cos":   round(avg_test_cos,   6),
        })
        log.info(
            f"[{pair_id}] {epoch + 1:02d}/{EPOCHS}"
            f"  train_loss={avg_train_loss:.5f}"
            f"  test_loss={avg_test_loss:.5f}"
            f"  test_cos={avg_test_cos:.4f}"
        )

    elapsed = time.perf_counter() - t0

    torch.save(
        {
            "state_dict": model.state_dict(),
            "config": {
                "src":        src,
                "tgt":        tgt,
                "in_dim":     in_dim,
                "out_dim":    out_dim,
                "hidden_dim": hidden,
            },
            "history": history,
        },
        save_path,
    )
    log.info(f"[{pair_id}] saved → {save_path.name}  ({elapsed:.1f}s)")

    if hasattr(torch, "mps") and hasattr(torch.mps, "empty_cache"):
        torch.mps.empty_cache()

    return {"history": history, "elapsed_s": elapsed}

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
                "  cd AI/ && python dataset_splitting.py"
            )
            raise SystemExit(1)

    log.info(
        f"Device: {DEVICE}  |  Pairs: {len(PAIRS)}  |  "
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

    summary = {
        "device":       DEVICE,
        "epochs":       EPOCHS,
        "batch_size":   BATCH_SIZE,
        "total_pairs":  len(PAIRS),
        "total_time_s": round(total_s, 2),
        "pairs": {
            key: {
                "final_train_loss": r["history"][-1]["train_loss"],
                "final_test_loss":  r["history"][-1]["test_loss"],
                "final_test_cos":   r["history"][-1]["test_cos"],
                "elapsed_s":        round(r["elapsed_s"], 2),
            }
            for key, r in all_results.items()
        },
    }
    summary_path = REPORTS_DIR / "training_summary.json"
    with open(summary_path, "w") as f:
        json.dump(summary, f, indent=2)

    log.info(
        f"\nAll done in {total_s / 60:.1f} min\n"
        f"Models   → {MODELS_DIR}/\n"
        f"Summary  → {summary_path}"
    )
