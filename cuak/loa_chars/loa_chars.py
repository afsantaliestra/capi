""" LOA CHARS - Heavily inspired by LostArk Helper"""
from datetime import datetime
from typing import List
from uuid import uuid4

from pydantic import BaseModel, Field

tasks = [
    {"name": "Chaos Dungeon", "reps": 2, "dones": 0},
    {"name": "Guardian Raid", "reps": 1, "dones": 0},
]


class Task(BaseModel):
    """Task"""

    name: str = Field(...)
    reps: int = Field(...)
    dones: int = Field(...)


class Character(BaseModel):
    """Character"""

    code: str = Field(...)
    name: str = Field(...)
    item_level: float = Field(...)
    text: str = Field(...)
    tasks: List[Task] = Field(...)
    past_tasks: List[List[Task]] = Field(...)


character = Character(
    code=uuid4().hex,
    name="Kayleenaiah",
    item_level=1611.66,
    text="This is my main character",
    tasks=[Task(name="Chaos Dungeon", reps=2, dones=0)],
    past_tasks=[],
)
print(character)
print(datetime(2024, 1, 1, 16))
print(datetime.now())
now = datetime.now()

print(now.hour)
if now.hour >= 10:
    # New Day, generate new tasks.
    character.past_tasks.append(character.tasks)
    character.tasks = tasks

    # TODO: Esto en la base de datos, serían registros nuevos con la información nueva y
    # moviendo la otra para poder sacar info de ella en un futuro.

print(character)

if now.hour >= 10:
    # New Day, generate new tasks.
    character.past_tasks.append(character.tasks)
    character.tasks = tasks

print(character)

"""
Tabla 1 - Personajes
Info del personaje + tareas del día.

Tabla 2 - Tareas Pasadas
Tareas hechas vinculadas a un personaje, por si se necesitasen.

TODO: Hacer la API.
"""
