"""src/__main__.py - API Entrypoint"""  # pylint: disable=no-member
from src import app


def launch_with_uvicorn() -> None:
    """Uvicorn"""
    import uvicorn  # pylint: disable=import-outside-toplevel

    uvicorn.run(
        "src:app",
        host=app.container.config.app.host(),
        port=app.container.config.app.port(),
        reload=True,
    )


def main(launch: str) -> None:
    """Main"""
    if launch == "uvicorn":
        launch_with_uvicorn()


if __name__ == "__main__":
    main("uvicorn")
