from sqlalchemy import Column, Integer, String, DateTime, func, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from dependencies.database import base


class Project(base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, unique=True, nullable=False)
    description = Column(String, nullable=True)
    brief_description = Column(String)
    created_at = Column(DateTime, default=func.current_timestamp())
    is_public = Column(Boolean, nullable=True, default=True)
    status = Column(String)
    ceo_id = Column(Integer, ForeignKey("users.id"), nullable=True, server_default="1")
    is_opensource = Column(Boolean, nullable=True, default=True, server_default="TRUE")
    is_dead = Column(Boolean, nullable=True, default=False, server_default="FALSE")
    tags = relationship(
        "Tag", secondary="project_tags", back_populates="projects", lazy="selectin"
    )

    def __repr__(self):
        return f"<Project({', '.join(f'{k}={getattr(self, k)!r}' for k in self.__table__.columns.keys())})>"
