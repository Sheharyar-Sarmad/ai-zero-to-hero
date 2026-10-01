# City Intelligence System, Streamlit version
#
# Run with:  streamlit run 05_autonomous_agent_ui.py
# Install:   pip install streamlit langchain langchain-groq langgraph tavily-python requests python-dotenv
#
# What changed compared to the command line version:
# 1. The input() based approval middleware cannot work in a web app, because a
#    web app cannot stop and wait on the terminal. It is replaced by the
#    built in HumanInTheLoopMiddleware, which pauses the agent (an interrupt)
#    and lets the UI resume it later with the user's decision.
# 2. A checkpointer stores the paused conversation, so the agent also remembers
#    earlier messages within the same conversation.
# 3. The agent is wrapped in Runnable chains (prepare input | agent | parse
#    output), so the UI only deals with plain strings and plain dictionaries.

from dotenv import load_dotenv
load_dotenv()

import os
import uuid
import logging
from typing import Any

import requests
import streamlit as st
from tavily import TavilyClient

from langchain_groq import ChatGroq
from langchain_core.tools import tool
from langchain_core.messages import AIMessage, HumanMessage, ToolMessage
from langchain_core.runnables import RunnableLambda
from langchain.agents import create_agent
from langchain.agents.middleware import HumanInTheLoopMiddleware
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.types import Command

logger = logging.getLogger(__name__)

# set_page_config must be the first Streamlit call in the script.
st.set_page_config(page_title="City Intelligence System", layout="centered")

# Stop early with a clear message if a required key is missing.
REQUIRED_KEYS = ["GROQ_API_KEY", "OPENWEATHER_API_KEY", "TAVILY_API_KEY"]
missing_keys = [k for k in REQUIRED_KEYS if not os.getenv(k)]
if missing_keys:
    st.error(f"Missing environment variables: {', '.join(missing_keys)}. Add them to your .env file.")
    st.stop()

# One shared Tavily client is reused by every news request.
tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))


# Tools
#
# The @tool decorator turns a function into a tool the LLM can call. The LLM
# reads the function name, type hints and docstring to decide when to call it.
# lru_cache is not used here on purpose. A Streamlit server runs for a long
# time, so a cache would keep returning old weather and old news.

@tool
def get_weather(city: str) -> str:
    """Get the current weather conditions for a specified city."""
    api_key = os.getenv("OPENWEATHER_API_KEY", "").strip().strip("'\"")
    clean_city = city.strip()

    try:
        # params lets requests URL-encode the city name safely.
        response = requests.get(
            "https://api.openweathermap.org/data/2.5/weather",
            params={"q": clean_city, "appid": api_key, "units": "metric"},
            timeout=10,
        )
        data: dict[str, Any] = response.json()

        # OpenWeather reports success with cod 200 and errors with another code.
        if str(data.get("cod")) != "200":
            return f"Error: {data.get('message', 'Could not fetch weather data.')}"

        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        desc = data["weather"][0]["description"]
        return f"Weather in {clean_city}: {desc.capitalize()}, {temp}°C, Humidity: {humidity}%"
    except Exception:
        # Generic message so the API key in the request URL can never leak.
        return "Error fetching weather: Unable to connect to OpenWeather service."


@tool
def get_news(city: str) -> str:
    """Get the latest news about a city."""
    try:
        response: dict[str, Any] = tavily_client.search(
            query=f"latest news in {city}",
            search_depth="basic",
            max_results=3,
        )
    except Exception:
        return "Error fetching news: Unable to connect to the news service."

    results: list[dict[str, Any]] = response.get("results", [])
    if not results:
        return f"No news found for {city}"

    news_list = []
    for r in results:
        title = r.get("title", "No title")
        url = r.get("url", "")
        snippet = r.get("content", "")
        news_list.append(f"- {title}\n  {url}\n  {snippet[:100]}...")

    return f"Latest news in {city}:\n\n" + "\n\n".join(news_list)


# Parsing helpers used inside the Runnable chains

def _message_text(content: Any) -> str:
    """Message content is a string for most models and a list of parts for some."""
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts = []
        for part in content:
            if isinstance(part, str):
                parts.append(part)
            elif isinstance(part, dict) and part.get("type") == "text":
                parts.append(part.get("text", ""))
        return "".join(parts)
    return str(content)


def parse_agent_output(result: dict[str, Any]) -> dict[str, Any]:
    """
    Convert the raw agent state into a simple dictionary for the UI:
      answer      final text answer (empty while the agent is paused)
      interrupts  tool calls waiting for human approval
      tools       tool calls made during the latest user turn, with results
    """
    # When the agent pauses for approval, invoke() returns the state plus an
    # "__interrupt__" entry. Each interrupt lists the actions to review.
    interrupts: list[dict[str, Any]] = []
    for item in result.get("__interrupt__", []) or []:
        value = getattr(item, "value", item)
        if isinstance(value, dict):
            interrupts.extend(value.get("action_requests", []))

    messages = result.get("messages", [])

    # Only look at messages after the latest human message (the current turn).
    last_human = max(
        (i for i, m in enumerate(messages) if isinstance(m, HumanMessage)),
        default=-1,
    )
    turn = messages[last_human + 1:]

    # Match each tool call with its result using the tool call id.
    tool_results = {m.tool_call_id: _message_text(m.content) for m in turn if isinstance(m, ToolMessage)}
    tools: list[dict[str, Any]] = []
    for m in turn:
        if isinstance(m, AIMessage):
            for call in m.tool_calls:
                tools.append({
                    "name": call["name"],
                    "args": call["args"],
                    "result": tool_results.get(call["id"], "Waiting for approval or not executed."),
                })

    answer = ""
    if not interrupts:
        for m in reversed(turn):
            if isinstance(m, AIMessage) and not m.tool_calls:
                answer = _message_text(m.content)
                break

    return {"answer": answer, "interrupts": interrupts, "tools": tools}


# Agent and Runnable chains
#
# st.cache_resource keeps one agent and one checkpointer alive across Streamlit
# reruns. Without it, every button click would rebuild the agent and lose the
# paused conversation.

@st.cache_resource(show_spinner=False)
def build_chains(require_approval: bool):
    llm = ChatGroq(model="openai/gpt-oss-120b", temperature=0.5, max_tokens=700)

    middleware = []
    if require_approval:
        # Pause before these tools run. Only approve and reject are allowed.
        policy = {"allowed_decisions": ["approve", "reject"]}
        middleware.append(
            HumanInTheLoopMiddleware(interrupt_on={"get_weather": policy, "get_news": policy})
        )

    # The compiled agent is itself a Runnable, so it can be piped into chains.
    # A checkpointer is required for interrupts and for conversation memory.
    agent = create_agent(
        model=llm,
        tools=[get_weather, get_news],
        system_prompt=(
            "You are a helpful assistant that provides weather and news information "
            "for cities. Use the tools provided to fetch the latest data."
        ),
        middleware=middleware,
        checkpointer=InMemorySaver(),
    )

    # Step 1 of the ask chain: plain user text becomes the agent input format.
    prepare_input = RunnableLambda(
        lambda text: {"messages": [{"role": "user", "content": text}]}
    )

    # Step 1 of the resume chain: a list of decisions becomes a resume command.
    prepare_resume = RunnableLambda(
        lambda decisions: Command(resume={"decisions": decisions})
    )

    # Last step of both chains: raw agent state becomes a simple dictionary.
    parse_output = RunnableLambda(parse_agent_output)

    # The pipe operator joins Runnables. The output of each step is the input
    # of the next one. Both chains share the same agent and the same thread.
    ask_chain = prepare_input | agent | parse_output
    resume_chain = prepare_resume | agent | parse_output
    return ask_chain, resume_chain


# Session state

def reset_conversation() -> None:
    """A new thread id gives the agent a fresh memory."""
    st.session_state.thread_id = str(uuid.uuid4())
    st.session_state.messages = []
    st.session_state.pending = None
    st.session_state.approval_round = 0


if "thread_id" not in st.session_state:
    reset_conversation()


# Sidebar

with st.sidebar:
    st.header("Settings")
    require_approval = st.checkbox("Require approval before tool calls", value=True)

    # Switching modes starts a new conversation, because each mode uses a
    # different agent.
    if st.session_state.get("last_mode") not in (None, require_approval):
        reset_conversation()
    st.session_state.last_mode = require_approval

    if st.button("New conversation", use_container_width=True):
        reset_conversation()
        st.rerun()

    st.caption(f"Thread: {st.session_state.thread_id[:8]}")
    st.caption("Ask about the weather or the latest news in any city.")

ask_chain, resume_chain = build_chains(require_approval)


# Running the chains

def run_chain(chain, payload: Any) -> None:
    # The thread id ties every call to the same stored conversation.
    config = {"configurable": {"thread_id": st.session_state.thread_id}}
    try:
        with st.spinner("The agent is working..."):
            result = chain.invoke(payload, config=config)
    except Exception as exc:
        # Log details on the server, show only the error type to the user.
        logger.exception("Agent run failed")
        st.session_state.pending = None
        st.session_state.messages.append({
            "role": "assistant",
            "content": f"The agent hit an error ({type(exc).__name__}). Try again, or start a new conversation.",
            "tools": [],
        })
        return

    if result["interrupts"]:
        # The agent is paused. Store the requests and ask the user.
        st.session_state.pending = result["interrupts"]
        st.session_state.approval_round += 1
    else:
        st.session_state.pending = None
        st.session_state.messages.append({
            "role": "assistant",
            "content": result["answer"] or "No response was produced.",
            "tools": result["tools"],
        })


# Rendering

def render_tools(tools: list[dict[str, Any]]) -> None:
    if not tools:
        return
    with st.expander(f"Tool calls ({len(tools)})"):
        for t in tools:
            st.markdown(f"**{t['name']}**")
            st.json(t["args"])
            st.text(t["result"])


def render_approval(pending: list[dict[str, Any]]) -> None:
    st.warning("The agent wants to run the following tool call(s). Review and decide.")
    round_id = st.session_state.approval_round

    # A form groups all decisions so they are submitted together, in the same
    # order as the actions. Keys include the round id so old widget values from
    # a previous approval are never reused.
    with st.form(f"approval_form_{round_id}"):
        choices = []
        for i, action in enumerate(pending):
            st.markdown(f"**{action.get('name', 'unknown tool')}**")
            st.json(action.get("args", {}))
            decision = st.radio(
                "Decision", ["Approve", "Reject"],
                key=f"decision_{round_id}_{i}", horizontal=True,
            )
            reason = st.text_input(
                "Reason (used only when rejecting)", key=f"reason_{round_id}_{i}",
            )
            choices.append((decision, reason))
        submitted = st.form_submit_button("Submit decision")

    if submitted:
        decisions = []
        for decision, reason in choices:
            if decision == "Approve":
                decisions.append({"type": "approve"})
            else:
                decisions.append({
                    "type": "reject",
                    "message": reason.strip() or "The user denied this tool call.",
                })
        st.session_state.pending = None
        run_chain(resume_chain, decisions)
        st.rerun()


# Main page

st.title("City Intelligence System")

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        render_tools(msg.get("tools", []))

pending = st.session_state.pending
if pending:
    render_approval(pending)

# New questions are blocked while an approval is waiting, because the paused
# conversation must be resumed first.
prompt = st.chat_input("Ask about a city", disabled=bool(pending))
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt, "tools": []})
    with st.chat_message("user"):
        st.markdown(prompt)
    run_chain(ask_chain, prompt)
    st.rerun()