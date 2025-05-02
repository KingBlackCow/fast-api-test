from pydantic import BaseModel, EmailStr, ConfigDict
from typing import List
from app.dtos.post_dtos import PostResponse

class UserCreate(BaseModel):
    name: str
    email: EmailStr


class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    posts: List[PostResponse] = []  # 연관된 Post 목록

    model_config = ConfigDict(from_attributes=True)  # ✅ Pydantic v2 스타일