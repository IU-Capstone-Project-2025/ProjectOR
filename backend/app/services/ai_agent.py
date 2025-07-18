from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider
from schemas.agent_response import GeneratedTagsResponse
from config import settings
from fastapi import Depends
from typing import Annotated


class AiAgent:
    def __init__(self):
        self.model = OpenAIModel(
            "gpt-4o-mini",
            provider=OpenAIProvider(
                base_url="https://api.chatanywhere.tech/v1",
                api_key=settings.OPENAI_API_KEY,
            ),
        )

    async def get_tags_by_description(
        self, project_description: str
    ) -> GeneratedTagsResponse:
        tag_generator_agent = Agent(
            self.model,
            output_type=GeneratedTagsResponse,
            system_prompt=f"You need to come up with a name for a tag based on the project description. You should provide 15 options. Write tags in English only",
        )

        result = await tag_generator_agent.run(user_prompt=project_description)

        return result.output


AiAgentDep = Annotated[AiAgent, Depends(AiAgent)]
