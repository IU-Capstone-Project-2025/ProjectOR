from sqlalchemy import Column, Integer, String, Date, func, Boolean, ForeignKey
from dependencies.database import base


class Project(base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, unique=True, nullable=False)
    description = Column(String)
    created_at = Column(Date, default=func.current_date())
    is_public = Column(Boolean, nullable=False)
    status = Column(String)
    ceo_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    is_opensource = Column(Boolean, nullable=False, default=True)
    is_dead = Column(Boolean, nullable=False, default=False)

    def __repr__(self):
        return f"<Project({', '.join(f'{k}={getattr(self, k)!r}' for k in self.__table__.columns.keys())})>"
