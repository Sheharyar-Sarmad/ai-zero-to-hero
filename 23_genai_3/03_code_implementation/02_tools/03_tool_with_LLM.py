# LangChain Tool Calling - Custom Tool
#
# This example demonstrates:
#
# 1. Creating a custom LangChain tool with @tool
# 2. Using @lru_cache for caching
# 3. Providing type hints for tool inputs and outputs
# 4. Initializing a ChatGroq LLM
# 5. Binding a custom tool to the LLM
# 6. Invoking the LLM and receiving an AIMessage

# Load environment variables from the .env file.
from dotenv import load_dotenv
load_dotenv()

# Groq chat model integration.
from langchain_groq import ChatGroq

# LangChain's @tool decorator for creating custom tools.
from langchain_core.tools import tool

# Python's built-in LRU cache for caching repeated function calls.
from functools import lru_cache

# AIMessage is the type returned by llm.invoke().
from langchain_core.messages import AIMessage

# Rich provides better formatted terminal output.
from rich import print

# Create a Custom Tool
@tool
@lru_cache
def get_text_length(text: str) -> int:
    """
    Return the number of characters in the given text.
    """

    return len(text)

# Initialize the Groq LLM
llm: ChatGroq = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.6,
    max_tokens=500
)

# Bind the Tool to the LLM
#
# bind_tools() makes the custom tool available to the LLM.
#
# It does NOT execute get_text_length().
#
# Instead, the model receives information about:
#
# - Tool name
# - Tool description
# - Tool input schema
#
# The model can then decide whether it wants to request
# a tool call.
#
llm_with_tool: ChatGroq = llm.bind_tools(
    [get_text_length]
)

# Invoke the LLM
#
# llm.invoke() returns an AIMessage.
#
# Therefore, the correct type hint is:

result: AIMessage = llm.invoke(
    "How many characters are in the text: Hello my name is Sheharyar?"
)

result_with_tool: AIMessage = llm_with_tool.invoke(
    "How many characters are in the text: Hello my name is Sheharyar?"
)

# Print the AI Response
print(f"{result}\n\n\n{result_with_tool}")
