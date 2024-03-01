"""DB"""
from typing import List

from pydantic import BaseModel, Field


# APP ITEMS
class Base(BaseModel):
    """Base"""

    code: str = Field(None)


class Server(Base):
    """Server"""

    name: str = Field(...)


class Content(Base):
    """Content"""

    title: str = Field(
        ...,
        title="Title",
        description="Title of the raid",
        examples=["Brel Hard Mode"],
    )
    min_ilvl: int = Field(
        ...,
        title="Min Item Level",
        description="Minimal item level to access the content.",
        examples=[1540, 1580],
    )
    max_ilvl: int | None = Field(
        None,
        title="Max Item Level",
        description="Maximun item level to access the content (normally to get gold from it).",
        examples=[None, 1540, 1580],
    )
    modes: List[str] | None = Field(
        None,
        title="Modes",
        description="Modes of the content",
        examples=[["Rehershal", "Normal", "Hard", "Inferno"]],
    )
    gates: int | None = Field(
        None,
        title="Gates",
        description="Gates in the content, if any.",
        examples=[2, 3, 4],
    )


# APP ITEMS -- Legion Raids
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


class LegionRaidContent(Base):
    """Legion Raid Content"""

    title: str = Field(...)
    modes: List[LegionRaidModeContent] = Field(...)


class Task(Base):
    """Task"""

class RaidTask(Task):
    """Raid Task"""

class AbyssalDungeonTask(Task):
    """Abyssal Dungeon Task"""
# USER ITEMS
class User(Base):
    """User"""

    username: str = Field(..., examples=["Necros", "Sorcen"])


class Account(Base):
    """Account"""

    name: str = Field(...)
    # Links
    user: User = Field(...)


class Rooster(Base):
    """Rooster"""

    # Links
    server: Server = Field(...)
    account: Account = Field(...)


class Character(Base):
    """Character"""

    name: str = Field(...)
    # Links
    user: User = Field(...)
    account: Account = Field(...)
    rooster: Rooster = Field(...)


class TaskRepetitions(BaseModel):
    """Task Repetitions"""

    max: int = Field(...)
    actual: int = Field(...)


class Task(Base):
    """Task"""

    title: str = Field(...)
    scope: str = Field(...)
    frequenzy: str = Field(...)
    repetitions: TaskRepetitions = Field(...)


print(
    [
        LegionRaidContent(
            **{
                "title": "Valtan",
                "modes": [
                    {
                        "mode": "normal",
                        "min_ilvl": 1415,
                        "max_ilvl": None,
                        "gates": 2,
                    },
                    {
                        "mode": "hard",
                        "min_ilvl": 1445,
                        "max_ilvl": None,
                        "gates": 2,
                    },
                    {
                        "mode": "inferno",
                        "min_ilvl": 1445,
                        "max_ilvl": None,
                        "gates": 2,
                    },
                    {
                        "mode": "extreme",
                        "min_ilvl": 1415,
                        "max_ilvl": None,
                        "gates": 2,
                    },
                ],
            }
        ),
        LegionRaidContent(
            **{
                "title": "Brel",
                "modes": [
                    {
                        "mode": "rehershal",
                        "min_ilvl": 1460,  # TODO: Review
                        "max_ilvl": None,
                        "gates": 3,
                    },
                    {
                        "mode": "normal",
                        "gates": [
                            {
                                "gate": 1,
                                "min_ilvl": 1490,
                                "max_ilvl": None,
                            },
                            {
                                "gate": 2,
                                "min_ilvl": 1490,
                                "max_ilvl": None,
                            },
                            {
                                "gate": 3,
                                "min_ilvl": 1500,
                                "max_ilvl": None,
                            },
                            {
                                "gate": 4,
                                "min_ilvl": 1520,
                                "max_ilvl": None,
                            },
                        ],
                    },
                    {
                        "mode": "hard",
                        "gates": [
                            {
                                "gate": 1,
                                "min_ilvl": 1540,
                                "max_ilvl": None,
                            },
                            {
                                "gate": 2,
                                "min_ilvl": 1540,
                                "max_ilvl": None,
                            },
                            {
                                "gate": 3,
                                "min_ilvl": 1550,
                                "max_ilvl": None,
                            },
                            {
                                "gate": 4,
                                "min_ilvl": 1560,
                                "max_ilvl": None,
                            },
                        ],
                    },
                    {
                        "mode": "inferno",
                        "gates": [
                            {
                                "gate": 1,
                                "min_ilvl": 1490,  # TODO: Review
                                "max_ilvl": None,
                            },
                            {
                                "gate": 2,
                                "min_ilvl": 1490,  # TODO: Review
                                "max_ilvl": None,
                            },
                        ],
                    },
                ],
            }
        ),
    ]
)
