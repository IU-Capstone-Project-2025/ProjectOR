from dependencies.database import DBSessionDep
from fastapi import Depends
from typing import Annotated
from sqlalchemy import select, update
from models import User
from models.users import UserRole


class UserDataAccess:
    def __init__(self, db_session: DBSessionDep):
        self.db_session = db_session

    async def get_user_by_username(self, username: str) -> User | None:
        res = await self.db_session.execute(
            select(User).where(User.username == username)
        )
        return res.scalars().first()

    async def get_user_by_id(self, user_id: int) -> User | None:
        res = await self.db_session.execute(select(User).where(User.id == user_id))
        return res.scalars().first()

    async def set_user_role(self, username: str, role: UserRole) -> None:
        await self.db_session.execute(
            update(User).where(User.username == username).values(role=role)
        )


UserDataAccessDep = Annotated[UserDataAccess, Depends(UserDataAccess)]
