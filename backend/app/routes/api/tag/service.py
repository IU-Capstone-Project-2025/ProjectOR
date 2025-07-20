from routes.api.project.data_access import ProjectsDataAccessDep
from schemas.generic import GenericResponse
from services.ai_agent import AiAgentDep
from schemas.agent_response import GeneratedTagsResponse
from fastapi import HTTPException, Depends
from typing import Annotated
from routes.api.tag.data_access import TagDataAccessDep
from routes.api.tag.schemas import TagSchema
from schemas.user import UserInDB


class TagService:
    def __init__(
        self,
        ai_agent: AiAgentDep,
        data_access: ProjectsDataAccessDep,
        tag_data_access: TagDataAccessDep,
    ):
        self.data_access = data_access
        self.ai_agent = ai_agent
        self.tag_data_access = tag_data_access

    async def get_tags(self, project_id: int) -> GeneratedTagsResponse:
        project = await self.data_access.get_project_by_id(project_id)
        if project is None:
            raise HTTPException(status_code=404, detail="Project not found")
        result = await self.ai_agent.get_tags_by_description(project.brief_description)

        return result

    async def add_project_tags(
        self, project_id: int, tags: list[TagSchema], user: UserInDB
    ) -> list[TagSchema]:
        project = await self.data_access.get_project_by_id(project_id)
        if project is None:
            raise HTTPException(status_code=404, detail="Project not found")
        if user.id != project.ceo_id:
            raise HTTPException(
                status_code=403, detail="Only CEO cad add tags to the project"
            )

        return await self.tag_data_access.add_tags_to_project(project_id, tags)

    async def remove_project_tags(
        self, project_id: int, tags: list[TagSchema], user: UserInDB
    ) -> GenericResponse:
        project = await self.data_access.get_project_by_id(project_id)
        if project is None:
            raise HTTPException(status_code=404, detail="Project not found")
        if user.id != project.ceo_id:
            raise HTTPException(
                status_code=403, detail="Only CEO can remove tags from the project"
            )

        res = await self.tag_data_access.remove_tags_from_project(
            project_id, [tag.name for tag in tags]
        )

        return GenericResponse(
            success=res > 0,
            message=f"Removed {res} tags from the project"
            if res > 0
            else "No tags removed",
        )


TagServiceDep = Annotated[TagService, Depends(TagService)]
