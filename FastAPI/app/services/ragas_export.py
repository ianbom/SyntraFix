"""Export chat data into a Markdown format suitable for RAGAS test prep."""
from datetime import datetime
from pathlib import Path
import re
from typing import Dict, Iterable, List, Mapping, Optional, Set

from sqlalchemy.orm import Session

from app.models.chat import Chat, ChatReference, ChatRole, Conversation
from app.models.document_chunk import DocumentChunk


EXPORT_DIR = Path(__file__).resolve().parents[1] / "ragas_exports"


def _safe_filename(value: str) -> str:
    cleaned = re.sub(r"[^a-zA-Z0-9._-]+", "_", value.strip())
    cleaned = cleaned.strip("._")
    return cleaned or "ragas_dataset"


def _normalize_markdown_text(value: Optional[str]) -> str:
    text = (value or "").strip()
    return text if text else "-"


def _reference_context_text(
    reference: ChatReference,
    chunk_content_by_id: Mapping[int, str],
) -> str:
    if reference.chunk_id and reference.chunk_id in chunk_content_by_id:
        chunk_content = _normalize_markdown_text(chunk_content_by_id[reference.chunk_id])
        if chunk_content != "-":
            return chunk_content

    return _normalize_markdown_text(reference.quote)


def _format_retrieved_context(
    references: Iterable[ChatReference],
    chunk_content_by_id: Optional[Mapping[int, str]] = None,
) -> str:
    quotes = []
    chunk_content_by_id = chunk_content_by_id or {}

    for index, reference in enumerate(references, start=1):
        quote = _reference_context_text(reference, chunk_content_by_id)
        source_parts = []
        if reference.document_title:
            source_parts.append(reference.document_title)
        if reference.page_number is not None:
            source_parts.append(f"page {reference.page_number}")

        source = f" ({', '.join(source_parts)})" if source_parts else ""
        quotes.append(f"{index}. {quote}{source}")

    return "\n\n".join(quotes) if quotes else "-"


def _collect_reference_chunk_ids(conversations: Iterable[Conversation]) -> Set[int]:
    chunk_ids: Set[int] = set()
    for conversation in conversations:
        for chat in conversation.chats:
            for reference in chat.references:
                if reference.chunk_id:
                    chunk_ids.add(reference.chunk_id)
    return chunk_ids


def _load_chunk_content_by_id(db: Session, chunk_ids: Set[int]) -> Dict[int, str]:
    if not chunk_ids:
        return {}

    rows = (
        db.query(DocumentChunk.id, DocumentChunk.content)
        .filter(DocumentChunk.id.in_(chunk_ids))
        .all()
    )
    return {chunk_id: content for chunk_id, content in rows if content}


def _find_previous_user_chat(chats: List[Chat], bot_index: int) -> Optional[Chat]:
    for index in range(bot_index - 1, -1, -1):
        if chats[index].role == ChatRole.USER:
            return chats[index]
    return None


def _build_ragas_markdown(
    conversations: List[Conversation],
    chunk_content_by_id: Optional[Mapping[int, str]] = None,
) -> str:
    lines = [
        "# RAGAS Test Data",
        "",
        "File ini digenerate dari tabel `chats`, `chat_references`, dan `document_chunks`.",
        "`retrieved_context` memakai `document_chunks.content` jika tersedia, lalu fallback ke `chat_references.quote`.",
        "`reference` sengaja dikosongkan agar dapat diisi manual.",
        "",
    ]
    chunk_content_by_id = chunk_content_by_id or {}

    sample_index = 1
    for conversation in conversations:
        chats = sorted(conversation.chats, key=lambda chat: (chat.created_at, chat.id))
        for index, chat in enumerate(chats):
            if chat.role != ChatRole.BOT:
                continue

            user_chat = _find_previous_user_chat(chats, index)
            if not user_chat:
                continue

            references = sorted(
                chat.references,
                key=lambda reference: (
                    -(reference.relevance_score or 0.0),
                    reference.id,
                ),
            )

            lines.extend(
                [
                    f"## Sample {sample_index}",
                    "",
                    f"- conversation_id: {conversation.id}",
                    f"- user_chat_id: {user_chat.id}",
                    f"- bot_chat_id: {chat.id}",
                    "",
                    "### user_input",
                    "",
                    _normalize_markdown_text(user_chat.message),
                    "",
                    "### retrieved_context",
                    "",
                    _format_retrieved_context(references, chunk_content_by_id),
                    "",
                    "### response",
                    "",
                    _normalize_markdown_text(chat.message),
                    "",
                    "### reference",
                    "",
                    "",
                    "---",
                    "",
                ]
            )
            sample_index += 1

    if sample_index == 1:
        lines.extend(
            [
                "Belum ada pasangan chat user-bot yang dapat diexport.",
                "",
            ]
        )

    return "\n".join(lines)


def export_ragas_markdown(
    db: Session,
    user_id: int,
    conversation_id: Optional[int] = None,
) -> Path:
    """Generate a Markdown file containing user_input, contexts, response, reference."""
    query = (
        db.query(Conversation)
        .filter(Conversation.user_id == user_id)
        .order_by(Conversation.created_at.asc(), Conversation.id.asc())
    )
    if conversation_id is not None:
        query = query.filter(Conversation.id == conversation_id)

    conversations = query.all()
    chunk_content_by_id = _load_chunk_content_by_id(
        db,
        _collect_reference_chunk_ids(conversations),
    )
    markdown = _build_ragas_markdown(conversations, chunk_content_by_id)

    EXPORT_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    scope = f"conversation_{conversation_id}" if conversation_id is not None else f"user_{user_id}"
    output_path = EXPORT_DIR / f"{_safe_filename(scope)}_ragas_{timestamp}.md"
    output_path.write_text(markdown, encoding="utf-8")
    return output_path
