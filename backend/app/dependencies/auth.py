from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated
from services.auth import AuthServiceDep
from schemas.user import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/token")


async def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    auth_service: AuthServiceDep,
) -> User:
    token_data = auth_service.decode_token(token)
    return await auth_service.get_user_by_username(token_data.username)


AuthUserDep = Annotated[User, Depends(get_current_user)]
