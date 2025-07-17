from dependencies.database import DBSessionDep
from routes.api.tag.schemas import TagSchema
from models import Tag, ProjectTag
from sqlalchemy import select
from sqlalchemy.dialects.postgresql import insert
from typing import Annotated
from fastapi import Depends


class TagDataAccess:
    def __init__(self, db_session: DBSessionDep):
        self.db_session = db_session

    async def add_tags_to_project(
        self, project_id: int, tags: list[TagSchema]
    ) -> list[TagSchema]:
        added_tags = []

        for tag_data in tags:
            query = insert(Tag).values(**tag_data.model_dump())
            await self.db_session.execute(
                query.on_conflict_do_nothing(index_elements=["name"])
            )
            await self.db_session.flush()

            tag_query = select(Tag).where(Tag.name == tag_data.name)
            res = await self.db_session.execute(tag_query)
            tag_obj = res.scalar_one()

            stmt = insert(ProjectTag).values(project_id=project_id, tag_id=tag_obj.id)
            await self.db_session.execute(
                stmt.on_conflict_do_nothing(index_elements=["project_id", "tag_id"])
            )

            added_tags.append(TagSchema.model_validate(tag_obj.__dict__))

        return added_tags

    async def get_project_tags(self, project_id: int) -> list[TagSchema] | None:
        query = (
            select(Tag)
            .join(ProjectTag, ProjectTag.tag_id == Tag.id)
            .where(ProjectTag.project_id == project_id)
        )

        res = await self.db_session.execute(query)

        tags = res.scalars().all()

        return [TagSchema.model_validate(tag.__dict__) for tag in tags]


TagDataAccessDep = Annotated[TagDataAccess, Depends(TagDataAccess)]
