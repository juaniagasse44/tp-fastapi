from typing import Optional

from fastapi import APIRouter, HTTPException, status
from models.libros import (
    Libro,
    GetLibrosResponse,
    LibroResponse,
    DeleteLibroResponse,
)

router = APIRouter()

libros: list[Libro] = [
    Libro(
        id=1, titulo="Rayuela", autor="Julio Cortazar",
        anio=1963, genero="novela",
    ),
    Libro(
        id=2, titulo="Ficciones", autor="Jorge Luis Borges",
        anio=1944, genero="cuentos",
    ),
    Libro(
        id=3, titulo="El tunel", autor="Ernesto Sabato",
        anio=1948, genero="novela",
    ),
]


def no_encontrado() -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Libro no encontrado",
    )


# Listar libros. Filtros opcionales: ?genero=novela y/o ?autor=borges
# (el autor busca coincidencia parcial, sin importar mayusculas).
@router.get("/libro")
def get_libros(
    genero: Optional[str] = None, autor: Optional[str] = None
) -> GetLibrosResponse:
    resultado = libros
    if genero is not None:
        resultado = [
            lb for lb in resultado if lb.genero.lower() == genero.lower()
        ]
    if autor is not None:
        resultado = [
            lb for lb in resultado if autor.lower() in lb.autor.lower()
        ]
    return GetLibrosResponse(libros=resultado)


@router.get("/libro/{id}")
def get_libro(id: int) -> Libro:
    for libro in libros:
        if libro.id == id:
            return libro
    raise no_encontrado()


@router.post("/libro", status_code=status.HTTP_201_CREATED)
def create_libro(libro: Libro) -> LibroResponse:
    for existente in libros:
        if existente.id == libro.id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Ya existe un libro con ese id",
            )
    libros.append(libro)
    return LibroResponse(message="libro creado", libro=libro)


@router.put("/libro/{id}")
def update_libro(id: int, datos: Libro) -> LibroResponse:
    for i, libro in enumerate(libros):
        if libro.id == id:
            actualizado = datos.model_copy(update={"id": id})
            libros[i] = actualizado
            return LibroResponse(
                message="libro modificado", libro=actualizado
            )
    raise no_encontrado()


@router.delete("/libro/{id}")
def delete_libro(id: int) -> DeleteLibroResponse:
    for libro in libros:
        if libro.id == id:
            libros.remove(libro)
            return DeleteLibroResponse(message="libro borrado")
    raise no_encontrado()