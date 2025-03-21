import asyncio
from collections.abc import AsyncGenerator
from bond.utils.response import to_streaming_response
from pydantic import BaseModel
from fastapi.responses import StreamingResponse


from agno.agent import Agent
from agno.models.ollama import Ollama
from agno.utils.pprint import pprint_run_response
import time

agent = Agent(
    model=Ollama(host = 'host.docker.internal'),
    description="You are an enthusiastic news reporter with a flair for storytelling!",
    markdown=True
)






class ChatInput(BaseModel):
    text: str


class ChatResponse(BaseModel):
    text: str


async def stream_chat_response(input: ChatInput) -> AsyncGenerator[ChatResponse, None]:
    async for c in await agent.arun(input.text, stream=True):
        yield ChatResponse(text=c.content)

async def chat(input: ChatInput) -> StreamingResponse:
    return to_streaming_response(stream_chat_response, input)
