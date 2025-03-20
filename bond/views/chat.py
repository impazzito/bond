import asyncio
from collections.abc import AsyncGenerator

from bond.utils.response import to_streaming_response
from pydantic import BaseModel


class ChatInput(BaseModel):
    text: str


class ChatMessage(BaseModel):
    text: str
    user: bool = False


async def stream_chat_response(input: ChatInput) -> AsyncGenerator[str, None]:
    for msg in [
        ChatMessage(text="Hello {}".format(input.text)),
        ChatMessage(text=input.text.upper()),
        ChatMessage(text="Message length: {}".format(len(input.text))),
        ChatMessage(text="Goodbye"),
    ]:
        yield msg
        await asyncio.sleep(0.2)


async def chat(input: ChatInput):
    return to_streaming_response(stream_chat_response, **input.dict())
