"""Database models."""

from redis_om import HashModel, get_redis_connection

from fastapi_warehouse_store.config import settings

redis_conn = get_redis_connection(
    host=settings.redis_endpoint,
    port=settings.redis_port,
    password=settings.redis_password,
    decode_responses=True,
)


class Product(HashModel):
    """Product model."""

    name: str
    price: float
    quantity: int

    class Meta:
        """Model Metadata."""

        database = redis_conn
