from __future__ import annotations
from app.models.user import User
from app.models.post import Post
from app.dtos.user_dtos import UserCreate
from sqlalchemy.ext.asyncio import AsyncSession
from app.dtos.user_dtos import UserResponse
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload

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

async def get_user_with_posts(db: AsyncSession, user_id: str) -> UserResponse | None:
    result = await db.execute(
        select(User)
        .options(
            selectinload(User.posts).selectinload(Post.comments)
        )
        .where(User.id == user_id)
    )
    user = result.scalars().first()
    return user