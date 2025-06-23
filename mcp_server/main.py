# mcp_servre/main.py{router in this only}
from fastapi import FastAPI, Request
import httpx

app = FastAPI()

AGENT_ROUTES = {
    "resume_agent": "http://localhost:8001/process",
    "research_agent": "http://localhost:8002/process",
    "career_agent": "http://localhost:8003/process",
}

@app.post("/route")
async def route_message(request: Request):
    msg = await request.json()
    receiver = msg.get("receiver")

    if receiver not in AGENT_ROUTES:
        return {"error": "Unknown agent"}

    async with httpx.AsyncClient() as client:
        await client.post(AGENT_ROUTES[receiver], json=msg)

    return {"status": f"Message routed to {receiver}"}
