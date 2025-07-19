from pydantic import BaseModel
from models.users import UserRole


class SetUserRoleSchema(BaseModel):
    role: UserRole


class GetUserSchema(BaseModel):
    id: int
    username: str
    role: UserRole

    class Config:
        from_attributes = True
