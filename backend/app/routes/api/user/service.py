from typing import Annotated
from fastapi import Depends, HTTPException
from models.users import UserRole
from routes.api.user.data_access import UserDataAccessDep, UserDataAccess
from routes.api.user.schemas import SetUserRoleSchema, GetUserSchema
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

    async def get_users_by_ids(self, users_ids: list[int]) -> list[GetUserSchema]:
        users = await self.user_repository.get_users_by_ids(users_ids)
        if not users:
            raise HTTPException(
                status_code=404, detail="No users found with the provided IDs."
            )
        return users


UserServiceDep = Annotated[UserService, Depends(UserService)]
