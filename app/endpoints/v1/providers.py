"""BYOK provider config routes."""

from __future__ import annotations

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from controllers import providers_controller
from endpoints.v1.view import render

router = APIRouter()


@router.post("/providers", response_class=HTMLResponse)
async def save_providers(request: Request):
    form = dict(await request.form())
    ctx = providers_controller.save({k: str(v) for k, v in form.items()})
    ctx["saved"] = True
    return render(request, "_providers_table.html", ctx)
