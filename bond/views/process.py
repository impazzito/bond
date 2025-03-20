import asyncio
from collections.abc import AsyncGenerator
from enum import Enum

from bond.utils.agenerators import join_generators
from bond.utils.response import to_streaming_response
from pydantic import BaseModel


# Enum to distinguish stdout and stderr
class StreamType(str, Enum):
    STDOUT = "stdout"
    STDERR = "stderr"

# Input model for process execution
class ProcessInput(BaseModel):
    bin: str
    args: list[str] = []


# Message format
class ProcessMessage(BaseModel):
    text: str
    stream: StreamType

class ProcessExit(BaseModel):
    code: int

async def read_stream(stream, stream_type: StreamType):
    """Reads from a stream (stdout or stderr) and yields messages."""

    while not stream.at_eof():
        # Read all available output
        chunk = await stream.read(2056)  # Read up to 1024 bytes at a time
        if chunk:
            yield ProcessMessage(text=chunk.decode(), stream=stream_type)


async def stream_process(bin: str, args: list[str]) -> AsyncGenerator[str, None]:
    """Runs a process asynchronously and streams its output."""
    process = await asyncio.create_subprocess_exec(
        bin, *args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )

    async for el in join_generators(
        read_stream(process.stdout, StreamType.STDOUT),
        read_stream(process.stderr, StreamType.STDERR),
    ):
        yield el

    await process.wait()  # Ensure process completes

    yield ProcessExit(code=process.returncode)


async def process(input: ProcessInput):
    return to_streaming_response(stream_process, **input.dict())
