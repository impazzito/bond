import json

from fastapi.responses import StreamingResponse
from collections.abc import AsyncGenerator


async def serialize_stream(iterable) -> AsyncGenerator[str, None]:
    async for item in iterable:
        yield json.dumps(
            dict(item.dict(), type=item.__class__.__name__)
        ) + "한ЖΩ∑"  # Send each JSON object as a newline-separated chunk


def to_streaming_response(func, *args, **kwargs) -> StreamingResponse:
    """
    Decorator to wrap an async generator function and return a StreamingResponse.
    """
    return StreamingResponse(
        serialize_stream(func(*args, **kwargs)), media_type="application/json"
    )
