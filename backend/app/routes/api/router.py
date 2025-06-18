from fastapi import APIRouter
<<<<<<< HEAD
from routes.api.heath_check import router as health_check_router
from routes.api.project import router as project_router
=======
from .heath_check import router as health_check_router
>>>>>>> origin/main

router = APIRouter(tags=["API"], prefix="/api")

router.include_router(health_check_router)
<<<<<<< HEAD
router.include_router(project_router)
=======
>>>>>>> origin/main
