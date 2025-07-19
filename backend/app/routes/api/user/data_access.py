from dependencies.database import DBSessionDep
from fastapi import Depends
from typing import Annotated
from sqlalchemy import select, update
from models import User
from models.users import UserRole
from routes.api.user.schemas import GetUserSchema


class UserDataAccess:
    def __init__(self, db_session: DBSessionDep):
        self.db_session = db_session

    async def get_user_by_username(self, username: str) -> User | None:
        res = await self.db_session.execute(
            select(User).where(User.username == username)
        )
        return res.scalars().first()

    async def set_user_role(self, username: str, role: UserRole) -> None:
        await self.db_session.execute(
            update(User).where(User.username == username).values(role=role)
        )

    async def get_users_by_ids(self, users_ids: list[int]) -> list[GetUserSchema]:
        res = await self.db_session.execute(select(User).where(User.id.in_(users_ids)))
        users = res.scalars().all()
        return [GetUserSchema.model_validate(user) for user in users]


UserDataAccessDep = Annotated[UserDataAccess, Depends(UserDataAccess)]
