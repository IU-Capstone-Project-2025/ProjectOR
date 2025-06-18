from fastapi import APIRouter
<<<<<<< HEAD
from routes.api.heath_check.service import HealthCheckServiceDep

router = APIRouter(tags=["Health"])


@router.get("/health-check", summary="Health Check")
async def health_check(service: HealthCheckServiceDep):
    return service.get_health_check()
=======

router = APIRouter(tags=["Health"])

@router.get("/health-check", summary="Health Check")
async def health_check():
    """
    Health check endpoint to verify the service is running.
    Returns a simple message indicating the service is healthy.
    """
    return {"status": "healthy"}
>>>>>>> origin/main
