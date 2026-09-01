"""Adapter catalog fragment routes (the full page lives in dashboard.py)."""

from __future__ import annotations

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from controllers import adapters_controller, jobs_controller
from endpoints.v1.view import render

router = APIRouter()


@router.get("/adapters/_preview", response_class=HTMLResponse)
def adapter_preview(request: Request, source_model: str, target_model: str, rows: int = 100_000):
    return render(request, "_preview.html",
                  {"preview": jobs_controller.preview(source_model, target_model, rows)})


@router.get("/adapters/_table", response_class=HTMLResponse)
def adapter_table(request: Request):
    return render(request, "_adapters_table.html", adapters_controller.list_context())
