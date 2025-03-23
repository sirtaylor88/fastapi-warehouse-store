"""Order schema."""

from pydantic import BaseModel


class ProductOrderBase(BaseModel):
    """Base Product Order schema for validation."""

    product_id: str
    quantity: int


class OrderBase(BaseModel):
    """Base Order schema for validation."""

    product_id: str
    price: float
    fee: float
    total: float
    quantity: int
    status: str
