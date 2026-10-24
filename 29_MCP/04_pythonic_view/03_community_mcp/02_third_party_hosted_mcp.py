import asyncio
import os
from typing import Any

from dotenv import load_dotenv
from rich import print
from langchain_core.tools import BaseTool
from langchain_mcp_adapters.client import MultiServerMCPClient

# Load environment variables from the .env file.
load_dotenv()

# Read the Tavily API key without hardcoding the secret in Python.
TAVILY_API_KEY: str | None = os.getenv("TAVILY_API_KEY")

if not TAVILY_API_KEY:
    raise RuntimeError(
        "TAVILY_API_KEY is missing. Add it to your .env file."
    )

# Connect to Tavily's official remote MCP server over Streamable HTTP.
# The Bearer token authenticates requests without exposing the key in the URL.
client: MultiServerMCPClient = MultiServerMCPClient(
    {
        "tavily": {
            "transport": "streamable_http",
            "url": "https://mcp.tavily.com/mcp/",
            "headers": {
                "Authorization": f"Bearer {TAVILY_API_KEY}",
            },
        }
    }
)

async def main() -> None:
    # Discover the tools that Tavily exposes through MCP.
    tools: list[BaseTool] = await client.get_tools()

    print("\n[bold cyan]Available Tavily MCP tools:[/bold cyan]")

    for tool in tools:
        print(f"\nName: {tool.name}")
        print(f"Description: {tool.description}")
        print(f"Input schema: {tool.args_schema}")

    # Find the search tool by its name rather than assuming the server's
    # exact naming convention.
    search_tool: BaseTool | None = next(
        (
            tool
            for tool in tools
            if "search" in tool.name.lower()
        ),
        None,
    )

    if search_tool is None:
        raise RuntimeError(
            "No search tool was found in the Tavily MCP server."
        )

    # Send a real query to Tavily through the discovered MCP tool.
    question: str = (
        "What is edge computing, and what are its real-world applications?"
    )

    print(f"\n[bold yellow]Question:[/bold yellow] {question}")
    print("\n[bold cyan]Searching with Tavily...[/bold cyan]")

    result: Any = await search_tool.ainvoke(
        {
            "query": question,
            "max_results": 5,
        }
    )

    # Display the search results returned by Tavily.
    print("\n[bold green]Search results:[/bold green]")
    print(result)


if __name__ == "__main__":
    asyncio.run(main())
