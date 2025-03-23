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

### Warehouse microservice

```bash
uvicorn src.warehouse.main:app --reload
uvicorn src.store.main:app --reload --port 8001
```
