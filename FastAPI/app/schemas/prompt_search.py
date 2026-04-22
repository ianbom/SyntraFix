from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class PromptSearchRequest(BaseModel):
    question: str = Field(..., min_length=1)
    prompt: Optional[str] = None


class PromptSearchResponse(BaseModel):
    run_id: str
    output_file: str
    best_iteration: Optional[int]
    best_score: Optional[float]
    best_prompt: Optional[str]
    iterations: List[Dict[str, Any]]

