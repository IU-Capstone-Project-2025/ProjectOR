from typing import Annotated
from pydantic import ValidationError
from dependencies.database import DBSessionDep
from sqlalchemy import select, insert
from fastapi import Depends
from schemas.user import UserInDB
from models import User


class UserDataAccess:
    def __init__(self, db_session: DBSessionDep):
        self.db_session = db_session

    async def get_user_by_username(self, username: str) -> UserInDB | None:
        res = await self.db_session.execute(
            select(User).where(User.username == username)
        )
        user = res.scalars().first()
        try:
            return UserInDB.model_validate(user)
        except ValidationError as e:
            return None

    async def create_user(self, user: UserInDB):
        await self.db_session.execute(
            insert(User), user.model_dump(exclude_unset=True, by_alias=True)
        )
        await self.db_session.commit()


UserDataAccessDep = Annotated[UserDataAccess, Depends(UserDataAccess)]
