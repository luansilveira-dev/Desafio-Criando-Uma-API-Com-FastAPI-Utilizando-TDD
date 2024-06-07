from fastapi import APIRouter

from store.controllers.product import router as products

api_router = APIRouter()

api_router.include_router(products, prefix="/products")
