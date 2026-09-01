# Queryn Engine — HTTP endpoints

Reference for every route served by `app/` (`queryn serve` / `uvicorn main:app`).

The engine is a server-rendered app: routes return either a **full HTML page**
(extends `templates/base.html`) or an **HTMX fragment** (a partial swapped into a
page by an `hx-*` attribute). There is no JSON API for the dashboard — the only
machine endpoints are `/healthz` and the FastAPI-generated schema docs.

Base URL in development: `http://127.0.0.1:8000`.

- Router wiring: `app/endpoints/v1/router.py` (fragment/literal routes are
  registered before the catch-all `GET /jobs/{job_id}`).
- Shared renderer: `app/endpoints/v1/view.py` (`render()` injects `nav` and
  `app_version`, resolves the template).
- View logic lives in `app/controllers/*`; routes stay thin.

---

## Pages

### `GET /`
Dashboard. Job list + the "new migration" form.

| | |
|---|---|
| Handler | `endpoints/v1/dashboard.py:dashboard` |
| Controller | `controllers/jobs_controller.list_context()` |
| Template | `templates/dashboard.html` (+ `_job_rows.html`) |
| Notes | The `<tbody>` self-refreshes every 3 s via `GET /jobs/_rows` while any job is `running` or `queued`. |

### `GET /jobs/{job_id}`
Job detail: phase stepper, live progress card, adapter card, estimate card,
Cancel / Resume actions.

| | |
|---|---|
| Path param | `job_id` — 12-char hex id from `POST /jobs` |
| Handler | `endpoints/v1/dashboard.py:job_detail` |
| Controller | `controllers/jobs_controller.detail_context()` |
| Template | `templates/job_detail.html` (embeds `_progress.html`) |
| Responses | `200` page · `404` `templates/not_found.html` if the id is unknown |

### `GET /adapters`
Adapter catalog — all 49 v1 pairs with dims, architecture, and held-out cosine.

| | |
|---|---|
| Handler | `endpoints/v1/dashboard.py:adapters_page` |
| Controller | `controllers/adapters_controller.list_context()` |
| Template | `templates/adapters.html` (+ `_adapters_table.html`) |
| Data source | real `Adapters/models/exported/v1/manifest.json` if present, else `app/data/manifest.sample.json` |

### `GET /providers`
BYOK provider config. Editable base URL + key env var per model; key value is
never shown, only present / missing (read from the environment).

| | |
|---|---|
| Handler | `endpoints/v1/dashboard.py:providers_page` |
| Controller | `controllers/providers_controller.list_context()` |
| Template | `templates/providers.html` (+ `_providers_table.html`) |

---

## Mutations

### `POST /jobs`
Create a migration job (status `queued`). The background runner picks it up when
no other job is running.

| | |
|---|---|
| Body | `application/x-www-form-urlencoded`: `source_model`, `target_model`, `rows` (int) |
| Handler | `endpoints/v1/jobs.py:create_job` → `controllers/jobs_controller.create_job()` |
| Response | `303 See Other` → `Location: /jobs/{job_id}` |
| Side effects | inserts a row in `queryn.db`; the adapter for the pair is resolved from the catalog (null ⇒ job would take the re-embed fallback) |

### `POST /jobs/{job_id}/cancel`
Request cancellation. A `running` job stops at its next batch boundary and
becomes `cancelled`; a `queued` job is marked `cancelled` immediately.

| | |
|---|---|
| Handler | `endpoints/v1/jobs.py:cancel_job` |
| Mechanism | sets a flag on `app.state.migrator`; the runner's `guard()` raises at the next batch |
| Response | `303` → `/jobs/{job_id}` |

### `POST /jobs/{job_id}/resume`
Re-queue an `interrupted` or `failed` job. The runner resumes from
`jobs/{id}/checkpoint.json` (skips the `reading` prelude, continues from the last
completed batch).

| | |
|---|---|
| Handler | `endpoints/v1/jobs.py:resume_job` |
| Guard | no-op unless `status` is `interrupted` or `failed` |
| Response | `303` → `/jobs/{job_id}` |

### `POST /providers`
Save provider config to `app/data/providers.yaml` (atomic write). Only `base_url`
and `api_key_env` are persisted; `model` and `dim` are fixed per pipeline. No
secret is ever written.

| | |
|---|---|
| Body | form fields `"{model}.base_url"` and `"{model}.api_key_env"` for each provider |
| Handler | `endpoints/v1/providers.py:save_providers` → `controllers/providers_controller.save()` |
| Response | `200` — `templates/_providers_table.html` fragment (re-rendered table with a "Saved" notice), swapped in place by HTMX |

---

## HTMX fragments

These return partial HTML, not full pages. They are polled or triggered by
`hx-*` attributes in the templates; hitting them directly just returns the
partial.

### `GET /jobs/{job_id}/progress`
The live progress card: phase checklist, chevron progress bar, stat grid
(rows / throughput / ETA / cost / sampled cosine / phase), sparkline, event feed.

| | |
|---|---|
| Handler | `endpoints/v1/jobs.py:job_progress_fragment` |
| Controller | `controllers/jobs_controller.progress_fragment_context()` |
| Template | `templates/_progress.html` |
| Self-polling | the returned fragment includes `hx-get … hx-trigger="every 2s"` **only while the job is `running`**; on any terminal status the attributes are absent and polling stops |
| Data | derived from the SQLite row + the tail of `jobs/{id}/progress.jsonl` |
| Responses | `200` fragment · `404` empty body if the id is unknown |

### `GET /jobs/_rows`
The dashboard job-table `<tbody>`.

| | |
|---|---|
| Handler | `endpoints/v1/jobs.py:job_rows_fragment` |
| Template | `templates/_job_rows.html` |
| Self-polling | includes `hx-get="/jobs/_rows" hx-trigger="every 3s"` only while a job is active |

### `GET /adapters/_preview`
Live estimate for the "new migration" form — adapter match, dims, batch count,
ETA, adapter-path cost vs. re-embed cost.

| | |
|---|---|
| Query params | `source_model`, `target_model`, `rows` (default `100000`) |
| Handler | `endpoints/v1/adapters.py:adapter_preview` → `controllers/jobs_controller.preview()` |
| Template | `templates/_preview.html` |
| Triggered by | `change` on the form's selects/inputs (`hx-include="closest form"`); also `hx-trigger="load"` for the initial render |

### `GET /adapters/_table`
The adapter catalog table body on its own (`templates/_adapters_table.html`).
Not currently polled — provided for a future filter/refresh control.

---

## Operational

### `GET /healthz`
Liveness probe. `include_in_schema=False`.

```json
{ "status": "ok", "version": "0.1.0" }
```

### `GET /docs`, `GET /redoc`, `GET /openapi.json`
FastAPI's built-in interactive docs and schema. Only `/healthz` carries a useful
schema; the HTML routes are documented here instead.

### `GET /static/*`
Static mount (`app/static/`) — `queryn.css`, the logo, and vendored
`htmx.min.js` / `alpine.min.js` / fonts. No build step.

---

## Route summary

| Method | Path | Kind | Purpose |
|---|---|---|---|
| GET | `/` | page | dashboard: jobs + new-migration form |
| GET | `/jobs/{job_id}` | page | job detail + live progress |
| GET | `/adapters` | page | adapter catalog |
| GET | `/providers` | page | BYOK provider config |
| POST | `/jobs` | mutation → 303 | create a migration job |
| POST | `/jobs/{job_id}/cancel` | mutation → 303 | request cancellation |
| POST | `/jobs/{job_id}/resume` | mutation → 303 | re-queue an interrupted/failed job |
| POST | `/providers` | mutation → fragment | save `providers.yaml` |
| GET | `/jobs/{job_id}/progress` | fragment | live progress card (self-polls while running) |
| GET | `/jobs/_rows` | fragment | dashboard table body (self-polls while active) |
| GET | `/adapters/_preview` | fragment | new-migration live estimate |
| GET | `/adapters/_table` | fragment | adapter catalog table body |
| GET | `/healthz` | JSON | liveness probe |
| GET | `/docs`, `/redoc`, `/openapi.json` | — | FastAPI schema docs |
| — | `/static/*` | files | CSS, logo, vendored JS + fonts |
