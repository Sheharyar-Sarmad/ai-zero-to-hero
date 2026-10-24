import asyncio
from typing import Any

from rich import print
from langchain_core.tools import BaseTool
from langchain_mcp_adapters.client import MultiServerMCPClient

# Community MCP servers are built by developers or organizations and expose
# tools that other applications can discover and use through the MCP protocol.
#
# Here, we use the community-developed duckduckgo-mcp-server to access
# DuckDuckGo, a free search engine. No search API key is required for this
# setup, although automated requests may be rate-limited.
#
# MultiServerMCPClient connects to MCP servers and converts their tools into
# LangChain-compatible tools that we can invoke directly or use with an agent.
client: MultiServerMCPClient = MultiServerMCPClient(
    {
        "duckduckgo": {
            # stdio transport launches the MCP server as a local subprocess
            # and communicates with it through standard input and output.
            "transport": "stdio",
            "command": "uvx",
            "args": ["duckduckgo-mcp-server"],
        }
    }
)

async def main() -> None:
    # Discover the tools provided by the community MCP server.
    # The adapter starts the server and retrieves its tool definitions.
    tools: list[BaseTool] = await client.get_tools()

    print("\n[bold cyan]Available community MCP tools:[/bold cyan]")

    for tool in tools:
        print(f"\nName: {tool.name}")
        print(f"Description: {tool.description}")
        print(f"Input schema: {tool.args_schema}")

    # Select the first discovered tool named "search".
    # next() retrieves the first match from the generator expression.
    search_tool: BaseTool = next(
        tool for tool in tools if tool.name == "search"
    )

    # Send a question directly to DuckDuckGo through the MCP search tool.
    # This performs a web search; it does not use an LLM to generate an answer.
    question: str = (
        "What is edge computing, and what are its real-world applications?"
    )

    print(f"\n[bold yellow]Question:[/bold yellow] {question}")
    print("\n[bold cyan]Searching DuckDuckGo...[/bold cyan]")

    # ainvoke() executes the discovered tool asynchronously.
    # Direct MCP tool calls do not consume LLM tokens, but search requests
    # can still be subject to DuckDuckGo or server-side rate limits.
    result: Any = await search_tool.ainvoke(
        {
            "query": question,
            "max_results": 5,
        }
    )

    # Display the search results returned by the MCP server.
    print("\n[bold green]DuckDuckGo search results:[/bold green]")
    print(result)

if __name__ == "__main__":
    # Run the asynchronous client.
    # The MCP server is launched automatically through uvx when needed.
    asyncio.run(main())
