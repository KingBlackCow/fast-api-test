from __future__ import annotations

from app.schemas.user_schema import UserResponse

# 실제 DB 연결 대신 메모리 데이터
_fake_users = [
    UserResponse(id=1, name="Alice", email="alice@example.com"),
    UserResponse(id=2, name="Bob", email="bob@example.com"),
]

def get_user_by_id(user_id: int) -> UserResponse | None:
    return next((user for user in _fake_users if user.id == user_id), None)