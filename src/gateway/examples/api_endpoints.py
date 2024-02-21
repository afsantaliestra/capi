"""src/gateway/examples/api_endpoints.py - API Endpoints"""
from typing import Any

from fastapi import APIRouter, status
from typing_extensions import Annotated, Doc

from src.gateway.examples.objects import (
    ExampleDomain,
    ExampleModel,
    PostExampleSchema,
    ResponseExampleSchema,
    ResponseExamplesSchema,
)

router = APIRouter(prefix="/examples", tags=["Examples"])


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=ResponseExamplesSchema,
)
async def get_examples() -> Any:
    """
    Get Examples

    Returns:
    ----
        ResponseExamplesSchema:
            status_code: 200
            <description_placeholder>
    """
    return {}


@router.get(
    "/{example_id}",
    status_code=status.HTTP_200_OK,
    response_model=ResponseExampleSchema,
    responses={
        status.HTTP_404_NOT_FOUND: {
            "model": {},  # TODO: Necesita un modelo si no lo encuentra.
        },
    },
)
async def get_example_by_id(
    example_id: Annotated[
        int,
        Doc(
            """
            <description>

            <example>
            """
        ),
    ]
):
    """
    Get Example Id
    """
    return example_id


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=ResponseExampleSchema,
    response_description="<response_description_placeholder>",
)
async def post_example(
    example: Annotated[
        PostExampleSchema,
        Doc(
            """
            <description>

            <example>
            """
        ),
    ],
) -> Any:
    """Post Example

    Args:
    ----
    <description_placeholder>

        example (Annotated[ PostExampleSchema, Doc):
            <description_placeholder>

    Returns:
    ----
    <description_placeholder>

        ResponseExampleSchema:
            status_code: 201
            <description_placeholder>
    """
    # Turn to in-app object
    example_domain = ExampleDomain.from_api(example)
    # Turn to db object
    example_model = ExampleModel.from_domain(example_domain)
    # Perform save.
    example_model.save()
    # Turn again to in-app object or just sync models if needed.
    return example_domain


@router.put("/{example_id}")
async def put_example(
    example_id: Annotated[
        int,
        Doc(
            """
            <description>

            <example>
            """
        ),
    ],
    example: Annotated[
        dict,
        Doc(
            """
            <description>

            <example>
            """
        ),
    ],
) -> Any:
    """<summary_placeholder>

    Args:
        example_id (int): <description_placeholder>
        example (dict): <description_placeholder>
    """
    return {"example_id": example_id, "example": example}


@router.delete("/{example_id}")
async def delete_example(
    example_id: Annotated[
        int,
        Doc(
            """
            <description>

            <example>
            """
        ),
    ],
) -> Any:
    """Delete Example"""
    return {"example_id": example_id}
