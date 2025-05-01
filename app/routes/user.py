from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.user import User
from app.dependencies import get_db
from app.schemas.user_schema import UserCreate, UserResponse
from app.services.user_service import create_user
router = APIRouter(prefix="/users", tags=["users"])

@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalars().first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
@router.post("/", response_model=UserResponse, status_code=201)
async def create_new_user(user_data: UserCreate, db: AsyncSession = Depends(get_db)):
    return await create_user(db, user_data)