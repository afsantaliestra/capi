"""src/gateway/schemas/users.py - Users API schemas"""
from typing import List

from pydantic import BaseModel, Field


class PostContentSchema(BaseModel):
    """Post Content Schema"""

    name: str = Field(...)
    group: str = Field(...)
    level: str = Field(...)
    min_ilvl: str = Field(...)


class ContentResponseSchema(PostContentSchema):
    """Content Response Schema"""

    code: str = Field(...)


class ContentsResponseSchema(BaseModel):
    """Contents Response Schema"""

    count: int = Field(...)
    users: List[ContentResponseSchema] = Field(...)
