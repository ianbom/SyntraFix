from datetime import date, datetime, timezone

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.models.chat import Chat, ChatRole, Conversation
from app.models.document import Document, DocumentType
from app.models.user import User, UserRole


def make_session():
    engine = create_engine("sqlite:///:memory:")
    for table in (User.__table__, Document.__table__, Conversation.__table__, Chat.__table__):
        table.create(bind=engine)
    return sessionmaker(bind=engine)()


def test_list_admin_users_maps_existing_user_fields_with_pagination():
    from app.services.admin import list_admin_users

    db = make_session()
    db.add_all(
        [
            User(email="admin@example.com", username="admin", password="x", role=UserRole.admin, is_active=True),
            User(email="user@example.com", username="budi", password="x", role=UserRole.user, is_active=False),
        ]
    )
    db.commit()

    result = list_admin_users(db, page=1, per_page=10, search="bud", status="inactive")

    assert result.total == 1
    assert result.pages == 1
    assert result.users[0].username == "budi"
    assert result.users[0].email == "user@example.com"
    assert result.users[0].is_active is False


def test_get_admin_dashboard_uses_real_counts_and_recent_documents():
    from app.services.admin import get_admin_dashboard

    db = make_session()
    db.add_all(
        [
            User(email="admin@example.com", username="admin", password="x", role=UserRole.admin, is_active=True),
            User(email="user@example.com", username="user", password="x", role=UserRole.user, is_active=False),
            Document(
                title="Completed Paper",
                type=DocumentType.JOURNAL,
                processing_status="completed",
                created_at=datetime(2026, 6, 1, tzinfo=timezone.utc),
                date=date(2026, 1, 1),
            ),
            Document(
                title="Processing Paper",
                type=DocumentType.THESIS,
                processing_status="processing",
                created_at=datetime(2026, 6, 2, tzinfo=timezone.utc),
                date=date(2026, 1, 2),
            ),
        ]
    )
    db.commit()

    conversation = Conversation(user_id=1, title="Chat")
    db.add(conversation)
    db.commit()
    db.add_all(
        [
            Chat(conversation_id=conversation.id, role=ChatRole.USER, message="Q"),
            Chat(conversation_id=conversation.id, role=ChatRole.BOT, message="A"),
        ]
    )
    db.commit()

    result = get_admin_dashboard(db)

    assert result.stats.total_users == 2
    assert result.stats.active_users == 1
    assert result.stats.inactive_users == 1
    assert result.stats.total_documents == 2
    assert result.stats.processed_documents == 1
    assert result.stats.processing_documents == 1
    assert result.stats.failed_documents == 0
    assert result.stats.total_conversations == 1
    assert result.stats.total_chats == 2
    assert result.recent_documents[0].title == "Processing Paper"
    assert result.chart
