"""src/gateway/schemas/accounts.py - Account Schemas"""
from pydantic import BaseModel, Field


class PostAccount(BaseModel):
    """Post Account"""

    name: str = Field(...)


class AccountResponse(PostAccount):
    """Account Response"""
