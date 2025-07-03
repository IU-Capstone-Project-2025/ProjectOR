from fastapi import APIRouter, Depends
from dependencies.auth import get_current_user
from routes.api.user.service import UserServiceDep
from routes.api.user.schemas import SetUserRoleSchema


router = APIRouter(prefix="/user", tags=["user"])


@router.post("/set-role")
async def set_user_role(
    user_role: SetUserRoleSchema,
    service: UserServiceDep,
    current_user=Depends(get_current_user),
):
    await service.set_user_role(user_role, current_user)
