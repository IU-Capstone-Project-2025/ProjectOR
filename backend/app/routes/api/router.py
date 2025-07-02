from fastapi import APIRouter
from routes.api.health_check import router as health_check_router
from routes.api.project import router as project_router
from routes.api.auth import router as auth_router
from routes.api.user import router as user_router

router = APIRouter(tags=["API"], prefix="/api")

for r in [
    health_check_router,
    project_router,
    auth_router,
    user_router,
]:
    router.include_router(r)
