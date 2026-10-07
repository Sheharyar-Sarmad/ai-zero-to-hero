import asyncio
from typing import TypedDict
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from langgraph.graph import StateGraph, START, END

# Load environment variables (GROQ_API_KEY)
load_dotenv()

# 1. Define the graph state schema tracking multi-step data flow
class State(TypedDict):
    query: str
    intermediate_step: str
    final_answer: str

# 2. Define sequential graph nodes representing distinct execution events
def analyzer_node(state: State) -> dict:
    """Node 1: Analyzes the raw user query and prepares context."""
    print("-> [Runtime] Running analyzer node...")
    return {"intermediate_step": f"Analyzed context for: {state['query']}"}

def generator_node(state: State) -> dict:
    """Node 2: Uses an LLM to generate the final response from the analyzed context."""
    print("-> [Runtime] Running generator node...")
    llm = ChatGroq(model="openai/gpt-oss-20b", temperature=0.5)
    msg = llm.invoke([HumanMessage(content=state["intermediate_step"])])
    return {"final_answer": msg.content}

# 3. Build and compile the multi-node graph workflow
builder = StateGraph(State)
builder.add_node("analyzer_node", analyzer_node)
builder.add_node("generator_node", generator_node)

builder.add_edge(START, "analyzer_node")
builder.add_edge("analyzer_node", "generator_node")
builder.add_edge("generator_node", END)

app = builder.compile()

# 4. Event-by-Event Streamer function using stream_mode="updates"
async def stream_graph_events(user_query: str):
    """
    Asynchronously streams graph execution event-by-event using stream_mode='updates'.
    Captures node completions instantly and extracts their exact return payloads.
    """
    initial_state = {
        "query": user_query,
        "intermediate_step": "",
        "final_answer": ""
    }

    print(f"Initializing Event-by-Event Stream for query: '{user_query}'\n")

    # astream with stream_mode="updates" yields a dictionary of node updates as they finish
    async for chunk in app.astream(initial_state, stream_mode="updates"):
        
        # Iterate through the node name and its corresponding state update dictionary
        for node_name, state_update in chunk.items():
            print(f"[EVENT TRIGGERED] Node Finished: '{node_name}'")
            print(f"Incremental State Update: {state_update}")
            print("-" * 50)

# 5. Local execution loop
if __name__ == "__main__":
    test_query = "Why event-driven streaming is essential for modern AI applications."
    asyncio.run(stream_graph_events(test_query))