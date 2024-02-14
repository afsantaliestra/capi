"""src/__main__.py - API Entrypoint"""


def launch_with_uvicorn() -> None:
    """Uvicorn"""
    import uvicorn  # pylint: disable=import-outside-toplevel

    uvicorn.run(
        "src:app",
        host="0.0.0.0",
        port=8080,
        reload=True,
    )


def main(launch: str) -> None:
    """Main"""
    if launch == "uvicorn":
        launch_with_uvicorn()


if __name__ == "__main__":
    main("uvicorn")
