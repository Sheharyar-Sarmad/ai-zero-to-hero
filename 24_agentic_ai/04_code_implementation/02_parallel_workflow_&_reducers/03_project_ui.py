# This code is also generated from claude i paste the 02_project.py file and say that 
# Give me the streamlit ui file with rate limiting of 5 searches for 90 mins per IP
# And here's what it generated: 

import re
import time
import threading
from collections import defaultdict, deque
from typing import TypedDict, Annotated

import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langgraph.graph import StateGraph, START, END

load_dotenv()

# ---------------- Config ----------------
MAX_SEARCHES = 5
WINDOW_SECONDS = 90 * 60  # 90 minutes
MAX_CHARS = 5000

st.set_page_config(page_title="Safety Analyzer", page_icon="🛡️", layout="centered")


# ---------------- LangGraph backend ----------------
def merge_score_dicts(existing: dict, newupdate: dict) -> dict:
    if existing is None:
        return newupdate
    return {**existing, **newupdate}


class AnalyzerState(TypedDict):
    raw_text: str
    safety_score: Annotated[dict[str, int], merge_score_dicts]


@st.cache_resource
def get_graph():
    llm = ChatGroq(
        model="openai/gpt-oss-20b",
        max_tokens=1024,
        temperature=0.1,
    )

    def get_score(prompt: str) -> int:
        response = llm.invoke(prompt)
        match = re.search(r"\d+", str(response.content))
        if not match:
            return 0
        return max(0, min(100, int(match.group())))

    def toxicity_node(state: AnalyzerState) -> dict:
        prompt = (
            "Analyze the following text for profanity, aggression, hate speech, or toxicity. "
            "Provide a score from 0 to 100, where 0 means perfectly clean and 100 means highly toxic. "
            "Return ONLY the plain integer number, nothing else.\n\n"
            f"Text:\n{state['raw_text']}"
        )
        return {"safety_score": {"toxicity_level": get_score(prompt)}}

    def copyright_node(state: AnalyzerState) -> dict:
        prompt = (
            "Analyze the following text. Judge if it sounds heavily plagiarized, unoriginal, "
            "or presents a corporate trademark risk. Provide a score from 0 to 100, "
            "where 0 means entirely original and 100 means high risk. "
            "Return ONLY the plain integer number, nothing else.\n\n"
            f"Text:\n{state['raw_text']}"
        )
        return {"safety_score": {"copyright_risk": get_score(prompt)}}

    def culture_node(state: AnalyzerState) -> dict:
        prompt = (
            "Analyze the following text for regional sensitivities, political landmines, "
            "or cultural insensitivity that might offend a global audience. Provide a score from 0 to 100, "
            "where 0 means completely safe and 100 means highly offensive. "
            "Return ONLY the plain integer number, nothing else.\n\n"
            f"Text:\n{state['raw_text']}"
        )
        return {"safety_score": {"cultural_insensitivity": get_score(prompt)}}

    builder = StateGraph(AnalyzerState)
    builder.add_node("toxicity_node", toxicity_node)
    builder.add_node("copyright_node", copyright_node)
    builder.add_node("culture_node", culture_node)

    builder.add_edge(START, "toxicity_node")
    builder.add_edge(START, "copyright_node")
    builder.add_edge(START, "culture_node")

    builder.add_edge("toxicity_node", END)
    builder.add_edge("copyright_node", END)
    builder.add_edge("culture_node", END)

    return builder.compile()


def analyze_text(text: str) -> dict[str, int]:
    result = get_graph().invoke({"raw_text": text})
    scores = result["safety_score"]
    return {
        "toxicity_level": scores.get("toxicity_level", 0),
        "copyright_risk": scores.get("copyright_risk", 0),
        "cultural_insensitivity": scores.get("cultural_insensitivity", 0),
    }


# ---------------- Rate limiter ----------------
class RateLimiter:
    """Sliding-window limiter stored on the server, so refreshing the page
    does not reset the counter."""

    def __init__(self, max_calls: int, window: int):
        self.max_calls = max_calls
        self.window = window
        self.calls: dict[str, deque] = defaultdict(deque)
        self.lock = threading.Lock()

    def _prune(self, key: str, now: float):
        q = self.calls[key]
        while q and now - q[0] >= self.window:
            q.popleft()

    def status(self, key: str) -> tuple[int, float]:
        now = time.time()
        with self.lock:
            self._prune(key, now)
            q = self.calls[key]
            remaining = self.max_calls - len(q)
            wait = (q[0] + self.window - now) if q and remaining <= 0 else 0
            return remaining, max(0, wait)

    def try_acquire(self, key: str) -> bool:
        now = time.time()
        with self.lock:
            self._prune(key, now)
            if len(self.calls[key]) >= self.max_calls:
                return False
            self.calls[key].append(now)
            return True


@st.cache_resource
def get_limiter() -> RateLimiter:
    return RateLimiter(MAX_SEARCHES, WINDOW_SECONDS)


def get_client_id() -> str:
    try:
        headers = st.context.headers
        forwarded = headers.get("X-Forwarded-For")
        if forwarded:
            return forwarded.split(",")[0].strip()
        real_ip = headers.get("X-Real-Ip")
        if real_ip:
            return real_ip
    except Exception:
        pass
    # Local run / no proxy headers: treat everyone on this server as one client
    return "local-client"


def fmt_duration(seconds: float) -> str:
    seconds = int(seconds)
    h, rem = divmod(seconds, 3600)
    m, s = divmod(rem, 60)
    if h:
        return f"{h}h {m}m"
    if m:
        return f"{m}m {s}s"
    return f"{s}s"


def risk_label(score: int) -> str:
    if score < 30:
        return "🟢 Low"
    if score < 60:
        return "🟡 Medium"
    return "🔴 High"


# ---------------- UI ----------------
limiter = get_limiter()
client_id = get_client_id()

st.title("🛡️ Safety Analyzer")
st.caption("Analyze your text for toxicity, copyright risk, and cultural sensitivity.")

remaining, wait = limiter.status(client_id)

with st.sidebar:
    st.header("Usage")
    st.metric("Searches left", f"{remaining} / {MAX_SEARCHES}")
    st.progress(remaining / MAX_SEARCHES)
    if remaining <= 0:
        st.warning(f"Next search available in **{fmt_duration(wait)}**.")
    else:
        st.caption(f"Limit: {MAX_SEARCHES} searches per 90 minutes.")

text = st.text_area(
    "Enter your text",
    height=200,
    max_chars=MAX_CHARS,
    placeholder="Paste or type the text you want to analyze...",
)

analyze_clicked = st.button(
    "Analyze", type="primary", use_container_width=True, disabled=remaining <= 0
)

if remaining <= 0:
    st.error(
        f"Rate limit reached ({MAX_SEARCHES} searches per 90 minutes). "
        f"Please try again in {fmt_duration(wait)}."
    )

if analyze_clicked:
    if not text.strip():
        st.warning("Please enter some text first.")
    elif not limiter.try_acquire(client_id):
        st.error("Rate limit reached. Please try again later.")
    else:
        try:
            with st.spinner("Running 3 analyses in parallel..."):
                st.session_state.last_scores = analyze_text(text)
        except Exception as e:
            st.error(f"Analysis failed: {e}")
        else:
            st.rerun()  # refresh sidebar counter

# ---------------- Results ----------------
scores = st.session_state.get("last_scores")
if scores:
    st.subheader("Results")
    items = [
        ("Toxicity Level", scores["toxicity_level"]),
        ("Copyright Risk", scores["copyright_risk"]),
        ("Cultural Insensitivity", scores["cultural_insensitivity"]),
    ]
    cols = st.columns(3)
    for col, (name, value) in zip(cols, items):
        with col:
            st.metric(name, f"{value}/100")
            st.progress(value / 100)
            st.caption(risk_label(value))