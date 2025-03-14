from fastapi import FastAPI, WebSocket
import asyncio
import types_pb2  # Import generated Protobuf classes

app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    print("Client connected!")

    try:
        while True:
            # Receive binary data
            data = await websocket.receive_bytes()

            # Deserialize Protobuf request
            request = chat_pb2.ApiRequest.FromString(data)
            print(f"Received request: {request.text}")

            # Simulate multiple responses
            responses = [
                chat_pb2.ApiResponse(cell_id="cell1", stream_id="stream1", payload="Processing..."),
                chat_pb2.ApiResponse(cell_id="cell1", stream_id="stream1", payload="Analyzing input..."),
                chat_pb2.ApiResponse(cell_id="cell1", stream_id="stream1", payload="Response ready!"),
            ]

            for response in responses:
                # Serialize response to Protobuf binary
                await websocket.send_bytes(response.SerializeToString())
                await asyncio.sleep(1)

    except Exception as e:
        print(f"WebSocket error: {e}")
    finally:
        print("Client disconnected")