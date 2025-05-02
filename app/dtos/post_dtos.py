from pydantic import BaseModel

class PostResponse(BaseModel):
    id: int
    title: str
    content: str

    model_config = {"from_attributes": True}