from fastapi import APIRouter

from dependencies.auth import AuthUserDep
from routes.api.project.schemas import (
    ProjectSchema,
    NewProjectSchema,
    ApplicationSchema,
    ApproveApplicationSchema,
    ProjectMemberSchema,
    ActionResponse,
)
from routes.api.project.service import ProjectServiceDep

router = APIRouter(prefix="/projects", tags=["projects"])


@router.get("/")
async def get_projects(
    service: ProjectServiceDep,
    user: AuthUserDep,
) -> list[ProjectSchema]:
    return await service.get_projects()


@router.post("/")
async def create_project(
    project_data: NewProjectSchema,
    service: ProjectServiceDep,
    user: AuthUserDep,
) -> ProjectSchema:
    return await service.create_project(project_data, user)


@router.get("/all-applications")
async def get_user_applications(
    user: AuthUserDep, service: ProjectServiceDep
) -> list[ApplicationSchema]:
    return await service.get_user_applications(user)


@router.get("/{project_id}")
async def get_project_by_id(
    project_id: int,
    service: ProjectServiceDep,
) -> ProjectSchema:
    return await service.get_project_by_id(project_id)


@router.post("/{project_id}/apply")
async def apply_to_project(
    project_id: int,
    service: ProjectServiceDep,
    user: AuthUserDep,
) -> ApplicationSchema:
    return await service.apply_to_project(project_id, user.id)


@router.get("/{project_id}/applications")
async def get_project_applications(
    project_id: int,
    service: ProjectServiceDep,
    user: AuthUserDep,
) -> list[ApplicationSchema]:
    return await service.get_project_applications(project_id, user.id)


@router.get("/{project_id}/new-applications")
async def get_project_new_applications(
    project_id: int,
    service: ProjectServiceDep,
    user: AuthUserDep,
) -> list[ApplicationSchema]:
    return await service.get_project_applications(project_id, user.id, True)


@router.patch("/{project_id}/applications/approve")
async def approve_application(
    project_id: int,
    approve_schema: ApproveApplicationSchema,
    service: ProjectServiceDep,
    user: AuthUserDep,
) -> ProjectMemberSchema:
    return await service.approve_application(project_id, user, approve_schema)


@router.delete("/{project_id}/applications/cancel")
async def delete_application(
    project_id: int, service: ProjectServiceDep, user: AuthUserDep
) -> ActionResponse:
    return await service.delete_application(project_id, user)


@router.delete("/{project_id}")
async def delete_project(
    project_id: int,
    service: ProjectServiceDep,
    user: AuthUserDep,
) -> ActionResponse:
    return await service.delete_project(project_id, user)
