from bond.views.chat import stream_chat, ChatInput
from bond.views.process import  stream_process, ProcessInput
from bond.views.python import  stream_python, PythonInput
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from bond.utils.response import to_streaming_response
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

@app.post('/chat')
def chat(input: ChatInput) -> StreamingResponse:
    return to_streaming_response(stream_chat, input)

@app.post('/process')
def process(input: ProcessInput) -> StreamingResponse:
    return to_streaming_response(stream_process, input)

@app.post('/python')
def python(input: PythonInput) -> StreamingResponse:
    return to_streaming_response(stream_python, input)
