"""Aggregates every v1 router into one include for `main.py`."""

from __future__ import annotations

from fastapi import APIRouter

from endpoints.v1 import adapters, dashboard, jobs, providers

api_router = APIRouter()
# Literal fragment routes (/jobs/_rows, /jobs/{id}/progress, /adapters/_*) must be
# registered before the catch-all page route /jobs/{job_id} in dashboard.
api_router.include_router(jobs.router, tags=["jobs"])
api_router.include_router(adapters.router, tags=["adapters"])
api_router.include_router(providers.router, tags=["providers"])
api_router.include_router(dashboard.router, tags=["dashboard"])
