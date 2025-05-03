from pydantic import BaseModel
from typing import List
from app.schemas.comment_schemas import CommentResponse

class PostResponse(BaseModel):
    id: int
    title: str
    content: str
    comments: List[CommentResponse] = []

    model_config = {"from_attributes": True}