import gradio as gr
from smolagents import MCPClient, CodeAgent, OllamaModel

mcp_client = MCPClient({"url": "http://127.0.0.1:6277/sse"})
tools = mcp_client.get_tools()
model = OllamaModel(model="llama3")
agent = CodeAgent(tools=tools, model=model)

demo = gr.ChatInterface(
    fn=lambda msg, hist: str(agent.run(msg)),
    type="messages",
    title="Chat Calculator via MCP Inspector",
    description="Ask math questions and get answers using MCP tool with LLM via Inspector."
)

if __name__ == "__main__":
    demo.launch()