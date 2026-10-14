from fastapi import FastAPI

from routers import users, libros

app = FastAPI(title="TP1 - ABM de Usuarios y Libros")

app.include_router(users.router, tags=["Usuarios"])
app.include_router(libros.router, tags=["Libros"])