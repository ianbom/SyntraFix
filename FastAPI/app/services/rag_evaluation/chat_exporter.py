import csv
import json
from datetime import datetime
from io import StringIO
from typing import Iterable

from sqlalchemy.orm import Session, selectinload

from app.models.chat import Chat, ChatRole, Conversation
from app.models.document_chunk import DocumentChunk


CHAT_EXPORT_HEADERS = [
    "user_input",
    "response",
    "retrieved_contexts",
    "reference",
]


def export_chat_csv(
    db: Session,
    user_ids: list[int] | None = None,
    conversation_ids: list[int] | None = None,
    only_with_references: bool = False,
    date_from: datetime | None = None,
    date_to: datetime | None = None,
) -> bytes:
    rows = build_chat_export_rows(
        db,
        user_ids=user_ids,
        conversation_ids=conversation_ids,
        only_with_references=only_with_references,
        date_from=date_from,
        date_to=date_to,
    )
    output = StringIO()
    writer = csv.DictWriter(output, fieldnames=CHAT_EXPORT_HEADERS)
    writer.writeheader()
    writer.writerows(rows)
    return output.getvalue().encode("utf-8")


def build_chat_export_rows(
    db: Session,
    user_ids: list[int] | None = None,
    conversation_ids: list[int] | None = None,
    only_with_references: bool = False,
    date_from: datetime | None = None,
    date_to: datetime | None = None,
) -> list[dict[str, str]]:
    query = db.query(Conversation).options(
        selectinload(Conversation.chats).selectinload(Chat.references),
    )
    if user_ids:
        query = query.filter(Conversation.user_id.in_(user_ids))
    if conversation_ids:
        query = query.filter(Conversation.id.in_(conversation_ids))

    conversations = query.order_by(Conversation.created_at.asc(), Conversation.id.asc()).all()
    chunk_content = _load_chunk_content(db, conversations)
    rows: list[dict[str, str]] = []

    for conversation in conversations:
        chats = sorted(conversation.chats, key=lambda chat: (chat.created_at, chat.id))
        for index, bot_chat in enumerate(chats):
            if bot_chat.role != ChatRole.BOT:
                continue
            if not _is_within_date_range(bot_chat.created_at, date_from=date_from, date_to=date_to):
                continue
            user_chat = _previous_user_chat(chats, index)
            if user_chat is None:
                continue
            references = sorted(bot_chat.references, key=lambda ref: (-(ref.relevance_score or 0.0), ref.id))
            if only_with_references and not references:
                continue
            rows.append(
                {
                    "user_input": user_chat.message,
                    "response": bot_chat.message,
                    "retrieved_contexts": json.dumps(
                        [_context_for_reference(ref, chunk_content) for ref in references], ensure_ascii=False
                    ),
                    "reference": "",
                }
            )
    return rows


def _load_chunk_content(db: Session, conversations: Iterable[Conversation]) -> dict[int, str]:
    chunk_ids = {
        reference.chunk_id
        for conversation in conversations
        for chat in conversation.chats
        for reference in chat.references
        if reference.chunk_id
    }
    if not chunk_ids:
        return {}
    rows = db.query(DocumentChunk.id, DocumentChunk.content).filter(DocumentChunk.id.in_(chunk_ids)).all()
    return {chunk_id: content for chunk_id, content in rows if content}


def _previous_user_chat(chats: list[Chat], bot_index: int) -> Chat | None:
    for index in range(bot_index - 1, -1, -1):
        if chats[index].role == ChatRole.USER:
            return chats[index]
    return None


def _context_for_reference(reference, chunk_content: dict[int, str]) -> str:
    return chunk_content.get(reference.chunk_id) or reference.quote or ""

def _is_within_date_range(
    value: datetime | None,
    date_from: datetime | None = None,
    date_to: datetime | None = None,
) -> bool:
    if value is None:
        return False if date_from or date_to else True
    if date_from and value < date_from:
        return False
    if date_to and value > date_to:
        return False
    return True
