"""src/gateway/api/checklist.py - Connectivity Routes"""

from enum import Enum
from typing import List, Type
from uuid import UUID, uuid4

from aiotinydb import AIOTinyDB
from fastapi import APIRouter
from pydantic import BaseModel, Field, field_serializer
from tinydb import Query
from tinydb.database import Table

router = APIRouter(tags=["Checklist"])
tinydb: AIOTinyDB = AIOTinyDB("./local_dbs/tiny_db.json")


class TaskValue(BaseModel):
    """Task Value"""

    value: int = Field(...)
    max: int = Field(...)


class Taskilvl(BaseModel):
    """Task ilvl"""

    min: int = Field(...)
    max: int = Field(...)


class TaskScopeEnum(Enum):
    """Task Scope Enum"""

    USER = "user"
    ACCOUNT = "account"
    ROOSTER = "rooster"
    CHARACTER = "character"


class TaskFrequencyEnum(Enum):
    """Task Frequency Enum"""

    DAILY = "daily"
    WEEKLY = "weekly"
    BI_WEEKLY = "bi_weekly"
    SPECIFIC_DAYS = "specific_days"


class Task(BaseModel):
    """Task"""

    # Meta
    scope: TaskScopeEnum = Field(...)
    frequency: TaskFrequencyEnum = Field(...)

    # Data
    name: str = Field(...)
    ilvl: Taskilvl = Field(...)
    value: TaskValue = Field(...)

    @field_serializer("scope", "frequency")
    def code_serializer(self, field: Type[Enum], _info):
        """Code Serializer"""
        return field.value


class Tasks(BaseModel):
    """Tasks"""

    dailies: List[Task] = Field(None)
    weeklies: List[Task] = Field(None)
    bi_weeklies: List[Task] = Field(None)
    specific_days: List[Task] = Field(None)


global_tasks = {  # TODO: Review Min y Max ilvl of tasks.
    "user_global_tasks": Tasks(),
    "account_global_tasks": Tasks(),
    "rooster_global_tasks": Tasks(
        dailies=[
            Task(
                scope=TaskScopeEnum.ROOSTER,
                frequency=TaskFrequencyEnum.DAILY,
                name="Playtime Rewards",
                ilvl=Taskilvl(min=1400, max=9999),
                value=TaskValue(value=0, max=6),
            ),
            Task(
                scope=TaskScopeEnum.ROOSTER,
                frequency=TaskFrequencyEnum.DAILY,
                name="Event",
                ilvl=Taskilvl(min=1400, max=9999),
                value=TaskValue(value=0, max=1),
            ),
        ],
        weeklies=[
            Task(
                scope=TaskScopeEnum.ROOSTER,
                frequency=TaskFrequencyEnum.WEEKLY,
                name="Challenge Guardian Raids",
                ilvl=Taskilvl(min=1400, max=9999),
                value=TaskValue(value=0, max=3),
            ),
            Task(
                scope=TaskScopeEnum.ROOSTER,
                frequency=TaskFrequencyEnum.WEEKLY,
                name="Challenge Abyssal Dungeons",
                ilvl=Taskilvl(min=1400, max=9999),
                value=TaskValue(value=0, max=2),
            ),
        ],
        specific_days=[
            Task(
                scope=TaskScopeEnum.ROOSTER,
                frequency=TaskFrequencyEnum.SPECIFIC_DAYS,
                name="World Boss",
                ilvl=Taskilvl(min=1400, max=9999),
                value=TaskValue(value=0, max=1),
            ),
            Task(
                scope=TaskScopeEnum.ROOSTER,
                frequency=TaskFrequencyEnum.SPECIFIC_DAYS,
                name="Chaos Gate",
                ilvl=Taskilvl(min=1400, max=9999),
                value=TaskValue(value=0, max=1),
            ),
        ],
    ),
    "character_global_tasks": Tasks(
        dailies=[
            Task(
                scope=TaskScopeEnum.CHARACTER,
                frequency=TaskFrequencyEnum.DAILY,
                name="Guild Donation",
                ilvl=Taskilvl(min=0, max=9999),
                value=TaskValue(value=0, max=1),
            ),
            Task(
                scope=TaskScopeEnum.CHARACTER,
                frequency=TaskFrequencyEnum.DAILY,
                name="Chaos Dungeon",
                ilvl=Taskilvl(min=1400, max=9999),
                value=TaskValue(value=0, max=2),
            ),
            Task(
                scope=TaskScopeEnum.CHARACTER,
                frequency=TaskFrequencyEnum.DAILY,
                name="Guardian Raid",
                ilvl=Taskilvl(min=1400, max=9999),
                value=TaskValue(value=0, max=1),
            ),
            Task(
                scope=TaskScopeEnum.CHARACTER,
                frequency=TaskFrequencyEnum.DAILY,
                name="UNA's Tasks (Dailies)",
                ilvl=Taskilvl(min=1400, max=9999),
                value=TaskValue(value=0, max=3),
            ),
        ],
        weeklies=[
            Task(
                scope=TaskScopeEnum.CHARACTER,
                frequency=TaskFrequencyEnum.WEEKLY,
                name="UNA's Tasks (Weeklies)",
                ilvl=Taskilvl(min=1400, max=9999),
                value=TaskValue(value=0, max=3),
            ),
            Task(
                scope=TaskScopeEnum.CHARACTER,
                frequency=TaskFrequencyEnum.WEEKLY,
                name="Oreha's Well",
                ilvl=Taskilvl(min=1400, max=9999),
                value=TaskValue(value=0, max=2),
            ),
            Task(
                scope=TaskScopeEnum.CHARACTER,
                frequency=TaskFrequencyEnum.WEEKLY,
                name="Argos",
                ilvl=Taskilvl(min=1400, max=9999),
                value=TaskValue(value=0, max=3),
            ),
            Task(
                scope=TaskScopeEnum.CHARACTER,
                frequency=TaskFrequencyEnum.WEEKLY,
                name="Valtan",
                ilvl=Taskilvl(min=1400, max=9999),
                value=TaskValue(value=0, max=2),
            ),
            Task(
                scope=TaskScopeEnum.CHARACTER,
                frequency=TaskFrequencyEnum.WEEKLY,
                name="Vykas",
                ilvl=Taskilvl(min=1400, max=9999),
                value=TaskValue(value=0, max=2),
            ),
            Task(
                scope=TaskScopeEnum.CHARACTER,
                frequency=TaskFrequencyEnum.WEEKLY,
                name="Kakul-Saydon",
                ilvl=Taskilvl(min=1400, max=9999),
                value=TaskValue(value=0, max=3),
            ),
            Task(
                scope=TaskScopeEnum.CHARACTER,
                frequency=TaskFrequencyEnum.WEEKLY,
                name="Brelshaza 1-2",
                ilvl=Taskilvl(min=1400, max=9999),
                value=TaskValue(value=0, max=2),
            ),
            Task(
                scope=TaskScopeEnum.CHARACTER,
                frequency=TaskFrequencyEnum.WEEKLY,
                name="Brelshaza 3",
                ilvl=Taskilvl(min=1400, max=9999),
                value=TaskValue(value=0, max=1),
            ),
            Task(
                scope=TaskScopeEnum.CHARACTER,
                frequency=TaskFrequencyEnum.WEEKLY,
                name="Kayangel",
                ilvl=Taskilvl(min=1400, max=9999),
                value=TaskValue(value=0, max=3),
            ),
            Task(
                scope=TaskScopeEnum.CHARACTER,
                frequency=TaskFrequencyEnum.WEEKLY,
                name="Akkan",
                ilvl=Taskilvl(min=1400, max=9999),
                value=TaskValue(value=0, max=3),
            ),
            Task(
                scope=TaskScopeEnum.CHARACTER,
                frequency=TaskFrequencyEnum.WEEKLY,
                name="Ivory Tower of Chaos",
                ilvl=Taskilvl(min=1400, max=9999),
                value=TaskValue(value=0, max=4),
            ),
        ],
        bi_weeklies=[
            Task(
                scope=TaskScopeEnum.CHARACTER,
                frequency=TaskFrequencyEnum.BI_WEEKLY,
                name="Brelshaza 4",
                ilvl=Taskilvl(min=1400, max=9999),
                value=TaskValue(value=0, max=1),
            ),
            Task(
                scope=TaskScopeEnum.CHARACTER,
                frequency=TaskFrequencyEnum.BI_WEEKLY,
                name="Valtan Extreme",
                ilvl=Taskilvl(min=1400, max=9999),
                value=TaskValue(value=0, max=2),
            ),
        ],
    ),
}


class DataModelWithTasks(BaseModel):
    """Data Model With Tasks"""

    tasks: Tasks = Field(None)

    @field_serializer("tasks")
    def tasks_serializer(self, tasks: Tasks, _info):
        """Tasks Serializer"""
        if tasks.model_dump(exclude_unset=True):
            return tasks
        return {}


class CharacterData(DataModelWithTasks):
    """Character Data"""

    name: str = Field(...)
    classs: str = Field(..., alias="class")
    sub_class: str = Field(...)
    ilvl: float = Field(...)
    tasks: Tasks = Field(default=global_tasks["character_global_tasks"])


class RoosterData(DataModelWithTasks):
    """Roooster Data"""

    name: str = Field(...)
    characters: List[CharacterData] = Field(...)
    tasks: Tasks = Field(default=global_tasks["rooster_global_tasks"])


class AccountData(DataModelWithTasks):
    """Account Data"""

    name: str = Field(...)
    roosters: List[RoosterData] = Field(...)
    tasks: Tasks = Field(default=global_tasks["account_global_tasks"])


class UserData(DataModelWithTasks):
    """User Data"""

    code: UUID = Field(..., default_factory=uuid4)
    username: str = Field(...)
    display_name: str = Field(...)
    accounts: List[AccountData] = Field(...)
    tasks: Tasks = Field(default=global_tasks["user_global_tasks"])

    @field_serializer("code")
    def code_serializer(self, code: UUID, _info):
        """Code Serializer"""
        return code.hex


@router.post(
    "/",
)
async def create_user(user: UserData):
    """Create User"""
    async with tinydb as database:
        table: Table = database.table("users")

        if table.contains(Query()["username"] == user.username):
            return None  # TODO: Improve response to a 404.

        # Insert user
        table.insert(user.model_dump(warnings=False, by_alias=True))

    return user


@router.get(
    "/{code}",
)
async def read_user(code: str):
    """Read User"""
    async with tinydb as database:
        table: Table = database.table("users")
        data = table.get(Query()["code"] == code)

    return data


@router.put(
    "/{code}",
)
async def update_all_user(code: str, user: UserData):
    """Update All User"""


@router.post(
    "/{code}",
)
async def update_user(user: UserData):
    """Update User"""
