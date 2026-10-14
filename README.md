# TP1 - ABM de Usuarios + ABM de Libros (FastAPI)

API hecha con FastAPI y Pydantic. Los datos se guardan en memoria
(se reinician cada vez que se apaga el servidor).

## Requisitos

Python 3.13 (con versiones más nuevas algunas dependencias todavía
no tienen soporte).

## Instalación

Desde la carpeta del proyecto, crear el entorno virtual:


python -m venv .venv


Activarlo:


# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# macOS / Linux
source .venv/bin/activate


Instalar las dependencias:


pip install -r requirements.txt


## Levantar la aplicación


fastapi dev main.py


La API queda en `http://127.0.0.1:8000`.

## Probar los endpoints

Entrar a **`http://127.0.0.1:8000/docs`** (Swagger). Ahí aparecen todos
los endpoints agrupados en "Usuarios" y "Libros". Para probar uno:
hacer clic, apretar **Try it out**, completar los datos y **Execute**.

## Endpoints

### Usuarios (Parte 1)

| Método | Ruta | Descripción |

| GET  `/user` | Lista todos los usuarios |
| GET | `/user?is_active=true` | Lista solo los activos (`false` para inactivos) |
| POST | `/user` | Crea un usuario |
| PUT | `/user/{id}` | Modifica un usuario |
| DELETE | `/user/{id}` | Elimina un usuario |

### Libros (Parte 2)

Campos: `id`, `titulo`, `autor`, `anio`, `genero`.

| Método | Ruta | Descripción |

| GET | `/libro` | Lista todos los libros |
| GET | `/libro?genero=novela` | Filtra por género |
| GET | `/libro?autor=borges` | Filtra por autor (coincidencia parcial) |
| GET | `/libro/{id}` | Obtiene un libro por id |
| POST | `/libro` | Crea un libro |
| PUT | `/libro/{id}` | Modifica un libro |
| DELETE | `/libro/{id}` | Elimina un libro |

Si el id no existe, los endpoints devuelven error **404**.