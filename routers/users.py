from typing import Optional

from fastapi import APIRouter, HTTPException, status
from models.users import (
    User,
    GetUsersResponse,
    CreateUserResponse,
    DeleteUserResponse,
    UpdateUserResponse,
)

router = APIRouter()

usuarios: list[User] = [
    User(id=1, name="juan perez"),
    User(id=2, name="pepe sanchez"),
]


# Listar usuarios. Con ?is_active=true o ?is_active=false filtra por
# estado; sin el parametro devuelve todos.
@router.get("/user")
def get_users(is_active: Optional[bool] = None) -> GetUsersResponse:
    if is_active is None:
        resultado = usuarios
    else:
        resultado = [u for u in usuarios if u.is_active == is_active]
    return GetUsersResponse(users=resultado)


@router.delete("/user/{id}")
def delete_user(id: int) -> DeleteUserResponse:
    for user in usuarios:
        if user.id == id:
            usuarios.remove(user)
            return DeleteUserResponse(message="usuario borrado")

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Usuario no encontrado",
    )


@router.post("/user")
def create_user(user: User) -> CreateUserResponse:
    usuarios.append(user)
    return CreateUserResponse(message="usuario creado")


# Modificar un usuario existente: reemplaza sus datos por los enviados.
# El id de la URL manda, asi no se puede cambiar el id por error.
@router.put("/user/{id}")
def update_user(id: int, datos: User) -> UpdateUserResponse:
    for i, user in enumerate(usuarios):
        if user.id == id:
            actualizado = User(
                id=id, name=datos.name, is_active=datos.is_active
            )
            usuarios[i] = actualizado
            return UpdateUserResponse(
                message="usuario modificado", user=actualizado
            )

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Usuario no encontrado",
    )