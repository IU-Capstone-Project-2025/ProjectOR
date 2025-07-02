from typing import Annotated
from fastapi import Depends, HTTPException

from models.users import UserRole
from routes.api.user.data_access import UserDataAccessDep, UserDataAccess
from routes.api.user.schemas import SetUserRoleSchema
from schemas.user import User


class UserService:
    def __init__(self, user_repository: UserDataAccessDep):
        self.user_repository: UserDataAccess = user_repository

    async def set_user_role(self, user_role: SetUserRoleSchema, current_user: User):
        user = await self.user_repository.get_user_by_username(current_user.username)
        if user is None:
            raise HTTPException(
                status_code=404,
                detail=f"User '{current_user.username}' not found.",
            )
        if user.role == user_role.role:
            raise HTTPException(
                status_code=400,
                detail="You cannot set the same role as your own.",
            )
        if user_role.role not in UserRole.__members__:
            raise HTTPException(
                status_code=400,
                detail=f"Role '{user_role.role}' is not a valid user role.",
            )
        await self.user_repository.set_user_role(user.username, user_role.role)


UserServiceDep = Annotated[UserService, Depends(UserService)]
