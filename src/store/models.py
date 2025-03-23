"""Store models."""

from redis_om import HashModel

from src.db import redis_conn


class ProductOrder(HashModel):
    """Product Order model."""

    product_id: str
    quantity: int

    class Meta:
        """Model Metadata."""

        database = redis_conn


class Order(HashModel):
    """Order model."""

    product_id: str
    price: float
    fee: float
    total: float
    quantity: int
    status: str

    class Meta:
        """Model Metadata."""

        database = redis_conn
