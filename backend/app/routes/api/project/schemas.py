from pydantic import BaseModel
from typing import Optional


class NewProjectSchema(BaseModel):
    title: str
    description: Optional[str]
    is_public: bool


class ProjectSchema(NewProjectSchema):
    id: int

    class Config:
        from_attributes = True
