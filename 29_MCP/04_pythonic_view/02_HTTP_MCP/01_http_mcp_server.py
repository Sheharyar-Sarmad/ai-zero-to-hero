# We already know how to create an MCP server and register tools.
# In this module, our focus shifts to exposing that server over Streamable HTTP
# so clients can communicate with it through an HTTP endpoint.
from fastmcp import FastMCP

from rich import print

# Create the MCP server instance that will hold our registered tools.
mcp: FastMCP = FastMCP()

# Register a tool that represents fetching data from an external source.
# FastMCP uses the function's name, docstring, and signature to describe the tool.
@mcp.tool(name="fetch")
def fetch_http():
    """
    Fetch data from an external source.

    A real implementation could call an API, query a database, or retrieve
    information from another service.
    """
    return {"data": "Hello, MCP!"}


# Register another independent tool for processing data.
# Registering multiple tools does not automatically connect them into a workflow.
@mcp.tool(name="processed")
def processed_http():
    """
    Process data.

    A real implementation could validate, transform, or calculate results
    from data supplied by a caller or another part of the application.
    """
    return {"data": "Data has been processed!"}

if __name__ == "__main__":
    # Start the MCP server using Streamable HTTP.
    #
    # Unlike stdio, where a client typically launches the server as a local
    # subprocess, Streamable HTTP lets a client connect through a URL.
    #
    # transport="http" selects FastMCP's Streamable HTTP transport.
    #
    # host="0.0.0.0" binds the server to all available IPv4 network interfaces.
    # This can make it reachable from other machines, depending on firewall,
    # network, and deployment configuration. It is not itself a public IP address.
    #
    # port=8050 selects the TCP port on which the HTTP server listens.
    # The port must be available and allowed by the host's firewall or platform.
    #
    # The endpoint path is provided by FastMCP; with its default configuration,
    # the MCP endpoint is typically available at /mcp.
    #
    # Local development URL:
    # http://127.0.0.1:8050/mcp
    #
    # A client on another machine must use a hostname or IP address reachable
    # from that machine, rather than 127.0.0.1 or 0.0.0.0.
    #
    # Production considerations:
    # - Bind to an appropriate interface for the deployment environment.
    # - Put public services behind HTTPS, commonly using a reverse proxy
    #   or a hosting platform's TLS termination.
    # - Configure authentication and authorization when the server exposes
    #   protected data or performs privileged operations.
    # - Restrict network access, validate tool inputs, and avoid exposing
    #   sensitive error details or credentials.
    # - Configure timeouts, logging, monitoring, and graceful shutdown.
    # - Use environment variables or deployment configuration for host and port
    #   instead of hardcoding them when deploying across environments.
    #
    # Streamable HTTP changes the transport, not the tools themselves.
    # The same registered tools can be exposed over different MCP transports.
    mcp.run(
        transport="http",
        host="0.0.0.0",
        port=8050,
    )
