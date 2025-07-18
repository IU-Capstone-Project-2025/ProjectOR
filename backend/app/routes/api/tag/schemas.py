from pydantic import BaseModel


class TagSchema(BaseModel):
    name: str

    class Config:
        from_attributes = True
