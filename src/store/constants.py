"""Constants for `store` microservice."""

from enum import Enum


class OrderStatus(str, Enum):
    """Statuses of an order."""

    CANCELLED = "cancelled"
    PENDING = "pending"
    COMPLETED = "completed"
