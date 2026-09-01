"""SQLite job registry — the queryable source of truth for job state.

One writer (the API process / the runner inside it). The dashboard only reads.
WAL mode so reads never block the writer. The high-frequency progress feed does
*not* live here — see core/progress.py.
"""

from __future__ import annotations

import sqlite3
import uuid
from collections.abc import Iterator
from contextlib import contextmanager
from datetime import datetime

from core.config import Settings, get_settings
from core.models import Job, JobStatus, Phase, utcnow

_SCHEMA = """
CREATE TABLE IF NOT EXISTS jobs (
    id            TEXT PRIMARY KEY,
    source_model  TEXT NOT NULL,
    target_model  TEXT NOT NULL,
    rows_total    INTEGER NOT NULL,
    adapter_pair_id TEXT,
    status        TEXT NOT NULL,
    phase         TEXT NOT NULL,
    rows_done     INTEGER NOT NULL DEFAULT 0,
    cost_usd      REAL NOT NULL DEFAULT 0,
    cos_sample    REAL,
    error         TEXT,
    created_at    TEXT NOT NULL,
    started_at    TEXT,
    finished_at   TEXT
);
CREATE INDEX IF NOT EXISTS ix_jobs_status  ON jobs(status);
CREATE INDEX IF NOT EXISTS ix_jobs_created ON jobs(created_at);
"""


def _dt(value: str | None) -> datetime | None:
    return datetime.fromisoformat(value) if value else None


def _row_to_job(row: sqlite3.Row) -> Job:
    return Job(
        id=row["id"],
        source_model=row["source_model"],
        target_model=row["target_model"],
        rows_total=row["rows_total"],
        adapter_pair_id=row["adapter_pair_id"],
        status=JobStatus(row["status"]),
        phase=Phase(row["phase"]),
        rows_done=row["rows_done"],
        cost_usd=row["cost_usd"],
        cos_sample=row["cos_sample"],
        error=row["error"],
        created_at=_dt(row["created_at"]),
        started_at=_dt(row["started_at"]),
        finished_at=_dt(row["finished_at"]),
    )


class Registry:
    def __init__(self, settings: Settings | None = None) -> None:
        self.settings = settings or get_settings()
        self.settings.ensure_dirs()
        self._init_db()

    @contextmanager
    def _conn(self) -> Iterator[sqlite3.Connection]:
        conn = sqlite3.connect(self.settings.db_path, timeout=30)
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA journal_mode=WAL")
        conn.execute("PRAGMA foreign_keys=ON")
        conn.execute("PRAGMA busy_timeout=5000")
        try:
            yield conn
            conn.commit()
        finally:
            conn.close()

    def _init_db(self) -> None:
        with self._conn() as conn:
            conn.executescript(_SCHEMA)

    # ---- writes -----------------------------------------------------------

    def create_job(
        self,
        *,
        source_model: str,
        target_model: str,
        rows_total: int,
        adapter_pair_id: str | None,
    ) -> Job:
        job = Job(
            id=uuid.uuid4().hex[:12],
            source_model=source_model,
            target_model=target_model,
            rows_total=rows_total,
            adapter_pair_id=adapter_pair_id,
            status=JobStatus.QUEUED,
            phase=Phase.QUEUED,
        )
        with self._conn() as conn:
            conn.execute(
                """INSERT INTO jobs (id, source_model, target_model, rows_total,
                       adapter_pair_id, status, phase, created_at)
                   VALUES (?,?,?,?,?,?,?,?)""",
                (
                    job.id, job.source_model, job.target_model, job.rows_total,
                    job.adapter_pair_id, job.status.value, job.phase.value,
                    job.created_at.isoformat(),
                ),
            )
        return job

    def update(self, job_id: str, **fields: object) -> None:
        if not fields:
            return
        cols, vals = [], []
        for key, value in fields.items():
            if isinstance(value, (JobStatus, Phase)):
                value = value.value
            if isinstance(value, datetime):
                value = value.isoformat()
            cols.append(f"{key} = ?")
            vals.append(value)
        vals.append(job_id)
        with self._conn() as conn:
            conn.execute(f"UPDATE jobs SET {', '.join(cols)} WHERE id = ?", vals)

    def mark_started(self, job_id: str) -> None:
        self.update(
            job_id,
            status=JobStatus.RUNNING,
            phase=Phase.READING,
            started_at=utcnow(),
            error=None,
        )

    def mark_finished(self, job_id: str, status: JobStatus, error: str | None = None) -> None:
        self.update(
            job_id,
            status=status,
            phase=Phase.DONE if status is JobStatus.DONE else self.get(job_id).phase,
            finished_at=utcnow(),
            error=error,
        )

    def mark_orphans_interrupted(self) -> list[str]:
        """Startup sweep: any row still `running` after a crash has no live runner."""
        with self._conn() as conn:
            rows = conn.execute(
                "SELECT id FROM jobs WHERE status = ?", (JobStatus.RUNNING.value,)
            ).fetchall()
            ids = [r["id"] for r in rows]
            if ids:
                conn.executemany(
                    "UPDATE jobs SET status = ?, finished_at = ? WHERE id = ?",
                    [(JobStatus.INTERRUPTED.value, utcnow().isoformat(), i) for i in ids],
                )
        return ids

    # ---- reads ----------------------------------------------------------

    def get(self, job_id: str) -> Job:
        with self._conn() as conn:
            row = conn.execute("SELECT * FROM jobs WHERE id = ?", (job_id,)).fetchone()
        if row is None:
            raise KeyError(job_id)
        return _row_to_job(row)

    def try_get(self, job_id: str) -> Job | None:
        try:
            return self.get(job_id)
        except KeyError:
            return None

    def list_jobs(self, limit: int = 100) -> list[Job]:
        with self._conn() as conn:
            rows = conn.execute(
                "SELECT * FROM jobs ORDER BY created_at DESC LIMIT ?", (limit,)
            ).fetchall()
        return [_row_to_job(r) for r in rows]

    def claim_next_queued(self) -> Job | None:
        """Atomically move the oldest queued job to running. Serial runner (§6):
        returns None while another job is already running."""
        with self._conn() as conn:
            running = conn.execute(
                "SELECT COUNT(*) AS n FROM jobs WHERE status = ?",
                (JobStatus.RUNNING.value,),
            ).fetchone()["n"]
            if running >= self.settings.max_concurrent_jobs:
                return None
            row = conn.execute(
                "SELECT * FROM jobs WHERE status = ? ORDER BY created_at ASC LIMIT 1",
                (JobStatus.QUEUED.value,),
            ).fetchone()
            if row is None:
                return None
            conn.execute(
                "UPDATE jobs SET status = ?, phase = ?, started_at = ? WHERE id = ?",
                (JobStatus.RUNNING.value, Phase.READING.value, utcnow().isoformat(), row["id"]),
            )
        return self.get(row["id"])

    def counts_by_status(self) -> dict[str, int]:
        with self._conn() as conn:
            rows = conn.execute(
                "SELECT status, COUNT(*) AS n FROM jobs GROUP BY status"
            ).fetchall()
        return {r["status"]: r["n"] for r in rows}

    def has_active(self) -> bool:
        c = self.counts_by_status()
        return bool(c.get("running", 0) or c.get("queued", 0))
