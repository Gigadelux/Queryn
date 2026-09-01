# Queryn — project architecture

## What Queryn is

Queryn is an **embedding translation and enrichment engine**. Given a text chunk
and its embedding produced by model A, it returns the equivalent embedding in
model B's space — without re-embedding the source corpus. Embedding spaces from
different models are geometrically incompatible, so migrating a vector store
between models normally means a full, expensive re-embed. Queryn replaces that
with a small learned transform per model pair.

It ships as a **local, credentialed program** run against a customer's own
infrastructure — not a hosted API.

---

## Repository layout

The repo is two halves with a clean handoff between them:

```
queryn/
├── Adapters/        Part 1 — dataset construction + per-pair mapper training
│                    Produces the trained checkpoints and the distributables.
├── app/             Part 2 — the engine: the local program customers run.
├── docs/            Deep docs (this file, endpoint reference, ADR log, changelog)
├── LICENSE          Apache 2.0
└── README.md
```

The handoff artifact is the **adapter set**: `Adapters/` trains mappers and
exports them as ONNX + `manifest.json`; `app/` consumes that manifest and runs
the ONNX at migration time. Neither half imports the other — they meet at the
manifest / the Hugging Face repos.

---

## The three product layers

| Layer | What | Where |
|---|---|---|
| **Layer 0 — Translation core** | One transform per directed model pair. Two single-hidden-layer architectures are trained and compared per pair — a **linear** projection and a **deep** compressed-latent MLP (`Linear → GELU → Linear`) — and the better one on held-out cosine is kept. | `Adapters/architectures/`, `Adapters/pipelines/v1_adapter_model_training.py` |
| **Layer 1 — Regex enrichment** | Deterministic per-chunk signals (code detection, URL / identifier / path patterns) → a `RETRIEVAL_HINT` of `"BM25"` or `"vector"`. Auditable, no LLM cost. | computed in `Adapters/dataset_generator.py`; consumed by the engine at migration time (planned) |
| **Layer 2 — Domain adapters** | Per-customer mappers fine-tuned on the customer's own corpus, distributed as private Hugging Face repos. Phase 2. | not built |

Paper basis: **Vec2Vec** (arXiv:2306.12689) for the nonlinear-through-latent
case, **mini-vec2vec** (arXiv:2510.02348) for "a linear map is often enough". v1
results: linear wins 39 / 49 pairs.

---

## Part 1 — the Adapters pipeline (`Adapters/`)

A sequence of directly-run Python scripts (no build system, no test suite). Each
stage writes a durable artifact the next stage reads.

```
5 raw Kaggle datasets                     raw_datasets/
        │  dataset_generator.py           merge, dedup, tag domain, compute Layer-1 signals
        ▼
unified_dataset.parquet                   349,674 rows × 14 cols
        │  embedding_pipeline.py           embed every row with 8 models (OpenRouter + local ONNX)
        │                                  resumable, atomic 96-row shards, checkpointed
        ▼
data/embeddings/{model}.parquet  +  embeddings.parquet   (ID + one fixed_size_list<float> col per model)
        │  dataset_splitting.py            80 / 20 train / test
        ▼
data/splits/{train,test}.parquet
        │  pipelines/v1_adapter_model_training.py
        │                                  per pair: train linear + deep, keep the better, best-epoch checkpoint
        ▼
models/v1/{src}_to_{tgt}.pt                49 directed pairs
        │  ptConverter.py                  .pt → model.onnx (opset 17, dynamic batch, L2-norm baked in)
        │                                        + model.safetensors + config.json + manifest.json (sha256 per file)
        ▼
models/exported/v1/                        ← the handoff to the engine
        │
        ├── hf_upload.py                    one HF model repo per pair + a collection  (QuerynAi/…)
        └── kaggle_upload.py                one Kaggle dataset: text/ (raw corpora) + embeddings/
```

Embedding models covered (key · dim): `ada-002` 1536, `te3-small` 1536,
`qwen3-emb-8b` 4096, `bge-m3` 1024, `me5-large` 1024, `pplx-embed-1` 1024,
`nemotron-1b-free` 2048, `fastembed-bge-small` 384.

Design properties carried throughout: **atomic writes** (`file.tmp` →
`os.replace`), **append-only** progress, **resumability** from a checkpoint keyed
on a stable sort — the engine inherits all three.

Full detail: [`Adapters.md`](Adapters.md).

---

## Part 2 — the engine (`app/`)

> **Status: demo boilerplate.** The architecture below is real — the module
> boundaries, the state layer, the serial runner. The pieces that touch a
> customer's infrastructure (vector-store connectors, ONNX inference) are
> **mock implementations** so the whole thing runs end-to-end. Rationale for
> each decision is in [`engine-design-decisions.md`](engine-design-decisions.md)
> (not committed).

### Shape

- **`queryn-core`** — a library: domain types, persistence, connectors, adapter
  inference, orchestration.
- **`queryn serve`** — a FastAPI process that renders a Jinja2 + HTMX dashboard
  and hosts the job API. This is what exists today (`uvicorn main:app`).
- **`queryn` CLI** — `migrate` / `estimate` / `adapters pull`. Not built yet; a
  thin `typer` wrapper over the same core.

### Module map

```
app/
├── main.py                 create_app() factory + lifespan
│                           (orphan sweep → seed demo → start background runner)
│
├── core/                   domain types + persistence — no framework imports
│   ├── config.py           Settings: DATA_DIR, on-disk paths, DEMO_MODE, runner tuning
│   ├── models.py           Job, ProgressEvent, AdapterInfo, ProviderConfig, Estimate;
│   │                       JobStatus / Phase enums
│   ├── registry.py         SQLite (WAL) job registry — the queryable source of truth
│   ├── progress.py         append-only progress.jsonl writer + tail readers
│   ├── checkpoint.py       atomic checkpoint.json (resume state)
│   ├── providers.py        providers.yaml load/save; key status from env only
│   ├── catalog.py          load manifest (real export or bundled sample); pick_adapter()
│   ├── connectors/         VectorStoreConnector Protocol + MockVectorStore
│   └── adapters/           AdapterRunner Protocol + MockAdapterRunner
│
├── services/
│   ├── migrator.py         the serial job runner (one job at a time, background asyncio task)
│   ├── estimator.py        pre-flight cost / time / bytes estimate
│   └── demo_seed.py        first-boot demo jobs (only when registry empty + DEMO_MODE)
│
├── controllers/            view logic — build template context from services/core
│   ├── jobs_controller.py
│   ├── providers_controller.py
│   └── adapters_controller.py
│
├── endpoints/v1/           FastAPI routers (thin) + the shared Jinja renderer
│   ├── router.py           aggregates the routers
│   ├── view.py             render() helper, template env
│   ├── dashboard.py        full pages
│   ├── jobs.py             job mutations + HTMX fragments
│   ├── providers.py        providers save fragment
│   └── adapters.py         catalog + preview fragments
│
├── helpers/
│   ├── atomic.py           write_atomic() — file.tmp → fsync → os.replace
│   ├── sparkline.py        server-rendered inline-SVG sparkline (no chart lib)
│   └── formatting.py       humanize bytes / duration / rate / cost
│
├── templates/              Jinja2 — base.html + pages + `_*.html` fragments
├── static/                 queryn.css, logo, vendored htmx / Alpine / fonts (no build step)
└── data/                   runtime state (gitignored) + bundled manifest.sample.json
```

Dependency direction is one-way: `endpoints → controllers → services → core →
helpers`. `core` never imports FastAPI; `controllers` never import
`fastapi.APIRouter`.

### Request lifecycle

```
HTTP request
  → endpoints/v1/*  (parse form/query, no logic)
  → controllers/*   (call services + core, shape a plain-dict context)
  → endpoints/v1/view.render(request, "template.html", ctx)
  → Jinja2 → HTML (full page) or partial (HTMX fragment)
```

The dashboard is **server-rendered**. Live updates are HTMX polling a fragment
endpoint and swapping a `<div>` — `_progress.html` includes its own
`hx-trigger="every 2s"` only while the job is `running`, so polling is
self-terminating. No JSON API, no client state, one vendored `Alpine.js` file for
the one client-side bit (disable the submit button after click).

### The serial runner and job state machine

`services/migrator.py` runs **one migration at a time** (decision §6). A
background `asyncio` task loops:

```
claim_next_queued()  ──none──►  sleep 1s, retry
        │ got a job
        ▼
run on a worker thread:
  reading  ── prelude, ~3 ticks (skipped on resume)
  translating / writing  ── the spine: for each batch
        connector.iter_batches() → adapter.translate() → connector.write_batch()
        emit ProgressEvent  ·  checkpoint every 20 batches  ·  check cancel/shutdown flag
  validating  ── coda: sampled cosine vs a re-embed baseline
  done
```

Job status transitions:

```
queued ──► running ──► done
                   ├──► failed        (exception in the runner)
                   ├──► cancelled     (user hit Cancel)
                   └──► interrupted   (process stopped mid-job)  ──► [Resume] ──► queued
```

On startup, any row still `running` (no live runner after a crash) is swept to
`interrupted` and offered for resume — `main.py` lifespan →
`registry.mark_orphans_interrupted()`.

### State model — split by concern (decision §3)

| State | Store | Why |
|---|---|---|
| Job registry — list, status, timestamps, config, result summary | **SQLite** `data/queryn.db` (WAL) | needs queries + concurrent dashboard reads |
| Live progress — per batch: rows, rate, cost, ETA, phase, cosine sample | **append-only** `data/jobs/{id}/progress.jsonl` | high write frequency, only the tail matters, decouples the runner from the DB |
| Resume point — batches done, rows done, cost, phase | **atomic** `data/jobs/{id}/checkpoint.json` | resume logic is cleaner against a dedicated file; one atomic replace |
| BYOK config — provider base URLs, key env var names | **`data/providers.yaml`** + env | diffable, mountable, set at deploy time; **never holds a secret** |

RAM holds only rebuildable view state. One writer to `queryn.db` (the
API / runner process). Delete `queryn.db` + `jobs/` to reset — both are rebuilt
on next boot.

### Adapter distribution and the catalog

`core/catalog.py` loads the pair manifest, preferring the real exported
`Adapters/models/exported/v1/manifest.json` when the checkout has it, falling
back to the bundled `app/data/manifest.sample.json` (49 pairs, tracked). In a
deployed engine this is what `queryn adapters pull` populates from the Hugging
Face Hub via `snapshot_download`, verifying each file's sha256 against the
manifest (decision §5). Runtime is `onnxruntime` only — no PyTorch in the image.

### What is mock vs. real right now

| Real | Mock (swap-in point) |
|---|---|
| SQLite registry, JSONL progress feed, atomic checkpoint, `providers.yaml` | `core/connectors/mock.py` — synthetic in-memory vector store |
| The serial runner, phase machine, checkpoint/resume, cancel | `core/adapters/mock.py` — seeded random linear projection, L2-normed |
| The FastAPI + Jinja2 + HTMX dashboard, all routes | `services/demo_seed.py` — first-boot sample jobs |
| Adapter catalog (reads the real manifest) | per-batch cost / rate / cosine numbers are plausible fabrications |

### Extension points

- **Real vector store**: add `core/connectors/qdrant.py` (or pgvector, Pinecone,
  …) implementing `VectorStoreConnector` — `count()`, `iter_batches()`,
  `write_batch()`. Nothing else changes.
- **Real inference**: add `core/adapters/onnx.py` implementing `AdapterRunner`
  (`translate()`), loading `model.onnx` for the pair under `onnxruntime`.
- **Re-embedding fallback**: an `AdapterRunner` that calls the target provider's
  embedding API for pairs with no trained adapter.
- **CLI**: `app/cli.py` (`typer`) calling `Migrator.run_job_blocking()` and the
  same `core` functions.

Full endpoint reference: [`engine-endpoints.md`](engine-endpoints.md).

---

## End-to-end data flow

```
raw corpora ─► unified_dataset.parquet ─► per-model embeddings ─► train linear+deep per pair
                                                                        │ keep better
                                                                        ▼
                                                          models/v1/*.pt ─► ptConverter.py
                                                                        │
                                                    models/exported/v1/  ─►  hf_upload.py ─► HF repos + collection
                                                       (onnx + manifest)          │
                                                                                  ▼
                    ┌──────────────────────  the engine  ──────────────────────────────────┐
                    │  queryn adapters pull → /data/adapters/   (verify sha256 vs manifest) │
                    │                                                                       │
customer source  ───┤  connector.iter_batches() ─► AdapterRunner.translate() ─► connector   │──►  customer target
vector store        │        (source space)              (onnx)               .write_batch() │     vector store
                    │                                                          (target space)│     (translated)
                    │  progress.jsonl  ·  queryn.db row  ·  checkpoint.json  as it goes       │
                    └───────────────────────────────────────────────────────────────────────┘
```

---

## Deployment model (planned)

One Docker image, two entrypoints (decision §8):

- `CMD` = `queryn serve` — dashboard + job API, long-lived.
- `docker run queryn migrate --config job.yaml` — headless one-shot for CI / cron.

Multi-stage build, slim base, `onnxruntime` only (no torch). `docker-compose.yml`
with a one-shot `migrate` service and a long-running `dashboard` service sharing a
`/data` volume. `queryn.db` must live on the mounted volume — not the container
overlay fs, not NFS/SMB (SQLite locking).

---

## Conventions

- **Atomic writes everywhere**: `file.tmp` → `fsync` → `os.replace(file)`
  (`helpers/atomic.py`). A crash mid-write leaves only a `.tmp` that readers
  ignore.
- **Append-only** for anything high-frequency (`progress.jsonl`). Readers
  tolerate a torn final line.
- **Stable batch boundaries**: derived from a sorted key so `batches_done` means
  the same thing on every restart.
- **No frontend build step**: Jinja2 + HTMX + one vendored Alpine file + vendored
  fonts. The container image has no Node stage and no `node_modules`.
- **Secrets are never written by the app**: `providers.yaml` carries only the
  *name* of the env var that holds each key.
- **Serial jobs**: throughput comes from bounded concurrent provider requests
  *within* a job, not from running jobs in parallel.

---

## Where to read more

| Doc | Contents |
|---|---|
| [`README.md`](../README.md) | project overview, the Adapters pipeline in depth, results |
| [`Adapters.md`](Adapters.md) | dataset construction, architecture research, training on other datasets |
| [`engine-endpoints.md`](engine-endpoints.md) | every HTTP route the engine serves |
| [`engine-design-decisions.md`](engine-design-decisions.md) | ADR-style rationale for the engine (not committed) |
| [`CHANGELOG.md`](CHANGELOG.md) | shipped work + the ordered engine roadmap |
| [`app/README.md`](../app/README.md) | how to run the engine demo |
