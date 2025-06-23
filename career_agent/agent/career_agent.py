#carrer_agent/agent/career_agent.py
from agent.coach_agent import career_coach_agent

def handle_career_agent(user_input, chat_history):
    """
    Routes request to the Career Coach Agent.
    """
    result = career_coach_agent.invoke({
        "input": user_input,
        "chat_history": chat_history
    })
    return result.get("output", "Sorry, I couldn't process your request.")
