import asyncio
from collections.abc import AsyncGenerator
from bond.utils.response import to_streaming_response
from pydantic import BaseModel
from fastapi.responses import StreamingResponse


class ChatInput(BaseModel):
    text: str


class ChatMessage(BaseModel):
    text: str


async def stream_chat_response(input: ChatInput) -> AsyncGenerator[ChatMessage, None]:
    for msg in [
        ChatMessage(text="Hello {}".format(input.text)),
        ChatMessage(text="Upper {}".format(input.text.upper())),
        ChatMessage(text="Length: {}".format(len(input.text))),
    ]:
        yield msg
        await asyncio.sleep(0.2)


async def chat(input: ChatInput) -> StreamingResponse:
    return to_streaming_response(stream_chat_response, input)
