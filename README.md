<p align="center">
  <img src="app/assets/queryn-logo.png" alt="Queryn logo" width="120">
</p>

# Queryn

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)

## Project Abstract

Queryn is an **embedding translation and enrichment engine**: given a text chunk and its existing embedding from Model A, it returns the equivalent embedding in Model B's space — without re-embedding the source corpus. It ships as a local program, invoked directly against a customer's own infrastructure and authenticated with credentials — not a hosted HTTP API. The core problem it solves is that embedding spaces from different models are geometrically incompatible, and every model migration today forces a full, expensive re-embedding job.

Queryn is open source, released under the Apache 2.0 license (see [`LICENSE`](LICENSE)). Contributions, issues, and forks are welcome — see [Contributing](#contributing) below.

**The repository is split into two parts:**

| Part | Purpose |
|---|---|
| [`Adapters/`](#adapters--data-gathering--model-training) | Data gathering and per-model-pair mapper training — builds Layer 0 and produces the trained checkpoints the engine loads. |
| [`app/`](#engine-app) | The Queryn engine itself — the local, credentialed program customers run. **Pre-development.** |

Deeper technical documentation lives in [`docs/`](docs/): [`docs/Adapters.md`](docs/Adapters.md) covers data gathering, architecture research, and how to train Adapters on other datasets, in more depth than this file; [`docs/CHANGELOG.md`](docs/CHANGELOG.md) tracks the roadmap.

The system has three product layers:

- **Layer 0 — Translation Core.** Each model pair is translated by one of two single-hidden-layer architectures — a **linear** mapper or a **deep** (compressed-latent) MLP — trained independently per pair, with the better-performing one kept. See [Adapters — Architectures](#architectures) below for the full rationale and paper citations.
- **Layer 1 — Regex Enrichment.** Deterministic, regex-based signals attached to every chunk at inference time: code detection, URL/identifier presence, path patterns. Output is a `RETRIEVAL_HINT` (`"BM25"` or `"vector"`) the customer's own retrieval stack can act on directly. Auditable, reproducible, zero LLM cost.
- **Layer 2 — Domain Adapters (Phase 2).** Fine-tuned per-customer mappers trained on the customer's own corpus, delivering materially better translation fidelity than the general-purpose model for specialized domains (legal, medical, finance, code).

**Tech stack:** Python · PyTorch · Streamlit (engine GUI) · PyArrow / Parquet · OpenRouter (embedding API) · FastEmbed / ONNX (local inference) · pandas · tiktoken

---

## Adapters — Data Gathering & Model Training

`Adapters/` builds the training data for Layer 0 and trains the per-model-pair mapper checkpoints that the engine loads at runtime.

There are **multiple versions of both the training pipeline and the mapper architectures**, each producing its own separate set of checkpoints and results rather than overwriting the previous version's — see `Adapters/pipelines/` for the versioned pipeline guides (`v0_adapter_model_pipeline_guide.md`, `v1_adapter_model_pipeline_guide.md`, …) and `docs/Adapters.md` for the full version-by-version comparison and results.

### Files

| File | Purpose |
|---|---|
| `dataset_generator.py` | Merges 5 raw datasets into `data/unified_dataset.parquet` |
| `embedding_pipeline.py` | Runs all configured embedding models over the unified dataset |
| `dataset_splitting.py` | Splits `embeddings.parquet` into `data/splits/{train,test}.parquet` (80/20) |
| `data_analysis.py` | Corpus-level analysis of the unified dataset |
| `read_chunks.py` | CLI tool to inspect batch shard files from the terminal |
| `architectures/` | `LinearMapper` and `DeepMapper` — pure `nn.Module` definitions shared across pipeline versions |
| `pipelines/v0_adapter_model_training.py` | v0 mapper training — 56 pairs, `DeepModel` only |
| `pipelines/v1_adapter_model_training.py` | v1 mapper training — 49 pairs, linear vs. deep per pair, best kept |
| `v0_result_analysis.py` / `v1_adapter_analysis.py` | Plot and compare per-pair training results |
| `data/unified_dataset.parquet` | 349,674-row corpus, all domains |
| `data/embeddings/` | Batch shards, per-model parquet files, final wide table |

### Unified Dataset

`dataset_generator.py` merges five sources into a single parquet:

| Source | Rows | Domain |
|---|---|---|
| arXiv abstracts | 287,421 | `science` |
| Australian case law | 24,951 | `legal` |
| SQuAD passages (deduplicated) | 20,233 | `qa` |
| PubMed abstracts (reconstructed) | 11,893 | `medical` |
| Crypto/markets news | 5,176 | `finance` |
| **Total** | **349,674** | |

Output columns: `ID · UUID · TEXT · TOPIC · DOMAIN · SOURCE_FILE · WORD_COUNT · CHAR_COUNT · TOKEN_COUNT · HAS_CODE · HAS_URL · HAS_IDENTIFIERS · RETRIEVAL_HINT · TEXT_QUALITY`

- `ID` — integer 0…N-1, stable primary key for all embedding joins
- `TOKEN_COUNT` — tiktoken `cl100k_base`, used to estimate per-batch token budgets
- `RETRIEVAL_HINT` — Layer 1 signal: `"BM25"` (24% of corpus) or `"vector"` (76%)

### Architectures

Two single-hidden-layer architectures are trained and compared for every model pair; whichever scores higher on held-out cosine similarity is kept (ties go to linear):

- **Linear** (`architectures/linear.py`) — a Procrustes-style linear projection, the baseline every nonlinear mapper is judged against. Motivated by **mini-vec2vec** (Dar, [arXiv:2510.02348](https://arxiv.org/abs/2510.02348)), which shows a purely linear transformation can match or exceed a full nonlinear vec2vec alignment at a fraction of the training cost on near-isomorphic embedding spaces.
- **Deep** (`architectures/deep.py`) — a 2-layer MLP (`Linear → GELU → Linear`) with exactly **one** hidden layer. Motivated by **Vec2Vec** (Gao, [arXiv:2306.12689](https://arxiv.org/abs/2306.12689)), which shows non-linear projection through a latent space outperforms a linear mapping for pairs that aren't near-isomorphic.

The choice to use just **one** hidden layer — rather than committing to either a deeper stack or dropping the hidden layer entirely — is deliberate, for two reasons:

1. **A latent space is sometimes necessary, not always.** Per the Vec2Vec paper, some pairs need a nonlinear bottleneck to translate well; others align almost as well with a single matrix. Training both architectures per pair and keeping whichever wins is how that's measured honestly instead of assumed up front.
2. **Keeping the network as small as possible.** Where a hidden layer is used, it's sized *below* both `in_dim` and `out_dim` (`latent_dim = min(in_dim, out_dim) × 0.5`, floored at 128) rather than wider than either, as in the original v0 pipeline. The hidden layer compresses the source embedding into a shared latent space before expanding it back out to the target dimension — keeping only the signal common to both spaces instead of over-parameterizing on either side's idiosyncrasies, the same reasoning that makes an autoencoder's code layer useful. This was a deliberate size constraint, not a default: the smallest network that could still do the job.

Full reasoning, the v0 → v1 ablation that motivated the switch from an expand-then-project hidden layer to this compressed one, and per-pair results are in `docs/Adapters.md`.

### Results (v1, 49 pairs)

Held-out cosine similarity across all 49 trained pairs: **mean 0.820, median 0.839**. The **linear** architecture won **39 of 49 pairs (80%)** — a direct, measured confirmation of the mini-vec2vec finding that a linear map is often enough once a pair is reasonably aligned; **deep** wins the remaining 10, concentrated on the harder pairs.

- **Best-performing target:** `me5-large` — every source translates into it at `test_cos ≥ 0.90` (mean 0.943); best single pair is `qwen3-emb-8b → me5-large` at **0.954**.
- **Weakest-performing target:** `nemotron-1b-free` — mean 0.688 across all sources; worst single pair is `fastembed-bge-small → nemotron-1b-free` at **0.553**. This model is the clearest current candidate for the "weakest adapters" architecture study in the [roadmap](docs/CHANGELOG.md).
- **v0 → v1 improvement:** mean cosine similarity across the 49 shared pairs rose by **+0.064**. The gain is concentrated in pairs sourced from `pplx-embed-1` and `qwen3-emb-8b` — e.g. `pplx-embed-1 → qwen3-emb-8b` went from 0.413 to 0.797 (+0.384) — confirming the v0 training instability diagnosis (a fixed learning rate overshooting on high-magnitude embeddings) that motivated v1's cosine-similarity loss and `ReduceLROnPlateau` schedule.

Full per-pair numbers, plots, and the linear/deep architecture-comparison breakdown are in `Adapters/reports/v1/` and `docs/Adapters.md`.

### Embedding Pipeline

`embedding_pipeline.py` is a zero-downtime, resumable pipeline that runs the unified dataset through multiple embedding models and produces a wide table of paired embeddings for mapper training.

#### Models

```python
# OpenRouter (paid API)
ada-002          openai/text-embedding-ada-002         dim=1536  $0.10/M tokens
te3-small        openai/text-embedding-3-small         dim=1536  $0.02/M tokens
qwen3-emb-8b     qwen/qwen3-embedding-8b               dim=4096  $0.01/M tokens
bge-m3           baai/bge-m3                           dim=1024  $0.01/M tokens
me5-large        intfloat/multilingual-e5-large        dim=1024  $0.01/M tokens
pplx-embed-1     perplexity/pplx-embed-v1-0.6b        dim=1024  $0.004/M tokens
nemotron-1b-free nvidia/llama-nemotron-embed-vl-1b-v2  dim=2048  free

# Local (FastEmbed / ONNX, no API key)
fastembed-bge-small   BAAI/bge-small-en-v1.5   dim=384   batch_size=256
```

Total estimated cost for the full 349k-row corpus: ~$14.

#### Output Layout

```
data/embeddings/
├── {model_key}/
│   └── batches/
│       ├── batch_000000000.parquet   ← atomic shard (96 rows)
│       ├── batch_000000096.parquet
│       └── …
├── {model_key}.parquet               ← merged model file (all rows)
├── {model_key}_checkpoint.json       ← resume state
└── embeddings.parquet                ← final wide table (ID + all model columns)
```

Each shard has two columns: `ID (int64)` and `{model_key}-EMBEDDING (fixed_size_list<float>[dim])`.

#### Workflow — Step by Step

The pipeline is structured as a Zed REPL file with `# %%` cell delimiters. Run cells in order:

**1. `# %% [run all models]`**

Iterates over every model in `EMBEDDING_MODELS`. For each:
- Loads the unified dataset sorted by `ID` (stable order → same batch boundaries on every resume)
- Reads the checkpoint to find already-completed batches, skips them
- Truncates each text to the model's `max_chars` limit before sending
- Calls the embedding API (OpenRouter or FastEmbed)
- Writes each completed batch atomically: `batch_{i:09d}.tmp.parquet` → `batch_{i:09d}.parquet` (POSIX rename)
- Updates the checkpoint JSON atomically after each successful flush

On SIGINT / SIGTERM the current batch completes and the process exits cleanly. Re-running the script resumes from the first incomplete batch.

**2. `# %% [merge batch shards per model]`**

Streams all shards for each model through a `pq.ParquetWriter` into a single `{model_key}.parquet`, preserving the `fixed_size_list<float>[dim]` schema. Atomic write (tmp → rename).

**3. `# %% [validate shard health]`**

Reads every shard for every model and prints null counts, schema type, and the first embedding value. Use this cell — not a GUI parquet viewer — to verify data integrity. Most parquet viewer apps cannot render `fixed_size_list` columns and display them as NULL even when the data is correct.

**4. `# %% [build final wide embeddings table]`**

Builds `embeddings.parquet` using pure PyArrow (no pandas merge). Only **fully-complete** models (row count == 349,674, zero nulls) are included — partial models are listed and skipped. Validates the output with a read-back check and reports null count + type per column.

#### Resilience Details

| Failure mode | Handling |
|---|---|
| Network error / timeout | Exponential backoff with jitter, up to 6 retries |
| HTTP 429 rate limit | Respects `Retry-After` header, then backoff |
| HTTP 402 credits exhausted | Clean stop, checkpoint preserved, resume on re-run |
| Token limit exceeded (per-batch or per-text) | Texts trimmed proportionally to fit budget, up to 3 retries |
| Crash mid-flush | `.tmp.parquet` left on disk (not visible to merge), next run re-embeds that batch |
| Script killed (SIGINT) | Current batch completes, then exits; checkpoint intact |

#### Reading Shards

```bash
python read_chunks.py                    # list all models and shard counts
python read_chunks.py ada-002            # list every shard with null counts
python read_chunks.py ada-002 0          # print first embedding from batch 0
```

#### Requirements

```
pyarrow
pandas
fastembed
httpx
tiktoken
python-dotenv
torch
```

`.env` file required for OpenRouter models:
```
OPENROUTER_API_KEY=sk-or-v1-...
```

---

## Engine (`app/`)

**Status: pre-development.** `app/` is scaffolded but not yet functional — `main.py`, `controllers/`, `services/migrator.py`, `core/adapters/`, and `core/connectors/` exist as empty stubs.

Planned structure:

- **GUI** — a basic interface built with **Streamlit**.
- **Adapters** (`core/adapters/`) — pair-to-pair translators: load a trained checkpoint from `Adapters/models/` and translate a single embedding from model A's space into model B's space.
- **Connectors** (`core/connectors/`) — vector database connectors: read and write embeddings against a customer's own vector DB.

This is the local, credentialed program described in the [Project Abstract](#project-abstract) above — not a hosted API.

---

## Contributing

Issues and PRs are welcome. See [`docs/Adapters.md`](docs/Adapters.md) for how to run the Adapters pipelines against your own dataset or architecture, and [`docs/CHANGELOG.md`](docs/CHANGELOG.md) for the current roadmap.

## License

Apache License 2.0 — see [`LICENSE`](LICENSE) for the full text.
