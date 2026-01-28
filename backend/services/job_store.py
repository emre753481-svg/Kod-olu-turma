from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, Literal
import time
import uuid

Status = Literal["queued", "running", "completed", "failed"]

@dataclass
class Job:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    status: Status = "queued"
    progress: int = 0
    message: str | None = None
    created_at: float = field(default_factory=time.time)
    updated_at: float = field(default_factory=time.time)
    results: dict[str, Any] | None = None
    error: str | None = None

class InMemoryJobStore:
    def __init__(self) -> None:
        self._jobs: dict[str, Job] = {}

    def create(self) -> Job:
        job = Job()
        self._jobs[job.id] = job
        return job

    def get(self, job_id: str) -> Job:
        return self._jobs[job_id]

    def update(self, job_id: str, **kwargs: Any) -> Job:
        job = self._jobs[job_id]
        for k, v in kwargs.items():
            setattr(job, k, v)
        job.updated_at = time.time()
        self._jobs[job_id] = job
        return job
