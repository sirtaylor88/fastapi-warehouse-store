"""Warehouse models."""

from pydantic import BaseModel


class ProductBase(BaseModel):
    """Base Product schema for validation."""

    name: str
    price: float
    quantity: int
