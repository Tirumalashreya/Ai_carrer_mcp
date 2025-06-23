career_agent/agent/tools

import json
import os
from langchain_core.tools import tool

COURSES_PATH = os.path.join(os.path.dirname(__file__), "../data/mock_courses.json")

def load_courses():
    try:
        with open(COURSES_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        return []

@tool
def recommend_courses_tool(goal: str) -> str:
    """Recommend relevant courses based on user's career goal."""
    courses = load_courses()
    goal_lower = goal.lower()

    matched_courses = []
    for course in courses:
        if any(tag in goal_lower for tag in course["tags"]):
            matched_courses.append(course["title"])

    if matched_courses:
        return "Here are some recommended courses:\n" + "\n".join(f"- {title}" for title in matched_courses)
    else:
        return "Sorry, no matching courses found. Please provide a more specific goal."

@tool
def plan_career_path_tool(goal: str) -> str:
    """Provide a step-by-step career path plan based on the user's goal."""
    return (
        f"Career path for {goal}:\n"
        "- Learn the fundamentals\n"
        "- Build projects\n"
        "- Contribute to open source\n"
        "- Network with professionals\n"
        "- Apply for internships/jobs"
    )

@tool
def build_learning_roadmap_tool(goal: str) -> str:
    """Generate a monthly learning roadmap tailored to the career goal."""
    return (
        f"Learning roadmap for {goal}:\n"
        "Month 1: Basics and core skills\n"
        "Month 2: Intermediate projects\n"
        "Month 3: Real-world projects & portfolio\n"
        "Month 4+: Job applications and networking"
    )
