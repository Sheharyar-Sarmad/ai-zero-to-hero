# Import FastMCP, a high-level Python framework for building MCP servers.
# FastMCP handles much of the MCP protocol implementation for us, including
# exposing Python functions as tools and handling incoming MCP messages.
from fastmcp import FastMCP


# Create an MCP server instance.
# Think of this as creating the server-side application that will expose
# capabilities to an MCP client, such as an AI application.
# The server instance keeps track of registered tools and other MCP features.
mcp: FastMCP = FastMCP()


# Register a Python function as an MCP tool named "fetch".
# The @mcp.tool decorator tells FastMCP that this function should be exposed
# as a tool that connected MCP clients can discover and call.
# At startup, FastMCP uses the function's metadata, including its name,
# docstring, and signature, to build the tool definition. The function does
# not need to be executed just to register it.
# When a client discovers available tools, the "fetch" tool can be included
# in the server's tool list. When a client calls it, FastMCP invokes this
# Python function and returns its result through the MCP protocol.
@mcp.tool(name="fetch")
def fetch():
    """
    Fetch data from an API, database, or another external data source.

    This docstring describes the tool's purpose. FastMCP can use it as part
    of the description shown to an MCP client so the model can understand
    when this tool is appropriate to call.

    In a real application, you could validate inputs, call an external API,
    query a database, and handle possible errors here.
    """
    # This is mock data for our first MCP server.
    # Returning a Python dictionary allows FastMCP to serialize the result
    # into a format suitable for an MCP tool response.
    return {"data": "Hello, MCP!"}


# Register another MCP tool named "processed".
# This is a separate tool from "fetch". Registering both tools does NOT
# automatically create a workflow in which "fetch" runs before "processed".
# The AI application or other client decides which tool to call and when.
# If one tool depends on another tool's output, that workflow must be
# orchestrated explicitly by the client or implemented in server-side logic.
@mcp.tool(name="processed")
def processed():
    """
    Process previously fetched data.

    In a real application, this function could transform records, validate
    data, calculate results, or prepare information for another operation.
    """
    # Return mock processing output.
    # Notice that this example does not actually receive or process the
    # output of fetch(); it simply demonstrates a second independent tool.
    return {"data": "Data has been processed!"}


if __name__ == "__main__":
    # This block runs only when this Python file is executed directly.
    # For example:
    #     python server.py
    # If another Python module imports this file, the tools are registered,
    # but this block will not automatically start the server.

    # Start the MCP server using stdio transport.
    #
    # RUNTIME OVERVIEW:
    # 1. FastMCP starts running and waits for MCP messages from its client.
    # 2. The client and server communicate through standard input (stdin)
    #    and standard output (stdout) of this Python process.
    # 3. The client can initialize the MCP session and discover tools.
    # 4. When the client calls "fetch" or "processed", FastMCP dispatches
    #    the request to the corresponding Python function.
    # 5. FastMCP serializes the result and sends the response to the client.
    # 6. The server continues handling messages while the process is running.
    #
    # IMPORTANT:
    # - stdout is reserved for protocol communication. Avoid print() calls
    #   there because arbitrary text can corrupt the protocol stream.
    # - Use logging to stderr for debugging instead.
    # - With stdio, the MCP client commonly launches and manages this process.
    #
    # TRANSPORT OPTIONS:
    # - "stdio": local communication through stdin/stdout.
    # - "http": network communication using FastMCP's Streamable HTTP
    #   transport. For current FastMCP versions, use transport="http".
    #   Configure the host and port as needed, for example:
    #
    #       mcp.run(transport="http", host="127.0.0.1", port=8000)
    #
    #   A remote HTTP server also needs appropriate authentication,
    #   authorization, and network security for its deployment context.
    #
    # Streamable HTTP is an MCP transport; it is not a separate tool or
    # a different MCP protocol. The same registered tools can be exposed
    # over either transport.
    mcp.run(transport="stdio")
