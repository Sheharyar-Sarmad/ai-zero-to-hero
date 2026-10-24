import asyncio
from typing import Any

from rich import print
from langchain_groq import ChatGroq
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_core.tools import BaseTool
from langchain_core.messages import BaseMessage
from langgraph.graph import StateGraph, MessagesState, START
from langgraph.prebuilt import ToolNode, tools_condition
from dotenv import load_dotenv

load_dotenv()

# Connect to the MCP server that is already running separately.
# Streamable HTTP lets this client communicate with the server through
# HTTP requests and responses at the /mcp endpoint.
mcp_client: MultiServerMCPClient = MultiServerMCPClient(
    {
        "http_mcp_server": {
            "transport": "streamable_http",
            "url": "http://127.0.0.1:8050/mcp",
        }
    }
)

async def main() -> None:
    # Discover the tools exposed by the MCP server.
    # The adapter converts MCP tool definitions into LangChain-compatible
    # tools that the model and LangGraph can work with.
    tools: list[BaseTool] = await mcp_client.get_tools()

    print("[bold cyan]Available MCP tools[/bold cyan]")
    for tool in tools:
        print(f"{tool.name}: {tool.description}")

    # Create a Groq-hosted model that supports tool calling.
    # GROQ_API_KEY is read from the environment automatically.
    model: ChatGroq = ChatGroq(
        model="openai/gpt-oss-20b",
        temperature=0,
    )

    # Make the discovered tools available to the model.
    # This lets the model request a tool call, but does not execute it.
    model_with_tools: Any = model.bind_tools(tools)

    async def assistant(state: MessagesState) -> dict[str, list[BaseMessage]]:
        # The conversation messages are the current graph state.
        # The model returns either a normal answer or a tool-call request.
        response: BaseMessage = await model_with_tools.ainvoke(
            state["messages"]
        )

        # Add the new model response to the existing message history.
        return {"messages": [response]}

    # ToolNode executes the tool calls requested by the model.
    # The MCP adapter routes each call to its configured server.
    tool_node: ToolNode = ToolNode(tools)

    # Define the nodes and transitions of the LangGraph workflow.
    graph_builder: StateGraph = StateGraph(MessagesState)
    graph_builder.add_node("assistant", assistant)
    graph_builder.add_node("tools", tool_node)

    # Every run starts by asking the model to respond to the user.
    graph_builder.add_edge(START, "assistant")

    # Route to the tools node when the model requests tools.
    # If it returns a normal response, the graph finishes.
    graph_builder.add_conditional_edges(
        "assistant",
        tools_condition,
    )

    # After tools execute, give their results back to the model.
    # The model can then call another tool or produce its final answer.
    graph_builder.add_edge("tools", "assistant")

    # Compile the graph into an executable workflow.
    graph = graph_builder.compile()

    # Run the workflow with a task supported by the MCP server.
    result: dict[str, Any] = await graph.ainvoke(
        {
            "messages": [
                (
                    "user",
                    "Use the available MCP tools to fetch data "
                    "and explain the result.",
                )
            ]
        }
    )

    # Display the final message after the tool-calling loop finishes.
    final_message: BaseMessage = result["messages"][-1]

    print("\n[bold green]Final answer[/bold green]")
    print(final_message.content)

if __name__ == "__main__":
    # Run the asynchronous workflow using Python's event loop.
    asyncio.run(main())
