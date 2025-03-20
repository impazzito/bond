from itertools import chain

from bond.utils.response import to_streaming_response
from bond.views.process import ProcessInput, stream_process
from pydantic import BaseModel


class PythonInput(BaseModel):
    text: str
    version: str = "3.13.2"
    dependencies: list[str] = []


async def python(input: PythonInput):
    return to_streaming_response(
        stream_process,
        ProcessInput(
            bin="uv",
            args=(
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
            ),
        ),
    )
