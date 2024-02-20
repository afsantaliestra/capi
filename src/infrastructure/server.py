"""src/infrastructure/servers.py - Servers"""
from beanie import Document
from pydantic import Field


class Server(Document):
    """Server"""

    name: str = Field(...)
    region: str = Field(...)

    class Settings:
        """Server Settings"""

        name = "servers"
