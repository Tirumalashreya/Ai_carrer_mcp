# carrer_agent/main_dev.py
from agent.career_agent import handle_career_agent

chat_history = []
print("Career Coach is ready! (type 'exit' to quit)")

while True:
    user_input = input("You: ")
    if user_input.lower() in {"exit", "quit"}:
        print("Goodbye! 👋")
        break
    result = handle_career_agent(user_input, chat_history)
    print("CoachGPT:", result)
    chat_history.append({"role": "user", "content": user_input})
    chat_history.append({"role": "assistant", "content": result})
