# LangChain Built-in Tools - Tavily News Summarizer

# This is a great example of how LangChain built-in tools work.
#
# Tavily acts as a search tool that allows the application to
# retrieve current information from the web.
#
# Flow:
#
# User Query
#     ↓
# Tavily Search Tool
#     ↓
# Search Results
#     ↓
# Chat Prompt
#     ↓
# Groq LLM
#     ↓
# StrOutputParser
#     ↓
# News Summary

# Load environment variables from .env
from dotenv import load_dotenv
load_dotenv()

# Tavily provides web search capabilities to the application.
# Tavily API key should be stored in .env:
# TAVILY_API_KEY=your_tavily_api_key

from langchain_tavily import TavilySearch

# LangChain components used to build the LLM pipeline.
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import Runnable

# Groq LLM integration.
from langchain_groq import ChatGroq

# Initialize the Tavily Search Tool

# This is the built-in/external tool that retrieves current
# information from the web.

# max_results=5 means Tavily will return up to 5 search results.

search_tool: TavilySearch = TavilySearch(
    max_results=5
)

# Initialize the LLM

# Groq is used as the language model that will summarize the
# information returned by the Tavily search tool.

llm: ChatGroq = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=1,
    max_tokens=1000
)

# Create the Prompt Template

# The search results will be inserted into the {news} variable.

prompt: ChatPromptTemplate = ChatPromptTemplate.from_template(
    """
You are a helpful news summarization assistant.

Summarize the following search results into concise bullet points.
Do not invent facts. If information is uncertain or conflicting,
clearly indicate that.

News:
{news}
"""
)

# Build the LangChain Chain

# The pipeline is:

# Prompt → LLM → String Output Parser

chain: Runnable = prompt | llm | StrOutputParser()

# Execute the Tavily Search Tool

# Tavily searches the web for current information.
news_result: list[dict[str, str]] = search_tool.run(
    "Latest 2027 upcoming news!"
)

# Send Search Results to the LLM Chain

# The Tavily search results are passed to the {news} variable
# in the prompt.
result: str = chain.invoke(
    {"news": news_result}
)

# Display the Final Summary
print(result)
