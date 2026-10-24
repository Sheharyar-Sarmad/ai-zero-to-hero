# asyncio runs asynchronous code and lets us wait for MCP communication
# without blocking the event loop during I/O.
import asyncio

# os builds portable file paths without hardcoding the project location.
import os

# Rich makes terminal output easier to read during development.
from rich import print

# This adapter connects to MCP servers and converts their tools into
# LangChain-compatible tools for agents and workflows.
from langchain_mcp_adapters.client import MultiServerMCPClient

# MultiServerMCPClient lets one application discover tools from multiple
# MCP servers, even when those servers use different transports.
#
# The MCP adapter bridges MCP tool definitions and LangChain's tool
# interface, allowing LangChain agents and workflows to use these tools
# without manually implementing a separate integration for each server.
client: MultiServerMCPClient = MultiServerMCPClient(
    {
        # This server runs separately and communicates over HTTP.
        "data_fetch_mcp_http": {
            # The LangChain MCP adapter uses "streamable_http" as the
            # transport name for MCP Streamable HTTP connections.
            "transport": "streamable_http",

            # Point to the MCP endpoint exposed by the FastMCP server.
            # The server must already be running on this address and port.
            "url": "http://127.0.0.1:8050/mcp",
        },
    }
)


async def main() -> None:
    # Discover tools exposed by the configured MCP servers.
    # This is asynchronous because the client must communicate with the
    # servers to retrieve their tool definitions and input schemas.
    tools = await client.get_tools()

    # These are LangChain tool objects, not just names returned as strings.
    # Their descriptions and schemas help an agent understand which tools
    # are available and what arguments each tool expects.
    print("\nAvailable MCP tools:")

    for tool in tools:
        print(f"\nName: {tool.name}")
        print(f"Description: {tool.description}")
        print(f"Input schema: {tool.args_schema}\n")


if __name__ == "__main__":
    # asyncio.run() manages the event loop and executes the main coroutine.
    asyncio.run(main())
