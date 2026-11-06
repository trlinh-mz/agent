from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def health():
    return {
        "status": "ok"
    }

@app.post("/chat")
def chat(request: dict):
    return {
        "message": "Hello from deployed agent",
        "received": request
    }
