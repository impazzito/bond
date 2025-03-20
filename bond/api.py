from bond.views.chat import chat
from bond.views.process import process
from bond.views.python import python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend running at http://localhost:8300 to access FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8300"],  # 👈 Set this to match your frontend URL
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
    allow_credentials=True,
)

app.post("/chat")(chat)
app.post("/process")(process)
app.post("/python")(python)
