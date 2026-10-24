# Community and Hosted MCP Servers

Learn how to connect Python applications to community-developed and hosted MCP servers using LangChain MCP Adapters.

## Files

- `01_community_mcp.py` — Connects to the community-developed DuckDuckGo MCP server to discover tools and perform web searches.
- `02_third_party_hosted_mcp.py` — Connects to Tavily's hosted MCP server to discover tools and search the web.

## Setup

Install the required dependencies:

```powershell
uv add langchain-mcp-adapters python-dotenv rich
```

Install `uv` if it is not already available, since the DuckDuckGo example launches its server using `uvx`.

## Environment Variables

Create a `.env` file in this directory for Tavily authentication:

```dotenv
TAVILY_API_KEY=your_tavily_api_key
```

Keep `.env` out of version control.

## Run

Run the DuckDuckGo MCP client:

```powershell
python 01_community_mcp.py
```

Run the Tavily hosted MCP client:

```powershell
python 02_third_party_hosted_mcp.py
```

## Concepts