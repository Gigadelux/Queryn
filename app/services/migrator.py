"""The migration orchestrator.

One job runs at a time (decision §6). A background asyncio task claims the oldest
queued job, runs it on a worker thread, and moves on. Each job:

    reading  -> translating -> writing -> validating -> done

The batch loop over `translating`+`writing` is the progress spine (rows_done goes
0 -> rows_total); `reading` is a short prelude and `validating` a short coda that
fills in the sampled-cosine reading. State is written three ways as it goes:
SQLite row (coarse, queryable), `progress.jsonl` (per-batch feed), and
`checkpoint.json` (atomic, every N batches) so an interrupted job resumes.
"""

from __future__ import annotations

import asyncio
import random
import time
from datetime import datetime, timezone

import numpy as np

from core.adapters.mock import MockAdapterRunner
from core.checkpoint import Checkpoint
from core.checkpoint import load as load_checkpoint
from core.checkpoint import save as save_checkpoint
from core.config import Settings, get_settings
from core.connectors.mock import MockVectorStore
from core.models import Job, JobStatus, Phase, ProgressEvent
from core.progress import ProgressWriter
from core.registry import Registry


class _Cancelled(Exception):
    pass


class Migrator:
    def __init__(self, registry: Registry | None = None, settings: Settings | None = None) -> None:
        self.settings = settings or get_settings()
        self.registry = registry or Registry(self.settings)
        self._task: asyncio.Task | None = None
        self._stopping = asyncio.Event()
        self._cancel: set[str] = set()

    # ---- lifecycle ----------------------------------------------------------

    def start(self) -> None:
        if self._task is None or self._task.done():
            self._stopping.clear()
            self._task = asyncio.create_task(self._loop(), name="queryn-migrator")

    async def stop(self) -> None:
        self._stopping.set()
        if self._task is not None:
            try:
                await asyncio.wait_for(self._task, timeout=10)
            except (asyncio.TimeoutError, asyncio.CancelledError):
                self._task.cancel()

    def request_cancel(self, job_id: str) -> None:
        self._cancel.add(job_id)

    async def _loop(self) -> None:
        while not self._stopping.is_set():
            job = self.registry.claim_next_queued()
            if job is None:
                try:
                    await asyncio.wait_for(self._stopping.wait(), timeout=1.0)
                except asyncio.TimeoutError:
                    pass
                continue
            await asyncio.to_thread(self._run_job, job)

    # ---- one job ---------------------------------------------------------

    def run_job_blocking(self, job_id: str) -> Job:
        """Synchronous entry point (for a future CLI `queryn migrate`)."""
        job = self.registry.get(job_id)
        if job.status is JobStatus.QUEUED:
            self.registry.mark_started(job_id)
            job = self.registry.get(job_id)
        self._run_job(job)
        return self.registry.get(job_id)

    def _run_job(self, job: Job) -> None:
        reg = self.registry
        bs = self.settings.batch_size
        rng = np.random.default_rng(int(job.id[:8], 16))

        try:
            adapter = MockAdapterRunner.for_pair(job.source_model, job.target_model)
        except KeyError as exc:
            reg.mark_finished(job.id, JobStatus.FAILED, error=str(exc))
            return

        store = MockVectorStore(job.rows_total, adapter.in_dim, seed=int(job.id[:6], 16))
        target = MockVectorStore(job.rows_total, adapter.out_dim)

        cp = load_checkpoint(job.id) or Checkpoint(job_id=job.id, batch_size=bs)
        resuming = cp.batches_done > 0
        rows_done = cp.rows_done
        cost = cp.cost_usd
        total_batches = (job.rows_total + bs - 1) // bs

        writer = ProgressWriter(job.id)
        window: list[tuple[float, int]] = []

        def emit(phase: Phase, batch_index: int, cos: float | None, msg: str = "") -> None:
            now = time.monotonic()
            window.append((now, rows_done))
            del window[:-8]
            rate = 0.0
            if len(window) >= 2 and window[-1][0] > window[0][0]:
                rate = (window[-1][1] - window[0][1]) / (window[-1][0] - window[0][0])
            eta = (job.rows_total - rows_done) / rate if rate > 0 else None
            writer.emit(ProgressEvent(
                job_id=job.id,
                ts=datetime.now(timezone.utc).isoformat(),
                phase=phase.value,
                rows_done=rows_done,
                rows_total=job.rows_total,
                batch_index=batch_index,
                rate_s=round(rate, 1),
                cost_usd=round(cost, 4),
                eta_s=round(eta, 1) if eta is not None else None,
                cos_sample=round(cos, 4) if cos is not None else None,
                message=msg,
            ))
            reg.update(job.id, phase=phase, rows_done=rows_done, cost_usd=cost,
                       cos_sample=cos if cos is not None else job.cos_sample)

        def guard() -> None:
            if job.id in self._cancel or self._stopping.is_set():
                raise _Cancelled

        try:
            # -- reading (prelude) --
            if not resuming:
                reg.update(job.id, phase=Phase.READING)
                emit(Phase.READING, 0, None, f"scanning source store · {job.source_model}")
                for _ in range(3):
                    guard()
                    time.sleep(self.settings.demo_batch_delay_s * 12)
                emit(Phase.READING, 0, None,
                     f"{job.rows_total:,} vectors · dim {adapter.in_dim} · adapter {adapter.pair_id}")

            # -- translating + writing (spine) --
            start_batch = cp.batches_done
            for b, batch in enumerate(
                store.iter_batches(bs, start_batch=start_batch), start=start_batch
            ):
                guard()
                translated = adapter.translate(batch.vectors)
                batch.vectors = translated
                target.write_batch(batch)

                rows_done = min(job.rows_total, (b + 1) * bs)
                cost += len(batch.ids) / 1_000_000 * 0.002
                time.sleep(self.settings.demo_batch_delay_s + rng.uniform(0, 0.004))

                phase = Phase.WRITING if (b % 2) else Phase.TRANSLATING
                if b % 3 == 0 or b == total_batches - 1:
                    emit(phase, b, None)

                if (b + 1 - start_batch) % self.settings.checkpoint_every == 0:
                    save_checkpoint(Checkpoint(
                        job_id=job.id, batch_size=bs, batches_done=b + 1,
                        rows_done=rows_done, cost_usd=cost, phase=phase.value,
                    ))

            rows_done = job.rows_total
            save_checkpoint(Checkpoint(
                job_id=job.id, batch_size=bs, batches_done=total_batches,
                rows_done=rows_done, cost_usd=cost, phase=Phase.VALIDATING.value,
            ))

            # -- validating (coda) --
            reg.update(job.id, phase=Phase.VALIDATING)
            sample_batches = max(3, total_batches // 20)
            cos = adapter.reported_cos
            for i in range(sample_batches):
                guard()
                cos = adapter.cosine_sample((i + 1) * bs, rng)
                time.sleep(self.settings.demo_batch_delay_s * 3)
                if i % 2 == 0 or i == sample_batches - 1:
                    emit(Phase.VALIDATING, total_batches + i, cos,
                         f"sampled cosine vs re-embed baseline · {cos:.4f}")

            emit(Phase.DONE, total_batches + sample_batches, cos, "migration complete")
            reg.update(job.id, cos_sample=cos)
            reg.mark_finished(job.id, JobStatus.DONE)

        except _Cancelled:
            self._cancel.discard(job.id)
            # server shutting down -> interrupted (resumable); user cancel -> cancelled
            status = JobStatus.INTERRUPTED if self._stopping.is_set() else JobStatus.CANCELLED
            emit(Phase(reg.get(job.id).phase.value), -1, None, f"stopped · {status.value}")
            reg.mark_finished(job.id, status, error=None)
        except Exception as exc:  # noqa: BLE001 - surface any runner failure on the row
            emit(Phase(reg.get(job.id).phase.value), -1, None, f"error · {exc}")
            reg.mark_finished(job.id, JobStatus.FAILED, error=repr(exc))
        finally:
            writer.close()
            store.close()
            target.close()
