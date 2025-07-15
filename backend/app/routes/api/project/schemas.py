from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class NewProjectSchema(BaseModel):
    title: str
    description: Optional[str]
    is_public: Optional[bool]
    is_opensource: Optional[bool]
    is_dead: Optional[bool]


class ProjectSchema(NewProjectSchema):
    id: int
    created_at: datetime
    ceo_id: Optional[int]

    class Config:
        from_attributes = True


class MessageSchema(BaseModel):
    msg: str
    success: bool


class ApplicationSchema(BaseModel):
    project_id: int
    user_id: int
    is_approved: Optional[bool]
    created_at: datetime
    feedback: Optional[str]

    class Config:
        from_attributes = True


class ApproveApplicationSchema(BaseModel):
    is_approved: bool
    user_id: int
    feedback: Optional[str]


class ProjectMemberSchema(BaseModel):
    project_id: int
    user_id: int

    class Config:
        from_attributes = True
