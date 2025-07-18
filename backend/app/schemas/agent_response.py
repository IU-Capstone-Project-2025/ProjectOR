from pydantic import BaseModel


class GeneratedTagsResponse(BaseModel):
    tags: list[str]
