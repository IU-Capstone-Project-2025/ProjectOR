from fastapi import APIRouter
from routes.api.health_check.service import HealthCheckServiceDep

router = APIRouter(tags=["Health"])


@router.get("/health-check", summary="Health Check")
async def health_check(service: HealthCheckServiceDep):
    return service.get_health_check()