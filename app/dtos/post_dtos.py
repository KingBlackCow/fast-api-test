from pydantic import BaseModel
from typing import List
from app.dtos.comment_dtos import CommentResponse

class PostResponse(BaseModel):
    id: int
    title: str
    content: str
    comments: List[CommentResponse] = []

    model_config = {"from_attributes": True}