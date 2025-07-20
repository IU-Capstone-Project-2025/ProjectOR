from fastapi import APIRouter, Depends
from dependencies.auth import get_current_user
from routes.api.user.service import UserServiceDep
from routes.api.user.schemas import SetUserRoleSchema
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


@router.get("/get-by-id/{user_id}")
async def get_user_by_id(
    user_id: int,
    service: UserServiceDep,
    current_user=Depends(get_current_user),
) -> User:
    return await service.get_user_by_id(user_id, current_user)
