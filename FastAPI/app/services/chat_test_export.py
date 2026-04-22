"""Export a single chat response as Markdown for RAGAS test preparation."""
from datetime import datetime
from pathlib import Path
import re
from typing import Iterable, Optional

from sqlalchemy.orm import Session

from app.models.chat import Chat, ChatReference, ChatRole, Conversation


CHAT_TEST_DIR = Path(__file__).resolve().parents[1] / "chat_test"


def safe_filename(value: str) -> str:
    """Return a Windows-safe filename segment."""
    cleaned = re.sub(r"[^a-zA-Z0-9._-]+", "_", (value or "").strip())
    cleaned = cleaned.strip("._")
    return cleaned[:120] or "chat_test"


def normalize_markdown_text(value: Optional[str]) -> str:
    text = (value or "").strip()
    return text if text else "-"


def format_retrieved_context(references: Iterable[ChatReference]) -> str:
    """Format chat references like the RAGAS markdown sample."""
    rows = []
    for index, reference in enumerate(references, start=1):
        quote = normalize_markdown_text(reference.quote)
        source_parts = []
        if reference.document_title:
            source_parts.append(reference.document_title)
        if reference.page_number is not None:
            source_parts.append(f"page {reference.page_number}")

        source = f" ({', '.join(source_parts)})" if source_parts else ""
        rows.append(f"{index}. {quote}{source}")

    return "\n\n".join(rows) if rows else "-"


def build_single_chat_test_markdown(
    conversation: Conversation,
    user_chat: Chat,
    bot_chat: Chat,
) -> str:
    """Build a one-sample Markdown file matching new-sample.md shape."""
    references = sorted(
        bot_chat.references,
        key=lambda reference: (
            -(reference.relevance_score or 0.0),
            reference.id,
        ),
    )

    lines = [
        "# RAGAS Test Data",
        "",
        "File ini digenerate dari tabel `chats` dan `chat_references`.",
        "`reference` sengaja dikosongkan agar dapat diisi manual.",
        "",
        "## Sample 1",
        "",
        f"- conversation_id: {conversation.id}",
        f"- user_chat_id: {user_chat.id}",
        f"- bot_chat_id: {bot_chat.id}",
        "",
        "### user_input",
        "",
        normalize_markdown_text(user_chat.message),
        "",
        "### retrieved_context",
        "",
        format_retrieved_context(references),
        "",
        "### response",
        "",
        normalize_markdown_text(bot_chat.message),
        "",
        "### reference",
        "",
        "",
        "---",
        "",
    ]
    return "\n".join(lines)


def export_single_chat_test_markdown(
    conversation: Conversation,
    user_chat: Chat,
    bot_chat: Chat,
    output_dir: Path = CHAT_TEST_DIR,
) -> Path:
    """Write a one-sample chat test Markdown file."""
    output_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    question_slug = safe_filename(user_chat.message)
    output_path = output_dir / (
        f"conversation_{conversation.id}_chat_{bot_chat.id}_{question_slug}_{timestamp}.md"
    )
    suffix = 1
    while output_path.exists():
        output_path = output_dir / (
            f"conversation_{conversation.id}_chat_{bot_chat.id}_"
            f"{question_slug}_{timestamp}_{suffix:02d}.md"
        )
        suffix += 1

    output_path.write_text(
        build_single_chat_test_markdown(conversation, user_chat, bot_chat),
        encoding="utf-8",
    )
    return output_path


def export_chat_test_markdown_for_bot_chat(db: Session, bot_chat_id: int) -> Path:
    """Find the user/bot pair and export it as a one-sample Markdown file."""
    bot_chat = (
        db.query(Chat)
        .filter(Chat.id == bot_chat_id, Chat.role == ChatRole.BOT)
        .first()
    )
    if not bot_chat:
        raise ValueError(f"Bot chat not found: {bot_chat_id}")

    conversation = (
        db.query(Conversation)
        .filter(Conversation.id == bot_chat.conversation_id)
        .first()
    )
    if not conversation:
        raise ValueError(f"Conversation not found: {bot_chat.conversation_id}")

    user_chat = (
        db.query(Chat)
        .filter(
            Chat.conversation_id == bot_chat.conversation_id,
            Chat.role == ChatRole.USER,
            Chat.id < bot_chat.id,
        )
        .order_by(Chat.id.desc())
        .first()
    )
    if not user_chat:
        raise ValueError(f"Previous user chat not found for bot chat: {bot_chat_id}")

    return export_single_chat_test_markdown(conversation, user_chat, bot_chat)
