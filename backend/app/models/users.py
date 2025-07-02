from sqlalchemy import Column, String, Integer
from sqlalchemy.dialects.postgresql import ENUM as PgEnum
from dependencies.database import base
from enum import Enum


class UserRole(str, Enum):
    VIEWER = "VIEWER"
    FOUNDER = "FOUNDER"
    DEVELOPER = "DEVELOPER"
    INVESTOR = "INVESTOR"


class User(base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(
        PgEnum(UserRole, name="user_role_enum", create_type=True),
        nullable=False,
        default=UserRole.VIEWER,
    )
