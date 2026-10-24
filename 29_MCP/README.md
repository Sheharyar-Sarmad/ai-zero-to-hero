# Model Context Protocol (MCP) — Zero to Hero

A structured learning module for understanding, implementing, integrating, and distributing applications built with the **Model Context Protocol (MCP)**.

This module follows a progression from foundational concepts and protocol internals to practical implementation, Python integrations, and package deployment.

The goal is not merely to learn how to call MCP tools. It is to understand how MCP works, why its architecture exists, how its components communicate, what trade-offs it introduces, and how to implement these concepts in code.

## Learning Resources

- **Main learning repository:** [AI Zero to Hero](https://github.com/Sheharyar-Sarmad/ai-zero-to-hero)
- **MCP module:** [29 — MCP](https://github.com/Sheharyar-Sarmad/ai-zero-to-hero/tree/main/29_MCP)
- **LinkedIn:** [Sheharyar Sarmad](https://www.linkedin.com/in/sheharyar-sarmad-9b7736289/)
- **Html File** [FreeMCP](https://freemcp.netlify.app/)

## Learning Roadmap

Follow the modules in order. The theory builds the mental model needed to understand the code, while the implementation modules turn those concepts into working examples.

```text
29_MCP
│
├── 01_foundation
│   Understand what MCP is and why it exists
│
├── 02_MCP_internals
│   Understand the protocol, architecture, and trade-offs
│
├── 03_MCP_implementation
│   Implement and integrate MCP systems
│
├── 04_pythonic_view
│   Explore MCP through practical Python examples
│
└── 05_MCP_deployment
    Package and distribute an MCP server through PyPI
```

## 1. Foundation

**Directory:** `01_foundation/`

Start by understanding the problem MCP addresses before studying its implementation.

Topics include:

- What the Model Context Protocol is.
- Why a standardized protocol is useful for connecting AI applications with external tools and context.
- The advantages, limitations, alternatives, and trade-offs of MCP.

By the end of this section, you should be able to explain what MCP solves, when it is useful, and when a simpler integration might be sufficient.

## 2. MCP Internals

**Directory:** `02_MCP_internals/`

Explore the underlying protocol and the behavior of its components.

| Topic | What you will understand |
|---|---|
| Protocol layers and JSON-RPC | Message structure, requests, responses, notifications, and protocol communication. |
| Discovery, capabilities, and versions | How clients discover server features and negotiate compatible protocol behavior. |
| Transports | How MCP messages travel between clients and servers. |
| Tools, resources, and prompts | The differences between executable actions, contextual data, and reusable prompt templates. |
| Client features and notifications | Additional client capabilities and how servers communicate changes. |
| Security and trust | Authentication, authorization, untrusted content, tool permissions, and security boundaries. |
| MCP system design | Architectural decisions, component boundaries, failure handling, and design trade-offs. |

**Learning goal:** Understand what happens behind the scenes when an MCP client connects to a server, discovers its capabilities, and invokes a tool.

## 3. MCP Implementation

**Directory:** `03_MCP_implementation/`

Move from conceptual understanding to practical implementation.

The modules cover:

- Building your own MCP server.
- Inspecting and debugging an MCP server with MCP Inspector.
- Integrating an MCP server into an application.
- Understanding how `uvx` and `npx` launch MCP servers.
- Working with hosted MCP servers.
- Exploring the deployment approaches covered in the deployment lessons.
- Understanding MCP gateways and MCP hubs.

This section teaches you how to work with MCP implementations, inspect their behavior, connect different components, and understand common integration patterns.

## 4. Pythonic View

**Directory:** `04_pythonic_view/`

This section implements MCP concepts using Python and related tools. **Complete the MCP theory and implementation lessons before starting this section.**

### `01_create_MCP/`

Build an MCP server and connect it to Python and LangChain clients.

You will practise:

- Creating an MCP server and exposing tools.
- Connecting with a Python MCP client.
- Discovering and invoking tools through LangChain.

### `02_HTTP_MCP/`

Explore MCP over Streamable HTTP and integrate MCP tools with LangChain and LangGraph.

You will practise:

- Running an HTTP-based MCP server.
- Connecting clients to the MCP endpoint.
- Integrating discovered tools into LangChain.
- Building a LangGraph workflow with model and tool nodes.

### `03_community_mcp/`

Connect to community-developed and hosted MCP servers.

The examples use:

- **DuckDuckGo MCP:** Search the web using a community-developed server.
- **Tavily hosted MCP:** Discover and execute tools exposed by Tavily's hosted MCP service.

These examples demonstrate how to reuse existing MCP integrations rather than implementing every external service yourself.

### Python Environment Setup

Open a terminal in `04_pythonic_view/` and install the dependencies:

```powershell
uv sync
```

Configure the required environment variables using `.env.example` as a reference. Keep secret values in `.env` and never commit them to Git.

Run an individual example from the project directory. For example:

```powershell
uv run python 01_create_MCP/01_mcp_server.py
```

Use separate terminals when an example requires a server to remain running while a client connects to it. Check each subdirectory's README for its specific execution instructions.

Some integrations require external services, API keys, or network access. Their availability and usage limits depend on the provider.

## 5. MCP Deployment

**Directory:** `05_MCP_deployment/`

This section focuses on distributing a Python MCP server as an installable package.

Topics include:

- Preparing package metadata in `pyproject.toml`.
- Organizing a Python package using the `src/` layout.
- Managing dependencies and versions.
- Building wheel and source distributions.
- Validating package metadata and testing installations.
- Publishing a package to TestPyPI and PyPI.
- Handling releases, version updates, and publishing credentials.

The example package in this directory is `agentic_terminal`.

### Important Distinction

Publishing a Python package to PyPI distributes installable code. It does **not** automatically host an MCP server as a live remote service.

Package distribution and remote server hosting are separate deployment concerns.

Read `05_MCP_deployment/README.md` for the full publishing workflow.

## Prerequisites

Before beginning this module, you should have a working understanding of:

- Python fundamentals and modules.
- Basic asynchronous programming with `asyncio`.
- JSON and client-server communication.
- APIs and request-response patterns.
- Virtual environments and dependency management.
- Basic terminal usage.

You do not need to master every advanced concept in advance. Learn the concepts in sequence and use the implementation exercises to reinforce your understanding.

## Recommended Learning Method

For each topic:

1. **Understand the concept.** Read the theory and identify the problem the concept solves.
2. **Understand the mechanism.** Learn how messages, components, and responsibilities fit together.
3. **Implement it.** Run the examples and examine what the code actually does.
4. **Experiment.** Change inputs, inspect outputs, test failure cases, and observe the behavior.
5. **Evaluate trade-offs.** Consider complexity, security, reliability, maintainability, and when an alternative might be better.

Avoid treating the code as something to memorize. The objective is to understand why each component exists and how the system behaves as a whole.

## Important Note About Projects

**This module is a learning resource, not a completed real-world product.**

The Python files demonstrate individual concepts and integration patterns. They are intended to help build a strong understanding of MCP before applying it to larger systems.

After completing the theory and code implementations, the next step is to build practical projects that solve real problems using MCP. Those projects can incorporate appropriate application architecture, persistence, authentication, error handling, observability, and deployment based on their actual requirements.

Not every project needs every component. Choose the architecture according to the problem being solved.

## Completion Goals

By the end of this module, you should be able to:

- Explain MCP architecture and its core concepts.
- Describe how clients and servers communicate.
- Understand tools, resources, prompts, transports, and capability discovery.
- Build and inspect a basic MCP server.
- Connect Python applications to MCP servers.
- Integrate MCP tools with LangChain and LangGraph.
- Use community-developed and hosted MCP servers.
- Identify security considerations when working with external tools.
- Package and distribute a Python MCP implementation through PyPI.
- Apply MCP appropriately when designing a practical application.

## References

Use official documentation when checking protocol details, API behavior, compatibility, or deployment procedures.

- [Official MCP documentation](https://modelcontextprotocol.io/)
- [MCP specification](https://modelcontextprotocol.io/specification/)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [LangChain documentation](https://python.langchain.com/docs/introduction/)
- [LangGraph documentation](https://docs.langchain.com/oss/python/langgraph/overview)
- [Python Packaging User Guide](https://packaging.python.org/)

---

**The guiding principle:** Understand the protocol first, implement it second, evaluate its trade-offs, and then use it to build something meaningful.