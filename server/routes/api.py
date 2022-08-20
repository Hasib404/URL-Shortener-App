from fastapi import APIRouter
from endpoints import shortener

router = APIRouter()
router.include_router(shortener.router)
