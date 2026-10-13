# my_mcp_server.py
from fastmcp import FastMCP   # alternative import (older/newer SDKs): from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Sample MCP Server")

@mcp.tool()
def greet(name: str) -> str:
    """Return a friendly greeting."""
    return f"Hello, {name}! Welcome to MCP Lab."

@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    """Add two integers."""
    return a + b

if __name__ == "__main__":
    # default transport is STDIO (good for local tests)
    mcp.run()