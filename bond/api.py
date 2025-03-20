import asyncio
import json
from collections.abc import AsyncGenerator

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

app = FastAPI()

# Allow frontend running at http://localhost:8300 to access FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8300"],  # 👈 Set this to match your frontend URL
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
    allow_credentials=True,
)


class ChatInput(BaseModel):
    text: str


class Message(BaseModel):
    message: str
    timestamp: int


async def serialize_stream(iterable):
    async for item in iterable:
        yield json.dumps(
            item.dict()
        ) + "한ЖΩ∑"  # Send each JSON object as a newline-separated chunk
        await asyncio.sleep(0.2)


def to_streaming_response(func, *args, **kwargs):
    """
    Decorator to wrap an async generator function and return a StreamingResponse.
    """
    return StreamingResponse(
        serialize_stream(func(*args, **kwargs)), media_type="application/json"
    )


async def json_stream(text: str) -> AsyncGenerator[str, None]:
    for msg in [
        Message(message="Hello {}".format(text), timestamp=1),
        Message(message=text.upper(), timestamp=2),
        Message(message="Message length: {}".format(len(text)), timestamp=3),
        Message(message="Goodbye", timestamp=4),
    ]:
        yield msg


@app.post("/chat")
async def chat(input: ChatInput) -> StreamingResponse:
    return to_streaming_response(json_stream, **input.dict())
