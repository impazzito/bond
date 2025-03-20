import asyncio
from collections.abc import AsyncGenerator

from bond.utils.response import to_streaming_response
from pydantic import BaseModel


class ChatInput(BaseModel):
    text: str


class ChatMessage(BaseModel):
    text: str
    user: bool = False


async def json_stream(text: str) -> AsyncGenerator[str, None]:
    for msg in [
        ChatMessage(text="Hello {}".format(text)),
        ChatMessage(text=text.upper()),
        ChatMessage(text="Message length: {}".format(len(text))),
        ChatMessage(text="Goodbye"),
    ]:
        yield msg
        await asyncio.sleep(0.2)


async def chat(input: ChatInput):
    return to_streaming_response(json_stream, **input.dict())
