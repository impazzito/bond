from itertools import chain

from bond.views.process import ProcessInput, stream_process
from pydantic import BaseModel


class PythonInput(BaseModel):
    text: str
    version: str = "3.13.2"
    dependencies: list[str] = []


async def stream_python(input: PythonInput):
    async for el in stream_process(ProcessInput(
        bin="uv",
        args=[
            "run",
            "--isolated",
            "--python",
            input.version,
            "--python-preference",
            "only-managed",
            *chain.from_iterable(("--with", d) for d in input.dependencies),
            "python",
            "-c",
            input.text,
        ],
    )):
        yield el
