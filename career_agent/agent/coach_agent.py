#coach_agent
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import SystemMessage
from agent.tools import recommend_courses_tool, plan_career_path_tool, build_learning_roadmap_tool

# Load environment variables
load_dotenv()

llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model_name=os.getenv("GROQ_MODEL_NAME", "meta-llama/llama-4-scout-17b-16e-instruct")
)

tools = [
    recommend_courses_tool,
    plan_career_path_tool,
    build_learning_roadmap_tool
]

prompt = ChatPromptTemplate.from_messages([
    SystemMessage(content="You are CoachGPT 🧠💼, a friendly and knowledgeable AI career coach. Based on user goals, provide clear, concise, and practical guidance."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("user", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad")
])

agent = create_tool_calling_agent(llm=llm, tools=tools, prompt=prompt)

career_coach_agent = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=False,
    handle_parsing_errors=True,
    return_intermediate_steps=False
)
