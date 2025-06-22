from fastapi import FastAPI, Request
import httpx
from utils.resume_processor import SimpleFallback

app = FastAPI()

@app.post("/process")
async def process_resume(request: Request):
    msg = await request.json()
    resume_text = msg["context"].get("resume_text", "")
    
    # Extract skills using your fallback logic
    skills = SimpleFallback.extract_skills_simple(resume_text)

    # (Optional) Print to console for debugging
    print("✅ Extracted Skills from Resume:", skills)

    # Prepare message for Research Agent
    response_msg = {
        "sender": "resume_agent",
        "receiver": "research_agent",
        "task_id": msg.get("task_id", "default-task"),
        "context": {
            "skills": skills,
            "resume_text": resume_text
        },
        "data": {}
    }

    # Send the message via MCP router
    async with httpx.AsyncClient() as client:
        await client.post("http://localhost:8000/route", json=response_msg)

    return {"status": "Skills extracted and forwarded to research agent"}
