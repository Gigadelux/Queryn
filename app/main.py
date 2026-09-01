"""Queryn engine — `queryn serve`.

FastAPI process that renders the Jinja2 + HTMX dashboard and hosts the migration
job API. One serial background runner (`services.migrator.Migrator`) drains the
queue. Run it with:

    uv run uvicorn main:app --reload
    # or
    python -m app            # (from the repo root)

State lives under `QUERYN_DATA_DIR` (default `app/data`). `QUERYN_DEMO_MODE=0`
turns off the synthetic connector/adapter and the seeded jobs.
"""

from __future__ import annotations

import logging
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from core import __version__
from core.config import get_settings
from core.registry import Registry
from endpoints.v1.router import api_router
from services.demo_seed import seed_if_empty
from services.migrator import Migrator

log = logging.getLogger("queryn")
_STATIC_DIR = Path(__file__).resolve().parent / "static"


@asynccontextmanager
async def lifespan(app: FastAPI):
    settings = get_settings()
    registry = Registry(settings)

    orphaned = registry.mark_orphans_interrupted()
    if orphaned:
        log.warning("marked %d orphaned job(s) interrupted: %s", len(orphaned), orphaned)

    if settings.demo_mode:
        seeded = seed_if_empty()
        if seeded:
            log.info("seeded %d demo job(s)", len(seeded))

    migrator = Migrator(registry=registry, settings=settings)
    migrator.start()
    app.state.settings = settings
    app.state.registry = registry
    app.state.migrator = migrator
    log.info("queryn %s serving · data_dir=%s · demo=%s",
             __version__, settings.data_dir, settings.demo_mode)
    try:
        yield
    finally:
        await migrator.stop()


def create_app() -> FastAPI:
    app = FastAPI(title="Queryn Engine", version=__version__, lifespan=lifespan)
    app.mount("/static", StaticFiles(directory=str(_STATIC_DIR)), name="static")
    app.include_router(api_router)

    @app.get("/healthz", include_in_schema=False)
    def healthz():
        return {"status": "ok", "version": __version__}

    return app


app = create_app()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
