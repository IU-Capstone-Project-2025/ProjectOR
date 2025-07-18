from sqlalchemy import (
    Column,
    Integer,
    Index,
    ForeignKey,
    PrimaryKeyConstraint,
)
from dependencies.database import base


class ProjectTag(base):
    __tablename__ = "project_tags"

    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)
    tag_id = Column(Integer, ForeignKey("tags.id"), nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint("project_id", "tag_id"),
        Index("ix_project_tags_project_id_tag_id", "project_id", "tag_id"),
    )
