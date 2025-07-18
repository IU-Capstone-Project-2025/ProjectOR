from fastapi import APIRouter
from routes.api.tag.service import TagServiceDep
from schemas.agent_response import GeneratedTagsResponse
from dependencies.auth import AuthUserDep
from routes.api.tag.schemas import TagSchema

router = APIRouter(prefix="/tags", tags=["tags"])


@router.get("/generate/{project_id}")
async def get_tags_by_description(
    project_id: int, service: TagServiceDep
) -> GeneratedTagsResponse:
    return await service.get_tags(project_id)


@router.post("/add/{project_id}")
async def add_project_tags(
    project_id: int, service: TagServiceDep, user: AuthUserDep, tags: list[TagSchema]
) -> list[TagSchema]:
    return await service.add_project_tags(project_id, tags, user)
