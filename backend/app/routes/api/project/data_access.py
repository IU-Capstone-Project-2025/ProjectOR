from typing import Annotated
from pydantic_core._pydantic_core import ValidationError
from dependencies.database import DBSessionDep
from models import Project, Application, ProjectMember
from sqlalchemy import select, update, delete

from routes.api.project.exceptions import ApplicationNotFoundError
from routes.api.project.schemas import (
    ProjectSchema,
    ApplicationSchema,
    NewProjectSchema,
    ApproveApplicationSchema,
    ProjectMemberSchema,
)
from fastapi import Depends


class ProjectsDataAccess:
    def __init__(self, db_session: DBSessionDep):
        self.db_session = db_session

    async def get_project_by_id(
        self, project_id: int, ceo_id: int = None
    ) -> ProjectSchema | None:
        query = select(Project).where(Project.id == project_id)
        if ceo_id is not None:
            query = query.where(Project.ceo_id == ceo_id)
        res = await self.db_session.execute(query)
        project = res.scalars().first()
        try:
            return ProjectSchema.model_validate(project)
        except ValidationError as e:
            return None

    async def get_project_by_title(self, title: str) -> ProjectSchema | None:
        res = await self.db_session.execute(
            select(Project).where(Project.title == title)
        )
        project = res.scalars().first()
        try:
            return ProjectSchema.model_validate(project)
        except ValidationError as e:
            return None

    async def get_all_projects(self) -> list[ProjectSchema]:
        res = await self.db_session.execute(select(Project))
        projects = res.scalars().all()
        return [ProjectSchema.model_validate(project) for project in projects]

    async def create_project(
        self,
        project_data: NewProjectSchema,
        ceo_id: int,
    ) -> ProjectSchema:
        project = Project(**project_data.model_dump())
        project.ceo_id = ceo_id
        self.db_session.add(project)
        await self.db_session.flush()
        return ProjectSchema.model_validate(project)

    async def get_project_applications(
        self,
        project_id: int,
        only_new: bool = False,
    ) -> list[ApplicationSchema]:
        query = select(Application).where(Application.project_id == project_id)
        if only_new:
            query = query.where(Application.is_approved.is_(None))
        res = await self.db_session.execute(query)
        applications = res.scalars().all()
        return [ApplicationSchema.model_validate(app) for app in applications]

    async def get_application_by_user_and_project_id(
        self, project_id: int, user_id: int
    ) -> ApplicationSchema | None:
        query = select(Application).where(
            Application.project_id == project_id, Application.user_id == user_id
        )
        res = await self.db_session.execute(query)
        application = res.scalars().first()
        if application:
            return ApplicationSchema.model_validate(application)
        return None

    async def apply_to_project(
        self,
        project_id: int,
        user_id: int,
    ) -> ApplicationSchema:
        application = Application(project_id=project_id, user_id=user_id)
        self.db_session.add(application)
        await self.db_session.flush()
        return ApplicationSchema.model_validate(application)

    async def approve_application(
        self, project_id: int, approve_schema: ApproveApplicationSchema
    ):
        query = (
            update(Application)
            .where(
                Application.project_id == project_id,
                Application.user_id == approve_schema.user_id,
            )
            .values(
                is_approved=approve_schema.is_approved, feedback=approve_schema.feedback
            )
            .returning(Application)
        )
        res = await self.db_session.execute(query)
        application = res.scalars().first()
        if not application:
            raise ApplicationNotFoundError(
                f"Application for user {approve_schema.user_id} not found in project {project_id}."
            )
        return ApplicationSchema.model_validate(application)

    async def add_user_to_project(
        self,
        project_id: int,
        user_id: int,
    ) -> ProjectMemberSchema:
        project_member = ProjectMember(project_id=project_id, user_id=user_id)
        self.db_session.add(project_member)
        await self.db_session.flush()
        return ProjectMemberSchema.model_validate(project_member)

    async def delete_project(self, project_id: int) -> bool:
        query = delete(Project).where(Project.id == project_id)
        res = await self.db_session.execute(query)
        return res.rowcount > 0

    async def get_user_applications(self, user_id: int) -> list[ApplicationSchema]:
        query = select(Application).where(Application.user_id == user_id)
        res = await self.db_session.execute(query)
        applications = res.scalars().all()
        return [
            ApplicationSchema.model_validate(application)
            for application in applications
        ]

    async def delete_application(self, project_id: int, user_id: int) -> bool:
        query = delete(Application).where(
            Application.user_id == user_id, Application.project_id == project_id
        )
        res = await self.db_session.execute(query)
        return res.rowcount > 0


ProjectsDataAccessDep = Annotated[ProjectsDataAccess, Depends(ProjectsDataAccess)]
