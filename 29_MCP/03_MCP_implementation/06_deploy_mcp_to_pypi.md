# Deploy an MCP Server to PyPI

> Package your server so anyone can run it with `uvx`.

**Reading time:** ~4 minutes

## The idea

**PyPI** is Python's public package index. If your server is a package with a command-line entry point, users can run it with `uvx your-package` or install it with `pip`.

## Steps

```mermaid
flowchart LR
    A[Write server] --> B[Add entry point<br/>in pyproject.toml]
    B --> C[Build package]
    C --> D[Publish to PyPI]
    D --> E["Users run: uvx your-package"]
```

**1. Add a `main()` that runs the server.** Use the run method for your SDK version (see the SDK's "Running your server" docs).

**2. Declare a command in `pyproject.toml`:**

```toml
[project]
name = "my-mcp-server"
version = "0.1.0"
dependencies = ["mcp"]

[project.scripts]
my-mcp-server = "my_mcp_server.server:main"
```

**3. Build and publish:**

```bash
uv build
uv publish
```

You need a PyPI account and API token.

**4. Use it in a host config:**

```json
{ "mcpServers": { "mine": { "command": "uvx", "args": ["my-mcp-server"] } } }
```

## Good practices

- Pick a unique package name.
- Bump the version on every release.
- Document tools and required environment variables in the README.
- Never bundle secrets.

## Summary

- Package + entry point + publish = installable server.
- Users run it with `uvx`.
- Keep secrets out of the package.

## Quick check

1. What makes `uvx my-mcp-server` work?
2. Why not include API keys in the package?

<details>
<summary>Answers</summary>

1. A published package with a `[project.scripts]` entry point.
2. Anyone could read them; pass secrets via environment variables instead.

</details>

## References

- https://py.sdk.modelcontextprotocol.io/