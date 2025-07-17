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
        added_tags = []

        for tag_data in tags:
            query = (
                insert(Tag)
                .values(**tag_data.model_dump())
                .on_conflict_do_nothing(index_elements=["name"])
                .returning(Tag)
            )
            res = await self.db_session.execute(query)

            tag_obj = res.scalar_one_or_none()

            if tag_obj:
                stmt = (
                    insert(ProjectTag)
                    .values(project_id=project_id, tag_id=tag_obj.id)
                    .on_conflict_do_nothing(index_elements=["project_id", "tag_id"])
                )

                await self.db_session.execute(stmt)

                added_tags.append(TagSchema.model_validate(tag_obj))

        return added_tags


TagDataAccessDep = Annotated[TagDataAccess, Depends(TagDataAccess)]
