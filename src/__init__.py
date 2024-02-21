"""src/__init__.py - API Configuration"""
from typing import Sequence

import toml
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.params import Depends

from src.conteiners import ApplicationContainer
from src.gateway.api import api_router, connectivity
from src.gateway.examples import api_endpoints
from src.gateway.middlewares import LoggingMiddleware, RequestIdMiddleware
from src.utils.lifespan import lifespan
from src.utils.logging import configure_logging


class API(FastAPI):
    """API"""

    container: ApplicationContainer

    def __init__(
        self,
        *,
        title: str | None = None,
        pyproject_path: str | None = None,
        dependencies: Sequence[Depends] | None = None,
    ) -> None:
        self.container = ApplicationContainer()

        if self.container.config.app.logging_level() in ["DEBUG", "INFO"]:
            configure_logging(level=self.container.config.app.logging_level(), service=title)

        _pyproject = toml.load(pyproject_path or "pyproject.toml")

        super().__init__(
            title=title or self.__doc__,  # type: ignore
            description=_pyproject["tool"]["poetry"]["description"],
            version=_pyproject["tool"]["poetry"]["version"],
            dependencies=dependencies,
            lifespan=lifespan,
            root_path=f"{self.container.config.app.server()}/" if self.container.config.app.server() else "",
        )

        self.include_router(connectivity.router)
        self.include_router(api_endpoints.router)


app = API(title="FastAPI - CAPI")

# app.include_router(api_router, prefix="/api")

app.add_middleware(LoggingMiddleware)
app.add_middleware(RequestIdMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
