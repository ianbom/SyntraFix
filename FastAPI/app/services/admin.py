from collections import defaultdict
from datetime import datetime, timedelta, timezone
from math import ceil

from sqlalchemy import or_
from sqlalchemy.orm import Session

from app.models.chat import Chat, Conversation
from app.models.document import Document
from app.models.user import User
from app.schemas.admin import (
    AdminDashboardChartPoint,
    AdminDashboardResponse,
    AdminDashboardStats,
    AdminRecentDocument,
    AdminUserListResponse,
)


def _as_aware_utc(value: datetime | None) -> datetime | None:
    if value is None:
        return None
    if value.tzinfo is None:
        return value.replace(tzinfo=timezone.utc)
    return value.astimezone(timezone.utc)


def _date_key(value: datetime | None) -> str | None:
    normalized = _as_aware_utc(value)
    if normalized is None:
        return None
    return normalized.date().isoformat()


def list_admin_users(
    db: Session,
    page: int = 1,
    per_page: int = 10,
    search: str | None = None,
    status: str | None = None,
) -> AdminUserListResponse:
    page = max(page, 1)
    per_page = min(max(per_page, 1), 100)

    query = db.query(User)
    normalized_search = (search or "").strip()
    if normalized_search:
        search_term = f"%{normalized_search}%"
        query = query.filter(or_(User.username.ilike(search_term), User.email.ilike(search_term)))

    if status == "active":
        query = query.filter(User.is_active.is_(True))
    elif status == "inactive":
        query = query.filter(User.is_active.is_(False))

    total = query.count()
    users = (
        query.order_by(User.created_at.desc(), User.id.desc())
        .offset((page - 1) * per_page)
        .limit(per_page)
        .all()
    )
    pages = ceil(total / per_page) if total else 1

    return AdminUserListResponse(
        users=users,
        total=total,
        page=page,
        per_page=per_page,
        pages=pages,
    )


def get_admin_dashboard(db: Session) -> AdminDashboardResponse:
    now = datetime.now(timezone.utc)
    start_of_month = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    chart_start = now - timedelta(days=29)

    total_users = db.query(User).count()
    active_users = db.query(User).filter(User.is_active.is_(True)).count()
    inactive_users = db.query(User).filter(User.is_active.is_(False)).count()
    total_documents = db.query(Document).count()
    processed_documents = db.query(Document).filter(Document.processing_status == "completed").count()
    processing_documents = db.query(Document).filter(Document.processing_status == "processing").count()
    failed_documents = db.query(Document).filter(Document.processing_status == "failed").count()
    total_conversations = db.query(Conversation).count()
    total_chats = db.query(Chat).count()

    users = db.query(User.created_at).all()
    documents = db.query(Document.created_at).all()
    chats = db.query(Chat.created_at).all()

    new_users_this_month = sum(
        1 for (created_at,) in users if (_as_aware_utc(created_at) or now) >= start_of_month
    )

    buckets: dict[str, dict[str, int]] = defaultdict(lambda: {"users": 0, "documents": 0, "chats": 0})
    for offset in range(30):
        key = (chart_start + timedelta(days=offset)).date().isoformat()
        buckets[key]

    for (created_at,) in users:
        normalized = _as_aware_utc(created_at)
        if normalized and normalized >= chart_start:
            buckets[normalized.date().isoformat()]["users"] += 1
    for (created_at,) in documents:
        normalized = _as_aware_utc(created_at)
        if normalized and normalized >= chart_start:
            buckets[normalized.date().isoformat()]["documents"] += 1
    for (created_at,) in chats:
        normalized = _as_aware_utc(created_at)
        if normalized and normalized >= chart_start:
            buckets[normalized.date().isoformat()]["chats"] += 1

    recent_documents = (
        db.query(Document)
        .order_by(Document.created_at.desc(), Document.id.desc())
        .limit(10)
        .all()
    )

    return AdminDashboardResponse(
        stats=AdminDashboardStats(
            total_users=total_users,
            active_users=active_users,
            inactive_users=inactive_users,
            new_users_this_month=new_users_this_month,
            total_documents=total_documents,
            processed_documents=processed_documents,
            processing_documents=processing_documents,
            failed_documents=failed_documents,
            total_conversations=total_conversations,
            total_chats=total_chats,
        ),
        chart=[
            AdminDashboardChartPoint(date=key, **values)
            for key, values in sorted(buckets.items())
        ],
        recent_documents=[
            AdminRecentDocument(
                id=document.id,
                title=document.title,
                type=getattr(document.type, "value", document.type),
                processing_status=document.processing_status,
                created_at=document.created_at,
            )
            for document in recent_documents
        ],
    )
