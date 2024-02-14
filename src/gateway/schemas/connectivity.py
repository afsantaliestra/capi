"""src/gateway/schemas/connectivity.py - Connectivity API schemas"""
from pydantic import BaseModel, Field


class HeartbeatResponseSchema(BaseModel):
    """Heartbeat Response Schema"""

    status: str = Field(...)
