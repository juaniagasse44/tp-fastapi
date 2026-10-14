from pydantic import BaseModel
from typing import List


class Libro(BaseModel):
    id: int
    titulo: str
    autor: str
    anio: int
    genero: str


class GetLibrosResponse(BaseModel):
    libros: List[Libro]


class LibroResponse(BaseModel):
    message: str
    libro: Libro


class DeleteLibroResponse(BaseModel):
    message: str