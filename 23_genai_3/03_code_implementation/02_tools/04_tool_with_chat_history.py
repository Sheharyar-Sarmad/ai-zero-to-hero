# Import load_dotenv to read environment variables from a .env file (like API keys)
from dotenv import load_dotenv
load_dotenv()

# Import the Groq chat model wrapper from LangChain
from langchain_groq import ChatGroq

# Import the tool decorator to convert Python functions into AI-usable tools
from langchain_core.tools import tool

# Import lru_cache for performance optimization (caches function results)
from functools import lru_cache

# Import LangChain message types to structure the conversation history
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage, ToolMessage

# Import types for type hinting
from langchain_core.runnables import Runnable
from langchain_core.language_models import LanguageModelInput
from typing import Callable, Any

# Import rich for formatted terminal printing
from rich import print

# Create a Custom Tool
# The @tool decorator makes this function recognizable by LangChain.
# The @lru_cache ensures that if the same text is passed twice, it doesn't recalculate.
# The docstring ("Return the number...") is read by the AI so it knows when to use the tool.
@tool
@lru_cache
def get_text_length(text: str) -> int:
    """
    Return the number of characters in the given text.
    """
    return len(text)

# Store the tool in a dictionary so we can look it up by its string name later
tools: dict[str, Any] = {
    "get_text_length": get_text_length
}

# Initialize the Groq language model
# temperature=0.5 makes the AI moderately creative but still focused
llm: ChatGroq = ChatGroq(
    model="llama3-70b-8192", # Replaced with a standard Groq model name for compatibility
    temperature=0.5,
    max_tokens=500
)

# Bind the tool to the LLM
# This step gives the LLM the instructions and schema for get_text_length
llm_with_tools: Runnable[LanguageModelInput, BaseMessage] = llm.bind_tools([get_text_length])

# Create an empty list to store the sequence of the conversation
messages: list[BaseMessage] = []

# Ask the user for input. Note: input() returns a string (str).
prompt: str = input("\nYou: ")

# Wrap the user's input in a HumanMessage object and add it to the conversation history
query: HumanMessage = HumanMessage(content=prompt)
messages.append(query)

# Send the conversation history to the AI
# At this point, the AI will decide if it needs to use the tool or answer directly
result: AIMessage = llm_with_tools.invoke(messages)

# Add the AI's initial response (which might be a tool call request) to the history
messages.append(result)

# Check if the AI decided it needs to use a tool
if result.tool_calls:
    
    # Print the tool call request for debugging purposes
    print("AI requested a tool call:", result.tool_calls[0])
    
    # Extract the name of the tool the AI wants to use
    tool_call = result.tool_calls[0]
    tool_name: str = tool_call["name"]
    
    # Extract the arguments the AI provided for the tool (e.g., the text to measure)
    tool_args: dict = tool_call["args"]
    
    # Look up the tool in our dictionary and run it with the arguments provided by the AI
    tool_output: Any = tools[tool_name].invoke(tool_args)
    
    # Wrap the raw output from the Python function into a ToolMessage
    # We must include the tool_call_id so the AI knows which request this answer belongs to
    tool_message: ToolMessage = ToolMessage(
        content=str(tool_output),
        tool_call_id=tool_call["id"]
    )
    
    # Add the tool's result back to the conversation history
    messages.append(tool_message)
    
    # Send the updated history back to the AI
    # Now the AI has the result of the tool and can formulate a final answer
    result = llm_with_tools.invoke(messages)

# Print the final natural language answer provided by the AI
print(f"\nAI final response: {result.content}\n")