"""Product router."""

from fastapi import APIRouter, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from redis_om.model import NotFoundError

from src.warehouse.models import Product
from src.warehouse.schema import ProductBase

router = APIRouter(prefix="/products", tags=["warehouse"])


@router.get("/")
def get_all_products() -> JSONResponse:
    """Get all products."""

    data = [Product.get(pk) for pk in Product.all_pks()]
    return JSONResponse(content=jsonable_encoder(data))


@router.post("/new")
def create_product(payload: ProductBase) -> Product:
    """Create a product."""
    product = Product(**payload.model_dump())
    return product.save()


@router.get("/{pk}")
def get_product(pk: str) -> Product:
    """Get a product."""

    try:
        return Product.get(pk)
    except NotFoundError as err:
        raise HTTPException(
            detail=f"Product with ID {pk} not found.",
            status_code=status.HTTP_404_NOT_FOUND,
        ) from err


@router.delete("/{pk}/delete")
def delete_product(pk: str) -> str:
    """Delete a product."""
    result = Product.delete(pk)
    if result:
        return "OK"

    raise HTTPException(
        detail=f"Product with ID {pk} not found.",
        status_code=status.HTTP_404_NOT_FOUND,
    )
