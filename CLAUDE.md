This file provides guidance when working with code in this repository.
Before any task involving project or planning context: use the `obsidian` MCP server to read `00_AI_GUIDE.md` from the vault root first, then follow its instructions before proceeding.

# What this repo is

Queryn is an **embedding translation engine**: given a text chunk and its embedding from Model A, return the equivalent embedding in Model B's space — without re-embedding the source corpus. It ships as a local program, invoked directly against a customer's own infrastructure and authenticated with credentials — not a hosted HTTP API. This directory contains the **dataset construction pipeline only**. The mapper training and the local program are elsewhere.

Three product layers:
- **Layer 0** — MLP mapper (per model pair, 1 hidden layer, GELU, Huber loss) trained on (text, embedding_A, embedding_B) triples. Non-linear over linear per Vec2Vec (arxiv:2306.12689); residual connections deferred to a later training phase.
- **Layer 1** — Deterministic regex signals: code detection, URL/identifier presence → `RETRIEVAL_HINT` (`"BM25"` or `"vector"`)
- **Layer 2** — Domain-adapted fine-tuned mappers per customer corpus (Phase 2)

## Running the pipeline

There are no build steps, test suites, or linters. The workflow is two Python scripts run directly:

```bash
# Step 1 — generate the unified training corpus (run once, or to regenerate after corruption)
cd Adapters/
python dataset_generator.py

# Step 2 — embed with all configured models (resumable — safe to Ctrl-C and re-run)
python embedding_pipeline.py

# Inspect shard data from the terminal (GUI parquet viewers cannot render fixed_size_list columns)
python read_chunks.py ada-002
```

Requires a `.env` file at the repo root or `Adapters/` directory:
```
OPENROUTER_API_KEY=sk-or-v1-...
```

## Architecture of the embedding pipeline

`embedding_pipeline.py` is structured as `# %%` cells (Jupyter/Zed REPL style) that run top-to-bottom. Each cell is also designed to run standalone:

| Cell | What it does |
|---|---|
| `[run all models]` | Main loop — embeds all 349,674 rows for each model in `EMBEDDING_MODELS`, writing atomic shards |
| `[merge batch shards per model]` | Concatenates all `batch_*.parquet` shards for each model into one file |
| `[validate shard health]` | Reads every shard, prints null counts + schema — the only reliable way to verify data |
| `[build final wide embeddings table]` | Joins complete models into `embeddings.parquet` (ID + all embedding columns) |

**Resumability:** a `{model_key}_checkpoint.json` tracks completed batch start-indices. The dataframe is always sorted by `ID` before batching, so batch boundaries are stable across restarts. On Ctrl-C the current batch finishes, then the script exits cleanly — merge and final-build cells are skipped on interrupt.

**Atomic writes:** every shard write goes through `file.tmp.parquet` → `os.replace()` → `file.parquet`. A crashed mid-write leaves only a `.tmp` file, which is ignored by merge.

**RAM:** the final table builder uses `memory_map=True` + chunked row-group writes (2,000 rows at a time). Peak RAM is ~100 MB regardless of how many models or rows are complete.

## Token limit handling in `embed_openrouter`

OpenRouter returns HTTP 200 with `{"error": {...}}` (no `"data"` key) for token-limit violations. The handler catches all known provider error formats via regex, extracts the actual limit and requested count, then proportionally truncates all texts in the batch and retries up to 3 times (`_trunc` parameter). Adding a new format means adding one string to `any(phrase in err_msg for phrase in (...))` and two regexes (one for requested count, one for limit).

## Output layout

```
Adapters/data/
├── unified_dataset.parquet          ← 349,674 rows, 14 columns (written by dataset_generator.py)
└── embeddings/
    ├── {model_key}/batches/         ← atomic shards, 96 rows each
    ├── {model_key}_checkpoint.json  ← completed batch indices
    ├── {model_key}.parquet          ← merged model file
    └── embeddings.parquet           ← final wide table: ID + all model embedding columns
```

The `data/` directory is gitignored.

## Key schema detail

Embedding columns use PyArrow's `fixed_size_list<element: float>[dim]` type — **not** a list of lists. This type is not renderable by most GUI parquet viewers (they display NULL even when data is present). Always use `read_chunks.py` or the `[validate shard health]` cell to inspect embedding data.

## Configured embedding models

| Key | Provider | dim | Notes |
|---|---|---|---|
| `ada-002` | OpenRouter | 1536 | Mandatory baseline |
| `te3-small` | OpenRouter | 1536 | Ada migration pair |
| `qwen3-emb-8b` | OpenRouter | 4096 | Highest dim |
| `bge-m3` | OpenRouter | 1024 | |
| `me5-large` | OpenRouter | 1024 | 512-token context → `max_chars=1800` |
| `pplx-embed-1` | OpenRouter | 1024 | 120k token batch limit |
| `nemotron-1b-free` | OpenRouter | 2048 | Free tier, conservative `batch_size=32` |
| `fastembed-bge-small` | Local ONNX | 384 | No API key needed |

`fastembed-bge-large` is commented out.
