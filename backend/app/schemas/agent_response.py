from pydantic import BaseModel


class AgentResponseSchema(BaseModel):
    tags: list[str]
