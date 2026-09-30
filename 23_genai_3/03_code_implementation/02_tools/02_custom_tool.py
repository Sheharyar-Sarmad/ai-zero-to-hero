# Import lru_cache for performance optimization (caches function results)
from functools import lru_cache

# Import the tool decorator to convert Python functions into AI-usable tools
from langchain.tools import tool

# Create a Custom Tool
# The @tool decorator makes this function recognizable by LangChain.
# The @lru_cache ensures that if the same name is passed twice, it doesn't recalculate.
# The docstring is read by the AI so it knows what this tool does and when to use it.
@tool
@lru_cache
def get_greeting(name: str) -> str:
    """
    Generate the greeting message for a user.
    """
    return f"Hello {name}, Welcome to an AI world"

# Invoke the Tool
# .invoke() is the standard LangChain interface for executing a tool manually.
# The tool expects an input dictionary whose keys match the function parameters.
result: str = get_greeting.invoke(
    {"name": "Sheharyar"}
)

# Print the string returned by the tool execution
print(result)

# Inspect Tool Metadata
# Print the name automatically assigned to the LangChain tool (usually the function name)
print(get_greeting.name)

# Print the tool description.
# LangChain extracts this directly from the function's docstring.
# This description is critical because LLMs read it to decide which tool to trigger.
print(get_greeting.description)

# Print the input argument schema generated from the function's type hints.
# LangChain uses the type hints (name: str) to know exactly what data type to enforce.
print(get_greeting.args)