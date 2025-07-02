from typing import Annotated
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from schemas.token import Token
from schemas.user import UserRegister
from services.auth import AuthServiceDep

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    auth_service: AuthServiceDep,
) -> Token:
    return await auth_service.login(form_data)


@router.post("/register")
async def register(
    user_data: UserRegister,
    auth_service: AuthServiceDep,
) -> Token:
    return await auth_service.register(user_data)
