from models.users import UserRole
from pydantic import BaseModel


class User(BaseModel):
    username: str
    role: UserRole


class UserRegister(BaseModel):
    username: str
    password: str


class UserInDB(User):
    hashed_password: str

    class Config:
        from_attributes = True
