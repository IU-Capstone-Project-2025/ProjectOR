from fastapi import APIRouter
from .heath_check import router as health_check_router

router = APIRouter(tags=["API"], prefix="/api")

router.include_router(health_check_router)
