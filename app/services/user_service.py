from __future__ import annotations
from app.models.user import User
from app.schemas.user_schema import UserCreate
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.user_schema import UserResponse
from sqlalchemy.future import select

async def get_user(db: AsyncSession, user_id: int) -> UserResponse | None:
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalars().first()
    return user

async def create_user(db: AsyncSession, user_data: UserCreate) -> User:
    user = User(name=user_data.name, email=user_data.email)
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user