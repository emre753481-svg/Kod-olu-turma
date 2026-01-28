from fastapi import FastAPI, BackgroundTasks, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from weasyprint import HTML
from core.config import settings
from models.analysis import AnalyzeRequest, AnalyzeResponse, StatusResponse, ResultsResponse
from services.job_store import InMemoryJobStore

app = FastAPI(title=settings.app_name)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.frontend_origin],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

store = InMemoryJobStore()

@app.get("/healthz")
async def healthz():
    return {"ok": True}

def run_analysis(job_id: str, req: AnalyzeRequest):
    # MVP placeholder: a real version will fetch repo + run AI analyzers.
    store.update(job_id, status="running", progress=10, message="Starting analysis")
    store.update(job_id, progress=60, message="Analyzing repository structure")
    results = {
        "repo_url": req.repo_url,
        "documents": {
            "scope": {"summary": "MVP scope document (placeholder)"},
            "requirements": {"functional": [], "non_functional": []},
        },
    }
    store.update(job_id, status="completed", progress=100, message="Done", results=results)

@app.post("/api/analyze", response_model=AnalyzeResponse)
async def analyze(req: AnalyzeRequest, bg: BackgroundTasks):
    job = store.create()
    bg.add_task(run_analysis, job.id, req)
    return AnalyzeResponse(analysis_id=job.id)

@app.get("/api/analysis/{analysis_id}/status", response_model=StatusResponse)
async def status(analysis_id: str):
    try:
        job = store.get(analysis_id)
    except KeyError:
        raise HTTPException(status_code=404, detail="Not found")
    return StatusResponse(
        analysis_id=job.id,
        status=job.status,
        progress=job.progress,
        message=job.message,
    )

@app.get("/api/analysis/{analysis_id}/results", response_model=ResultsResponse)
async def results(analysis_id: str):
    try:
        job = store.get(analysis_id)
    except KeyError:
        raise HTTPException(status_code=404, detail="Not found")
    return ResultsResponse(analysis_id=job.id, status=job.status, results=job.results)

@app.post("/api/export/{analysis_id}/{fmt}")
async def export(analysis_id: str, fmt: str):
    try:
        job = store.get(analysis_id)
    except KeyError:
        raise HTTPException(status_code=404, detail="Not found")
    if job.status != "completed" or not job.results:
        raise HTTPException(status_code=400, detail="Analysis not completed")

    if fmt == "json":
        return job.results

    if fmt == "markdown":
        md = f"# Analysis\\n\\nRepo: {job.results.get('repo_url')}\\n"
        return {"markdown": md}

    if fmt == "pdf":
        html = f"<h1>GitAnalyzer Pro</h1><p>Repo: {job.results.get('repo_url')}</p>"
        pdf_bytes = HTML(string=html).write_pdf()
        return {"content_type": "application/pdf", "bytes_base64": __import__("base64").b64encode(pdf_bytes).decode("ascii")}

    raise HTTPException(status_code=400, detail="Invalid format. Use pdf/markdown/json.")
backend/core/__init__.py

backend/models/__init__.py

backend/services/__init__.py

backend/analyzers/__init__.py
