from sqlalchemy import Column, Integer, String, DateTime, func, Boolean, ForeignKey
from dependencies.database import base


class Project(base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, unique=True, nullable=False)
    description = Column(String)
    created_at = Column(DateTime, default=func.current_timestamp())
    is_public = Column(Boolean, nullable=True, default=True)
    status = Column(String)
    ceo_id = Column(Integer, ForeignKey("users.id"), nullable=True, server_default="0")
    is_opensource = Column(Boolean, nullable=True, default=True, server_default="true")
    is_dead = Column(Boolean, nullable=True, default=False, server_default="false")

    def __repr__(self):
        return f"<Project({', '.join(f'{k}={getattr(self, k)!r}' for k in self.__table__.columns.keys())})>"
