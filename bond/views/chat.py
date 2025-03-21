import asyncio
from collections.abc import AsyncGenerator
from bond.utils.response import to_streaming_response
from pydantic import BaseModel
from fastapi.responses import StreamingResponse
from bond.views.python import PythonInput
from pydantic_ai import Agent, RunContext
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider

from pydantic_ai import Agent, RunContext
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from pydantic import BaseModel

import time, asyncio
import time

class ChatInput(BaseModel):
    text: str

class ChatResponse(BaseModel):
    text: str


agent = Agent(
    OpenAIModel(
        model_name='llama3.1',
        provider=OpenAIProvider(base_url='http://host.docker.internal:11434/v1')
    ),
)


async def stream_chat(input: ChatInput) -> AsyncGenerator[ChatResponse, None]:
    async with agent.run_stream(input.text) as result:
        async for message in result.stream_text(delta=True):
            yield ChatResponse(text=message)