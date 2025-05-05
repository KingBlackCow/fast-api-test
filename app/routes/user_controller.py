from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import get_db
from app.exceptions.custom_exceptions import UserNotFoundException
from app.schemas.user_schemas import UserCreate, UserResponse
from app.services.user_service import create_user, get_user, get_user_with_posts

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/{user_id}", response_model=UserResponse)
async def get_user_by_id(user_id: int, db: AsyncSession = Depends(get_db)):
    user = await get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/", response_model=UserResponse, status_code=201)
async def create_new_user(user_data: UserCreate, db: AsyncSession = Depends(get_db)):
    return await create_user(db, user_data)


@router.get("/with/{user_id}", response_model=UserResponse)
async def get_user_with_posts_(user_id: int, db: AsyncSession = Depends(get_db)):
    user = await get_user_with_posts(db, user_id)

    if not user:
        raise UserNotFoundException(user_id=user_id)

    return user
