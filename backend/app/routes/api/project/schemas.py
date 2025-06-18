from pydantic import BaseModel
from typing import Optional


class ProjectSchema(BaseModel):
    title: str
    description: Optional[str]
    is_public: bool

    class Config:
        from_attributes = True
