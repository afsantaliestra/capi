"""src/gateway/api/crud.py - CRUD Routes

TODO:
- [x] Move struct to another location. This file only generates. [improve]
- [x] Now only can have 1 field unique. Improve to a list of fields. [improve]
- [ ] Fiend by "pk" not works with the real "pk", just code. [fix]
"""

from typing import Any, List
from uuid import uuid4

from aiotinydb import AIOTinyDB
from fastapi import APIRouter
from pydantic import create_model
from tinydb import Query
from tinydb.database import Table

from src.utils.api_generic_struct import api_generic_struct

router = APIRouter()
tinydb: AIOTinyDB = AIOTinyDB("./local_dbs/tiny_db.json")


class GenericCRUD:
    struct: dict

    def __init__(self, struct: dict):
        self.struct = struct

    def create_post(self, category_data, category_router, category_model):
        """Create Post"""

        @category_router.post("/")
        async def generic_post(content: category_model) -> Any:
            """Generic Post"""
            new_data = {**content.model_dump(), category_data["pk"]: uuid4().hex}

            async with tinydb as database:
                table: Table = database.table(category_data["table_name"])
                fields = category_data["unique_fields"]

                # No other content with same unique_fields
                if fields:
                    q = Query()
                    query = None

                    for field in fields:
                        if query is None:
                            query = q[field] == new_data[field]
                        elif category_data.get("combo_key"):
                            query = query & (q[field] == new_data[field])
                        else:
                            query = query | (q[field] == new_data[field])

                    data = table.get(query)
                    if data:
                        return None  # TODO: Improve response to a 404.

                # Insert user
                table.insert(new_data)

            return new_data

    def create_get_all(self, category_data, category_router, category_response_model):
        """Create Get All"""

        @category_router.get("/")
        async def generic_get_all() -> Any:
            """Generic Get All"""
            async with tinydb as database:
                table: Table = database.table(category_data["table_name"])
                contents = table.all()

            return category_response_model(**{category_data["table_name"]: contents, "count": len(contents)})

    def create_get_by_pk(self, category_data, category_router, category_response_model):
        """Create Get All"""

        @category_router.get(
            f'/{{{category_data["pk"]}}}',
            response_model=category_response_model,
        )
        async def generic_get_by_pk(pk: str) -> Any:
            """Generic Get by Pk"""
            async with tinydb as database:
                table: Table = database.table(category_data["table_name"])
                data = table.get(Query()[category_data["pk"]] == pk)

            if not data:
                return None

            return category_response_model(**data)

    def generate(self):
        """Generate FastAPI Endpoints and Pydantic Models"""
        for _, category_data in self.struct.items():
            category_router = APIRouter(prefix=category_data["api"]["prefix"], tags=category_data["api"]["tags"])
            category_model = create_model(
                category_data["table_name"].capitalize(),
                **category_data["fields"],
            )
            category_response_model = create_model(
                f'{category_data["table_name"].capitalize()}Response',
                **{category_data["pk"]: (str, ...)},
                __base__=category_model,
            )
            category_response_model_list = create_model(
                f'{category_data["table_name"].capitalize()}Response',
                **{
                    "count": (int, ...),
                    category_data["table_name"]: (List[category_response_model], ...),
                },
            )

            if "post" in category_data["api"]["actions"]:
                self.create_post(category_data, category_router, category_model)

            if "get_all" in category_data["api"]["actions"]:
                self.create_get_all(category_data, category_router, category_response_model_list)

            if "get_all" in category_data["api"]["actions"]:
                self.create_get_by_pk(category_data, category_router, category_response_model)

            router.include_router(category_router)


GenericCRUD(api_generic_struct).generate()
