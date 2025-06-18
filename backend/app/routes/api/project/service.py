from typing import Annotated
from fastapi import Depends
from fastapi.exceptions import HTTPException
from routes.api.project.data_access import ProjectsDataAccessDep

class ProjectService:
    def __init__(self, data_access: ProjectsDataAccessDep):
        self.data_access = data_access

    async def get_project_by_id(self, project_id: int):
        data = await self.data_access.get_project_by_id(project_id)
        if data is None:
            raise HTTPException(status_code=404, detail=f"Project with ID {project_id} not found.")
        return data

    async def get_projects(self):
        return await self.data_access.get_all_projects()

    async def create_project(self, project_data):
        return await self.data_access.create_project(project_data)


ProjectServiceDep = Annotated[ProjectService, Depends(ProjectService)]