"""Idempotent admin user seeder for Docker startup."""
import os
import sys
from pathlib import Path

from sqlalchemy.exc import IntegrityError

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.database import SessionLocal
from app.models.user import User, UserRole
from app.utils.security import get_password_hash


ADMIN_EMAIL = os.getenv("ADMIN_EMAIL", "admin@gmail.com")
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "admin")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "admin123")


def seed_admin() -> None:
    db = SessionLocal()
    try:
        user = db.query(User).filter(User.email == ADMIN_EMAIL).first()

        if user is None:
            username_owner = db.query(User).filter(User.username == ADMIN_USERNAME).first()
            if username_owner is not None:
                raise RuntimeError(
                    f"Cannot seed admin: username '{ADMIN_USERNAME}' is already used by another user."
                )

            user = User(
                email=ADMIN_EMAIL,
                username=ADMIN_USERNAME,
                password=get_password_hash(ADMIN_PASSWORD),
                role=UserRole.admin,
                is_active=True,
            )
            db.add(user)
            action = "created"
        else:
            user.password = get_password_hash(ADMIN_PASSWORD)
            user.role = UserRole.admin
            user.is_active = True
            action = "updated"

        db.commit()
        print(f"Admin seed {action}: {ADMIN_EMAIL}")
    except IntegrityError as error:
        db.rollback()
        raise RuntimeError("Failed to seed admin user due to a database constraint.") from error
    finally:
        db.close()


if __name__ == "__main__":
    seed_admin()
