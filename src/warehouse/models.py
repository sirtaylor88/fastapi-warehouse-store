"""Warehouse models."""

from redis_om import HashModel

from src.db import redis_conn


class Product(HashModel):
    """Product model."""

    name: str
    price: float
    quantity: int

    class Meta:
        """Model Metadata."""

        database = redis_conn
