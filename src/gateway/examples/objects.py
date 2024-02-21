"""src/gateway/examples/api_schemas.py - API Schemas"""
from typing import List
from uuid import UUID, uuid4

from pydantic import BaseModel, field_serializer
from typing_extensions import Annotated, Doc

CodeUUIDAnnotation = Annotated[UUID, Doc("")]
CodeStrAnnotation = Annotated[str, Doc("")]
SimpleVar1Annotation = Annotated[str, Doc("")]
SimpleVar2Annotation = Annotated[int, Doc("")]


# SCHEMAS
class PostExampleSchema(BaseModel):
    """Post Example Schema"""

    simple_var_1: SimpleVar1Annotation
    simple_var_2: SimpleVar2Annotation


class ExampleSchema(PostExampleSchema):
    """Example Schema"""

    code: CodeUUIDAnnotation


class ResponseExampleSchema(ExampleSchema):
    """Response Example Schema"""


class ResponseExamplesSchema(BaseModel):
    """Response Examples Schema"""

    count: Annotated[int, Doc("")]
    examples: Annotated[List[ResponseExampleSchema], Doc("")]


# DOMAINS
class ExampleDomain(BaseModel):
    """Example Domain"""

    code: CodeUUIDAnnotation
    simple_var_1: SimpleVar1Annotation
    simple_var_2: SimpleVar2Annotation

    @classmethod
    def from_api(cls, example: ExampleSchema | PostExampleSchema, code: str = None) -> "ExampleDomain":
        """<summary_placeholder>

        Args:
            example (_type_): <description_placeholder>

        Returns:
            ExampleDomain: <description_placeholder>
        """
        example_data = example.model_dump()
        if not code:
            example_data["code"] = uuid4()

        return cls(**example_data)

    @field_serializer("code")
    def serialize_code(self, code: CodeUUIDAnnotation, _info) -> CodeStrAnnotation:
        """Serialize Code

        Args:
            code (CodeUUIDAnnotation): <description_placeholder>
            _info (_type_): <description_placeholder>

        Returns:
            CodeStrAnnotation: <description_placeholder>
        """
        return code.hex


# MODELS FOR DB
class ExampleModel(BaseModel):
    """Example Model"""

    code: CodeStrAnnotation
    simple_var_1: SimpleVar1Annotation
    simple_var_2: SimpleVar2Annotation

    @classmethod
    def from_domain(cls, example: ExampleDomain) -> "ExampleModel":
        """<summary_placeholder>

        Args:
            example (ExampleDomain): <description_placeholder>

        Returns:
            ExampleModel: <description_placeholder>
        """
        return cls(**example.model_dump())

    def save(self) -> None:
        """Save"""
