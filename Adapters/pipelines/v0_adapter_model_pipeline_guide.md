# Adapter Model Training Pipeline

## Overview

`adapter_model_training.py` trains **56 directed embedding-space mappers** (one per ordered model pair) using the split dataset produced by `dataset_splitting.py`. Each mapper is a residual MLP that translates a vector from model A's embedding space into the equivalent vector in model B's space, without touching the original text.

---

## Model pairs

8 configured models → **N × (N-1) = 56 directed pairs**.

| Model | Dim |
|---|---|
| ada-002 | 1536 |
| te3-small | 1536 |
| qwen3-emb-8b | 4096 |
| bge-m3 | 1024 |
| me5-large | 1024 |
| pplx-embed-1 | 1024 |
| nemotron-1b-free | 2048 |
| fastembed-bge-small | 384 |

---

## Architecture — `DeepModel`

A shallow 2-layer MLP (1 hidden layer). Architecture chosen over a plain linear projection following **Vec2Vec** (arxiv:2306.12689), which demonstrates that non-linear transformations outperform linear ones for embedding space translation. Residual connections are deferred to a later training phase.

```
input (in_dim)
    │
    ▼
Linear(in_dim → hidden) → GELU
    │
    ▼
Linear(hidden → out_dim)
    │
    ▼
output (out_dim)
```

`hidden = min(max(in_dim, out_dim), 2048)`

**Loss:** Huber loss (smooth L1 — robust to outlier embeddings).

---

## Data pipeline

```
data/splits/train.parquet  (279,739 rows)
data/splits/test.parquet   ( 69,935 rows)
```

Both files were produced by `dataset_splitting.py` with `SEED=42` and `TEST_RATIO=0.20`. The split mask is applied row-by-row, so the parquet column schema is identical to `embeddings.parquet`.

**Reading strategy:**

- `ParquetIterableDataset` streams the file via `pq.ParquetFile.iter_batches(batch_size=8192)`, loading only two embedding columns at a time (source + target).
- `DataLoader(dataset, batch_size=None)` disables PyTorch collation; the 8192-row parquet chunk arrives as a numpy array and is sub-batched manually into `MINI_BATCH=128` chunks for gradient steps.
- Peak RAM per training step: `128 × max_dim × 4 bytes ≈ 2 MB`. Peak per parquet chunk load: `8192 × (in_dim + out_dim) × 4 bytes ≤ 430 MB` (qwen3 pair).

---

## Training loop

| Hyperparameter | Value |
|---|---|
| Optimiser | Adam |
| Learning rate | 1e-3 |
| Loss | HuberLoss |
| Epochs | 15 |
| Mini-batch | 128 |
| Gradient clip | 1.0 (L2 norm) |
| Device | mps |

**Per epoch:**
1. Full pass over `train.parquet` → gradient steps in 128-row mini-batches
2. Full pass over `test.parquet` → avg Huber loss + avg cosine similarity (no gradients)
3. Both metrics logged to stdout and stored in `history`

---

## Output files

```
AI/models/
└── {src}_to_{tgt}.pt          ← one file per pair (56 total)

AI/reports/
├── PIPELINE_REPORT.md         ← this file
└── training_summary.json      ← written after all pairs finish
```

Each `.pt` checkpoint contains:

```python
{
    "state_dict": ...,          # model weights
    "config": {
        "src":        str,      # source model key
        "tgt":        str,      # target model key
        "in_dim":     int,
        "out_dim":    int,
        "hidden_dim": int,
    },
    "history": [                # one entry per epoch
        {"epoch": 1, "train_loss": float, "test_loss": float, "test_cos": float},
        ...
    ],
}
```

---

## Loading a saved mapper

```python
import torch
from adapter_model_training import ResidualMapper

ckpt  = torch.load("models/ada-002_to_te3-small.pt", weights_only=False)
cfg   = ckpt["config"]
model = ResidualMapper(cfg["in_dim"], cfg["out_dim"])
model.load_state_dict(ckpt["state_dict"])
model.eval()

# inference
src_embedding = torch.tensor([...], dtype=torch.float32).unsqueeze(0)  # (1, 1536)
with torch.no_grad():
    tgt_embedding = model(src_embedding)  # (1, 1536)
```

---

## Resumability

`train_pair` skips a pair if `models/{src}_to_{tgt}.pt` already exists. Re-running the script after a crash or Ctrl-C resumes from the first unfinished pair.

---

## Notes on existing classes (not modified)

The original stub (`train_df`, `train_loader`, `test_df`, `test_loader` at module level) uses placeholder paths and empty-string column names. These objects are constructed lazily and never iterated by the mapper pipeline, so they cause no runtime errors. They are preserved as-is per the no-modification constraint.

The `DataLoader(batch_size=256)` in those placeholders would not work correctly with `ParquetIterableDataset` because the dataset already yields full batches — collating 256 of them would produce a wrong tensor shape. The mapper pipeline avoids this by using `batch_size=None` and handling sub-batching explicitly.
