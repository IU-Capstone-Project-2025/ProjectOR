from typing import Annotated
from fastapi import Depends
from fastapi.exceptions import HTTPException
from models.users import UserRole
from routes.api.project.data_access import ProjectsDataAccessDep
from routes.api.project.exceptions import ProjectNotFoundError
from routes.api.project.schemas import (
    ProjectSchema,
    NewProjectSchema,
    ApplicationSchema,
    ApproveApplicationSchema,
)
from schemas.user import UserInDB


class ProjectService:
    def __init__(self, data_access: ProjectsDataAccessDep):
        self.data_access = data_access

    async def get_project_by_id(self, project_id: int) -> ProjectSchema:
        data = await self.data_access.get_project_by_id(project_id)
        if data is None:
            raise HTTPException(
                status_code=404, detail=f"Project with ID {project_id} not found."
            )
        return data

    async def get_projects(self) -> list[ProjectSchema]:
        return await self.data_access.get_all_projects()

    async def create_project(
        self,
        project_data: NewProjectSchema,
        user: UserInDB,
    ) -> ProjectSchema:
        if user.role != UserRole.FOUNDER:
            raise HTTPException(
                status_code=403,
                detail="Only founders can create projects.",
            )
        project = await self.data_access.get_project_by_title(project_data.title)
        if project:
            raise HTTPException(
                status_code=400,
                detail=f"Project with title '{project_data.title}' already exists.",
            )
        return await self.data_access.create_project(project_data, user.id)

    async def get_project_applications(
        self,
        project_id: int,
        user_id: int = None,
        only_new: bool = False,
    ) -> list[ApplicationSchema]:
        project = await self.data_access.get_project_by_id(project_id, user_id)
        if project is None:
            raise HTTPException(
                status_code=404,
                detail=f"Project with ID {project_id} not found or you do not have access.",
            )
        return await self.data_access.get_project_applications(project_id, only_new)

    async def apply_to_project(
        self,
        project_id: int,
        user_id: int,
    ) -> ApplicationSchema:
        project = await self.data_access.get_project_by_id(project_id)
        if project is None:
            raise HTTPException(
                status_code=404,
                detail=f"Project with ID {project_id} not found or you do not have access.",
            )
        if project.ceo_id == user_id:
            raise HTTPException(
                status_code=403,
                detail="You cannot apply to your own project.",
            )
        application = await self.data_access.get_application_by_user_and_project_id(
            project_id, user_id
        )
        if application:
            raise HTTPException(
                status_code=400,
                detail=f"You have already applied to project {project_id}.",
            )
        return await self.data_access.apply_to_project(project_id, user_id)

    async def approve_application(
        self,
        project_id: int,
        user: UserInDB,
        approve_schema: ApproveApplicationSchema,
    ) -> ApplicationSchema:
        project = await self.data_access.get_project_by_id(project_id)
        if project is None:
            raise HTTPException(
                status_code=404,
                detail=f"Project with ID {project_id} not found.",
            )
        if project.ceo_id != user.id:
            raise HTTPException(
                status_code=403,
                detail="Only the project CEO can approve applications.",
            )
        application = await self.data_access.get_application_by_user_and_project_id(
            project_id,
            approve_schema.user_id,
        )
        if application is None:
            raise HTTPException(
                status_code=404,
                detail=f"Application not found in project {project_id}.",
            )

        if application.user_id == user.id:
            raise HTTPException(
                status_code=403,
                detail="You cannot approve your own application.",
            )
        try:
            await self.data_access.approve_application(
                project_id,
                approve_schema,
            )
        except ProjectNotFoundError:
            raise HTTPException(
                status_code=404,
                detail=f"Application for user {approve_schema.user_id} not found in project {project_id}.",
            )
        return await self.data_access.add_user_to_project(
            project_id,
            application.user_id,
        )


ProjectServiceDep = Annotated[ProjectService, Depends(ProjectService)]
