from typing import Annotated
from fastapi import Depends, HTTPException

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
        await self.user_repository.set_user_role(user.username, user_role.role)
        return {
            "message": f"User '{user.username}' role set to {user_role.role.value}."
        }

    async def get_user_by_id(self, user_id: int, current_user: User) -> User:
        user = await self.user_repository.get_user_by_id(user_id)
        if user is None:
            raise HTTPException(
                status_code=404,
                detail=f"User with ID {user_id} not found.",
            )
        return user


UserServiceDep = Annotated[UserService, Depends(UserService)]
