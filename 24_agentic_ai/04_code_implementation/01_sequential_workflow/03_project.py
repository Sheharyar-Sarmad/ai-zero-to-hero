import os
from dotenv import load_dotenv
from typing import TypedDict
from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage

load_dotenv()

# Lets create the state first
class PipelineState(TypedDict):
    raw_input: str
    edited_text: str 
    script_text: str 
    final_output: str 

# Time for nodes. Nodes are just the workers for the graph like engineers in a software house

llm: ChatGroq = ChatGroq(
    model="openai/gpt-oss-20b",
    max_tokens=1024,
    temperature=0.7
)

# Lets create nodes

# Stage 1: Editor Node 
def editor_node(state: PipelineState) -> dict[str, str]:
    """Stage 1: Clean up raw input text."""
    try:
        print("\n--- [Stage 1] Executing Editor Node ---")
        
        prompt: str = (
            "You are an expert copyeditor. Clean up the following raw text. "
            "Fix any grammatical errors, spelling mistakes, and smooth out the transitions "
            "while keeping the core message intact. Return only the edited text.\n\n"
            f"Text:\n{state['raw_input']}"
        )
        
        response: AIMessage = llm.invoke(prompt)
        return {"edited_text": response.content.strip()}
        
    except Exception as err:
        raise Exception(f"Error in Editor Node & the error says: {err}")


# Stage 2: Scriptwriter Node 
def scriptwriter_node(state: PipelineState) -> dict[str, str]:
    """Stage 2: Format the clean text into an engaging video script style."""
    try:
        print("\n--- [Stage 2] Executing Scriptwriter Node ---")

        prompt: str = (
            "You are a charismatic YouTube content creator. Take this edited text and transform "
            "it into a highly engaging, punchy, conversational video script hook. Make it sound "
            "like a real person speaking passionately. Return only the script content.\n\n"
            f"Edited Text:\n{state['edited_text']}"
        )

        response: AIMessage = llm.invoke(prompt)

        # Fixed: .strip() ensures it returns a clean string instead of a word list (.split())
        return {"script_text": response.content.strip()}

    except Exception as err:
        raise Exception(f"Error comes while writing script from edited text & the error says: {err}")


# Stage 3: Roman Hinglish Translator Node 
def translator_node(state: PipelineState) -> dict[str, str]:
    """Stage 3: Translates the script into natural flowing Roman Hinglish (chatting style)."""
    try:
        print("\n--- [Stage 3] Executing Roman Hinglish Translator Node ---")
        
        prompt: str = (
            "You are an expert content localizer for a young, tech-savvy audience. Take the following script "
            "and convert it into natural, conversational 'Roman Hinglish' (written strictly in English/Latin alphabets, "
            "exactly like how people text and chat on WhatsApp, e.g., 'Bhai yeh code dekho, mast chal raha hai'). "
            "Do NOT use Devanagari script; use Roman letters only. Blend Hindi and English seamlessly just like "
            "a modern tech YouTuber or developer explaining things on a live stream. Keep the energy high! "
            "Return only the final Roman Hinglish text.\n\n"
            f"Script:\n{state['script_text']}"
        )
        
        response: AIMessage = llm.invoke(prompt)
        return {"final_output": response.content.strip()}
        
    except Exception as err:
        raise Exception(f"Error in Roman Hinglish Translator Node & the error says: {err}")

# Now our state and nodes are ready its time to create the graph but before creating the graph
# We need the nodes to be connected and we can connect these nodes using edges
# Edges are very important for creating the workflows but it will be simple 
# Because we are using the sequential workflow and we know that how nodes will be connected 
# So lets create the edges now! lets go 

# Graph Construction & Orchestration
# Wire the nodes together into a deterministic, sequential pipeline:
# START ➔ Editor ➔ Scriptwriter ➔ Roman Hinglish Translator ➔ END

from langgraph.graph import StateGraph, START, END
from langgraph.graph.state import CompiledStateGraph
from langgraph.checkpoint.memory import InMemorySaver

# Creating the checkpointer and graph
checkpointer: InMemorySaver = InMemorySaver()
graph: StateGraph[PipelineState] = StateGraph(PipelineState)

# Adding the nodes in our graph 
graph.add_node("editor", editor_node)
graph.add_node("scriptwriter", scriptwriter_node)
graph.add_node("translator", translator_node)

# Adding the edges for our nodes in our graph (sequential - one after one)
graph.add_edge(START, "editor")
graph.add_edge("editor", "scriptwriter")
graph.add_edge("scriptwriter", "translator")
graph.add_edge("translator", END)

# Compiling the graph so we can actually execute it and send input and get an output
app: CompiledStateGraph[PipelineState] = graph.compile(checkpointer=checkpointer)

# Output

print("\nWelcome to our app!\nTransform your raw idea into an engaging Roman Hinglish video script.")
print("Enter you 'exit' if you want to quite!\n")

class PipelineInput(TypedDict):
    raw_input: str

# Creating Loop in which user can ask question again and again and exit if want 
while True:
    pipeline_input: str = input("\nYou: ")

    if pipeline_input.lower() == 'exit':
        print("\nQuiting the app, Thanks for using our app!\n")

    result: PipelineInput = app.invoke(
        {"raw_input": pipeline_input},
        config={
            "configurable": {
                "thread_id": 1 # Its a CLI base app thats why we are hard coding at a time there will be only one person
            }
        }
    )

    print(f"\nAgent: {result['final_output']}\n")
    

