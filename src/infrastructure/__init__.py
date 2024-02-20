"""src/infrastructure/__init__.py - Init"""
from beanie import Document
from pydantic import BaseModel


class BaseDocument(Document):
    """Base Document"""

    @classmethod
    def from_api_object(cls, api_obj: BaseModel, **kwargs):
        """From API Object"""
        return cls(**api_obj.model_dump(), **kwargs)
