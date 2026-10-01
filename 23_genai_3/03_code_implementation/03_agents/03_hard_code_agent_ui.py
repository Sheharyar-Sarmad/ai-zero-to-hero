"""
Streamlit UI for the City Intelligence agent.

- Tools (get_weather, get_news), the LLM and the tool registry are imported from
  02_hard_code_agent.py (nothing is hard coded here).
- Rate limiting applies ONLY to the Tavily news search (get_news):
    * per IP   : PER_IP_MAX searches per PER_IP_WINDOW seconds
    * global   : GLOBAL_MAX searches per GLOBAL_WINDOW seconds (protects the Tavily quota)
- get_weather (OpenWeather) is not rate limited.

Run:  streamlit run 03_agents/03_hard_code_agent_ui.py
"""
import importlib.util
import threading
import time
from collections import defaultdict, deque
from pathlib import Path
from typing import Any

import streamlit as st
from langchain_core.messages import (
    AIMessage,
    BaseMessage,
    HumanMessage,
    ToolMessage,
)

# ----------------------------------------------------------------------------
# Config
# ----------------------------------------------------------------------------
AGENT_FILE = "02_hard_code_agent.py"          # CLI file that defines the tools
RATE_LIMITED_TOOLS = {"get_news"}             # only Tavily-backed tools are limited

PER_IP_MAX = 3                                # searches per IP ...
PER_IP_WINDOW = 90 * 60                       # ... per 1.5 hours

GLOBAL_MAX = 50                               # searches for ALL users combined ...
GLOBAL_WINDOW = 60 * 60                       # ... per hour (Tavily budget, 50-60)

MAX_AGENT_STEPS = 5                           # safety cap for the ReAct loop

st.set_page_config(page_title="City Intelligence System", page_icon="🌆", layout="centered")


# ----------------------------------------------------------------------------
# Import the tools from the CLI file (name starts with a digit, so a normal
# import is not possible -> load it by file path).
# ----------------------------------------------------------------------------
@st.cache_resource
def load_agent_module():
    path = Path(__file__).parent / AGENT_FILE
    spec = importlib.util.spec_from_file_location("hard_code_agent", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)  # CLI loop is guarded by __main__, so it won't run
    return module


agent = load_agent_module()
llm_with_tools = agent.llm_with_tools   # LLM with get_weather + get_news bound
tools: dict[str, Any] = agent.tools     # {"get_weather": ..., "get_news": ...}


# ----------------------------------------------------------------------------
# Rate limiter: per-IP window + global window (sliding windows, in memory)
# ----------------------------------------------------------------------------
class SearchRateLimiter:
    def __init__(self, ip_max: int, ip_window: int, global_max: int, global_window: int):
        self.ip_max = ip_max
        self.ip_window = ip_window
        self.global_max = global_max
        self.global_window = global_window
        self._ip_hits: dict[str, deque] = defaultdict(deque)
        self._global_hits: deque = deque()
        self._lock = threading.Lock()

    @staticmethod
    def _prune(q: deque, now: float, window: int) -> None:
        while q and now - q[0] >= window:
            q.popleft()

    def try_acquire(self, ip: str) -> tuple[bool, int, str]:
        """Consume one search. Returns (allowed, retry_after_seconds, blocked_by)."""
        now = time.time()
        with self._lock:
            ip_q = self._ip_hits[ip]
            self._prune(ip_q, now, self.ip_window)
            self._prune(self._global_hits, now, self.global_window)

            if len(ip_q) >= self.ip_max:
                return False, int(self.ip_window - (now - ip_q[0])) + 1, "ip"
            if len(self._global_hits) >= self.global_max:
                return False, int(self.global_window - (now - self._global_hits[0])) + 1, "global"

            ip_q.append(now)
            self._global_hits.append(now)
            return True, 0, ""

    def status(self, ip: str) -> tuple[int, int, int]:
        """Returns (used, remaining, seconds_until_oldest_expires) for this IP."""
        now = time.time()
        with self._lock:
            q = self._ip_hits[ip]
            self._prune(q, now, self.ip_window)
            used = len(q)
            reset_in = int(self.ip_window - (now - q[0])) + 1 if q else 0
            return used, self.ip_max - used, reset_in


@st.cache_resource
def get_limiter() -> SearchRateLimiter:
    # cache_resource => one limiter for the whole server process (all sessions/tabs)
    return SearchRateLimiter(PER_IP_MAX, PER_IP_WINDOW, GLOBAL_MAX, GLOBAL_WINDOW)


limiter = get_limiter()


def get_client_ip() -> str:
    """Best-effort client IP (works behind proxies/Streamlit Cloud too)."""
    try:
        headers = st.context.headers
        forwarded = headers.get("X-Forwarded-For")
        if forwarded:
            return forwarded.split(",")[0].strip()
        real_ip = headers.get("X-Real-Ip")
        if real_ip:
            return real_ip.strip()
    except Exception:
        pass
    try:
        ip = st.context.ip_address  # Streamlit >= 1.45
        if ip:
            return ip
    except Exception:
        pass
    return "local"


def fmt_duration(seconds: int) -> str:
    m, s = divmod(max(seconds, 0), 60)
    h, m = divmod(m, 60)
    if h:
        return f"{h}h {m}m"
    if m:
        return f"{m}m {s}s"
    return f"{s}s"


client_ip = get_client_ip()


# ----------------------------------------------------------------------------
# Session state
# ----------------------------------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages: list[BaseMessage] = []


# ----------------------------------------------------------------------------
# Sidebar: quota
# ----------------------------------------------------------------------------
st.sidebar.header("Usage limit")
quota_box = st.sidebar.empty()


def render_quota():
    used, remaining, reset_in = limiter.status(client_ip)
    with quota_box.container():
        st.progress(used / PER_IP_MAX, text=f"{used} / {PER_IP_MAX} news searches used")
        if remaining > 0:
            st.caption(f"{remaining} news search(es) left in this 1.5 hour window.")
        else:
            st.warning(f"News limit reached. Next search available in {fmt_duration(reset_in)}.")
        st.caption("Weather lookups are not limited.")
        st.caption(f"Your IP: `{client_ip}`")


render_quota()

if st.sidebar.button("🗑️ Clear chat"):
    st.session_state.messages = []
    st.rerun()


# ----------------------------------------------------------------------------
# Header + chat history
# ----------------------------------------------------------------------------
st.title("🌆 City Intelligence System")
st.caption("Ask about the weather or the latest news in any city.")

for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.markdown(msg.content)
    elif isinstance(msg, AIMessage) and msg.content and not msg.tool_calls:
        with st.chat_message("assistant"):
            st.markdown(msg.content)


# ----------------------------------------------------------------------------
# Agent loop (ReAct style, same logic as the CLI version)
# ----------------------------------------------------------------------------
def run_agent(user_input: str) -> None:
    messages: list[BaseMessage] = st.session_state.messages
    messages.append(HumanMessage(user_input))

    with st.chat_message("assistant"):
        status = st.status("Thinking...", expanded=False)
        final_answer = ""

        for _ in range(MAX_AGENT_STEPS):
            result: AIMessage = llm_with_tools.invoke(messages)
            messages.append(result)

            if not result.tool_calls:
                final_answer = result.content
                break

            for tool_call in result.tool_calls:
                tool_name: str = tool_call["name"]
                tool_args: dict[str, Any] = tool_call["args"]

                if tool_name not in tools:
                    tool_result = f"Error: unknown tool '{tool_name}'."
                else:
                    blocked = False
                    if tool_name in RATE_LIMITED_TOOLS:
                        allowed, retry_after, blocked_by = limiter.try_acquire(client_ip)
                        if not allowed:
                            blocked = True
                            if blocked_by == "ip":
                                tool_result = (
                                    f"Rate limit exceeded: this user can only run {PER_IP_MAX} news "
                                    f"searches every 1.5 hours. Try again in {fmt_duration(retry_after)}. "
                                    "Tell the user this politely and do not call the tool again."
                                )
                            else:
                                tool_result = (
                                    "The news search service is busy right now (too many requests "
                                    f"from all users). Try again in {fmt_duration(retry_after)}. "
                                    "Tell the user this politely and do not call the tool again."
                                )
                            status.write(f"⛔ `{tool_name}` blocked by rate limit")

                    if not blocked:
                        status.update(label=f"Running {tool_name}...", state="running")
                        status.write(f"🔧 `{tool_name}` with `{tool_args}`")
                        try:
                            tool_result = str(tools[tool_name].invoke(tool_args))
                        except Exception as e:
                            tool_result = f"Error while running {tool_name}: {type(e).__name__}"

                messages.append(ToolMessage(content=tool_result, tool_call_id=tool_call["id"]))
                render_quota()
        else:
            final_answer = "Sorry, I couldn't finish that request. Please try rephrasing it."

        status.update(label="Done", state="complete")
        st.markdown(final_answer)


# ----------------------------------------------------------------------------
# Chat input
# ----------------------------------------------------------------------------
if prompt := st.chat_input("e.g. What's the weather and news in Lahore?"):
    with st.chat_message("user"):
        st.markdown(prompt)
    run_agent(prompt)
    render_quota()