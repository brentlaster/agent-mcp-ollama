from mcp import tool

@tool
def reverse_string(text: str) -> str:
    """
    Reverses a string.

    Args:
        text (str): Input string

    Returns:
        str: Reversed string
    """
    return text[::-1]