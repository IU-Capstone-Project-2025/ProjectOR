from typing import Annotated
from fastapi import Depends
from fastapi.exceptions import HTTPException
from routes.api.project.data_access import ProjectsDataAccessDep
from routes.api.project.schemas import ProjectSchema, NewProjectSchema


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

    async def create_project(self, project_data: NewProjectSchema) -> ProjectSchema:
        project = await self.data_access.get_project_by_title(project_data.title)
        if project:
            raise HTTPException(
                status_code=400,
                detail=f"Project with title '{project_data.title}' already exists.",
            )
        return await self.data_access.create_project(project_data)


ProjectServiceDep = Annotated[ProjectService, Depends(ProjectService)]
