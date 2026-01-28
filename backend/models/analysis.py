from pydantic import BaseModel, Field
from typing import Literal, Any

class AnalyzeRequest(BaseModel):
    repo_url: str = Field(..., examples=["https://github.com/OWNER/REPO"])
    github_token: str | None = Field(None, description="If omitted, backend uses GITHUB_TOKEN env var.")
    provider: Literal["openai", "anthropic"] | None = None

class AnalyzeResponse(BaseModel):
    analysis_id: str

class StatusResponse(BaseModel):
    analysis_id: str
    status: Literal["queued", "running", "completed", "failed"]
    progress: int = 0
    message: str | None = None

class ResultsResponse(BaseModel):
    analysis_id: str
    status: Literal["queued", "running", "completed", "failed"]
    results: dict[str, Any] | None = None
