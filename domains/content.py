from typing import List

from domains import Base
from pydantic import BaseModel, Field


class Content(Base):
    """Content"""

    title: str = Field(
        ...,
        title="Title",
        description="Title of the raid",
        examples=[
            "Brel Hard Mode",
        ],
    )


class ItemLvlContent(BaseModel):
    """Item Lvl Content"""

    min_ilvl: int | None = Field(None)
    max_ilvl: int | None = Field(None)


class LegionRaidGateContent(ItemLvlContent):
    """Legion Raid Gate Content"""

    gate: int = Field(...)


class LegionRaidModeContent(ItemLvlContent):
    """Legion Raid Mode Content"""

    mode: str = Field(...)
    gates: List[LegionRaidGateContent] | int = Field(...)


class LegionRaidContent(Content):
    """Legion Raid Content"""

    modes: List[LegionRaidModeContent] = Field(...)
