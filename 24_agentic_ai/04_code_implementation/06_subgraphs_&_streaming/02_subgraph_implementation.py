from typing import TypedDict
from langgraph.graph import StateGraph, START, END

# 1. Define Subgraph Schema & Logic 
class SubgraphState(TypedDict):
    sub_input: str
    sub_output: str

def process_node(state: SubgraphState) -> dict:
    """Transforms input text inside the isolated subgraph."""
    processed = state["sub_input"].upper()
    return {"sub_output": f"Subgraph Processed: {processed}"}

# Build and compile the inner subgraph independently
sub_builder = StateGraph(SubgraphState)
sub_builder.add_node("process", process_node)
sub_builder.add_edge(START, "process")
sub_builder.add_edge("process", END)
compiled_subgraph = sub_builder.compile()

# 2. Define Parent Schema & Wrapper Node ---
class ParentState(TypedDict):
    raw_text: str
    final_output: str

def subgraph_wrapper_node(state: ParentState) -> dict:
    """Bridges parent state to subgraph schema and invokes it."""
    # Map parent state fields to subgraph input
    sub_input_payload = {"sub_input": state["raw_text"], "sub_output": ""}
    
    # Execute the compiled subgraph
    result = compiled_subgraph.invoke(sub_input_payload)
    
    # Map subgraph output back to parent state keys
    return {"final_output": result["sub_output"]}

# 3. Build & Compile Parent Graph ---
parent_builder = StateGraph(ParentState)
parent_builder.add_node("nested_subgraph_node", subgraph_wrapper_node)
parent_builder.add_edge(START, "nested_subgraph_node")
parent_builder.add_edge("nested_subgraph_node", END)

app = parent_builder.compile()

if __name__ == "__main__":
    print("Executing Parent Graph with Nested Subgraph...")
    initial_state = {"raw_text": "hello modular langgraph", "final_output": ""}
    output = app.invoke(initial_state)
    print("\nResult:", output)