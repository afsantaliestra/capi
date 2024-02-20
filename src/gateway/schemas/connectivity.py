"""src/gateway/schemas/connectivity.py - Connectivity API schemas"""
from pydantic import BaseModel, Field


class HeartbeatResponse(BaseModel):
    """Heartbeat Response"""

    status: str = Field(...)
    db_data: dict = Field(None)
