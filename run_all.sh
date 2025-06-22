#!/bin/bash
echo "🚀 Starting MCP Server..."
cd mcp_server && uvicorn main:app --port 8000 --reload &

echo "📝 Starting Resume Agent..."
cd ../resume_agent && uvicorn agent_api:app --port 8001 --reload &

echo "🔎 Starting Research Agent..."
cd ../research_agent && uvicorn agent_api:app --port 8002 --reload &

echo "🎓 Starting Career Coach Agent..."
cd ../career_agent && uvicorn main:app --port 8003 --reload &
