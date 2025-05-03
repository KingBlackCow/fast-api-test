from pydantic import BaseModel

class CommentResponse(BaseModel):
    id: int
    content: str

    model_config = {"from_attributes": True}