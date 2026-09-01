"""Job mutation + HTMX fragment routes."""

from __future__ import annotations

from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse

from controllers import jobs_controller
from core.models import JobStatus
from endpoints.v1.view import render

router = APIRouter()


@router.post("/jobs")
def create_job(
    request: Request,
    source_model: str = Form(...),
    target_model: str = Form(...),
    rows: int = Form(...),
):
    job = jobs_controller.create_job(source_model, target_model, rows)
    return RedirectResponse(f"/jobs/{job.id}", status_code=303)


@router.post("/jobs/{job_id}/cancel")
def cancel_job(request: Request, job_id: str):
    request.app.state.migrator.request_cancel(job_id)
    reg = jobs_controller.registry()
    job = reg.try_get(job_id)
    if job and job.status is JobStatus.QUEUED:
        reg.mark_finished(job_id, JobStatus.CANCELLED)
    return RedirectResponse(f"/jobs/{job_id}", status_code=303)


@router.post("/jobs/{job_id}/resume")
def resume_job(request: Request, job_id: str):
    reg = jobs_controller.registry()
    job = reg.try_get(job_id)
    if job and job.status.is_resumable:
        reg.update(job_id, status=JobStatus.QUEUED, phase="queued",
                   error=None, finished_at=None)
    return RedirectResponse(f"/jobs/{job_id}", status_code=303)


@router.get("/jobs/{job_id}/progress", response_class=HTMLResponse)
def job_progress_fragment(request: Request, job_id: str):
    reg = jobs_controller.registry()
    if reg.try_get(job_id) is None:
        return HTMLResponse("", status_code=404)
    return render(request, "_progress.html",
                  {"p": jobs_controller.progress_fragment_context(job_id)})


@router.get("/jobs/_rows", response_class=HTMLResponse)
def job_rows_fragment(request: Request):
    return render(request, "_job_rows.html", jobs_controller.rows_context())
