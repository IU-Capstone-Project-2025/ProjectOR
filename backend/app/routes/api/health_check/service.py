from typing import Annotated
from fastapi import Depends


class HealthCheckService:
    def get_health_check(self) -> dict:
        return {"status": "ok"}


HealthCheckServiceDep = Annotated[HealthCheckService, Depends(HealthCheckService)]
