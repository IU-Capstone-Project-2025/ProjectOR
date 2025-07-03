from pydantic import BaseModel
from models.users import UserRole


class SetUserRoleSchema(BaseModel):
    role: UserRole
