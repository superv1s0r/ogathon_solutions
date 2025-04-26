
from fastapi import FastAPI 
from src.api import endpoints
app = FastAPI(title="Hackathon Challenges", version="1.0")

# Include all subproblem endpoints
app.include_router(endpoints.router, prefix="", tags=["API"])


@app.get("/", tags=["Root"])
async def root():
    return {
        "message": "This is HackathonAPI, version 1.0.0, developed by superv1s0r, a.k.a Lex.",
        "version": "1.0.0",
        "status": "running",
        "docs": "/docs"
    }
