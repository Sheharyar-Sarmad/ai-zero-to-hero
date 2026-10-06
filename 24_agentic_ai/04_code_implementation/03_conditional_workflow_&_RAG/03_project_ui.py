# Same i have pasted the code of 01_project.py and claude give me the ui file!

import os
import re
import math
import time
import uuid
import hashlib
import threading
from pathlib import Path
from typing import TypedDict, Annotated, Literal

import streamlit as st
from dotenv import load_dotenv
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import InMemorySaver

from langchain_groq import ChatGroq
from langchain_core.messages import BaseMessage, AIMessage
from langchain_core.documents import Document
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

st.set_page_config(page_title="College Assistant", page_icon="🎓", layout="centered")

load_dotenv()  # Local runs: read GROQ_API_KEY from .env

# ----------------------------- Settings ------------------------------------
MAX_QUESTIONS: int = 5            # Questions allowed per window
WINDOW_MINUTES: int = 90          # 1.5 hours (set to 60 for 1 hour)
WINDOW_SECONDS: int = WINDOW_MINUTES * 60
MIN_CHARS: int = 3
MAX_CHARS: int = 500

BASE_DIR: Path = Path(__file__).parent            # PDFs sit next to this file
HF_CACHE_DIR: Path = BASE_DIR / "hf_cache"        # Hugging Face model downloaded here once
INDEX_ROOT: Path = BASE_DIR / "faiss_indexes"     # Saved vector stores (commit this folder)
ALLOWED_PROGRAMMES: tuple[str, ...] = ("BCA", "BBA", "B.Com(H)")

# Streamlit Cloud: key comes from Secrets. Must be set BEFORE ChatGroq is created.
try:
    if "GROQ_API_KEY" in st.secrets:
        os.environ["GROQ_API_KEY"] = st.secrets["GROQ_API_KEY"]
except Exception:
    pass  # No secrets file locally; .env is used instead


class State(TypedDict):
    programme: str
    messages: Annotated[list[BaseMessage], add_messages]
    query_type: str
    retrieved_context: str
    handbook_context: str
    course_context: str
    policy_context: str


# ------------------------------------------------------------------------
# Everything heavy is built ONCE per server process (not on every rerun
# or every user): embedding model, FAISS indexes, LLM and the graph.
# ------------------------------------------------------------------------
@st.cache_resource(show_spinner="Starting up the assistant (first load only)...")
def load_rag():
    # Embedding model: read from hf_cache after the first download
    embeddings_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        cache_folder=str(HF_CACHE_DIR),
        model_kwargs={"device": "cpu"},
    )

    def file_fingerprint(path: str) -> str:
        """SHA-256 of the PDF contents, used to detect when a PDF changed."""
        sha = hashlib.sha256()
        with open(path, "rb") as f:
            for block in iter(lambda: f.read(1024 * 1024), b""):
                sha.update(block)
        return sha.hexdigest()

    def build_retriever(pdf_path: str):
        """Load the saved FAISS index if present; build + save it only the first time."""
        try:
            if not os.path.isfile(pdf_path):
                raise FileNotFoundError(f"PDF file not found: {pdf_path}")

            index_dir = INDEX_ROOT / Path(pdf_path).stem
            meta_file = index_dir / "source.sha256"
            fingerprint = file_fingerprint(pdf_path)

            # Fast path: index exists and the PDF is unchanged -> just load from disk
            if (index_dir / "index.faiss").exists() and meta_file.exists() \
                    and meta_file.read_text().strip() == fingerprint:
                vectorstore = FAISS.load_local(
                    str(index_dir),
                    embeddings_model,
                    allow_dangerous_deserialization=True,  # Safe: files created by this app
                )
            else:
                # Slow path (once, or when the PDF changes)
                loader = PyPDFLoader(pdf_path)
                documents: list[Document] = loader.load()

                splitter = RecursiveCharacterTextSplitter(
                    chunk_size=800,
                    chunk_overlap=100
                )

                chunks: list[Document] = splitter.split_documents(documents)
                vectorstore = FAISS.from_documents(chunks, embeddings_model)

                index_dir.mkdir(parents=True, exist_ok=True)
                vectorstore.save_local(str(index_dir))
                meta_file.write_text(fingerprint)

            return vectorstore.as_retriever(search_kwargs={"k": 4})

        except Exception as err:
            raise Exception(f"Error building retriever: {err}") from err

    academic_retriever = build_retriever(str(BASE_DIR / "academics_handbook.pdf"))
    fee_retriever = build_retriever(str(BASE_DIR / "fee_structure.pdf"))

    llm = ChatGroq(
        model="openai/gpt-oss-20b",
        max_tokens=1024,
        temperature=0.4
    )

    # ---------------------------- Graph nodes (unchanged logic) ----------------------------
    def classifier_node(state: State) -> dict[str, str]:
        """Classify the student's query."""
        try:
            query: str = state["messages"][-1].content

            prompt: str = (
                "Classify this student query into exactly one category: "
                "'academic', 'fee', or 'general'.\n\n"
                "academic: attendance, exams, grading, credits, promotion, "
                "course structure, training, degree requirements.\n"
                "fee: tuition, payment, refund, late charges, scholarships, money.\n"
                "general: greetings, casual talk, or unrelated questions.\n\n"
                f"Query: {query}\n\n"
                "Return only: academic, fee, or general."
            )

            response: AIMessage = llm.invoke(prompt)
            category: str = response.content.strip().lower()

            if "academic" in category:
                category = "academic"
            elif "fee" in category:
                category = "fee"
            else:
                category = "general"

            return {"query_type": category}

        except Exception as err:
            raise Exception(f"Error in classifier_node: {err}") from err

    def academic_start_node(state: State) -> dict:
        """Start the parallel academic branch."""
        return {}

    def academic_handbook_node(state: State) -> dict[str, str]:
        """Retrieve general academic information."""
        try:
            query: str = state["messages"][-1].content
            docs: list[Document] = academic_retriever.invoke(query)
            context: str = "\n\n".join(doc.page_content for doc in docs)

            return {"handbook_context": context}

        except Exception as err:
            raise Exception(f"Error in academic_handbook_node: {err}") from err

    def course_structure_node(state: State) -> dict[str, str]:
        """Retrieve course-related information."""
        try:
            query: str = state["messages"][-1].content
            search_query: str = f"{query} course subjects curriculum credits programme"

            docs: list[Document] = academic_retriever.invoke(search_query)
            context: str = "\n\n".join(doc.page_content for doc in docs)

            return {"course_context": context}

        except Exception as err:
            raise Exception(f"Error in course_structure_node: {err}") from err

    def academic_policy_node(state: State) -> dict[str, str]:
        """Retrieve academic policy information."""
        try:
            query: str = state["messages"][-1].content
            search_query: str = f"{query} policy rules attendance examination requirements"

            docs: list[Document] = academic_retriever.invoke(search_query)
            context: str = "\n\n".join(doc.page_content for doc in docs)

            return {"policy_context": context}

        except Exception as err:
            raise Exception(f"Error in academic_policy_node: {err}") from err

    def merge_academic_node(state: State) -> dict[str, str]:
        """Merge parallel academic results."""
        try:
            context: str = "\n\n".join([
                f"HANDBOOK INFORMATION:\n{state.get('handbook_context', '')}",
                f"COURSE INFORMATION:\n{state.get('course_context', '')}",
                f"POLICY INFORMATION:\n{state.get('policy_context', '')}"
            ])

            return {"retrieved_context": context}

        except Exception as err:
            raise Exception(f"Error in merge_academic_node: {err}") from err

    def fee_rag_node(state: State) -> dict[str, str]:
        """Retrieve fee information."""
        try:
            query: str = state["messages"][-1].content
            docs: list[Document] = fee_retriever.invoke(query)
            context: str = "\n\n".join(doc.page_content for doc in docs)

            return {"retrieved_context": context}

        except Exception as err:
            raise Exception(f"Error in fee_rag_node: {err}") from err

    def general_node(state: State) -> dict[str, str]:
        """Handle queries that do not need retrieval."""
        return {"retrieved_context": "NO_RETRIEVAL_NEEDED"}

    def response_node(state: State) -> dict[str, list[tuple[str, str]]]:
        """Generate the final response."""
        try:
            query: str = state["messages"][-1].content
            programme: str = state.get("programme", "Unknown")
            context: str = state["retrieved_context"]

            if context == "NO_RETRIEVAL_NEEDED":
                prompt: str = (
                    f"You are a friendly college assistant helping a {programme} student.\n\n"
                    f"Question: {query}\n\n"
                    "Answer naturally and clearly."
                )
            else:
                prompt: str = (
                    f"You are a college assistant helping a {programme} student.\n\n"
                    "Use the official college information below to answer accurately.\n\n"
                    f"College context:\n{context}\n\n"
                    f"Question: {query}\n\n"
                    f"Give a clear answer relevant to {programme}. "
                    "Do not invent information that is not supported by the context."
                )

            response: AIMessage = llm.invoke(prompt)
            answer: str = response.content.strip()

            return {"messages": [("ai", answer)]}

        except Exception as err:
            raise Exception(f"Error in response_node: {err}") from err

    def route_query(state: State) -> Literal["academic_parallel", "fee_rag", "general"]:
        if state["query_type"] == "academic":
            return "academic_parallel"
        if state["query_type"] == "fee":
            return "fee_rag"
        return "general"

    # ---------------------------- Graph wiring (unchanged) ----------------------------
    graph = StateGraph(State)

    graph.add_node("classifier", classifier_node)
    graph.add_node("academic_start", academic_start_node)
    graph.add_node("academic_handbook", academic_handbook_node)
    graph.add_node("course_structure", course_structure_node)
    graph.add_node("academic_policy", academic_policy_node)
    graph.add_node("merge_academic", merge_academic_node)
    graph.add_node("fee_rag", fee_rag_node)
    graph.add_node("general", general_node)
    graph.add_node("response", response_node)

    graph.add_edge(START, "classifier")

    graph.add_conditional_edges("classifier", route_query, {
        "academic_parallel": "academic_start",
        "fee_rag": "fee_rag",
        "general": "general"
    })

    graph.add_edge("academic_start", "academic_handbook")
    graph.add_edge("academic_start", "course_structure")
    graph.add_edge("academic_start", "academic_policy")

    graph.add_edge("academic_handbook", "merge_academic")
    graph.add_edge("course_structure", "merge_academic")
    graph.add_edge("academic_policy", "merge_academic")

    graph.add_edge("merge_academic", "response")
    graph.add_edge("fee_rag", "response")
    graph.add_edge("general", "response")
    graph.add_edge("response", END)

    return graph.compile(checkpointer=InMemorySaver())


# ------------------- Rate limiter: shared across ALL sessions ---------------
@st.cache_resource
def get_rate_store() -> dict:
    """Server-wide store, so refreshing the page does NOT reset a user's quota."""
    return {"lock": threading.Lock(), "hits": {}}


def get_session_id() -> str:
    if "sid" not in st.session_state:
        st.session_state.sid = uuid.uuid4().hex
    return st.session_state.sid


def get_client_key() -> str:
    """Identify the user by IP (works behind Streamlit Cloud's proxy); fall back to session id."""
    try:
        forwarded = st.context.headers.get("X-Forwarded-For")  # Needs Streamlit >= 1.37
        if forwarded:
            return forwarded.split(",")[0].strip()
    except Exception:
        pass
    return get_session_id()


def _recent_hits(key: str, now: float) -> list[float]:
    store = get_rate_store()
    hits = [t for t in store["hits"].get(key, []) if now - t < WINDOW_SECONDS]
    store["hits"][key] = hits
    return hits


def rate_status(key: str) -> tuple[int, float]:
    """Return (questions_left, seconds_until_a_slot_frees_up)."""
    store = get_rate_store()
    with store["lock"]:
        now = time.time()
        hits = _recent_hits(key, now)
        left = MAX_QUESTIONS - len(hits)
        wait = 0.0 if left > 0 else hits[0] + WINDOW_SECONDS - now
        return left, wait


def consume_slot(key: str) -> bool:
    """Atomically use one question. Returns False if the limit is reached."""
    store = get_rate_store()
    with store["lock"]:
        now = time.time()
        hits = _recent_hits(key, now)
        if len(hits) >= MAX_QUESTIONS:
            return False
        hits.append(now)
        return True


def refund_slot(key: str) -> None:
    """Give the question back if the server failed (not the user's fault)."""
    store = get_rate_store()
    with store["lock"]:
        hits = store["hits"].get(key, [])
        if hits:
            hits.pop()


def fmt_wait(seconds: float) -> str:
    minutes = max(1, math.ceil(seconds / 60))
    hours, mins = divmod(minutes, 60)
    return f"{hours}h {mins}m" if hours else f"{mins}m"


# ------------------------------ Input checking ------------------------------
def validate_question(text: str) -> tuple[bool, str]:
    """Return (is_valid, cleaned_text_or_error_message)."""
    cleaned = re.sub(r"\s+", " ", text or "").strip()
    if not cleaned:
        return False, "Please type a question."
    if len(cleaned) < MIN_CHARS:
        return False, f"Your question is too short (minimum {MIN_CHARS} characters)."
    if len(cleaned) > MAX_CHARS:
        return False, f"Your question is too long (maximum {MAX_CHARS} characters)."
    if not re.search(r"\w", cleaned):
        return False, "Please include some words in your question."
    return True, cleaned


# ---------------------------------- UI --------------------------------------
rag_app = load_rag()
client_key = get_client_key()
session_id = get_session_id()

st.title("🎓 College Assistant")
st.caption("Ask about academics, attendance, exams, or fees. Answers come from the official college documents.")

# ----- Sidebar: programme + usage -----
with st.sidebar:
    st.header("Your details")
    programme = st.selectbox(
        "Programme",
        ALLOWED_PROGRAMMES,
        index=None,
        placeholder="Select your programme",
    )

    st.divider()
    left, wait = rate_status(client_key)
    st.subheader("Usage")
    st.progress(left / MAX_QUESTIONS, text=f"{left} of {MAX_QUESTIONS} questions left")
    if left == 0:
        st.warning(f"Limit reached. Try again in about {fmt_wait(wait)}.")
    else:
        st.caption(f"Limit: {MAX_QUESTIONS} questions every {WINDOW_MINUTES} minutes.")

    st.divider()
    if st.button("🗑️ Clear chat", use_container_width=True):
        st.session_state.chat = []
        st.session_state.thread_nonce = uuid.uuid4().hex  # Fresh graph memory (quota is NOT reset)
        st.rerun()

# ----- Programme required -----
if programme is None:
    st.info("👈 Select your programme in the sidebar to start chatting.")
    st.stop()

# Reset the conversation if the programme changes
if st.session_state.get("active_programme") != programme:
    st.session_state.active_programme = programme
    st.session_state.chat = []
    st.session_state.thread_nonce = uuid.uuid4().hex

st.session_state.setdefault("chat", [])
st.session_state.setdefault("thread_nonce", uuid.uuid4().hex)

# ----- Chat history -----
if not st.session_state.chat:
    st.markdown(
        f"👋 Hi! I'm here to help **{programme}** students. Try asking:\n"
        "- *What is the minimum attendance required to sit exams?*\n"
        "- *What is the late fee payment penalty?*"
    )

for msg in st.session_state.chat:
    with st.chat_message(msg["role"], avatar="🧑‍🎓" if msg["role"] == "user" else "🎓"):
        st.markdown(msg["content"])

# ----- Input -----
limit_reached = left == 0
user_input = st.chat_input(
    "Rate limit reached, please wait..." if limit_reached else "Ask your question...",
    max_chars=MAX_CHARS,
    disabled=limit_reached,
)

if user_input:
    ok, result = validate_question(user_input)
    if not ok:
        st.error(result)  # Invalid input does not use up a question
        st.stop()
    question = result

    # Enforce the limit server-side (atomic check + use)
    if not consume_slot(client_key):
        _, wait = rate_status(client_key)
        st.error(f"You've used all {MAX_QUESTIONS} questions. Please try again in about {fmt_wait(wait)}.")
        st.stop()

    st.session_state.chat.append({"role": "user", "content": question})
    with st.chat_message("user", avatar="🧑‍🎓"):
        st.markdown(question)

    state: State = {
        "programme": programme,
        "messages": [("human", question)],
        "query_type": "",
        "retrieved_context": "",
        "handbook_context": "",
        "course_context": "",
        "policy_context": "",
    }
    config = {"configurable": {"thread_id": f"{session_id}-{programme}-{st.session_state.thread_nonce}"}}

    with st.chat_message("assistant", avatar="🎓"):
        try:
            labels = {
                "academic": "Searching the academic handbook...",
                "fee": "Checking the fee structure...",
                "general": "Writing a reply...",
            }
            with st.status("Thinking...", expanded=False) as status:
                # Stream node-by-node so the label matches what is really happening
                for step in rag_app.stream(state, config, stream_mode="updates"):
                    if "classifier" in step:
                        status.update(label=labels[step["classifier"]["query_type"]])
                status.update(label="Done", state="complete")
            answer = rag_app.get_state(config).values["messages"][-1].content
            st.session_state.chat.append({"role": "assistant", "content": answer})
        except Exception:
            refund_slot(client_key)  # Server-side failure: don't charge the student
            st.session_state.chat.append({
                "role": "assistant",
                "content": "⚠️ Sorry, something went wrong while answering. "
                           "This question was not counted, please try again.",
            })

    st.rerun()  # Redraw so the sidebar counter updates