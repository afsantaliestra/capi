"""Base"""
from pydantic import BaseModel, Field


class Base(BaseModel):
    """Base"""

    code: str = Field(None)


class Server(Base):
    """Server"""

    name: str = Field(...)
