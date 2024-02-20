"""src/infrastructure/tasks.py - Tasks"""
from typing import TYPE_CHECKING

from beanie import BackLink, Document
from pydantic import Field

if TYPE_CHECKING:
    from src.infrastructure.character import Character
    from src.infrastructure.rooster import Rooster


class Task(Document):
    """Task"""

    name: str = Field(...)
    type: str = Field(...)
    frequency: str = Field(...)  # Daily, Weekly, Bi-Weekly, Specific-Days
    repetitions: int = Field(...)  # Number of times per frequency
    value: int = Field(...)  # Number of times done per frequency

    class Settings:
        """User Settings"""

        name = "tasks"


class RoosterTask(Task):
    """Rooster Task"""

    type: str = Field("rooster")
    rooster: BackLink["Rooster"] = Field(original_field="tasks")


class CharacterTask(Task):
    """Character Task"""

    type: str = Field("character")
    character: BackLink["Character"] = Field(original_field="tasks")
    min_ilvl: int = Field(...)
    max_ilvl: int = Field(...)
