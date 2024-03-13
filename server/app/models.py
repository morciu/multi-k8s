from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from .db_config import Base


class UserCreate(BaseModel):
    email: str
    name: str


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    email = Column(String(255), unique=True, index=True)