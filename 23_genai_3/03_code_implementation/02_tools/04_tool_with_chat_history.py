from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain_core.tools import tool
from functools import lru_cache
from langchain_core.messages import AIMessage
from langchain_core.runnables import Runnable
from langchain_core.language_models import LanguageModelInput
from langchain_core.messages import BaseMessage
from rich import print

# Create a Custom Tool
@tool
@lru_cache
def get_text_length(text: str) -> int:
    """
    Return the number of characters in the given text.
    """
    return len(text)

# Creating LLM
llm: ChatGroq = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.5,
    max_tokens=500
)

# Binding LLM
llm_with_tools: Runnable[LanguageModelInput, BaseMessage] = llm.bind_tools([get_text_length])

