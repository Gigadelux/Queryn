"""Runtime configuration and on-disk layout.

State is split by concern (see docs/engine-design-decisions.md §3):

    data/
      queryn.db                 SQLite job registry (WAL)
      providers.yaml            BYOK provider config (never holds secrets)
      jobs/<job_id>/
        progress.jsonl          append-only live progress feed
        checkpoint.json         atomic resume state

Everything is under DATA_DIR, which defaults to `app/data` and is overridable
with QUERYN_DATA_DIR so a container can point it at a mounted volume.
"""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path

_APP_DIR = Path(__file__).resolve().parent.parent  # .../app
_REPO_ROOT = _APP_DIR.parent


def _env_bool(name: str, default: bool) -> bool:
    raw = os.environ.get(name)
    if raw is None:
        return default
    return raw.strip().lower() in {"1", "true", "yes", "on"}


@dataclass(frozen=True)
class Settings:
    data_dir: Path
    app_dir: Path = _APP_DIR
    repo_root: Path = _REPO_ROOT

    # Demo mode: synthetic connector + adapter, fast fake batches, seeded jobs.
    demo_mode: bool = True

    # Runner tuning.
    batch_size: int = 512
    checkpoint_every: int = 20          # batches
    demo_batch_delay_s: float = 0.03    # per-batch sleep so progress is visibly live
    max_concurrent_jobs: int = 1        # decision §6 — serial

    # Where the real exported manifest lives, if this checkout has it.
    real_manifest: Path = field(
        default_factory=lambda: _REPO_ROOT
        / "Adapters" / "models" / "exported" / "v1" / "manifest.json"
    )
    bundled_manifest: Path = field(
        default_factory=lambda: _APP_DIR / "data" / "manifest.sample.json"
    )

    @property
    def db_path(self) -> Path:
        return self.data_dir / "queryn.db"

    @property
    def providers_path(self) -> Path:
        return self.data_dir / "providers.yaml"

    @property
    def jobs_dir(self) -> Path:
        return self.data_dir / "jobs"

    def job_dir(self, job_id: str) -> Path:
        return self.jobs_dir / job_id

    def progress_path(self, job_id: str) -> Path:
        return self.job_dir(job_id) / "progress.jsonl"

    def checkpoint_path(self, job_id: str) -> Path:
        return self.job_dir(job_id) / "checkpoint.json"

    def ensure_dirs(self) -> None:
        self.data_dir.mkdir(parents=True, exist_ok=True)
        self.jobs_dir.mkdir(parents=True, exist_ok=True)


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    data_dir = Path(
        os.environ.get("QUERYN_DATA_DIR", str(_APP_DIR / "data"))
    ).expanduser().resolve()
    settings = Settings(
        data_dir=data_dir,
        demo_mode=_env_bool("QUERYN_DEMO_MODE", True),
    )
    settings.ensure_dirs()
    return settings
