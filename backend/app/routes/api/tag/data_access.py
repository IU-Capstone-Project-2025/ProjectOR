from dependencies.database import DBSessionDep
from routes.api.tag.schemas import TagSchema
from models import Tag, ProjectTag
from sqlalchemy.dialects.postgresql import insert
from typing import Annotated
from fastapi import Depends


class TagDataAccess:
    def __init__(self, db_session: DBSessionDep):
        self.db_session = db_session

    async def add_tags_to_project(
        self, project_id: int, tags: list[TagSchema]
    ) -> list[TagSchema]:
        query = (
            insert(Tag)
            .values([tag.model_dump() for tag in tags])
            .on_conflict_do_nothing(index_elements=["name"])
            .returning(Tag)
        )
        res = await self.db_session.execute(query)

        tags = res.scalars().all()

        if tags:
            stmt = (
                insert(ProjectTag)
                .values([{"project_id": project_id, "tag_id": tag.id} for tag in tags])
                .on_conflict_do_nothing(index_elements=["project_id", "tag_id"])
            )

            await self.db_session.execute(stmt)

        return [TagSchema.model_validate(tag) for tag in tags]


TagDataAccessDep = Annotated[TagDataAccess, Depends(TagDataAccess)]
