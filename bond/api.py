from fastapi import FastAPI, WebSocket
import asyncio

from fastapi.responses import StreamingResponse
import asyncio
import json

import types_pb2  # Import generated Protobuf classes

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend running at http://localhost:8300 to access FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8300"],  # 👈 Set this to match your frontend URL
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

async def json_stream():
    messages = [
        {"message": "Hello", "timestamp": 1},
        {"message": "This is a stream", "timestamp": 2},
        {"message": "Sending multiple JSON messages", "timestamp": 3},
        {"message": "Goodbye", "timestamp": 4}
    ]

    for msg in messages:
        yield json.dumps(msg) + "한ЖΩ∑"  # Send each JSON object as a newline-separated chunk
        await asyncio.sleep(1)

@app.get("/chat")
async def stream_json():
    return StreamingResponse(json_stream(), media_type="application/json")