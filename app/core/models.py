"""Domain types shared across the engine. Plain dataclasses + enums, no framework
imports — these travel through the registry, the runner, and the templates.
"""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from enum import Enum


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


class JobStatus(str, Enum):
    QUEUED = "queued"
    RUNNING = "running"
    DONE = "done"
    FAILED = "failed"
    INTERRUPTED = "interrupted"       # process died with the job mid-flight
    CANCELLED = "cancelled"

    @property
    def is_terminal(self) -> bool:
        return self in {JobStatus.DONE, JobStatus.FAILED, JobStatus.CANCELLED}

    @property
    def is_resumable(self) -> bool:
        return self in {JobStatus.INTERRUPTED, JobStatus.FAILED}


class Phase(str, Enum):
    QUEUED = "queued"
    READING = "reading"              # pulling source vectors from the origin store
    TRANSLATING = "translating"      # adapter inference, source space -> target space
    WRITING = "writing"             # upserting translated vectors into the target store
    VALIDATING = "validating"        # sampled cosine check against a re-embed baseline
    DONE = "done"

    @classmethod
    def ordered(cls) -> list["Phase"]:
        return [cls.READING, cls.TRANSLATING, cls.WRITING, cls.VALIDATING]


@dataclass
class AdapterInfo:
    pair_id: str
    source_model: str
    target_model: str
    in_dim: int
    out_dim: int
    architecture: str               # "linear" | "deep"
    best_test_cos: float
    source: str = "bundled"         # "hub" | "local" | "bundled"


@dataclass
class ProviderConfig:
    name: str
    base_url: str
    api_key_env: str
    model: str
    dim: int
    key_present: bool = False       # derived from os.environ at read time; never the value


@dataclass
class Estimate:
    rows: int
    source_model: str
    target_model: str
    in_dim: int
    out_dim: int
    has_adapter: bool
    adapter_cos: float | None
    requests: int
    read_bytes: int
    write_bytes: int
    est_cost_usd: float             # translation path (adapter) — near-zero; re-embed shown separately
    est_reembed_cost_usd: float     # what a full re-embed would cost instead
    est_seconds: float


@dataclass
class ProgressEvent:
    job_id: str
    ts: str
    phase: str
    rows_done: int
    rows_total: int
    batch_index: int
    rate_s: float                   # rows/second, windowed
    cost_usd: float                 # cumulative
    eta_s: float | None
    cos_sample: float | None        # rolling sampled cosine during validating
    message: str = ""

    def to_json(self) -> str:
        return json.dumps(asdict(self))

    @classmethod
    def from_json(cls, line: str) -> "ProgressEvent":
        return cls(**json.loads(line))


@dataclass
class Job:
    id: str
    source_model: str
    target_model: str
    rows_total: int
    adapter_pair_id: str | None
    status: JobStatus = JobStatus.QUEUED
    phase: Phase = Phase.QUEUED
    rows_done: int = 0
    cost_usd: float = 0.0
    cos_sample: float | None = None
    error: str | None = None
    created_at: datetime = field(default_factory=utcnow)
    started_at: datetime | None = None
    finished_at: datetime | None = None

    @property
    def pct(self) -> float:
        if not self.rows_total:
            return 0.0
        return min(100.0, round(100.0 * self.rows_done / self.rows_total, 1))

    @property
    def duration_s(self) -> float | None:
        if not self.started_at:
            return None
        end = self.finished_at or utcnow()
        return (end - self.started_at).total_seconds()
