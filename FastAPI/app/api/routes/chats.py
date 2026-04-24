import json
import time
from typing import List, Optional
from functools import wraps
from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi.responses import FileResponse, StreamingResponse
from sqlalchemy.orm import Session
import google.generativeai as genai

from app.database import get_db
from app.models.user import User
from app.api.deps import get_current_user
from app.schemas.chat import ChatRequest, ChatResponse, ConversationResponse
from app.services.chat import ChatService
from app.services.chat_test_export import export_chat_test_markdown_for_bot_chat
from app.services.ragas_export import export_ragas_markdown
from app.config import get_settings

router = APIRouter(prefix="/chats", tags=["Chats"])
settings = get_settings()


def _print_timing(function_name: str, elapsed_seconds: float):
    """Print timing information for route-level instrumentation."""
    print(f"[CHAT API TIMING] {function_name}: {elapsed_seconds:.4f}s")


def _timed_async_route(function_name: str):
    """Decorator to print execution time for async route handlers."""
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            started_at = time.perf_counter()
            try:
                return await func(*args, **kwargs)
            finally:
                _print_timing(function_name, time.perf_counter() - started_at)

        return wrapper

    return decorator


@_timed_async_route("chat_interaction")
@router.post("/", response_model=ChatResponse)
async def chat_interaction(
    request: ChatRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Process a chat message from the user.
    Creates conversation if not exists, saves user message,
    generates bot response via LLM + RAG, and saves references.
    """
    total_started_at = time.perf_counter()
    chat_service = ChatService(db)
    process_chat_started_at = time.perf_counter()
    response = await chat_service.process_chat(current_user.id, request)
    _print_timing("chat_interaction.process_chat", time.perf_counter() - process_chat_started_at)
    try:
        export_started_at = time.perf_counter()
        export_chat_test_markdown_for_bot_chat(db, response.id)
        _print_timing(
            "chat_interaction.export_chat_test_markdown_for_bot_chat",
            time.perf_counter() - export_started_at,
        )
    except Exception as error:
        print(f"Warning: failed to export chat_test markdown for chat {response.id}: {error}")
    _print_timing("chat_interaction.total", time.perf_counter() - total_started_at)
    return response


@_timed_async_route("chat_interaction_stream")
@router.post("/stream")
async def chat_interaction_stream(
    request: ChatRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Stream chat response token-by-token for realtime UI updates.
    """
    chat_service = ChatService(db)

    async def stream_generator():
        total_started_at = time.perf_counter()
        process_stream_started_at = time.perf_counter()
        try:
            async for event in chat_service.process_chat_stream(current_user.id, request):
                if event.get("type") == "done":
                    _print_timing(
                        "chat_interaction_stream.process_chat_stream",
                        time.perf_counter() - process_stream_started_at,
                    )
                    chat_id = event.get("chat", {}).get("id")
                    if chat_id is not None:
                        try:
                            export_started_at = time.perf_counter()
                            export_chat_test_markdown_for_bot_chat(db, chat_id)
                            _print_timing(
                                "chat_interaction_stream.export_chat_test_markdown_for_bot_chat",
                                time.perf_counter() - export_started_at,
                            )
                        except Exception as export_error:
                            print(
                                "Warning: failed to export chat_test markdown "
                                f"for chat {chat_id}: {export_error}"
                            )
                yield json.dumps(event, ensure_ascii=False) + "\n"
        except Exception as error:
            yield json.dumps(
                {"type": "error", "message": str(error)},
                ensure_ascii=False,
            ) + "\n"
        finally:
            _print_timing("chat_interaction_stream.total", time.perf_counter() - total_started_at)

    return StreamingResponse(stream_generator(), media_type="application/x-ndjson")


@_timed_async_route("list_conversations")
@router.get("/conversations", response_model=List[ConversationResponse])
async def list_conversations(
    limit: int = Query(20, le=100),
    offset: int = 0,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """List interactions/conversations for the current user."""
    chat_service = ChatService(db)
    conversations = chat_service.list_conversations(current_user.id, limit, offset)
    return conversations


@_timed_async_route("get_conversation")
@router.get("/conversations/{conversation_id}", response_model=ConversationResponse)
async def get_conversation(
    conversation_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get history of a specific conversation."""
    chat_service = ChatService(db)
    conversation = chat_service.get_conversation(conversation_id, current_user.id)
    if not conversation:
        raise HTTPException(status_code=404, detail="Conversation not found")
    return conversation


@_timed_async_route("export_ragas_test_data")
@router.get("/ragas/export")
async def export_ragas_test_data(
    conversation_id: Optional[int] = Query(default=None),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    Export chat data for RAGAS test preparation as a Markdown file.

    Fields:
    - user_input: previous user chat message
    - retrieved_context: ChatReference.quote from the bot answer
    - response: bot chat message
    - reference: empty field to be filled manually
    """
    if conversation_id is not None:
        chat_service = ChatService(db)
        conversation = chat_service.get_conversation(conversation_id, current_user.id)
        if not conversation:
            raise HTTPException(status_code=404, detail="Conversation not found")

    output_path = export_ragas_markdown(
        db=db,
        user_id=current_user.id,
        conversation_id=conversation_id,
    )

    return FileResponse(
        path=output_path,
        media_type="text/markdown",
        filename=output_path.name,
    )


@_timed_async_route("list_embedding_models")
@router.get("/models/embedding")
async def list_embedding_models():
    """
    List all available Google Gemini embedding models.
    Returns models that support 'embedContent' method.
    """
    api_key = settings.GOOGLE_API_KEY or settings.GEMINI_API_KEY
    if not api_key:
        raise HTTPException(status_code=500, detail="Google API key not configured")
    
    try:
        genai.configure(api_key=api_key)
        
        embedding_models = []
        generation_models = []
        
        for m in genai.list_models():
            methods = m.supported_generation_methods
            
            model_info = {
                "name": m.name,
                "display_name": m.display_name,
                "description": m.description,
                "supported_methods": methods
            }
            
            # Categorize models
            if 'embedContent' in methods:
                embedding_models.append(model_info)
            if 'generateContent' in methods:
                generation_models.append(model_info)
        
        return {
            "current_embedding_model": settings.GOOGLE_EMBEDDING_MODEL,
            "current_generation_model": settings.GOOGLE_GENERATION_MODEL,
            "embedding_models": embedding_models,
            "generation_models": generation_models
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to list models: {str(e)}")
