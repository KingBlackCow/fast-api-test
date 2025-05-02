from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
from app.models.comment import Comment
from app.models.user import User

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    content = Column(String(500))
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship(User, back_populates="posts")
    comments = relationship(Comment, back_populates="post")