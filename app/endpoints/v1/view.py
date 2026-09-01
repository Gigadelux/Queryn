"""Shared Jinja2 environment for the dashboard endpoints."""

from __future__ import annotations

from pathlib import Path

from fastapi import Request
from fastapi.templating import Jinja2Templates

from core import __version__

_TEMPLATE_DIR = Path(__file__).resolve().parent.parent.parent / "templates"

templates = Jinja2Templates(directory=str(_TEMPLATE_DIR))
templates.env.globals["app_version"] = __version__


def render(request: Request, name: str, ctx: dict | None = None, *, status_code: int = 200):
    payload = {"nav": _nav_for(request.url.path)}
    if ctx:
        payload.update(ctx)
    return templates.TemplateResponse(
        request=request, name=name, context=payload, status_code=status_code
    )


def _nav_for(path: str) -> str:
    if path.startswith("/adapters"):
        return "adapters"
    if path.startswith("/providers"):
        return "providers"
    return "migrations"
