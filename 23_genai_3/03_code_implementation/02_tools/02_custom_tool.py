# Custom LangChain Tool with Caching
#
# This example demonstrates how to:
# 1. Create a custom LangChain tool using @tool
# 2. Use Python's @lru_cache for caching
# 3. Add type hints to the tool
# 4. Provide a docstring for the tool description
# 5. Invoke the tool using LangChain's .invoke() interface
# 6. Inspect the tool's metadata
#
# This is different from TavilySearch:
#
# TavilySearch = pre-built/external tool
# get_greeting = custom tool created by us

# Used for caching repeated function calls and improving performance.
from functools import lru_cache

# @tool converts a normal Python function into a LangChain tool.
from langchain.tools import tool

# Create a Custom LangChain Tool
@tool
@lru_cache
def get_greeting(name: str) -> str:
    """
    Generate the greeting message for a user.
    """

    return f"Hello {name}, Welcome to an AI world"

# Invoke the Tool
#
# .invoke() is the standard LangChain interface for executing
# a tool.
#
# The tool expects an input dictionary whose key matches the
# function parameter: "name".
#
# Input:
# {"name": "Sheharyar"}
#
# Output:
# "Hello Sheharyar, Welcome to an AI world"
#
result: str = get_greeting.invoke(
    {"name": "Sheharyar"}
)

print(result)

# Inspect Tool Metadata

# The name assigned to the LangChain tool.
print(get_greeting.name)

# The tool description.
#
# LangChain uses the function's docstring as the description.
# This description is especially important when an LLM/agent
# needs to decide which tool to use.
print(get_greeting.description)

# The input argument schema generated from the function's
# type hints.
#
# Because our function has:
#
# name: str
#
# LangChain knows that "name" is a required string argument.
print(get_greeting.args)
