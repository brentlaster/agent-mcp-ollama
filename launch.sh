#!/bin/bash
echo "🧠 Starting Ollama model..."
ollama serve &

echo "🚀 Starting MCP Server..."
python3 mcp_server.py &

echo "💬 Starting Gradio Agent UI..."
python3 gradio_agent.py