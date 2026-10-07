import os 
from typing import TypedDict, Annotated, Literal, Any
from langchain_groq import ChatGroq
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode
from langchain_tavily import TavilySearch
from langchain_core.runnables import Runnable
from langchain_core.messages import BaseMessage, AIMessage
from functools import lru_cache
from dotenv import load_dotenv

load_dotenv()

# Tools

search_tool: TavilySearch = TavilySearch(max_results=3)

tools: list[Any] = [search_tool]

# LLM's

# writer
writer_llm: ChatGroq = ChatGroq(
    model="openai/gpt-oss-120b",
    max_tokens=2048,
    temperature=0.8
)

writer_llm_with_tools: Runnable = writer_llm.bind_tools(tools)

# reviewer
reviewer_llm: ChatGroq = ChatGroq(
    model="openai/gpt-oss-20b",
    max_tokens=1024,
    temperature=0.3
)

# Building State

class State(TypedDict):
    topic: str 
    messages: Annotated[list[BaseMessage], add_messages]
    draft: str 
    review_feedback: str 
    is_approved: bool 
    attempts: int 

# Building Nodes 

WRITER_SYSTEM_PROMPT: str = (
    "You are an expert LinkedIn content writer. Your job is to write "
    "engaging, professional LinkedIn posts about the given topic. "
    "If the topic requires up-to-date information, statistics, or "
    "current trends, use the web search tool to gather fresh context "
    "before writing. If you have already received feedback on a "
    "previous draft, carefully address every point in the new draft. "
    "Rules for good LinkedIn posts: strong hook in the first line, "
    "1 clear takeaway, easy to skim (short paragraphs), around "
    "150–200 words, ends with a question or call-to-action to invite "
    "engagement. Do not use hashtags."
)

def writer_node(state: State) -> dict: 
    """Writes (or rewrites) the LinkedIn post. Can call Tavily to search first."""
    try:
        attempt: int = state("attempt", 0) + 1
        topic: str = state['topic']
        previous_feedback: str = state['review_feedback'][-1]

        if topic == 1: 
            user_message: str = (
                f"Write a Linkedin post on this topic: {topic}"
                f"If you need current info search the web first!"
            )
        else: 
            user_message = (
                f"your previous draft on '{topic}' was rejected"
                f"Here is the reviewer's feedback \n\n {previous_feedback}\n\n"
                f"Write a new, improved draft that fixes every issue mentiond"
                f"do not repeat the same mistake"
            )

        messages: list[tuple[str,str], tuple[str, str]] = [
            ("system", WRITER_SYSTEM_PROMPT),
            ("human", user_message)
        ]

        response: AIMessage = writer_llm_with_tools.invoke(messages)

        return {
            "messages": [("human", user_message), response],
            "attempt": attempt
        }

    except Exception as err:
        raise Exception(f"Error coming in writer node due to: {err}")

tool_node: ToolNode = ToolNode(tools)

def extract_draft_node(state: State) -> dict:
    try:
        last_message: str = state['messages'][-1].content
    except Exception as err:
        raise Exception(f"Error coming in extracting draft node due to: {err}")