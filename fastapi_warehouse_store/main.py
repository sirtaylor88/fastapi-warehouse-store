"""Main app."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse, Response

from fastapi_warehouse_store.routers import product

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=[""],
)

app.include_router(product.router)


@app.get("/", include_in_schema=False)
def index() -> Response:
    """Redirect to swagger and hide the endpoint from swagger."""
    return RedirectResponse("/docs")
