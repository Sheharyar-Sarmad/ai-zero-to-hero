# Importing all the libraries and loading .env file
import os
from typing import TypedDict, Annotated
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage
from langgraph.graph import StateGraph, START, END
from langgraph.graph.state import CompiledStateGraph
from langgraph.checkpoint.memory import InMemorySaver

load_dotenv()

# Initializing the LLM model
llm: ChatGroq = ChatGroq(
    model="openai/gpt-oss-20b",
    max_tokens=1024,
    temperature=0.1
)

# Merging Node's value
def merge_score_dicts(existing: dict, newupdate: dict) -> dict:
    if existing is None:
        return newupdate

    return {**existing, **newupdate}


class AnalyzerState(TypedDict):
    raw_text: str
    safety_score: Annotated[dict[str, int], merge_score_dicts]

# Nodes

def toxicity_node(state: AnalyzerState) -> dict:
    print("\n[Branch 1] Analyzing Toxicity and Hate Speech...")

    prompt = (
        "Analyze the following text for profanity, aggression, hate speech, or toxicity. "
        "Provide a score from 0 to 100, where 0 means perfectly clean and 100 means highly toxic. "
        "Return ONLY the plain integer number, nothing else.\n\n"
        f"Text:\n{state['raw_text']}"
    )

    response = llm.invoke(prompt)

    try:
        score = int(response.content.strip())
    except ValueError:
        score = 0

    # Return the toxicity score under the shared state key
    return {"safety_score": {"toxicity_level": score}}

def copyright_node(state: AnalyzerState) -> dict:
    print("\n[Branch 2] Analyzing Copyright & Originality Risks...")

    prompt = (
        "Analyze the following text. Judge if it sounds heavily plagiarized, unoriginal, "
        "or presents a corporate trademark risk. Provide a score from 0 to 100, "
        "where 0 means entirely original and 100 means high risk. "
        "Return ONLY the plain integer number, nothing else.\n\n"
        f"Text:\n{state['raw_text']}"
    )

    response = llm.invoke(prompt)

    try:
        score = int(response.content.strip())
    except ValueError:
        score = 0

    # Return the copyright score under the same shared state key
    return {"safety_score": {"copyright_risk": score}}

def culture_node(state: AnalyzerState) -> dict:
    print("\n[Branch 3] Analyzing Regional & Cultural Sensitivity...")

    prompt = (
        "Analyze the following text for regional sensitivities, political landmines, "
        "or cultural insensitivity that might offend a global audience. Provide a score from 0 to 100, "
        "where 0 means completely safe and 100 means highly offensive. "
        "Return ONLY the plain integer number, nothing else.\n\n"
        f"Text:\n{state['raw_text']}"
    )

    response = llm.invoke(prompt)

    try:
        score = int(response.content.strip())
    except ValueError:
        score = 0

    # Return the cultural score under the same shared state key
    return {"safety_score": {"cultural_insensitivity": score}}


checkpointer: InMemorySaver = InMemorySaver()
builder: CompiledStateGraph[AnalyzerState] = StateGraph(AnalyzerState)

# Adding nodes
builder.add_node("toxicity_node", toxicity_node)
builder.add_node("copyright_node", copyright_node)
builder.add_node("culture_node", culture_node)

# Adding edges for the parallel workflow
builder.add_edge(START, "toxicity_node")
builder.add_edge(START, "copyright_node")
builder.add_edge(START, "culture_node")

builder.add_edge("toxicity_node", END)
builder.add_edge("copyright_node", END)
builder.add_edge("culture_node", END)

# Compiling the graph so we can execute it and send input and get an output
app: CompiledStateGraph[AnalyzerState] = builder.compile(checkpointer=checkpointer)

# Output
print("\nWelcome to our Safety Analyzer!")
print("Analyze your text for toxicity, copyright risk, and cultural sensitivity.")
print("Enter 'exit' if you want to quit!\n")

class PipelineInput(TypedDict):
    raw_text: str

# Creating a loop in which the user can enter text again and again
while True:
    pipeline_input: str = input("\nYou: ")

    if pipeline_input.lower() == "exit":
        print("\nQuitting the app. Thanks for using our app!\n")
        break

    # Execute the graph with thread configuration tracking
    result: AnalyzerState = app.invoke(
        {"raw_text": pipeline_input},
        config={
            "configurable": {
                "thread_id": "1"
            }
        }
    )

    # Display the combined safety scores
    print("\nAgent:")
    print(f"Toxicity Level: {result['safety_score'].get('toxicity_level', 0)}")
    print(f"Copyright Risk: {result['safety_score'].get('copyright_risk', 0)}")
    print(
        f"Cultural Insensitivity: "
        f"{result['safety_score'].get('cultural_insensitivity', 0)}"
    )
    print()