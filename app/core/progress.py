"""Per-job append-only progress feed (`jobs/<id>/progress.jsonl`).

High write frequency, only the tail matters, and it decouples the job loop from
the SQLite writer. One `ProgressEvent` per batch. Readers tolerate a torn final
line (a crash mid-append) by skipping it.
"""

from __future__ import annotations

import os
from collections import deque
from pathlib import Path

from core.config import get_settings
from core.models import ProgressEvent


class ProgressWriter:
    def __init__(self, job_id: str) -> None:
        self.job_id = job_id
        self.path: Path = get_settings().progress_path(job_id)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self._fh = open(self.path, "a", encoding="utf-8")

    def emit(self, event: ProgressEvent) -> None:
        self._fh.write(event.to_json() + "\n")
        self._fh.flush()
        os.fsync(self._fh.fileno())

    def close(self) -> None:
        try:
            self._fh.close()
        except Exception:
            pass

    def __enter__(self) -> "ProgressWriter":
        return self

    def __exit__(self, *exc: object) -> None:
        self.close()


def _iter_events(job_id: str):
    path = get_settings().progress_path(job_id)
    if not path.exists():
        return
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                yield ProgressEvent.from_json(line)
            except (ValueError, TypeError):
                continue  # torn trailing line from a crash — ignore


def tail(job_id: str, n: int = 60) -> list[ProgressEvent]:
    return list(deque(_iter_events(job_id), maxlen=n))


def last_event(job_id: str) -> ProgressEvent | None:
    last = None
    for event in _iter_events(job_id):
        last = event
    return last


def series(job_id: str, field: str, n: int = 120) -> list[float]:
    """Pull one numeric field across the last `n` events — feeds the sparkline."""
    out: list[float] = []
    for event in tail(job_id, n):
        value = getattr(event, field, None)
        if value is not None:
            out.append(float(value))
    return out
