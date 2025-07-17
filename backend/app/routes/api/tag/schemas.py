from pydantic import BaseModel


class TagSchema(BaseModel):
    name: str
