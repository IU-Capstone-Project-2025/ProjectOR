from sqlalchemy import (
    Column,
    Integer,
    Index,
    DateTime,
    func,
    Boolean,
    ForeignKey,
    Text,
    PrimaryKeyConstraint,
)
from dependencies.database import base


class Application(base):
    __tablename__ = "applications"

    project_id = Column(Integer, ForeignKey("projects.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, default=func.current_timestamp())
    is_approved = Column(Boolean, nullable=True)
    feedback = Column(Text, nullable=True)

    __table_args__ = (
        Index("ix_applications_project_user", "project_id", "user_id", unique=True),
        PrimaryKeyConstraint("project_id", "user_id"),
    )
