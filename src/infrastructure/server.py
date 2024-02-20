"""src/infrastructure/tasks.py - Tasks"""
from typing import List

from beanie import Document
from pydantic import Field


class Server(Document):
    """Server"""

    name: str = Field(...)
    region: str = Field(...)
