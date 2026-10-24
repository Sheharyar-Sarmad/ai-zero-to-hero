# MCP over HTTP

A simple implementation of MCP using **Streamable HTTP** and integrations with LangChain and LangGraph.

## Files

- `01_http_mcp_server.py` — Runs an MCP server over HTTP on port `8050`.
- `02_langchain_client.py` — Connects MCP tools with LangChain.
- `03_langgraph_client.py` — Uses LangGraph to orchestrate an LLM and MCP tools.

## Run

Start the HTTP server:

```bash
uv run python 01_http_mcp_server.py
```

The MCP endpoint is:

```text
http://127.0.0.1:8050/mcp
```

Run a client in a separate terminal:

```bash
uv run python 02_langchain_client.py
```

Or run the LangGraph client:

```bash
uv run python 03_langgraph_client.py
```

Set `GROQ_API_KEY` in your environment before running clients that use Groq.

## Concepts

- Streamable HTTP transport
- MCP tool discovery and execution
- LangChain tool integration
- LangGraph nodes, edges, and conditional routing
- LLM tool-calling loops
