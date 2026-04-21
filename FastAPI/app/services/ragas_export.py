"""Export chat data into a Markdown format suitable for RAGAS test prep."""
from datetime import datetime
from pathlib import Path
import re
from typing import Iterable, List, Optional

from sqlalchemy.orm import Session

from app.models.chat import Chat, ChatReference, ChatRole, Conversation


EXPORT_DIR = Path(__file__).resolve().parents[1] / "ragas_exports"


def _safe_filename(value: str) -> str:
    cleaned = re.sub(r"[^a-zA-Z0-9._-]+", "_", value.strip())
    cleaned = cleaned.strip("._")
    return cleaned or "ragas_dataset"


def _normalize_markdown_text(value: Optional[str]) -> str:
    text = (value or "").strip()
    return text if text else "-"


def _format_retrieved_context(references: Iterable[ChatReference]) -> str:
    quotes = []
    for index, reference in enumerate(references, start=1):
        quote = _normalize_markdown_text(reference.quote)
        source_parts = []
        if reference.document_title:
            source_parts.append(reference.document_title)
        if reference.page_number is not None:
            source_parts.append(f"page {reference.page_number}")

        source = f" ({', '.join(source_parts)})" if source_parts else ""
        quotes.append(f"{index}. {quote}{source}")

    return "\n\n".join(quotes) if quotes else "-"


def _find_previous_user_chat(chats: List[Chat], bot_index: int) -> Optional[Chat]:
    for index in range(bot_index - 1, -1, -1):
        if chats[index].role == ChatRole.USER:
            return chats[index]
    return None


def _build_ragas_markdown(conversations: List[Conversation]) -> str:
    lines = [
        "# RAGAS Test Data",
        "",
        "File ini digenerate dari tabel `chats` dan `chat_references`.",
        "`reference` sengaja dikosongkan agar dapat diisi manual.",
        "",
    ]

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
                    _format_retrieved_context(references),
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
    markdown = _build_ragas_markdown(conversations)

    EXPORT_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    scope = f"conversation_{conversation_id}" if conversation_id is not None else f"user_{user_id}"
    output_path = EXPORT_DIR / f"{_safe_filename(scope)}_ragas_{timestamp}.md"
    output_path.write_text(markdown, encoding="utf-8")
    return output_path
