from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field


class ModelMetadata(BaseModel):
    model_id: str
    model_name: str
    algorithm: str
    problem_type: str
    version: str

    framework: str = "unknown"

    parameters: dict[str, Any] = Field(default_factory=dict)
    training_info: dict[str, Any] = Field(default_factory=dict)
    metrics: dict[str, float] = Field(default_factory=dict)

    model_path: str
    created_at: datetime = Field(default_factory=datetime.utcnow)