from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.prompt_search import PromptSearchRequest, PromptSearchResponse
from app.services.prompt_search.runner import PromptSearchRunner


router = APIRouter(prefix="/prompt-search", tags=["Prompt Search"])


@router.post("/run", response_model=PromptSearchResponse)
async def run_prompt_search(
    request: PromptSearchRequest,
    db: Session = Depends(get_db),
):
    """Run prompt-search experiment without saving to chat tables."""
    runner = PromptSearchRunner(db)
    return await runner.run(question=request.question, prompt=request.prompt)
