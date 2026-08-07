# Adapter Model Training Pipeline — v1

## Overview

`v1_adapter_model_training.py` trains **49 directed embedding-space
mappers** using the split dataset produced by `dataset_splitting.py`. It
supersedes `v0_adapter_model_training.py`: fewer pairs, architectures
imported from a shared `architectures/` package instead of defined inline,
best-epoch checkpointing instead of always saving the last epoch, and a
per-pair choice between two independently-trained architectures instead of
committing to one.

This file replaces the version that was previously an unmodified copy of
`v0_adapter_model_pipeline_guide.md`.

---

## What changed from v0

| | v0 | v1 |
|---|---|---|
| Pairs | 56 (N×(N-1), all 8 models) | **49** — `ada-002` dropped as a target |
| Architecture source | defined inline in the pipeline script | imported from `Adapters/architectures/` |
| Hidden-layer sizing | expand: `min(max(in_dim,out_dim), 2048)` | compress: `latent < min(in_dim,out_dim)` |
| Architectures trained per pair | 1 (`DeepModel` only) | 2 (`linear`, `deep`), best one kept |
| Checkpoint saved | last epoch, unconditionally | best epoch, by `test_cos` |
| Loss function | `HuberLoss` on raw embedding magnitude | `1 - cosine_similarity`, directly |
| Optimizer schedule | fixed `lr=1e-3` for all 15 epochs | `ReduceLROnPlateau` on `test_cos` |
| Linear baseline | defined (`linearModel`) but never trained or compared | trained and compared every pair |
| Device | hardcoded `"mps"` | detected via `torch.backends.mps.is_available()`, falls back to CPU |

### Why each change

**Dropping `ada-002` as a target.** `ada-002` is being deprecated by its
provider. It stays in `MODEL_DIMS` and as a valid *source* — existing
customers still hold corpora embedded with it and need a mapper off of it —
but nothing should be trained to produce new embeddings in a space that's
going away. This removes exactly the `N-1 = 7` pairs where `tgt ==
"ada-002"`.

**Architectures moved to a package.** `Adapters/architectures/` now holds
pure `nn.Module` definitions only — no optimizer, loss, or training loop.
`linear.py` → `LinearMapper`, `deep.py` → `DeepMapper`. Any future pipeline
version imports what it needs from there instead of redefining it inline,
so the model spec and the training orchestration can no longer drift out
of sync with each other silently.

**Compressed latent space instead of expansion.** v0's `DeepModel` used a
hidden layer *wider* than both `in_dim` and `out_dim` (up to a 2048 cap).
v1's `DeepMapper` inverts that: the hidden layer (`latent_dim =
min(in_dim, out_dim) * 0.5`, floored at 128) is *smaller* than both sides.
The hypothesis this tests: a wide hidden layer gives the network enough
free parameters to fit per-model idiosyncrasies that don't transfer, where
a bottleneck forces it to keep only the signal common to both embedding
spaces — the same reasoning that makes an autoencoder's code layer useful.
No residual/skip connection is used anywhere — not inside `DeepMapper`,
and not between `DeepMapper` and `LinearMapper` (they are trained fully
independently; the pipeline only compares their scores after training).

**Two architectures trained, best one kept.** v0 defined a linear baseline
(`linearModel`) but never actually trained or compared it — every pair
went straight to the MLP, so there was no way to tell which pairs actually
needed nonlinearity versus which would've done just as well (or better,
given v0's instability on some pairs) with a single matrix. v1 trains both
`linear` and `deep` for every pair and keeps whichever scores higher on
`test_cos`. **Ties go to `linear`** — if `deep` doesn't strictly beat the
linear baseline, the simpler model is saved. This also finally delivers
the honest linear-vs-nonlinear ablation story the project's benchmarking
strategy calls for.

**Best-epoch checkpointing.** v0 always saved the final epoch's weights.
Several v0 pairs peaked early and then degraded — e.g.
`pplx-embed-1_to_ada-002` hit `test_cos=0.858` at epoch 1 but the saved
checkpoint (epoch 15) was `0.558`. v1 tracks the best `test_cos` seen
across all `EPOCHS` for each architecture and keeps that epoch's
`state_dict`, discarding the rest.

**Cosine similarity loss and LR scheduling.** Two related v0 issues, fixed
together:

1. v0 trained `HuberLoss` on raw embedding magnitude, which isn't what the
   product measures or what a vector DB compares on (cosine similarity).
2. Several v0 pairs — specifically sources with high dimension or large
   raw magnitude (`qwen3-emb-8b`, `pplx-embed-1`) — showed real training
   instability: not overfitting (train loss itself oscillated epoch to
   epoch, not just test loss), but the optimizer overshooting a fixed,
   too-large learning rate given the embedding scale.

v1 trains directly against `cosine_loss(preds, targets) = 1 -
F.cosine_similarity(preds, targets, dim=-1).mean()` instead of Huber —
there's no approximation step, the loss *is* `1 - test_cos`, so gradient
descent is optimizing the exact metric the report cares about.
`F.cosine_similarity` normalizes both arguments internally, so neither
`preds` nor `targets` need pre-normalization at the loss. On top of that,
each architecture's Adam optimizer is wrapped in
`ReduceLROnPlateau(mode="max", factor=0.5, patience=2)` keyed on
`test_cos`, so a pair that stops improving (or starts oscillating) gets
its learning rate cut instead of continuing to bounce around a minimum for
the rest of its 15 epochs.

**Normalization moved inside the model.** The pipeline itself no longer
normalizes anything — `LinearMapper` and `DeepMapper` (in
`Adapters/architectures/`) each L2-normalize their own input on the way in
and their own output on the way out, inside `forward()`. Earlier this was
external (`_normalize` applied to `X`/`y` in the training loop), which
meant correctness at inference time depended on the caller remembering to
replicate that preprocessing — nothing in the saved `.pth` file enforced
it, since L2-normalize has no learned parameters to persist (unlike, say,
a fitted scaler with a saved mean/std). A raw, arbitrary-magnitude
embedding fed straight into a loaded model now produces a correct
unit-norm output with no manual normalization step required. This changes
*where* normalization happens, not the math — cosine similarity is
invariant to normalizing one side before comparing, so no metric or loss
value changed as a result of this move.

**Apple Silicon device selection.** v0 hardcoded `DEVICE = "mps"`, which
throws at the first `.to("mps")` call if the backend isn't actually usable
— e.g. torch installed without MPS support, or the Python interpreter
itself running as x86_64 under Rosetta on M-series hardware (a real
gotcha with older conda/venv setups, not a hypothetical). v1's
`_select_device()` checks `torch.backends.mps.is_available()` and falls
back to CPU with a logged warning instead of crashing.

---

## Model pairs

8 configured models, `ada-002` excluded as a target → **49 directed
pairs**.

| Model | Dim | Valid as target? |
|---|---|---|
| ada-002 | 1536 | no (deprecated) |
| te3-small | 1536 | yes |
| qwen3-emb-8b | 4096 | yes |
| bge-m3 | 1024 | yes |
| me5-large | 1024 | yes |
| pplx-embed-1 | 1024 | yes |
| nemotron-1b-free | 2048 | yes |
| fastembed-bge-small | 384 | yes |

---

## Architectures — `Adapters/architectures/`

```
Adapters/architectures/
├── __init__.py   ← exports LinearMapper, DeepMapper, ARCHITECTURES
├── linear.py      ← LinearMapper
└── deep.py         ← DeepMapper
```

`ARCHITECTURES = {"linear": LinearMapper, "deep": DeepMapper}` — an
ordered dict. `train_pair` iterates it to decide what to train, and the
order determines the tie-break (`linear` first ⇒ `linear` wins ties).

### `LinearMapper`

```
input (in_dim)
    │
    ▼
L2-normalize
    │
    ▼
Linear(in_dim → out_dim)
    │
    ▼
L2-normalize
    │
    ▼
output (out_dim), unit norm
```

The Procrustes-style baseline. No hyperparameters beyond `in_dim`/`out_dim`.

### `DeepMapper`

```
input (in_dim)
    │
    ▼
L2-normalize
    │
    ▼
Linear(in_dim → latent_dim) → GELU
    │
    ▼
Linear(latent_dim → out_dim)
    │
    ▼
L2-normalize
    │
    ▼
output (out_dim), unit norm
```

`latent_dim = max(int(min(in_dim, out_dim) * latent_ratio), min_latent)`
with defaults `latent_ratio=0.5`, `min_latent=128` — always strictly
smaller than both `in_dim` and `out_dim`. No residual connection.

Both classes are plain `nn.Module`s with no optimizer or loss attached —
those live in the pipeline (`train_architecture` in
`v1_adapter_model_training.py`), constructed fresh per architecture per
pair. Both normalize their own input and output internally (see "Loading
a saved mapper" below) — raw embeddings, any magnitude, go in and out.

---

## Data pipeline

Unchanged from v0:

```
data/splits/train.parquet  (279,739 rows)
data/splits/test.parquet   ( 69,935 rows)
```

`ParquetIterableDataset` streams via `pq.ParquetFile.iter_batches
(batch_size=8192)`, loading only the source and target embedding columns.
`DataLoader(dataset, batch_size=None)` disables collation; the 8192-row
chunk is sub-batched into `BATCH_SIZE=128` mini-batches inside
`train_architecture`. Two independent `DataLoader`s per architecture are
constructed per pair (the underlying dataset re-opens the parquet file on
each `__iter__`), so the linear and deep runs see the exact same data in
the same order.

---

## Training loop

| Hyperparameter | Value |
|---|---|
| Optimizer | Adam |
| Initial learning rate | 1e-3 |
| LR schedule | `ReduceLROnPlateau(mode="max", factor=0.5, patience=2)` on `test_cos` |
| Loss | `1 - cosine_similarity(pred, target)` |
| Epochs (per architecture) | 15 |
| Mini-batch | 128 |
| Gradient clip | 1.0 (L2 norm) |
| Device | `mps` if available, else `cpu` (`_select_device()`) |
| Architectures trained per pair | 2 (`linear`, `deep`) |

**Per epoch, per architecture:**
1. Full pass over `train.parquet` (raw `x`, `y`, no pipeline-side
   preprocessing) → gradient steps in 128-row mini-batches,
   `cosine_loss(model(x), y)` — normalization happens inside `model(x)`.
2. Full pass over `test.parquet` → avg cosine loss + avg cosine similarity
   (no gradients) — the two are related by `test_loss ≈ 1 - test_cos`.
3. `scheduler.step(test_cos)`.
4. If `test_cos` improved, snapshot the current `state_dict` (CPU, cloned)
   as the new best.
5. Metrics (including current LR) logged to stdout and stored in `history`.

**Per pair, after both architectures finish:** compare `best_test_cos`
between `linear` and `deep`; save the winner's best-epoch weights. Ties go
to `linear`.

---

## Output files

```
Adapters/models/v1/
└── {src}_to_{tgt}.pt          ← one file per pair (49 total), winning architecture only

Adapters/reports/v1/
├── v1_adapter_model_pipeline_guide.md   ← this file
└── training_report.json                 ← written after all pairs finish
```

Note: v1 writes to `models/v1/` and `reports/v1/`, separate from v0's flat
`models/*.pt` and `reports/v0/` — the two pipelines' outputs never collide,
and v0's 56 already-trained checkpoints are left untouched.

Each `.pt` checkpoint contains:

```python
{
    "state_dict": ...,          # winning architecture's best-epoch weights
    "config": {
        "src":          str,
        "tgt":          str,
        "in_dim":       int,
        "out_dim":      int,
        "architecture": str,      # "linear" or "deep"
        "arch_kwargs":  dict,     # e.g. {"latent_dim": 512} for "deep", {} for "linear"
        "best_epoch":   int,      # 1-indexed epoch the saved weights came from
        "self_normalizing": True, # informational — model normalizes its own I/O, not a caller contract
    },
    "history": [                 # winning architecture's per-epoch history
        # train_loss/test_loss are cosine loss (1 - cosine_similarity); test_loss ≈ 1 - test_cos
        {"epoch": 1, "train_loss": float, "test_loss": float, "test_cos": float, "lr": float},
        ...
    ],
    "architecture_comparison": {  # every architecture's own best epoch — the ablation record
        "linear": {"best_epoch": int, "best_test_cos": float, "arch_kwargs": {}},
        "deep":   {"best_epoch": int, "best_test_cos": float, "arch_kwargs": {...}},
    },
}
```

`training_report.json` (top level) mirrors this per pair under `"pairs"`,
plus run-level fields (`device`, `epochs`, `batch_size`, `architectures`,
`total_pairs`, `total_time_min`) — same shape `result_analysis.py` already
expects at `reports/v1/training_report.json`, so the existing plotting
script works against v1 output unmodified.

---

## Loading a saved mapper

No manual normalization step needed — `LinearMapper`/`DeepMapper`
normalize their own input and output inside `forward()` (see
"Architectures" above), so a raw, arbitrary-magnitude embedding can be fed
straight in and a unit-norm embedding comes straight out.

```python
import torch
from architectures import ARCHITECTURES

ckpt  = torch.load("models/v1/te3-small_to_bge-m3.pt", weights_only=False)
cfg   = ckpt["config"]
model = ARCHITECTURES[cfg["architecture"]](cfg["in_dim"], cfg["out_dim"], **cfg["arch_kwargs"])
model.load_state_dict(ckpt["state_dict"])
model.eval()

src_embedding = torch.tensor([...], dtype=torch.float32).unsqueeze(0)  # (1, in_dim), any magnitude
with torch.no_grad():
    tgt_embedding = model(src_embedding)  # (1, out_dim), unit norm
```

---

## Resumability

`train_pair` skips a pair if `models/v1/{src}_to_{tgt}.pt` already exists
— unchanged behavior from v0, just pointed at the v1 output directory.
Re-running the script after a crash or Ctrl-C resumes from the first
unfinished pair. Note the skip is per-*pair*, not per-architecture: an
interrupted pair re-trains both `linear` and `deep` from scratch on
resume, since neither's `best_state_dict` is persisted until the pair as a
whole finishes.
