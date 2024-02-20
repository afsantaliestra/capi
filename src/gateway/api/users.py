"""src/gateway/api/playground.py - Playground Routes"""
from fastapi import APIRouter, HTTPException, status

from src.infrastructure.user import User

router = APIRouter(prefix="/users", tags=["/Users"])


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
)
async def post_user(user: User):
    """
    Post User

    TODO: Genera un 500 al insertar un usuario que ya existe. Devolver un error mas específico.
    TODO: Acepta o no un _id. No debe dar la opción a que se le pueda enviar.
    """
    await user.insert()
    return user


@router.get(
    "/{_id}",
    status_code=status.HTTP_200_OK,
)
async def get_user_by_id(_id: str):
    """
    Get User by Id

    TODO: Genera un 500 al buscar una clave que no es un _id válido de mongo.
        - FIX: Devolver un error mas específico.
    TODO: Devuelve un 200 Ok con un null en el body cuando el _id es válido pero no lo encuentra.
        - FIX: Devolver un error más específico.
    """
    user = await User.get(_id)
    return user


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
)
async def get_all_users():
    """
    Get All Users
    """
    return await User.find_all().to_list()


@router.put(
    "/{_id}",
    status_code=status.HTTP_200_OK,
)
async def update_user_by_id(_id: str, new_username: str):
    """
    Update User by Id

    TODO: Genera un 500 al buscar una clave que no es un _id válido de mongo. Devolver un error mas específico.
    - Este lo genera el .get()
    TODO: Genera un 500 al buscar una clave _id válida pero no la encuentra. Devolver un error mas específico.
    - Este lo genera el user.username = new_username ya que user es None al no encontrarlo en el .get()

    Seguramente ambas deben ser la misma respuesta.
    """
    user = await User.get(_id)
    user.username = new_username
    await user.save()
    return user


@router.delete(
    "/{_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_user_by_id(_id: str):
    """
    Delete User by Id

    TODO: Genera un 500 al buscar una clave que no es un _id válido de mongo. Devolver un error mas específico.
    - Este lo genera el .get(...) -> Error 401, bad request.
    TODO: Genera un 500 al buscar una clave _id válida pero no la encuentra. Devolver un error mas específico.
    - Este lo genera el .delete() ya que el user es none tras el .get(...) -> Error 404, Not Found.

    Seguramente ambas deben ser la misma respuesta.
    """
    if not (user := await User.get(_id)):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"User with the _id {_id} not found."
        )
    await user.delete()

    return user
