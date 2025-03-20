import asyncio
import json
from collections.abc import AsyncGenerator

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel


async def serialize_stream(iterable):
    async for item in iterable:
        yield json.dumps(
            item.dict()
        ) + "한ЖΩ∑"  # Send each JSON object as a newline-separated chunk


def to_streaming_response(func, *args, **kwargs):
    """
    Decorator to wrap an async generator function and return a StreamingResponse.
    """
    return StreamingResponse(
        serialize_stream(func(*args, **kwargs)), media_type="application/json"
    )
