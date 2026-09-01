"""Atomic resume state (`jobs/<id>/checkpoint.json`).

Deliberately a dedicated file, not a SQLite column: resume logic stays simple and
the write is a single atomic replace. Batch boundaries derive from a stable sort
of the source IDs, so `batches_done` means the same thing on every restart.
"""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field

from core.config import get_settings
from helpers.atomic import write_json_atomic


@dataclass
class Checkpoint:
    job_id: str
    batch_size: int
    batches_done: int = 0
    rows_done: int = 0
    cost_usd: float = 0.0
    phase: str = "reading"
    updated_at: str = ""
    extra: dict = field(default_factory=dict)


def load(job_id: str) -> Checkpoint | None:
    path = get_settings().checkpoint_path(job_id)
    if not path.exists():
        return None
    try:
        return Checkpoint(**json.loads(path.read_text()))
    except (ValueError, TypeError):
        return None


def save(cp: Checkpoint) -> None:
    from core.models import utcnow

    cp.updated_at = utcnow().isoformat()
    write_json_atomic(get_settings().checkpoint_path(cp.job_id), asdict(cp))
