# Changelog & Roadmap

The near-term plan is to get the local migration engine (`app/`) usable as fast
as possible, building directly on what already ships: the trained adapter models
and the training dataset. Rationale for the architecture choices below is kept in
a team working note (`docs/engine-design-decisions.md`, not committed).

---

## Shipped

### Adapter models — on Hugging Face

- The **v1 adapters are published as ONNX**, one model repo per directed pair
  (49 pairs), all gathered into a collection. Each repo carries `model.onnx` +
  `config.json` (dims, IO contract, provenance) and a `model.safetensors` copy
  as the pickle-free source of truth, plus a generated model card with metrics,
  an `onnxruntime` usage snippet, and the training plots.
- Pipeline: `Adapters/ptConverter.py` converts the `.pt` checkpoints
  (`architectures/` rebuild → ONNX opset 17, dynamic batch axis, internal
  L2-normalize baked in) and writes a `manifest.json` with per-file sha256;
  `Adapters/hf_upload.py` creates/updates the repos and the collection.

### Training dataset — on Kaggle

- One Kaggle dataset with two top-level folders — `text/` (the five raw source
  corpora) and `embeddings/` (per-model embedding parquets + the joined
  `embeddings.parquet`) — packaged and published by `Adapters/kaggle_upload.py`
  (hard-linked staging, generated README + per-source `LICENSE` manifest +
  `dataset-metadata.json`).
- Source corpora and their licenses:

  | Corpus | Kaggle | License |
  |---|---|---|
  | arXiv abstracts | `sumitm004/arxiv-scientific-research-papers-dataset` | Apache 2.0 |
  | Australian case law | `amohankumar/legal-text-classification-dataset` | Apache 2.0 |
  | SQuAD passages | `ananthu017/squad-csv-format` | CC0 (CC BY-SA 4.0 upstream) |
  | PubMed RCT abstracts | `matthewjansen/pubmed-200k-rtc` | CC0 |
  | Financial/markets news | `belbino/financial-news-sentiment-vs-market-2020-present` | CC0 |

### Adapters pipeline

- Unified **349,674-row, five-domain corpus** (`dataset_generator.py`) and an
  embedding pipeline across **8 models** (`embedding_pipeline.py`) — resumable,
  atomic-shard writes, checkpointed.
- Two generations of per-pair mapper training:
  - **v0** — 56 directed pairs, single deep architecture, last-epoch checkpointing.
  - **v1** — 49 directed pairs (`ada-002` dropped as a target), linear vs. deep
    trained and compared per pair with the winner kept, best-epoch checkpointing,
    cosine-similarity loss with LR scheduling.

### Engine boilerplate (`app/`)

- **Architecture scaffold done** — real module boundaries and state layer, with
  mock implementations for the parts that touch a customer's infrastructure, so
  the engine runs end-to-end as a demo (`uv run uvicorn main:app`).
- Layout follows the planned convention: `core/` (domain types + persistence),
  `core/connectors/` + `core/adapters/` (`Protocol` + a mock impl each),
  `services/migrator.py` (serial job runner), `controllers/`, `endpoints/v1/`
  (FastAPI routers), `helpers/`, plus `templates/` + `static/`.
- State split wired up for real: **SQLite** job registry (`queryn.db`, WAL),
  append-only **`progress.jsonl`** per job, atomic **`checkpoint.json`**,
  **`providers.yaml`** (key status from env, never the value). Interrupt →
  resume-from-checkpoint verified.
- Dashboard: FastAPI + Jinja2 + HTMX, no build step — job list, live progress
  panel (self-terminating poll), adapter catalog (reads the real
  `manifest.json`), BYOK providers page. Vendored htmx / Alpine / fonts.
- Docs: [`architecture.md`](architecture.md) (whole-project) and
  [`engine-endpoints.md`](engine-endpoints.md) (every route).
- Still mock / not built: real vector-store connectors, real `onnxruntime`
  inference, the `queryn` CLI, the Dockerfile.

### Repo

- **Tauri desktop shell removed.** `app/` is now the engine boilerplate above
  (FastAPI + serial runner); the PyInstaller config is gone. The engine is a CLI
  + optional web dashboard, Docker-first (see roadmap).
- Project open-sourced under Apache 2.0.

---

## Roadmap — engine build-out (ship ASAP, in order)

Target: a `docker run` that migrates a customer's vector store from one embedding
model's space to another's, translating via a trained adapter or falling back to
re-embedding through the customer's own provider.

1. **`queryn-core` + CLI.** Core library (connectors, adapter inference,
   enrichment, orchestration, checkpointing) with a thin `queryn` CLI —
   `migrate`, `estimate`, `validate`. Runs with no server; scriptable; CI-safe.

2. **Adapter retrieval from Hugging Face.** `queryn adapters pull` populates
   `/data/adapters/` from the published repos via `snapshot_download`, verifying
   sha256 against `manifest.json`; accepts a local tarball for airgapped
   installs. Runtime is `onnxruntime` only — no torch in the image.

3. **Serial job runner + state layer.** One migration at a time with a queue
   (`queued → running → done | failed | interrupted`, resume on restart).
   State split: **SQLite** job registry (`queryn.db`, WAL) · append-only
   **`progress.jsonl`** per job for the live feed · atomic **`checkpoint.json`**
   for resume. Atomic `tmp → os.replace` writes everywhere.

4. **BYOK configuration.** `providers.yaml` (`name`, `base_url`, `api_key_env`,
   `model`, `dim`) + environment/secret-file keys, never written by the app.
   Per-provider `base_url` override so customers can point at OpenRouter, Azure
   OpenAI, self-hosted TEI/vLLM, etc.

5. **Docker image.** One image, two entrypoints — `queryn serve` (default) and
   `docker run queryn migrate --config job.yaml`. Multi-stage, slim base,
   `docker-compose.yml` with a one-shot `migrate` service and a long-running
   `dashboard` service sharing a `/data` volume.

6. **FastAPI + Jinja2/HTMX dashboard.** Served by the same process: job list,
   a live progress `<div>` (HTMX polling a fragment endpoint), a BYOK settings
   page, and a per-run report page. No JS build step.

7. **Re-embedding fallback.** For pairs without a trained (or trustworthy)
   adapter, re-embed directly through the customer's model provider — so the
   engine is useful before every pair has an adapter.

8. **Retrieval-strategy analysis (RAG advisor).** Per-chunk and corpus-level
   analysis that recommends *how* to retrieve, not only which embedding to
   translate to. Output is an auditable report per corpus (and per query set
   when a query log is supplied), surfaced as a dashboard report page — not a
   black-box score.
   - **Deterministic signals** (Layer 1, already computed on the corpus):
     code / identifiers in a chunk → hybrid or BM25-weighted; URLs and file
     paths → keyword-weighted retrieval; near-zero natural-language content →
     BM25.
   - **Structural signals:** long, chapter/section-partitioned documents →
     hierarchical / parent-child (chapter-based) retrieval; short flat chunks →
     flat dense; heavy heading nesting → section-scoped retrieval.
   - **Distributional signals:** near-duplicate density, chunk-length spread,
     and (with a query log) query–corpus term overlap → reranking depth,
     chunk-size / overlap adjustments, and a dense-vs-hybrid recommendation.
   - Later: an optional LLM/agent pass (BYOK) that reads a sample of chunks and
     drafts the retrieval config, grounded in the deterministic signals above.

9. **Weak-adapter study & architecture iteration.** Use the v1
   `architecture_comparison` ablation data to identify the worst-performing
   pairs (`nemotron-1b-free` targets are the current worst) and investigate
   architectures beyond the single-hidden-layer linear/deep choice.

10. **Layer 2 — domain adapters (Phase 2).** Per-customer mappers fine-tuned on
    the customer's own corpus, distributed as private Hugging Face repos.
