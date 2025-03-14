from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse

app = FastAPI(title="Bond API")

# HTML content with websocket client
html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Bond WebSocket Demo</title>
    </head>
    <body>
        <h1>Bond WebSocket Echo</h1>
        <div id="messages"></div>
        <script>
            var ws = new WebSocket(`ws://${window.location.host}/ws`);

            ws.onopen = function(event) {
                console.log("Connection opened");
                ws.send("Hello from client!");
            };

            ws.onmessage = function(event) {
                var messages = document.getElementById('messages');
                var message = document.createElement('div');
                message.innerHTML = `Received: ${event.data}`;
                messages.appendChild(message);
            };

            ws.onclose = function(event) {
                console.log("Connection closed");
            };
        </script>
    </body>
</html>
"""

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
