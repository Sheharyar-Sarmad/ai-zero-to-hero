# Basic MCP Server and Clients

A simple implementation of the **Model Context Protocol (MCP)** using Python.

## Files

- `01_mcp_server.py` — Creates an MCP server and exposes tools.
- `02_python_client.py` — Connects to the server using a Python MCP client.
- `03_langchain_client.py` — Connects MCP tools with LangChain.

## Run

Start the server:

```bash
uv run python 01_mcp_server.py
```

Run a client in a separate terminal:

```bash
uv run python 02_python_client.py
```

Or run the LangChain client:

```bash
uv run python 03_langchain_client.py
```

Keep the server running while executing a client.

## Concepts

- MCP servers and clients
- Tool discovery and execution
- Python MCP SDK
- LangChain integration
