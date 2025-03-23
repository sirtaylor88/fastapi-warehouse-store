"""Tasks for `store` app."""

import time
from src.store.models import Order
from src.store.constants import OrderStatus

__all__ = ["complete_order"]


def complete_order(order: Order) -> None:
    """Change order status to completed."""

    time.sleep(5)
    order.status = OrderStatus.COMPLETED.value
    order.save()
