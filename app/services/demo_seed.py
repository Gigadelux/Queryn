"""First-boot demo data.

Only runs when the registry is empty and DEMO_MODE is on. Inserts a few finished
jobs (with a plausible progress.jsonl each, so the report pages and sparklines
have something to draw) plus one queued job the live runner will pick up
seconds after the server starts.
"""

from __future__ import annotations

import random
from datetime import timedelta

from core.catalog import pick_adapter
from core.config import get_settings
from core.models import JobStatus, Phase, ProgressEvent, utcnow
from core.progress import ProgressWriter
from core.registry import Registry

_SEED_JOBS = [
    # (source, target, rows, final_status)
    ("ada-002", "bge-m3", 240_000, JobStatus.DONE),
    ("te3-small", "me5-large", 92_500, JobStatus.DONE),
    ("qwen3-emb-8b", "nemotron-1b-free", 51_200, JobStatus.FAILED),
    ("ada-002", "te3-small", 45_000, JobStatus.QUEUED),
]


def _write_fake_progress(job_id: str, source: str, rows: int, status: JobStatus,
                         cos: float) -> None:
    writer = ProgressWriter(job_id)
    bs = 512
    total_batches = (rows + bs - 1) // bs
    stop_at = total_batches if status is JobStatus.DONE else int(total_batches * 0.62)
    rate = random.uniform(38_000, 52_000)
    cost = 0.0
    now = utcnow()
    try:
        for b in range(0, stop_at, 3):
            rows_done = min(rows, (b + 1) * bs)
            cost += bs * 3 / 1_000_000 * 0.002
            frac = rows_done / rows
            phase = Phase.TRANSLATING if frac < 0.9 else Phase.VALIDATING
            writer.emit(ProgressEvent(
                job_id=job_id,
                ts=(now + timedelta(seconds=b * 0.02)).isoformat(),
                phase=phase.value,
                rows_done=rows_done,
                rows_total=rows,
                batch_index=b,
                rate_s=round(rate + random.uniform(-4000, 4000), 1),
                cost_usd=round(cost, 4),
                eta_s=round((rows - rows_done) / rate, 1),
                cos_sample=round(cos + random.uniform(-0.01, 0.01), 4) if phase is Phase.VALIDATING else None,
                message="",
            ))
        if status is JobStatus.DONE:
            writer.emit(ProgressEvent(
                job_id=job_id, ts=(now + timedelta(seconds=stop_at * 0.02)).isoformat(),
                phase=Phase.DONE.value, rows_done=rows, rows_total=rows,
                batch_index=total_batches, rate_s=round(rate, 1), cost_usd=round(cost, 4),
                eta_s=0.0, cos_sample=round(cos, 4), message="migration complete",
            ))
        else:
            writer.emit(ProgressEvent(
                job_id=job_id, ts=(now + timedelta(seconds=stop_at * 0.02)).isoformat(),
                phase=Phase.TRANSLATING.value, rows_done=min(rows, stop_at * bs),
                rows_total=rows, batch_index=stop_at, rate_s=0.0, cost_usd=round(cost, 4),
                eta_s=None, cos_sample=None,
                message="error · target store rejected batch (dimension mismatch 2048 != 2047)",
            ))
    finally:
        writer.close()


def seed_if_empty() -> list[str]:
    settings = get_settings()
    if not settings.demo_mode:
        return []
    reg = Registry(settings)
    if reg.list_jobs(limit=1):
        return []

    created: list[str] = []
    now = utcnow()
    for i, (src, tgt, rows, status) in enumerate(_SEED_JOBS):
        adapter = pick_adapter(src, tgt)
        job = reg.create_job(
            source_model=src, target_model=tgt, rows_total=rows,
            adapter_pair_id=adapter.pair_id if adapter else None,
        )
        created.append(job.id)
        if status is JobStatus.QUEUED:
            continue

        cos = (adapter.best_test_cos if adapter else 0.72) + random.uniform(-0.02, 0.01)
        started = now - timedelta(minutes=45 - i * 9)
        finished = started + timedelta(minutes=random.randint(3, 12))
        reg.update(
            job.id,
            status=status,
            phase=Phase.DONE if status is JobStatus.DONE else Phase.TRANSLATING,
            rows_done=rows if status is JobStatus.DONE else int(rows * 0.62),
            cost_usd=round(rows / 1_000_000 * 0.002, 4),
            cos_sample=round(cos, 4) if status is JobStatus.DONE else None,
            started_at=started,
            finished_at=finished,
            error=None if status is JobStatus.DONE
            else "target store rejected batch (dimension mismatch 2048 != 2047)",
        )
        _write_fake_progress(job.id, src, rows, status, cos)
    return created
