from fastapi import APIRouter, Depends, Query
from typing import Annotated
from dependencies.auth import get_current_user
from routes.api.user.service import UserServiceDep
from routes.api.user.schemas import SetUserRoleSchema, GetUserSchema
from schemas.user import User

router = APIRouter(prefix="/user", tags=["user"])


@router.post("/set-role")
async def set_user_role(
    user_role: SetUserRoleSchema,
    service: UserServiceDep,
    current_user=Depends(get_current_user),
) -> dict[str, str]:
    return await service.set_user_role(user_role, current_user)


@router.post("/get-me")
async def get_me(
    service: UserServiceDep,
    current_user=Depends(get_current_user),
) -> User:
    return current_user


@router.get("/get_users")
async def get_users_by_ids(
    service: UserServiceDep,
    users_ids: Annotated[list[int], Query(description="List of user IDs")],
) -> list[GetUserSchema]:
    return await service.get_users_by_ids(users_ids)
