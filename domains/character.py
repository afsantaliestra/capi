from typing import List

from base import Base
from pydantic import BaseModel, Field


class Gear(BaseModel):
    """Gear"""

    helmet: str = Field(...)
    pauldrons: str = Field(...)
    chest: str = Field(...)
    pants: str = Field(...)
    gaunlets: str = Field(...)
    weapon: str = Field(...)


class Jewelry(BaseModel):
    """Jewelry"""

    necklace: str = Field(...)
    ring_1: str = Field(...)
    ring_2: str = Field(...)
    earring_1: str = Field(...)
    earring_2: str = Field(...)
    bracelet: str = Field(...)
    stone: str = Field(...)


class Character(Base):
    """Character"""

    name: str = Field(...)
    gear: Gear = Field(...)
    jewelry: Jewelry = Field(...)
    gems: List[str] = Field(...)
