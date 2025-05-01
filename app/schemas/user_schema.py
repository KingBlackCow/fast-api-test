from pydantic import BaseModel, EmailStr, ConfigDict

class UserCreate(BaseModel):
    name: str
    email: EmailStr


class UserResponse(BaseModel):
    id: int
    name: str
    email: str

    model_config = ConfigDict(from_attributes=True)  # ✅ Pydantic v2 스타일