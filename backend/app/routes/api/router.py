from fastapi import APIRouter
from routes.api.health_check import router as health_check_router
from routes.api.project import router as project_router
from routes.api.auth import router as auth_router

router = APIRouter(tags=["API"], prefix="/api")

router.include_router(health_check_router)
router.include_router(project_router)
router.include_router(auth_router)
