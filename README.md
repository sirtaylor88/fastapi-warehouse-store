# FastAPI Warehouse store app

Warehouse app using microservices, Redis and ReactJS

## Install FastAPI

Install poetry to manage dependencies

```bash
pip install poetry
```

Init `pyproject.toml` using `poetry`

```bash
poetry init
```

Install `FastAPI` framework and `uvicorn`

```bash
poetry add fastapi "uvicorn[standard]"
```

## Run server

```bash
uvicorn fastapi_warehouse_store.main:app --reload
```
