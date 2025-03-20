import asyncio
from collections.abc import AsyncGenerator

from bond.views import to_streaming_response
from pydantic import BaseModel


class ChatInput(BaseModel):
    text: str


class Message(BaseModel):
    text: str
    timestamp: int


async def json_stream(text: str) -> AsyncGenerator[str, None]:
    for msg in [
        Message(message="Hello {}".format(text), timestamp=1),
        Message(message=text.upper(), timestamp=2),
        Message(message="Message length: {}".format(len(text)), timestamp=3),
        Message(message="Goodbye", timestamp=4),
    ]:
        yield msg
        await asyncio.sleep(0.2)


async def chat(input: ChatInput):
    return to_streaming_response(json_stream, **input.dict())
