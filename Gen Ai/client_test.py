# client_test.py
import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def main():
    # Launch the server subprocess and connect over STDIO
    server_params = StdioServerParameters(command="python", args=["my_mcp_server.py"])

    # Use context managers so subprocess gets cleaned up
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()

            # list tools
            tools_resp = await session.list_tools()
            print("Available tools:", [t.name for t in tools_resp.tools])

            # call greet
            greet_result = await session.call_tool("greet", {"name": "Alice"})
            print("greet result (raw):", greet_result)
            # Try to print content cleanly (structure may vary by version)
            if getattr(greet_result, "content", None):
                print("greet content:", greet_result.content)

            # call add_numbers
            add_result = await session.call_tool("add_numbers", {"a": 3, "b": 5})
            print("add result (raw):", add_result)
            if getattr(add_result, "content", None):
                print("add content:", add_result.content)

if __name__ == "__main__":
    asyncio.run(main())