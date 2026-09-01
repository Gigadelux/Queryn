# Queryn engine (`app/`) — demo boilerplate

The local migration engine: translate a vector store from one embedding model's
space into another's, using a trained adapter, without re-embedding the corpus.

This is a **working scaffold with mock data**. The architecture is real — the
state layer, the serial job runner, the module boundaries — but the pieces that
would touch a customer's infrastructure (vector-store connectors, ONNX adapter
inference) are synthetic so the whole thing runs end-to-end as a demo.

## Run it

```bash
cd app
uv sync
uv run uvicorn main:app --reload      # http://127.0.0.1:8000
```

On first boot it seeds a few finished jobs plus one queued job; the runner picks
the queued one up within a second or two and you can watch it stream.

- **Migrations** (`/`) — job list + a "new migration" form with a live estimate.
- **`/jobs/{id}`** — phase stepper, the chevron progress bar, throughput / ETA /
  cost / sampled-cosine, an event feed, and resume for interrupted jobs.
- **Adapters** (`/adapters`) — the 49-pair v1 catalog, read from the real
  exported `manifest.json` when present, otherwise `data/manifest.sample.json`.
- **Providers** (`/providers`) — BYOK config written to `data/providers.yaml`;
  API keys are read from the environment and shown only as present / missing.

## Layout

| Path | What |
|---|---|
| `main.py` | FastAPI app factory + lifespan (startup sweep, seed, start runner) |
| `core/` | domain types + persistence — `registry.py` (SQLite), `progress.py` (JSONL), `checkpoint.py`, `providers.py`, `catalog.py` |
| `core/connectors/`, `core/adapters/` | `Protocol` + a mock impl each; a real Qdrant/pgvector connector or an `onnxruntime` runner is one new file |
| `services/migrator.py` | the serial job runner — one migration at a time, `reading → translating → writing → validating`, checkpointed |
| `services/estimator.py` | pre-flight cost / time estimate |
| `controllers/` | view logic — builds template context from services/core |
| `endpoints/v1/` | FastAPI routers (pages + HTMX fragments) |
| `helpers/` | `atomic.py` (tmp → `os.replace`), `sparkline.py` (inline SVG), `formatting.py` |
| `templates/`, `static/` | Jinja2 + HTMX; vendored htmx / Alpine / fonts, no build step |
| `data/` | runtime state (gitignored) + the bundled adapter manifest |

## State, split by concern

| State | Store |
|---|---|
| job registry (list, status, timestamps, result) | `data/queryn.db` — SQLite, WAL |
| live progress (per batch: rows, rate, cost, ETA) | `data/jobs/<id>/progress.jsonl` — append-only |
| resume point | `data/jobs/<id>/checkpoint.json` — atomic write |
| BYOK config | `data/providers.yaml` (never holds a secret) |

Delete `data/queryn.db` and `data/jobs/` to reset; they are rebuilt on next boot.

## Environment

| Var | Default | Effect |
|---|---|---|
| `QUERYN_DATA_DIR` | `app/data` | where all runtime state lives (point at a volume) |
| `QUERYN_DEMO_MODE` | `1` | `0` disables seeded jobs and the synthetic connector/adapter |

## Not built yet

The `queryn` CLI (`migrate` / `estimate` / `adapters pull`), real vector-DB
connectors, real ONNX inference, the Dockerfile, and the RAG advisor. See
`../docs/CHANGELOG.md` for the roadmap.
