"""View logic for migration jobs: build the template context, create, cancel.

Pure Python — no FastAPI here. The endpoint layer calls these and renders.
"""

from __future__ import annotations

from core.catalog import MODEL_ROSTER, pick_adapter
from core.models import Job, JobStatus
from core.progress import last_event, series, tail
from core.registry import Registry
from helpers.formatting import (
    humanize_cost,
    humanize_count,
    humanize_duration,
    humanize_rate,
)
from helpers.sparkline import sparkline
from services.estimator import estimate

_registry = Registry()


def registry() -> Registry:
    return _registry


# ---- list -----------------------------------------------------------------

def _job_row(job: Job) -> dict:
    return {
        "id": job.id,
        "source": job.source_model,
        "target": job.target_model,
        "status": job.status.value,
        "phase": job.phase.value,
        "pct": job.pct,
        "rows_done": humanize_count(job.rows_done),
        "rows_total": humanize_count(job.rows_total),
        "cost": humanize_cost(job.cost_usd),
        "cos": f"{job.cos_sample:.3f}" if job.cos_sample is not None else "—",
        "duration": humanize_duration(job.duration_s),
        "adapter": job.adapter_pair_id or "re-embed",
        "is_active": job.status in (JobStatus.RUNNING, JobStatus.QUEUED),
    }


def list_context() -> dict:
    jobs = _registry.list_jobs()
    counts = _registry.counts_by_status()
    return {
        "jobs": [_job_row(j) for j in jobs],
        "any_active": _registry.has_active(),
        "counts": {
            "running": counts.get("running", 0),
            "queued": counts.get("queued", 0),
            "done": counts.get("done", 0),
            "failed": counts.get("failed", 0) + counts.get("interrupted", 0),
        },
        "models": list(MODEL_ROSTER.keys()),
    }


def rows_context() -> dict:
    jobs = _registry.list_jobs()
    return {"jobs": [_job_row(j) for j in jobs], "any_active": _registry.has_active()}


# ---- detail ---------------------------------------------------------------

_PHASES = ["reading", "translating", "writing", "validating"]


def _phase_steps(job: Job) -> list[dict]:
    done_terminal = job.status in (JobStatus.DONE,)
    cur = job.phase.value
    cur_idx = _PHASES.index(cur) if cur in _PHASES else (len(_PHASES) if done_terminal else -1)
    steps = []
    for i, name in enumerate(_PHASES):
        if done_terminal or i < cur_idx:
            state = "done"
        elif i == cur_idx and job.status == JobStatus.RUNNING:
            state = "active"
        elif i == cur_idx:
            state = "stopped"
        else:
            state = "pending"
        steps.append({"name": name, "state": state})
    return steps


def detail_context(job_id: str) -> dict | None:
    job = _registry.try_get(job_id)
    if job is None:
        return None
    est = estimate(job.source_model, job.target_model, job.rows_total)
    adapter = pick_adapter(job.source_model, job.target_model)
    return {
        "job": job,
        "row": _job_row(job),
        "progress": progress_fragment_context(job_id),
        "phase_steps": _phase_steps(job),
        "adapter": adapter,
        "estimate": est,
        "est_view": {
            "read": _bytes(est.read_bytes),
            "write": _bytes(est.write_bytes),
            "requests": humanize_count(est.requests),
            "reembed_cost": humanize_cost(est.est_reembed_cost_usd),
            "adapter_cost": humanize_cost(est.est_cost_usd),
        },
        "can_cancel": job.status in (JobStatus.RUNNING, JobStatus.QUEUED),
        "can_resume": job.status.is_resumable,
    }


def progress_fragment_context(job_id: str) -> dict:
    job = _registry.get(job_id)
    ev = last_event(job_id)
    rate = ev.rate_s if ev else 0.0
    eta = ev.eta_s if ev else None
    cos_points = series(job_id, "cos_sample", 80) if job.phase.value == "validating" \
        or job.status == JobStatus.DONE else []
    rate_points = series(job_id, "rate_s", 80)
    spark = sparkline(cos_points) if cos_points else sparkline(rate_points)
    return {
        "job_id": job.id,
        "status": job.status.value,
        "phase": job.phase.value,
        "pct": job.pct,
        "rows_done": humanize_count(job.rows_done),
        "rows_total": humanize_count(job.rows_total),
        "rate": humanize_rate(rate),
        "eta": humanize_duration(eta),
        "cost": humanize_cost(job.cost_usd),
        "cos": f"{job.cos_sample:.4f}" if job.cos_sample is not None else "—",
        "message": ev.message if ev else "",
        "sparkline": spark,
        "spark_label": "sampled cosine" if cos_points else "throughput (rows/s)",
        "phase_steps": _phase_steps(job),
        "polling": job.status == JobStatus.RUNNING,
        "log": [
            {"ts": e.ts[11:19], "phase": e.phase, "msg": e.message
             or f"{e.rows_done:,}/{e.rows_total:,} rows"}
            for e in reversed(tail(job_id, 12))
        ],
    }


# ---- mutations ----------------------------------------------------------

def create_job(source_model: str, target_model: str, rows: int) -> Job:
    adapter = pick_adapter(source_model, target_model)
    return _registry.create_job(
        source_model=source_model,
        target_model=target_model,
        rows_total=max(1, int(rows)),
        adapter_pair_id=adapter.pair_id if adapter else None,
    )


def preview(source_model: str, target_model: str, rows: int) -> dict:
    est = estimate(source_model, target_model, max(1, int(rows)))
    return {
        "has_adapter": est.has_adapter,
        "adapter_cos": f"{est.adapter_cos:.3f}" if est.adapter_cos else None,
        "pair_id": f"{source_model}_to_{target_model}",
        "in_dim": est.in_dim,
        "out_dim": est.out_dim,
        "requests": humanize_count(est.requests),
        "eta": humanize_duration(est.est_seconds),
        "adapter_cost": humanize_cost(est.est_cost_usd),
        "reembed_cost": humanize_cost(est.est_reembed_cost_usd),
    }


def _bytes(n: int) -> str:
    from helpers.formatting import humanize_bytes

    return humanize_bytes(n)
