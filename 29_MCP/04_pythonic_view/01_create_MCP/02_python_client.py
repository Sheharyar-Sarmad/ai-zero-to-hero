# Import os to construct the absolute path to our MCP server script.
import os

# Import sys to access the Python interpreter currently running this client.
import sys

# Import asyncio to run asynchronous functions and manage the async runtime.
import asyncio

from rich import print # For better printing style 

# Import stdio_client to launch a local MCP server as a subprocess and
# establish communication with it through standard input/output streams.
from mcp.client.stdio import stdio_client

# Import ClientSession to manage the MCP protocol session between the client
# and server, including initialization, tool discovery, and tool execution.
#
# Import StdioServerParameters to configure how the local server process
# should be started, including the Python executable, script arguments,
# and environment variables.
from mcp import ClientSession, StdioServerParameters


# Create an absolute path to our MCP server script.
#
# __file__ refers to the current client script, not the terminal directory.
# abspath() resolves the client script path.
# dirname() extracts the directory containing the client.
# join() appends the MCP server filename to that directory.
#
# This makes the path reliable even when the client is executed from
# another working directory.
mcp_server_script: str = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "01_mcp_server.py"
)

print(f"MCP server script: {mcp_server_script}")


# Configure how the MCP server process should be launched.
server_params: StdioServerParameters = StdioServerParameters(
    # command must be a STRING, not a list.
    #
    # sys.executable points to the Python interpreter running this client.
    # This helps the server use the same virtual environment and installed
    # dependencies as the client.
    command=sys.executable,

    # Arguments passed to the Python interpreter.
    # The resulting command is equivalent to:
    #
    #     python "absolute/path/to/01_mcp_server.py"
    #
    # The interpreter executes this file, which starts our FastMCP server.
    args=[mcp_server_script],

    # None means inherit the current environment variables.
    # This can be useful when the server needs environment configuration.
    env=None
)


# Define the asynchronous client entry point.
#
# MCP communication uses asynchronous operations so the client can wait for
# network or process responses without blocking the event loop unnecessarily.
async def main() -> None:
    # Start the MCP server as a subprocess and establish stdio communication.
    #
    # The context manager provides two communication streams:
    # - read: receive messages sent by the MCP server.
    # - write: send messages to the MCP server.
    #
    # When this context exits, the stdio client handles process cleanup.
    async with stdio_client(server_params) as (read, write):

        # Create an MCP session over the communication streams.
        #
        # ClientSession manages the MCP protocol messages exchanged between
        # this client and the server. It does not launch the server itself;
        # stdio_client has already handled that responsibility.
        async with ClientSession(read, write) as session:

            # Initialize the MCP session.
            #
            # This performs the initial protocol handshake and establishes
            # the session before we request tools or call them.
            await session.initialize()

            # Request the list of tools registered by the MCP server.
            #
            # This discovers available tools; it does not execute them.
            # The server returns tool metadata such as names, descriptions,
            # and input schemas.
            tools_result = await session.list_tools()

            print("\nAvailable MCP tools:")

            # Display each discovered tool in a readable format.
            for tool in tools_result.tools:
                print(f"\nName: {tool.name}")
                print(f"Description: {tool.description}")
                print(f"Input schema: {tool.input_schema}")


if __name__ == "__main__":
    # This block runs only when this Python file is executed directly.
    #
    # asyncio.run() creates and manages an event loop, runs main(), and
    # cleans up the event loop when the coroutine finishes.
    #
    # RUNTIME OVERVIEW:
    # 1. The client constructs the server's launch configuration.
    # 2. stdio_client starts 01_mcp_server.py as a separate process.
    # 3. ClientSession initializes communication using the MCP protocol.
    # 4. list_tools() requests the tools exposed by the server.
    # 5. The server responds with metadata for tools such as "fetch"
    #    and "processed".
    # 6. The client displays the discovered tool information.
    #
    # IMPORTANT:
    # Discovering a tool does not execute it. To execute a tool, use:
    #
    #     result = await session.call_tool("fetch", {})
    #
    # For stdio transport, the server's stdout is reserved for protocol
    # messages. Use logging to stderr for server-side debugging.
    #
    # TRANSPORT:
    # This client uses stdio because it launches a local Python server.
    # For a server using Streamable HTTP, the client would connect using
    # the appropriate HTTP client transport instead.
    asyncio.run(main())
