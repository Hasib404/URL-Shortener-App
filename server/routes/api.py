from fastapi import APIRouter
from endpoints import product

router = APIRouter()
router.include_router(product.router)