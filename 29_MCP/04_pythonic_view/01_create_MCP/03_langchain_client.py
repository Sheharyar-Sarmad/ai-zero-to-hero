# asyncio provides the event loop and asynchronous execution primitives
# needed to run coroutines and wait for asynchronous MCP communication.
import asyncio

# os provides path-handling functions for constructing filesystem paths
# in a platform-independent way, including on Windows and Linux.
import os

# Rich provides enhanced terminal output, making tool information and
# Python objects easier to read during development and debugging.
from rich import print

# MultiServerMCPClient manages connections to configured MCP servers
# and retrieves their tools as LangChain-compatible tool objects.
from langchain_mcp_adapters.client import MultiServerMCPClient


# __file__ contains the path of this Python file.
# abspath() converts it to an absolute path, and dirname() extracts
# the directory containing this client script.
client_directory: str = os.path.dirname(os.path.abspath(__file__))

# The MCP server script is located in the same directory as this client.
# join() combines path components using the correct separator for the OS,
# avoiding manually hardcoding Windows backslashes.
mcp_server_script: str = os.path.join(
    client_directory,
    "01_mcp_server.py",
)

# The project root is the parent directory of the client script's directory.
# dirname() moves one level upward from client_directory.
project_root: str = os.path.dirname(client_directory)

# The virtual environment is stored in the project's root directory.
# Constructing this path dynamically allows the project to be moved
# without needing to rewrite an absolute path in the client configuration.
venv_directory: str = os.path.join(
    project_root,
    ".venv",
)

# Build the path to the virtual environment's Python interpreter.
# On Windows, the interpreter is under Scripts\python.exe.
# This explicitly selects the project's Python environment to launch the
# MCP server with the dependencies installed for that environment.
python_executable: str = os.path.join(
    venv_directory,
    "Scripts",
    "python.exe",
)


async def main():
    # Configure an MCP client that can communicate with one or more servers.
    # Each dictionary entry identifies a server and describes how to launch
    # or connect to it. The client uses this configuration for communication
    # and tool discovery.
    client: MultiServerMCPClient = MultiServerMCPClient(
        {
            # This is a logical name for the server within the client.
            # It is used as a configuration key, not as a network hostname
            # or the actual Python script name.
            "data_fetch_mcp_stdio": {
                # The stdio transport communicates through the server process's
                # standard input and standard output streams. The client launches
                # the server as a subprocess, so no HTTP endpoint is required.
                "transport": "stdio",

                # Specify the Python interpreter used to run the MCP server.
                # Using the project interpreter helps ensure that the server
                # has access to the expected packages and environment.
                "command": python_executable,

                # Arguments passed to the interpreter after the executable.
                # Here, the argument is the path to the MCP server script.
                # The server process starts and registers the tools it exposes.
                "args": [mcp_server_script],
            }
        }
    )

    # Discover the tools exposed by the configured MCP server.
    # get_tools() is asynchronous because discovery involves communication
    # with the server and retrieval of its tool definitions over MCP.
    # await suspends this coroutine until discovery completes, allowing
    # the event loop to schedule other asynchronous work when possible.
    tools = await client.get_tools()

    # Print the discovered LangChain tool objects for inspection.
    # Each object typically includes metadata such as its name, description,
    # and input schema, which describes the arguments the tool accepts.
    print("Available tools:", tools)


if __name__ == "__main__":
    # asyncio.run() creates and manages an event loop for the main coroutine.
    # It runs main() until completion and then closes the event loop.
    # This is the standard entry point for a standalone asynchronous script.
    asyncio.run(main())
