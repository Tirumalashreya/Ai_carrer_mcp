from fastapi import FastAPI, Request
import httpx
from research_agent import run_research_agent

app = FastAPI()

@app.post("/process")
async def process_research(request: Request):
    msg = await request.json()
    skills = msg["context"].get("skills", [])
    query = " ".join(skills)

    print("[Research Agent] Received skills:", skills)

    # Run your research pipeline
    results = run_research_agent(query, skills)

    # Forward to career agent
    response_msg = {
        "sender": "research_agent",
        "receiver": "career_agent",
        "task_id": msg["task_id"],
        "context": msg["context"],
        "data": {
            "job_listings": results["matched_jobs"],
            "trending_skills": results["trending_skills"]
        }
    }

    async with httpx.AsyncClient() as client:
        await client.post("http://localhost:8000/route", json=response_msg)

    return {"status": "Research results sent to Career Agent"}
 