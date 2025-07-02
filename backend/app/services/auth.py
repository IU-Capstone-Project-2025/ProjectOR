from fastapi import HTTPException, status, Depends
from typing import Annotated
from datetime import datetime, timedelta, timezone
from fastapi.security import OAuth2PasswordRequestForm
from jwt import encode, decode
from jwt.exceptions import InvalidTokenError
from passlib.context import CryptContext
from schemas.token import Token, TokenData
from models.users import User, UserRole
from data_access.auth import UserDataAccessDep
from schemas.user import UserRegister, UserInDB
from config import settings

SECRET_KEY = settings.JWT_SECRET_KEY
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7  # 7 days

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class AuthService:
    def __init__(self, user_data_access: UserDataAccessDep):
        self.user_data_access = user_data_access

    @staticmethod
    def _verify_password(plain: str, hashed: str) -> bool:
        return pwd_context.verify(plain, hashed)

    @staticmethod
    def _create_token(username: str) -> str:
        expire = datetime.now(timezone.utc) + timedelta(
            minutes=ACCESS_TOKEN_EXPIRE_MINUTES
        )
        payload = {"sub": username, "exp": expire}
        return encode(payload, SECRET_KEY, algorithm=ALGORITHM)

    @staticmethod
    def decode_token(token: str) -> TokenData:
        try:
            payload = decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            username = payload.get("sub")
            if username is None:
                raise ValueError("Missing username in token")
            return TokenData(username=username)
        except ValueError as e:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=str(e),
                headers={"WWW-Authenticate": "Bearer"},
            )
        except InvalidTokenError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid or expired token",
                headers={"WWW-Authenticate": "Bearer"},
            )

    async def login(self, form_data: OAuth2PasswordRequestForm) -> Token:
        user = await self.user_data_access.get_user_by_username(form_data.username)
        if not user or not self._verify_password(
            form_data.password, user.hashed_password
        ):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        access_token = self._create_token(user.username)
        return Token(access_token=access_token, token_type="bearer")

    async def register(self, user_data: UserRegister) -> Token:
        existing_user = await self.user_data_access.get_user_by_username(
            user_data.username
        )
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username already exists",
            )

        hashed_password = pwd_context.hash(user_data.password)
        user_in_db = UserInDB(
            username=user_data.username,
            hashed_password=hashed_password,
            role=UserRole.VIEWER,
        )
        await self.user_data_access.create_user(user_in_db)

        access_token = self._create_token(user_data.username)
        return Token(access_token=access_token, token_type="bearer")

    async def get_user_by_username(self, username: str) -> User:
        user = await self.user_data_access.get_user_by_username(username)
        if not user:
            raise HTTPException(status_code=401, detail="User not found")
        return user


AuthServiceDep = Annotated[AuthService, Depends(AuthService)]
