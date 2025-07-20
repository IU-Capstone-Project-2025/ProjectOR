from typing import Optional

from pydantic import Field, BaseModel


class GenericResponse(BaseModel):
    success: bool = Field(default=True)
    message: Optional[str] = Field(default=None)
