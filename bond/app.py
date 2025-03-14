from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

import os


app = FastAPI(title="Bond API")

# HTML content with websocket client
html = """
<!DOCTYPE html>
<html>
    <head><title>Bond WebSocket Demo</title></head>
    <script defer="defer" async="async" type="module" src="/static/index.js" crossorigin></script>
    <body id='body'></body>
</html>
"""

# Mount static files directory
@app.on_event("startup")
async def startup_event():
    # Check if static directory exists, create if it doesn't
    static_dir = os.path.join(os.path.dirname(__file__), "frontend", "static")
    if not os.path.exists(static_dir):
        os.makedirs(static_dir)

    # Mount the static directory
    app.mount("/static", StaticFiles(directory=static_dir), name="static")

@app.get("/")
async def get():
    """Serve HTML with WebSocket client."""
    return HTMLResponse(html)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """WebSocket endpoint that echoes messages back to the client."""
    await websocket.accept()

    # Send initial welcome message
    await websocket.send_text("Welcome to the Bond WebSocket server!")

    try:
        while True:
            # Receive and echo back any messages
            data = await websocket.receive_text()
            await websocket.send_text(f"Echo 1: {data}")
            await websocket.send_text(f"Echo 2: {data}")
    except Exception:
        pass

def create_app() -> FastAPI:
    """Create and configure a FastAPI application."""
    return app
