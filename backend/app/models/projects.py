from sqlalchemy import Column, Integer, String, Date, func, Boolean
from dependencies.database import base



class Project(base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, nullable=False)
    description = Column(String)
    created_at = Column(Date, default=func.current_date())
    is_public = Column(Boolean, nullable=False)
    status = Column(String)
