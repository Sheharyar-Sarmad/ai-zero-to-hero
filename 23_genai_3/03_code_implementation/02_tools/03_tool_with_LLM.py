# Import load_dotenv to load environment variables from a .env file.
# This is typically used to load your GROQ_API_KEY securely.
from dotenv import load_dotenv
load_dotenv()

# Import the ChatGroq class to interact with Groq's language models.
from langchain_groq import ChatGroq

# Import the tool decorator. This tells LangChain that a Python function
# can be used as a tool by the AI.
from langchain_core.tools import tool

# Import lru_cache from functools.
# This caches the results of function calls. If the AI asks for the length
# of the exact same sentence twice, Python returns the saved answer instantly.
from functools import lru_cache

# Import AIMessage. This is the specific type of object the AI returns
# when it replies to a prompt.
from langchain_core.messages import AIMessage

# Import print from the rich library for cleaner, colorized terminal output.
from rich import print

# Define the custom tool using the @tool decorator.
# The AI reads the function name, the type hints (text: str), and the docstring
# to understand exactly what this tool does and when to use it.
@tool
@lru_cache
def get_text_length(text: str) -> int:
    """
    Return the number of characters in the given text.
    """
    return len(text)

# Initialize the language model using ChatGroq.
# We set the model name, a temperature of 0.6 (slightly creative but focused),
# and a maximum token limit for the response.
llm: ChatGroq = ChatGroq(
    model="llama3-70b-8192", 
    temperature=0.6,
    max_tokens=500
)

# Bind the custom tool to the language model.
# The bind_tools method passes the tool's description to the AI.
# It does not run the tool. It just gives the AI the instruction manual for it.
# If the AI thinks it needs the tool, it will reply with a tool call request.
llm_with_tool = llm.bind_tools(
    [get_text_length]
)

# Ask the standard, tool-less LLM to count the characters.
# The AI will try to guess or calculate this internally, which LLMs are bad at.
result: AIMessage = llm.invoke(
    "How many characters are in the text: Hello my name is Sheharyar?"
)

# Ask the tool-equipped LLM the exact same question.
# Because it knows the get_text_length tool exists, it will realize it should
# use the tool instead of guessing. It will return a tool_calls request.
result_with_tool: AIMessage = llm_with_tool.invoke(
    "How many characters are in the text: Hello my name is Sheharyar?"
)

# Print both results to compare them.
# The first will be a standard text response.
# The second will contain a tool_calls list showing the AI's request to use the tool.
print(f"Result WITHOUT tool:\n{result}\n\n\nResult WITH tool:\n{result_with_tool}")