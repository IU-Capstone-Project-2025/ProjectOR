from sqlalchemy import (
    Column,
    Integer,
    Index,
    DateTime,
    func,
    ForeignKey,
    PrimaryKeyConstraint,
)
from dependencies.database import base


class ProjectMember(base):
    __tablename__ = "project_members"

    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime, default=func.current_timestamp())

    __table_args__ = (
        PrimaryKeyConstraint("project_id", "user_id"),
        Index("ix_project_members_project_id_user_id", "project_id", "user_id"),
    )
