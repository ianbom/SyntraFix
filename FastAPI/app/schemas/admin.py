from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

from app.schemas.user import UserRole


class AdminUserItem(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    username: str
    email: str
    role: UserRole
    is_active: bool
    created_at: datetime
    updated_at: datetime | None = None


class AdminUserListResponse(BaseModel):
    users: list[AdminUserItem]
    total: int
    page: int
    per_page: int
    pages: int


class AdminDashboardStats(BaseModel):
    total_users: int
    active_users: int
    inactive_users: int
    new_users_this_month: int
    total_documents: int
    processed_documents: int
    processing_documents: int
    failed_documents: int
    total_conversations: int
    total_chats: int


class AdminDashboardChartPoint(BaseModel):
    date: str
    users: int = 0
    documents: int = 0
    chats: int = 0


class AdminRecentDocument(BaseModel):
    id: int
    title: str
    type: str | None = None
    processing_status: str | None = None
    created_at: datetime


class AdminDashboardResponse(BaseModel):
    stats: AdminDashboardStats
    chart: list[AdminDashboardChartPoint]
    recent_documents: list[AdminRecentDocument]


AdminUserStatus = Literal["active", "inactive"]
