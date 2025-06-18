from typing import Annotated
from pydantic_core._pydantic_core import ValidationError
from dependencies.database import DBSessionDep
from models.projects import Project
from sqlalchemy import select
from routes.api.project.schemas import ProjectSchema
from fastapi import Depends


class ProjectsDataClass:
    def __init__(self, db_session: DBSessionDep):
        self.db_session = db_session

    async def get_project_by_id(self, project_id: int) -> ProjectSchema | None:
        res = await self.db_session.execute(
            select(Project).where(Project.id == project_id)
        )
        project = res.scalars().first()
        try:
            return ProjectSchema.model_validate(project)
        except ValidationError as e:
            return None

    async def get_all_projects(self) -> list[ProjectSchema]:
        res = await self.db_session.execute(select(Project))
        projects = res.scalars().all()
        return [ProjectSchema.model_validate(project) for project in projects] if projects else []

    async def create_project(self, project_data: ProjectSchema) -> ProjectSchema:
        project = Project(**project_data.model_dump())
        self.db_session.add(project)
        await self.db_session.commit()
        return ProjectSchema.model_validate(project)


ProjectsDataAccessDep = Annotated[ProjectsDataClass, Depends(ProjectsDataClass)]
