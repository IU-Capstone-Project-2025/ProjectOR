from fastapi import APIRouter
from routes.api.project.schemas import ProjectSchema
from routes.api.project.service import ProjectServiceDep

router = APIRouter(prefix="/projects", tags=["projects"])


@router.get("/")
async def get_projects(service: ProjectServiceDep) -> list[ProjectSchema]:
    return await service.get_projects()


@router.get("/{project_id}")
async def get_project_by_id(
    project_id: int, service: ProjectServiceDep
) -> ProjectSchema:
    return await service.get_project_by_id(project_id)


@router.post("/")
async def create_project(
    project_data: ProjectSchema, service: ProjectServiceDep
) -> ProjectSchema:
    return await service.create_project(project_data)
