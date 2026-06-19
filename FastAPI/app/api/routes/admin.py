from typing import Annotated

from fastapi import APIRouter, Query

from app.api.deps import AdminUser, DBSession
from app.schemas.admin import AdminDashboardResponse, AdminUserListResponse, AdminUserStatus
from app.services.admin import get_admin_dashboard, list_admin_users

router = APIRouter(prefix="/admin", tags=["Admin"])


@router.get("/users", response_model=AdminUserListResponse)
def get_admin_users(
    current_user: AdminUser,
    db: DBSession,
    page: Annotated[int, Query(ge=1)] = 1,
    per_page: Annotated[int, Query(ge=1, le=100)] = 10,
    search: Annotated[str | None, Query()] = None,
    status: Annotated[AdminUserStatus | None, Query()] = None,
) -> AdminUserListResponse:
    return list_admin_users(db, page=page, per_page=per_page, search=search, status=status)


@router.get("/dashboard", response_model=AdminDashboardResponse)
def get_dashboard(current_user: AdminUser, db: DBSession) -> AdminDashboardResponse:
    return get_admin_dashboard(db)
