import asyncio
from collections.abc import AsyncGenerator

from bond.utils.agenerators import join_generators
from bond.utils.response import to_streaming_response
from pydantic import BaseModel


class ProcessInput(BaseModel):
    bin: str
    args: list[str] = []

class ProcessStdout(BaseModel):
    text: str

class ProcessStderr(BaseModel):
    text: str

class ProcessExit(BaseModel):
    code: int


async def read_stream(stream, stream_type):
    """Reads from a stream (stdout or stderr) and yields messages."""

    while not stream.at_eof():
        # Read all available output
        chunk = await stream.read(2056)  # Read up to 1024 bytes at a time
        if chunk:
            yield stream_type(text=chunk.decode())


async def stream_process(input: ProcessInput) -> AsyncGenerator[BaseModel, None]:

    """Runs a process asynchronously and streams its output."""
    process = await asyncio.create_subprocess_exec(
        input.bin, *input.args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )

    async for el in join_generators(
        read_stream(process.stdout, ProcessStdout),
        read_stream(process.stderr, ProcessStderr),
    ):
        yield el

    await process.wait()  # Ensure process completes

    yield ProcessExit(code=process.returncode or 0)


async def process(input: ProcessInput):
    return to_streaming_response(stream_process, input)
