# Same for all the time its a claude generated file from 
# 02_project.py file 

import hashlib
import importlib.util
import json
import threading
import uuid
from datetime import datetime, timezone
from pathlib import Path

import streamlit as st

# Config
DAILY_LIMIT_PER_IP: int = 3
MAX_TOPIC_CHARS: int = 300
USAGE_FILE: Path = Path(__file__).parent / "usage_log.json"
BACKEND_FILE: Path = Path(__file__).parent / "02_project.py"

st.set_page_config(page_title="LinkedIn Post Generator", page_icon="✍️", layout="centered")


# Backend loader
# 02_project.py starts with a digit, so it can't be imported with a normal
# `import` statement. Load it by file path and cache it so the graph and the
# shared Groq rate limiter are created only once per server process.
@st.cache_resource(show_spinner=False)
def load_backend():
    spec = importlib.util.spec_from_file_location("linkedin_backend", BACKEND_FILE)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


# Per-IP daily usage tracker
class UsageTracker:
    """Thread-safe, file-backed counter: N generations per IP per UTC day."""

    def __init__(self, path: Path, limit: int):
        self.path = path
        self.limit = limit
        self._lock = threading.Lock()
        self._data: dict = {"date": self._today(), "counts": {}}
        self._load()

    @staticmethod
    def _today() -> str:
        return datetime.now(timezone.utc).strftime("%Y-%m-%d")

    @staticmethod
    def _key(ip: str) -> str:
        return hashlib.sha256(ip.encode()).hexdigest()[:16]

    def _load(self) -> None:
        try:
            if self.path.exists():
                saved = json.loads(self.path.read_text())
                if saved.get("date") == self._today():
                    self._data = saved
        except Exception:
            pass

    def _save(self) -> None:
        try:
            self.path.write_text(json.dumps(self._data))
        except Exception:
            pass

    def _roll_day(self) -> None:
        today = self._today()
        if self._data.get("date") != today:
            self._data = {"date": today, "counts": {}}

    def used(self, ip: str) -> int:
        with self._lock:
            self._roll_day()
            return self._data["counts"].get(self._key(ip), 0)

    def remaining(self, ip: str) -> int:
        return max(0, self.limit - self.used(ip))

    def try_consume(self, ip: str) -> bool:
        """Atomically reserve one generation. Returns False if the limit is hit."""
        with self._lock:
            self._roll_day()
            key = self._key(ip)
            count = self._data["counts"].get(key, 0)
            if count >= self.limit:
                return False
            self._data["counts"][key] = count + 1
            self._save()
            return True

    def refund(self, ip: str) -> None:
        """Give the slot back if the run crashed before producing a post."""
        with self._lock:
            self._roll_day()
            key = self._key(ip)
            count = self._data["counts"].get(key, 0)
            if count > 0:
                self._data["counts"][key] = count - 1
                self._save()


@st.cache_resource(show_spinner=False)
def get_tracker() -> UsageTracker:
    return UsageTracker(USAGE_FILE, DAILY_LIMIT_PER_IP)


def get_client_ip() -> str:
    """Best-effort client IP. Falls back to 'local' when running on localhost."""
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
        ip = st.context.ip_address
        if ip:
            return ip
    except Exception:
        pass
    return "local"


# Workflow runner
NODE_LABELS = {
    "writer": "✍️ Writer is drafting",
    "tools": "🔎 Searching the web (Tavily)",
    "extract_draft": "📄 Extracting draft",
    "content_reviewer": "🧐 Content review",
    "compliance_reviewer": "✅ Compliance review",
    "aggregate_reviews": "⚖️ Aggregating reviews",
}


def run_workflow(graph, topic: str) -> dict:
    config = {
        "configurable": {"thread_id": str(uuid.uuid4())},
        "recursion_limit": 25,
    }
    initial_state = {
        "topic": topic,
        "messages": [],
        "draft": "",
        "content_feedback": "",
        "compliance_feedback": "",
        "review_feedback": "",
        "content_approved": False,
        "compliance_approved": False,
        "is_approved": False,
        "attempts": 0,
        "tool_calls_used": 0,
    }

    with st.status("Running the agent...", expanded=True) as status:
        for output in graph.stream(initial_state, config=config):
            for node_name in output.keys():
                st.write(NODE_LABELS.get(node_name, node_name))
        status.update(label="Workflow finished", state="complete", expanded=False)

    return graph.get_state(config).values


# UI
st.title("✍️ LinkedIn Post Generator")
st.caption(
    "A writer agent drafts your post (with one optional web search), then two "
    "reviewers check it. It rewrites up to 3 times until approved."
)

backend = load_backend()
tracker = get_tracker()
client_ip = get_client_ip()
remaining = tracker.remaining(client_ip)

with st.sidebar:
    st.header("Usage")
    st.metric("Posts left today", f"{remaining} / {DAILY_LIMIT_PER_IP}")
    st.progress((DAILY_LIMIT_PER_IP - remaining) / DAILY_LIMIT_PER_IP)
    st.caption("Limit resets daily at 00:00 UTC.")
    st.divider()
    st.caption(
        f"Max attempts: {backend.MAX_ATTEMPTS}  \n"
        f"Max Tavily searches: {backend.MAX_TOOL_CALLS}  \n"
        "Groq calls are rate-limited (~24 requests/min)."
    )

topic = st.text_area(
    "Post topic",
    placeholder="e.g. Why vanilla JS still wins for fast landing pages",
    max_chars=MAX_TOPIC_CHARS,
    height=100,
)

generate = st.button(
    "Generate post",
    type="primary",
    disabled=(remaining == 0),
    use_container_width=True,
)

if remaining == 0:
    st.error(
        f"Daily limit reached: {DAILY_LIMIT_PER_IP} posts per day per user. "
        "Please come back tomorrow."
    )

if generate:
    clean_topic = topic.strip()

    if not clean_topic:
        st.warning("Please enter a topic first.")
    elif not tracker.try_consume(client_ip):
        st.error("Daily limit reached. Please come back tomorrow.")
    else:
        try:
            st.session_state["result"] = run_workflow(backend.app, clean_topic)
        except Exception as err:
            tracker.refund(client_ip)  # don't charge the user for a crashed run
            st.session_state.pop("result", None)
            st.error(f"Something went wrong while generating the post: {err}")
        else:
            st.rerun()

result = st.session_state.get("result")

if result:
    st.divider()

    if result.get("is_approved"):
        st.success("Approved by both reviewers.")
    else:
        st.warning(
            "Reached the attempt limit without full approval. "
            "Showing the latest draft."
        )

    st.subheader("Final LinkedIn Post")
    draft = result.get("draft") or "No draft generated."
    st.text_area("Draft", value=draft, height=320, label_visibility="collapsed")
    st.code(draft, language=None)  # built-in copy button

    col1, col2, col3 = st.columns(3)
    col1.metric("Attempts used", f"{result.get('attempts', 0)} / {backend.MAX_ATTEMPTS}")
    col2.metric("Web searches", f"{result.get('tool_calls_used', 0)} / {backend.MAX_TOOL_CALLS}")
    col3.metric("Words", len(draft.split()))

    with st.expander("Reviewer feedback"):
        st.markdown(f"**Content:** {result.get('content_feedback', '-')}")
        st.markdown(f"**Compliance:** {result.get('compliance_feedback', '-')}")