# Adapters — Data Gathering & Architecture Research

This document is the deep-dive companion to the [`Adapters/` section of the root README](../README.md#adapters--data-gathering--model-training). It covers where the training data comes from, why the mapper architectures are built the way they are (with paper citations and reasoning), how the pipeline versions differ, and how to point the same pipelines at a different dataset or a new architecture.

---

## 1. Data Gathering

`dataset_generator.py` merges five public sources into one corpus (`data/unified_dataset.parquet`, 349,674 rows), each contributing a distinct domain so that mapper training and evaluation aren't biased toward one register of text:

| Source | Rows | Domain | Why included |
|---|---|---|---|
| arXiv abstracts | 287,421 | `science` | Bulk volume, dense technical vocabulary, code/identifier-adjacent text |
| Australian case law | 24,951 | `legal` | Long-form, formal, domain-specific jargon — stress-tests translation fidelity outside general web text |
| SQuAD passages (deduplicated) | 20,233 | `qa` | Short, clean, general-domain passages — a "how well does this work on easy text" control |
| PubMed abstracts (reconstructed) | 11,893 | `medical` | Another specialized-vocabulary domain, distinct from legal |
| Crypto/markets news | 5,176 | `finance` | Recent, informal, entity-and-number-dense text |

Each row also gets deterministic, regex-derived metadata computed at generation time — `HAS_CODE`, `HAS_URL`, `HAS_IDENTIFIERS`, and the derived `RETRIEVAL_HINT` (`BM25` vs `vector`) — which is Layer 1's signal, piggybacked onto the same corpus rather than generated separately.

`embedding_pipeline.py` then runs every row through every configured embedding model (see the model table in the README) to produce `(text, embedding_A, embedding_B, …)` tuples for every model in the pool — this is the paired training data the mappers below are trained on. `dataset_splitting.py` deterministically splits the resulting wide table 80/20 (`SEED=42`) into `data/splits/{train,test}.parquet`, streamed row-group-by-row-group so the ~18 GB embeddings table is never fully loaded into memory.

---

## 2. Why This Architecture — Paper Grounding

Queryn's mapper design rests on two papers, used for two different (complementary, not competing) claims:

### Vec2Vec — justifying the use of a latent space

**Vec2Vec: A Compact Neural Network Approach for Transforming Text Embeddings with High Fidelity** ([arXiv:2306.12689](https://arxiv.org/abs/2306.12689))

Vec2Vec shows that a compact nonlinear network — projecting through a hidden latent space — outperforms a purely linear mapping when translating between embedding spaces that aren't already near-isomorphic. This is the justification for the **deep** architecture (`Adapters/architectures/deep.py`): a 2-layer MLP (`Linear → GELU → Linear`) that gives the mapper a nonlinear bottleneck to work with when a straight linear projection isn't enough.

### mini-vec2vec — justifying the linear architecture

**mini-vec2vec: Scaling Universal Geometry Alignment with Linear Transformations** (Dar, [arXiv:2510.02348](https://arxiv.org/abs/2510.02348))

mini-vec2vec shows that a purely linear transformation can match or exceed the alignment quality of a full nonlinear vec2vec-style approach, at a fraction of the computational cost, on embedding spaces that are already close to isomorphic. This is the justification for training the **linear** architecture (`Adapters/architectures/linear.py`) as a first-class candidate rather than only as a discard-able baseline: for pairs where the source and target spaces are near-isomorphic, the linear mapper isn't a fallback — it's frequently the better answer, and much cheaper to train and run.

**How the two are reconciled in the pipeline:** rather than picking one architecture up front, v1 of the training pipeline trains *both* per pair and keeps whichever wins on held-out cosine similarity (ties go to linear). This turns "linear vs. nonlinear" from an assumption into a measured, per-pair, honest result — see §4 for the mechanics.

### Why exactly one hidden layer, not zero or several

Given that a latent space is sometimes warranted (Vec2Vec) and sometimes not (mini-vec2vec), the deep architecture is deliberately kept to the *minimum* nonlinear structure needed to test that question — a single hidden layer — for two concrete reasons:

1. **The latent space is a hypothesis to test per pair, not a default to commit to.** Since some pairs align well linearly and others need nonlinearity, going straight to a deep, multi-hidden-layer network would make it impossible to tell how much of a deep model's advantage (if any) actually comes from nonlinearity versus from raw parameter count. One hidden layer is the smallest structure that lets the comparison isolate the effect Vec2Vec claims.
2. **Keep the network as small as possible.** Beyond just "one" hidden layer, its *width* is constrained too: `latent_dim = min(in_dim, out_dim) × 0.5`, floored at 128 — strictly smaller than both the input and output dimensions, not wider (v0's `DeepModel` used `hidden = min(max(in_dim, out_dim), 2048)`, an expand-then-project width that gave the network room to overfit per-model idiosyncrasies rather than the signal shared between the two spaces). The v1 `DeepMapper` compresses the source embedding into this smaller latent space before expanding back out to the target dimension — the same reasoning that makes an autoencoder's code layer useful: forcing the bottleneck below both dimensions keeps only the signal common to both embedding spaces.

---

## 3. Architectures — Specification

Both live in `Adapters/architectures/`, are pure `nn.Module` definitions (no optimizer/loss/training-loop logic), and are shared across pipeline versions via `ARCHITECTURES = {"linear": LinearMapper, "deep": DeepMapper}` in `architectures/__init__.py`.

### `LinearMapper` (`architectures/linear.py`)

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

The Procrustes-style baseline. No hyperparameters beyond `in_dim`/`out_dim`. Normalizes its own input and output to unit vectors internally — training and evaluation both optimize/measure cosine similarity, which is invariant to input magnitude, so normalization is baked into the saved model rather than left as a contract the caller has to remember.

### `DeepMapper` (`architectures/deep.py`)

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

`latent_dim = max(int(min(in_dim, out_dim) * latent_ratio), min_latent)` with defaults `latent_ratio=0.5`, `min_latent=128` — always strictly smaller than both `in_dim` and `out_dim`. No residual/skip connection: input and latent live in different, differently-shaped spaces, so there's no identity path to add back.

---

## 4. Pipeline Versions — What Changed and Why

Multiple versions of the training pipeline exist side by side, each writing to its own output directory so results never collide (`models/*.pt` + `reports/v0/` for v0, `models/v1/*.pt` + `reports/v1/` for v1). This lets every version's results be compared directly rather than overwritten.

### v0 (`pipelines/v0_adapter_model_training.py`)

- **56 pairs** — all `N × (N-1)` directed pairs across the 8 configured models.
- Single architecture: `DeepModel` only (no linear baseline actually trained, despite one being defined).
- `hidden = min(max(in_dim, out_dim), 2048)` — an **expand**-then-project hidden layer.
- Loss: `HuberLoss` on raw embedding magnitude.
- Fixed `lr=1e-3` for all 15 epochs, no LR scheduling.
- Checkpoint: last epoch, unconditionally — several pairs peaked early and degraded afterward (e.g. `pplx-embed-1_to_ada-002` hit `test_cos=0.858` at epoch 1 but the saved epoch-15 checkpoint was `0.558`).
- Device hardcoded to `"mps"`.

### v1 (`pipelines/v1_adapter_model_training.py`)

Supersedes v0. Full list of changes and the reasoning behind each is in `pipelines/v1_adapter_model_pipeline_guide.md`; summarized here:

| | v0 | v1 |
|---|---|---|
| Pairs | 56 | **49** — `ada-002` dropped as a target (deprecated by its provider; stays valid as a *source*) |
| Architecture source | defined inline | imported from `Adapters/architectures/` |
| Hidden-layer sizing | expand: `min(max(in_dim,out_dim), 2048)` | **compress**: `latent < min(in_dim,out_dim)` |
| Architectures trained per pair | 1 (deep only) | **2** (linear, deep) — best kept, ties → linear |
| Checkpoint saved | last epoch | **best epoch**, by `test_cos` |
| Loss | `HuberLoss` on raw magnitude | `1 - cosine_similarity`, directly |
| LR schedule | fixed | `ReduceLROnPlateau(mode="max", factor=0.5, patience=2)` on `test_cos` |
| Device | hardcoded `"mps"` | detected, falls back to CPU |

The net effect: v1 produces an honest linear-vs-nonlinear ablation per pair (the `architecture_comparison` block in every checkpoint records both architectures' best scores, not just the winner's), fixes the early-peak/late-degrade issue with best-epoch checkpointing, and trains directly against the metric the product cares about (cosine similarity) instead of an L2-family proxy.

### Results

Per-pair results for each version are written to `reports/{version}/training_report.json` and can be plotted/compared with `v0_result_analysis.py` / `v1_adapter_analysis.py`, which group pairs by source model, color by target model, and (for v1) mark the winning architecture per pair (`○` linear, `▲` deep). Use these scripts — not a one-off read of the JSON — to compare a new pipeline version's results against the existing ones, since the plotting keeps model→color mapping stable across runs for a fair visual comparison.

---

## 5. Training a New Dataset or Architecture

The pipelines are designed so a new dataset or a new architecture can be dropped in without touching the rest of the flow:

**New dataset:**
1. Replace or extend `dataset_generator.py`'s sources, keeping the same output schema (`ID · TEXT · …`, see the README's Unified Dataset section for the full column list) — `ID` must stay a stable 0…N-1 integer key.
2. Run `embedding_pipeline.py` to produce paired embeddings for the new corpus. Add any new embedding model to `EMBEDDING_MODELS` first if needed.
3. Run `dataset_splitting.py` to produce a fresh `data/splits/{train,test}.parquet`.
4. Point a training pipeline (`v1_adapter_model_training.py` or later) at the new splits and run it — resumability means a crash or Ctrl-C just picks back up from the first unfinished pair.

**New architecture:**
1. Add a pure `nn.Module` (no optimizer/loss/training loop) to `Adapters/architectures/`, following `LinearMapper`/`DeepMapper` as templates — in particular, keep input/output normalization *inside* `forward()` so a raw, arbitrary-magnitude embedding always produces a correct unit-norm output with no caller-side preprocessing contract.
2. Register it in `ARCHITECTURES` in `architectures/__init__.py`. Dict order determines tie-break behavior in pipelines that compare multiple architectures per pair (first key wins ties).
3. Point a training pipeline at it — the pipeline iterates whatever's in `ARCHITECTURES`, so no pipeline code needs to change to add a third candidate architecture.

**Loading any saved mapper** (works the same across architectures, since normalization is internal to each model):

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

## References

- Gao, A. K., **Vec2Vec: A Compact Neural Network Approach for Transforming Text Embeddings with High Fidelity**. [arXiv:2306.12689](https://arxiv.org/abs/2306.12689).
- Dar, G., **mini-vec2vec: Scaling Universal Geometry Alignment with Linear Transformations**. [arXiv:2510.02348](https://arxiv.org/abs/2510.02348).
