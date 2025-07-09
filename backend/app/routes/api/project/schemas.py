from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class NewProjectSchema(BaseModel):
    title: str
    description: Optional[str]
    is_public: bool
    is_opensource: bool
    is_dead: bool


class ProjectSchema(NewProjectSchema):
    id: int
    created_at: datetime
    ceo_id: int

    class Config:
        from_attributes = True


class ApplicationSchema(BaseModel):
    project_id: int
    user_id: int
    is_approved: Optional[bool]
    created_at: datetime

    class Config:
        from_attributes = True


class ApproveApplicationSchema(BaseModel):
    is_approved: bool
    user_id: int


class ProjectMemberSchema(BaseModel):
    project_id: int
    user_id: int

    class Config:
        from_attributes = True
