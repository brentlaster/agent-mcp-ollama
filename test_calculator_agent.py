from smolagents import MCPClient, CodeAgent, OllamaModel

mcp_client = MCPClient({"url": "http://127.0.0.1:6277/sse"})
tools = mcp_client.get_tools()
model = OllamaModel(model="llama3")
agent = CodeAgent(tools=tools, model=model)

question = "What is 12 * (5 + 3)?"
response = agent.run(question)

print(f"\n🧠 Prompt: {question}\n📎 Response: {response}")