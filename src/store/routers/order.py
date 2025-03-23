"""Order router."""

import requests
from fastapi import APIRouter, BackgroundTasks, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from redis_om.model import NotFoundError

from src.store.constants import OrderStatus
from src.store.models import Order
from src.store.schema import ProductOrderBase
from src.store.tasks import complete_order

router = APIRouter(prefix="/orders", tags=["store"])


@router.get("/")
def get_all_orders() -> JSONResponse:
    """Get all orders."""

    data = [Order.get(pk) for pk in Order.all_pks()]
    return JSONResponse(content=jsonable_encoder(data))


@router.post("/new")
def create_order(payload: ProductOrderBase, bacground_tasks: BackgroundTasks) -> Order:
    """Create an order."""
    response = requests.get(
        f"http://localhost:8000/products/{payload.product_id}",
        timeout=10,
    )
    product = response.json()
    fee = product["price"] * 0.2

    order = Order(
        product_id=payload.product_id,
        price=product["price"],
        fee=fee,
        total=product["price"] + fee,
        quantity=payload.quantity,
        status=OrderStatus.PENDING.value,
    )

    order.save()
    bacground_tasks.add_task(complete_order, order)

    return order


@router.get("/{pk}")
def get_order(pk: str) -> Order:
    """Get an order."""

    try:
        return Order.get(pk)
    except NotFoundError as err:
        raise HTTPException(
            detail=f"Order with ID {pk} not found.",
            status_code=status.HTTP_404_NOT_FOUND,
        ) from err
