# MCP — Pythonic View

A hands-on implementation of **Model Context Protocol (MCP)** using Python, the MCP SDK, LangChain, LangGraph, and third-party MCP servers.

This directory focuses on understanding how MCP works through code, from creating your own MCP server to integrating existing community and hosted servers.

## Learning Resources

- **Complete AI learning repository:** [ai-zero-to-hero](https://github.com/Sheharyar-Sarmad/ai-zero-to-hero)
- **MCP theory and learning module:** [29 — MCP](https://github.com/Sheharyar-Sarmad/ai-zero-to-hero/tree/main/29_MCP)
- **LinkedIn:** [Sheharyar Sarmad](https://www.linkedin.com/in/sheharyar-sarmad-9b7736289/)

## Prerequisites

**Complete the MCP theory module before starting these implementations.**

Study the concepts in the [`29_MCP` module](https://github.com/Sheharyar-Sarmad/ai-zero-to-hero/tree/main/29_MCP) first. Understand the MCP architecture, hosts, clients, servers, tools, resources, prompts, transports, and communication flow before moving into the code.

You should also have Python and `uv` installed and understand basic Python asynchronous programming with `asyncio`.

## Directory Structure

```text
04_pythonic_view/
├── 01_create_MCP/
│   ├── 01_mcp_server.py
│   ├── 02_python_client.py
│   ├── 03_langchain_client.py
│   └── README.md
├── 02_HTTP_MCP/
│   ├── 01_http_mcp_server.py
│   ├── 02_langchain_client.py
│   ├── 03_langgraph_client.py
│   └── README.md
├── 03_community_mcp/
│   ├── 01_community_mcp.py
│   ├── 02_third_party_hosted_mcp.py
│   └── README.md
├── .env
├── .env.example
├── .gitignore
├── pyproject.toml
├── requirements.txt
└── uv.lock
```

## Modules

### 01 — Create an MCP Server

Learn to build an MCP server, expose tools, connect a Python client, and integrate the tools with LangChain.

### 02 — MCP over HTTP

Explore Streamable HTTP transport and connect MCP tools with LangChain and LangGraph.

### 03 — Community and Hosted MCP Servers

Connect to community-developed and third-party hosted MCP servers, including DuckDuckGo and Tavily, to discover and execute external tools.

## Setup

From this directory, install the project dependencies:

```bash
uv sync
```

Configure any required environment variables in your local `.env` file. Refer to `.env.example` for the expected variable names.

Keep API keys and other secrets out of version control.

## Important Note

**This repository section is for learning and code implementation, not a completed real-world project.**

The goal is to understand MCP concepts by implementing them step by step. After completing the code implementations and building a solid understanding of the underlying concepts, the next step will be to create practical, real-world projects using MCP.

