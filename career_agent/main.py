from fastapi import FastAPI, Request
from agent.career_agent import handle_career_agent

app = FastAPI()

@app.post("/process")
async def process_career_agent(request: Request):
    msg = await request.json()

    job_listings = msg["data"].get("job_listings", [])
    trending_skills = msg["data"].get("trending_skills", [])

    job_summary = ", ".join(job_listings)
    trend_summary = ", ".join(trending_skills)

    user_query = (
        f"Based on the following job listings and trending skills:\n"
        f"Jobs: {job_summary}\n"
        f"Trending Skills: {trend_summary}\n"
        f"Suggest a learning roadmap and career plan."
    )

    result = handle_career_agent(user_query, chat_history=[])

    return {
        "response": result[0],
        "jobs": job_listings,
        "trending_skills": trending_skills
    }
