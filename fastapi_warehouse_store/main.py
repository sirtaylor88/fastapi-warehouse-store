"""Main app."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from redis_om import get_redis_connection

from fastapi_warehouse_store.config import get_settings

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=[""],
)


settings = get_settings()

redis = get_redis_connection(
    host=settings.redis_endpoint,
    port=settings.redis_port,
    password=settings.redis_password,
    decode_responses=True,
)
