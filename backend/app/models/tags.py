from sqlalchemy import (
    Column,
    Integer,
    String,
)
from dependencies.database import base


class Tag(base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
