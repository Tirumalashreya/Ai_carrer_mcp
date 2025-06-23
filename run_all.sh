#!/bin/bash

echo "🚀 Starting MCP Server..."
cd mcp_server && uvicorn main:app --port 8000 --reload &

cd ..
echo "📝 Starting Resume Agent..."
cd resume_agent && uvicorn agent_api:app --port 8001 --reload &

cd ..
echo "🔎 Starting Research Agent..."
cd research_agent && uvicorn agent_api:app --port 8002 --reload &

cd ..
echo "🎓 Starting Career Coach Agent..."
cd career_agent && uvicorn main:app --port 8003 --reload &
