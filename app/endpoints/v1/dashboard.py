"""Full-page dashboard routes."""

from __future__ import annotations

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from controllers import adapters_controller, jobs_controller, providers_controller
from endpoints.v1.view import render

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
def dashboard(request: Request):
    return render(request, "dashboard.html", jobs_controller.list_context())


@router.get("/jobs/{job_id}", response_class=HTMLResponse)
def job_detail(request: Request, job_id: str):
    ctx = jobs_controller.detail_context(job_id)
    if ctx is None:
        return render(request, "not_found.html", {"what": f"job {job_id}"}, status_code=404)
    return render(request, "job_detail.html", ctx)


@router.get("/adapters", response_class=HTMLResponse)
def adapters_page(request: Request):
    return render(request, "adapters.html", adapters_controller.list_context())


@router.get("/providers", response_class=HTMLResponse)
def providers_page(request: Request):
    return render(request, "providers.html", providers_controller.list_context())
