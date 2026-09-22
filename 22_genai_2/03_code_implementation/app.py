# ============================================================
# SQLite patch for Streamlit Cloud (Linux) — MUST be first!
# ============================================================
__import__("pysqlite3")
import sys
sys.modules["sqlite3"] = sys.modules.pop("pysqlite3")

# ============================================================
# Imports
# ============================================================
import os
import shutil
import hashlib
import tempfile
import datetime
import streamlit as st

from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.vectorstores import VectorStoreRetriever
from langchain_core.documents import Document
from langchain_core.prompt_values import ChatPromptValue
from langchain_core.messages import AIMessage, HumanMessage, BaseMessage


# ============================================================
# Page config — MUST be the FIRST Streamlit call
# ============================================================
st.set_page_config(
    page_title="Chat with your PDF",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# Load secrets — works BOTH locally (.env) and on Streamlit Cloud (st.secrets)
# ============================================================
load_dotenv()  # reads local .env if present


def get_secret(key: str) -> str | None:
    """
    Read a secret in this priority order:
      1. st.secrets       (Streamlit Cloud)
      2. os.environ       (local .env / shell)
    Returns None if not found anywhere.
    """
    # 1. Try Streamlit secrets — may raise if no secrets.toml exists
    try:
        if key in st.secrets:
            return st.secrets[key]
    except Exception:
        # StreamlitSecretNotFoundError (or others) — fall through
        pass

    # 2. Fall back to environment variables (loaded from .env)
    return os.environ.get(key)


# Resolve the Groq API key and stop early if missing
groq_api_key: str | None = get_secret("GROQ_API_KEY")
if not groq_api_key:
    st.error(
        "❌ `GROQ_API_KEY` not found.\n\n"
        "**Local:** add it to `.env` → `GROQ_API_KEY=gsk_...`\n\n"
        "**Streamlit Cloud:** add it under *Settings → Secrets* → "
        "`GROQ_API_KEY = \"gsk_...\"`"
    )
    st.stop()


# ============================================================
# Title
# ============================================================
st.title("📄 Chat with your PDF")
st.caption(
    "Upload a PDF, then ask anything about it. "
    "The index is private to your session and is deleted when you close the tab."
)


# ============================================================
# Session state init
# ============================================================
if "messages" not in st.session_state:
    st.session_state.messages = []
if "stats" not in st.session_state:
    st.session_state.stats = {}
if "show_debug" not in st.session_state:
    st.session_state.show_debug = False
if "chroma_tmp_dir" not in st.session_state:
    st.session_state.chroma_tmp_dir = None


# ============================================================
# Cleanup — delete session's Chroma temp dir
# ============================================================
def _cleanup_session_db() -> None:
    """Delete the session's Chroma temp dir."""
    tmp_dir = st.session_state.get("chroma_tmp_dir")
    if tmp_dir and os.path.isdir(tmp_dir):
        shutil.rmtree(tmp_dir, ignore_errors=True)
    st.session_state.chroma_tmp_dir = None


# ============================================================
# Sidebar
# ============================================================
with st.sidebar:
    st.header("📊 Document Info")

    if st.session_state.stats:
        s = st.session_state.stats
        st.markdown(f"**File:** `{s['file_name']}`")
        c1, c2, c3 = st.columns(3)
        c1.metric("Pages", s["pages"])
        c2.metric("Chunks", s["chunks"])
        c3.metric("Chars", f"{s['chars']:,}")
    else:
        st.info("No document indexed yet. Upload a PDF to begin.")

    st.divider()

    st.header("⚙️ Controls")
    st.session_state.show_debug = st.toggle(
        "Show debug panels", value=st.session_state.show_debug
    )

    if st.button("🔄 Clear chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    if st.button("🗑️ Delete document & reset", use_container_width=True):
        _cleanup_session_db()
        st.session_state.clear()
        st.rerun()

    st.divider()

    st.header("🤖 Model")
    st.markdown(
        "- **LLM:** `openai/gpt-oss-120b`\n"
        "- **Embeddings:** `BAAI/bge-small-en-v1.5`\n"
        "- **Retriever:** MMR (k=6, λ=0.5)\n"
        "- **Vector DB:** Chroma (temp dir)"
    )

    st.divider()
    st.caption(
        "🔒 Your PDF is processed on the app server and never stored. "
        "Closing the tab wipes the index."
    )


# ============================================================
# Prompt + LLM
# ============================================================
prompt: ChatPromptTemplate = ChatPromptTemplate.from_messages([
    (
        "system",
        """You are a helpful AI assistant with access to a document provided as context.

You have FOUR response modes:

1. DIRECT — If the answer IS in the provided context, answer directly from it.
   You may cite pages like "(page 3)".

2. INFERRED — If the answer is NOT literally in the context but CAN reasonably be
   inferred from it, start your reply with:
   "The document doesn't specify this directly, but based on the context:"
   Then give your informed answer.

3. GENERAL — If the input is a greeting, small talk, a follow-up that doesn't need
   the document, or a general knowledge question UNRELATED to the document,
   answer helpfully from your own knowledge. Do NOT refuse these.
   Examples:
     - "hello" / "hi" / "heeloo" → greet back warmly
     - "how are you?" → reply conversationally
     - "tell me a joke" → tell one
     - "what is 2+2?" → answer it
     - "what is machine learning?" (general concept) → explain briefly
   For these, do NOT say "I could not find the answer in the document."

4. REFUSAL — Only use this if the user is CLEARLY asking about THIS SPECIFIC
   document's contents, but the information genuinely isn't there. Then respond
   with exactly:
   "I could not find the answer in the document."

HOW TO DECIDE:
- Is the user asking about the document? (mentions "the document", "the CV",
  "the file", asks about specific content) → use DIRECT, INFERRED, or REFUSAL.
- Is the user just chatting, greeting, or asking general knowledge? → use GENERAL.

Use the conversation history to resolve follow-ups like "is he good?".

Be concise, friendly, and well-structured.""",
    ),
    MessagesPlaceholder(variable_name="history"),
    (
        "human",
        """Context from document:
{context}

User: {query}""",
    ),
])

llm: ChatGroq = ChatGroq(
    model="openai/gpt-oss-120b",
    api_key=groq_api_key,
    streaming=True,
)


# ============================================================
# PDF uploader
# ============================================================
uploaded_file = st.file_uploader("Upload a PDF", type="pdf")


# ============================================================
# Build retriever — session-scoped temp Chroma
# ============================================================
@st.cache_resource(show_spinner="Indexing your PDF...")
def build_retriever(
    file_hash: str, file_bytes: bytes, file_name: str
) -> tuple[VectorStoreRetriever, dict, str]:
    """
    Build a fresh retriever backed by a session-scoped temp Chroma dir.

    Returns:
        (retriever, stats_dict, tmp_dir_path)

    NOTE: This function MUST be pure — it does NOT touch st.session_state.
    The caller is responsible for storing the returned values.
    """
    # 1. Write PDF to its own temp file
    tmp_dir = tempfile.mkdtemp(prefix="pdf_rag_")
    tmp_pdf = os.path.join(tmp_dir, "uploaded.pdf")
    with open(tmp_pdf, "wb") as f:
        f.write(file_bytes)

    # 2. Disk-backed Chroma dir inside the same temp tree
    chroma_dir = os.path.join(tmp_dir, "chroma_db")

    try:
        docs: list[Document] = PyPDFLoader(tmp_pdf).load()

        total_chars = sum(len(d.page_content.strip()) for d in docs)
        if not docs or total_chars == 0:
            raise ValueError(
                "No text could be extracted from this PDF. "
                "It may be a scanned/image-only PDF (needs OCR)."
            )

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=100,
        )
        chunks: list[Document] = splitter.split_documents(docs)
        if not chunks:
            raise ValueError("Splitting produced no chunks.")

        embeddings = HuggingFaceEmbeddings(
            model_name="BAAI/bge-small-en-v1.5",
            encode_kwargs={"normalize_embeddings": True},
        )

        vectorstore = Chroma.from_documents(
            documents=chunks,
            embedding=embeddings,
            persist_directory=chroma_dir,
        )

        stats = {
            "file_name": file_name,
            "pages": len(docs),
            "chunks": len(chunks),
            "chars": total_chars,
        }

        retriever = vectorstore.as_retriever(
            search_type="mmr",
            search_kwargs={"k": 6, "fetch_k": 15, "lambda_mult": 0.5},
        )

        return retriever, stats, tmp_dir

    except Exception:
        # Clean up on failure too
        shutil.rmtree(tmp_dir, ignore_errors=True)
        raise


# ============================================================
# Main chat UI
# ============================================================
if uploaded_file is not None:
    file_bytes: bytes = uploaded_file.getvalue()
    file_name: str = uploaded_file.name
    file_hash: str = hashlib.sha256(file_bytes).hexdigest()

    try:
        # Unpack the cached result and store stats + temp dir in session state
        retriever, stats, tmp_dir = build_retriever(file_hash, file_bytes, file_name)
        st.session_state.stats = stats
        st.session_state.chroma_tmp_dir = tmp_dir

        st.success(
            f"✅ Indexed **{stats['file_name']}** — "
            f"{stats['pages']} pages · {stats['chunks']} chunks · {stats['chars']:,} chars"
        )
    except Exception as e:
        st.error(f"❌ Failed to index PDF: {e}")
        st.stop()

    # Render existing messages
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
            if msg.get("sources"):
                st.caption(f"📄 Sources: pages {msg['sources']}")

    # Input
    query: str | None = st.chat_input("Ask a question about your PDF...")

    if query:
        # --- User message ---
        st.session_state.messages.append({"role": "user", "content": query})
        with st.chat_message("user"):
            st.markdown(query)

        # --- Retrieve ---
        docs: list[Document] = retriever.invoke(query)
        pages = sorted({str(d.metadata.get("page", "?")) for d in docs})
        pages_str = ", ".join(pages)

        if st.session_state.show_debug:
            with st.expander(f"🔍 Retrieved {len(docs)} chunks", expanded=False):
                for i, d in enumerate(docs):
                    page = d.metadata.get("page", "?")
                    preview = d.page_content[:300].replace("\n", " ")
                    st.write(f"**Chunk {i+1} (page {page}):** {preview}…")

        context: str = "\n\n".join(doc.page_content for doc in docs)

        # --- History ---
        history: list[BaseMessage] = []
        for m in st.session_state.messages[:-1]:
            if m["role"] == "user":
                history.append(HumanMessage(content=m["content"]))
            else:
                history.append(AIMessage(content=m["content"]))

        # --- Prompt ---
        final_prompt: ChatPromptValue = prompt.invoke({
            "history": history,
            "context": context,
            "query": query,
        })

        if st.session_state.show_debug:
            with st.expander("🐛 Prompt sent to LLM", expanded=False):
                for m in final_prompt.to_messages():
                    st.markdown(f"**{m.type}**: {m.content[:800]}")

        # --- Stream response ---
        with st.chat_message("assistant"):
            response_text = st.write_stream(
                chunk.content for chunk in llm.stream(final_prompt)
            )
            if pages_str:
                st.caption(f"📄 Sources: pages {pages_str}")

        # --- Save ---
        st.session_state.messages.append({
            "role": "assistant",
            "content": response_text,
            "sources": pages_str,
        })

    # --- Export chat ---
    if st.session_state.messages:
        with st.sidebar:
            st.divider()
            st.header("💾 Export")
            chat_text = "\n\n".join(
                f"**{m['role'].title()}:** {m['content']}"
                for m in st.session_state.messages
            )
            st.download_button(
                "Download chat (.md)",
                data=chat_text,
                file_name=f"chat_{datetime.datetime.now():%Y%m%d_%H%M%S}.md",
                mime="text/markdown",
                use_container_width=True,
            )

else:
    # Welcome screen
    st.info("👆 Upload a PDF above to get started.")
    with st.expander("ℹ️ How it works"):
        st.markdown(
            """
            1. **Upload a PDF** — it's loaded, chunked, and embedded locally.
            2. **Ask questions** — the retriever finds the most relevant chunks.
            3. **Get answers** — the LLM answers using only your PDF, with the
               ability to infer when something isn't stated directly.
            4. **Your privacy** — everything runs on the app server; the index is
               destroyed when you close the tab.
            """
        )