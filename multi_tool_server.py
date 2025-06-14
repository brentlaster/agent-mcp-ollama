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

# Combine tools into one FastMCP app
app = FastMCP().app

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("multi_tool_server:app", host="0.0.0.0", port=7860, reload=True)