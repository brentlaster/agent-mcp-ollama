[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/brentlaster/agent-mcp-ollama?quickstart=1)

# 🧠 Agent with MCP Tools and Ollama (Codespaces Ready)

This project demonstrates how to use `smolagents`, `mcp`, and `Ollama` in GitHub Codespaces, and how to integrate with GitHub's **remote MCP server (public preview)**.

---

## Lab 1: Use Local MCP Inspector in Codespaces

### ✅ Setup

1. Open this repo in **GitHub Codespaces**
2. Ensure `.devcontainer` builds the container with `Ollama` and Python dependencies
3. In terminal:

```bash
pip install mcp
mcp dev calculator.py
```

- MCP Inspector UI at: `http://localhost:6274`
- SSE endpoint at: `http://localhost:6277/sse`

### ✅ Test Agent via CLI

```bash
python test_calculator_agent.py
```

### ✅ Or Use Chat UI

```bash
python chat_calculator_agent.py
```

---

## Lab 2: Use GitHub’s New Remote MCP Server (Public Preview)

🆕 As of [June 12, 2025](https://github.blog/changelog/2025-06-12-remote-github-mcp-server-is-now-available-in-public-preview/), you can register and use remote tools on GitHub’s cloud MCP platform.

### 🛠 Steps

1. Install latest `mcp` CLI:

```bash
pip install --upgrade mcp
```

2. Register your tool with GitHub’s MCP cloud server:

```bash
mcp register --tool calculator.py --remote
```

3. Start agent with remote tools:

```python
mcp_client = MCPClient({
    "url": "https://mcp.github.dev/sse",
    "token": "<your GitHub token>"
})
```

4. Run the CLI agent or Gradio app as usual
---

### 🔁 Lab 3: Add a Second Tool (Reverse String)

This lab shows how to add another tool to the MCP Inspector workflow.

#### ✅ Setup

Create `reverse_string.py`:

```python
from mcp import tool

@tool
def reverse_string(text: str) -> str:
    return text[::-1]
```

Then launch it:

```bash
mcp dev reverse_string.py
```

Update your test agent or Gradio interface to prompt:
> "Reverse the string 'hello world'"

🧠 The LLM will choose the appropriate tool via schema-based reasoning.
---

## 🎁 Bonus: Multi-Tool MCP Server

Instead of running individual tools, you can host multiple tools in a single server using FastMCP.

### ✅ Setup

Create a file `multi_tool_server.py`:

```python
from fastapi import FastAPI
from fastmcp import FastMCP
from mcp import tool

@tool
def calculator(expression: str) -> str:
    try:
        result = eval(expression, {"__builtins__": {}})
        return str(result)
    except Exception as e:
        return f"Error: {str(e)}"

@tool
def reverse_string(text: str) -> str:
    return text[::-1]

app = FastMCP().app
```

Run it with:

```bash
python multi_tool_server.py
```

Then connect your agent to:

```python
MCPClient({"url": "http://127.0.0.1:7860/sse"})
```

Now you can access **both tools** from one endpoint!
