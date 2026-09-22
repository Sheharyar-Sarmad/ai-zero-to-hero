import tempfile
import os
import shutil
import hashlib
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

load_dotenv()

st.set_page_config(page_title="Chat with your PDF", page_icon="📄")
st.title("📄 Chat with your PDF")

# ---------- 1. Upload PDF ----------
uploaded_file = st.file_uploader("Upload a PDF", type="pdf")


# ---------- 2. Build retriever (cached per unique PDF content) ----------
@st.cache_resource(show_spinner="Indexing your PDF...")
def build_retriever(file_hash: str, file_bytes: bytes, file_name: str) -> VectorStoreRetriever:
    """
    Build a fresh in-memory retriever from a PDF's raw bytes.
    Cached by `file_hash` — identical content won't re-index.
    """
    tmp_dir = tempfile.mkdtemp(prefix="pdf_rag_")
    tmp_path = os.path.join(tmp_dir, "uploaded.pdf")
    with open(tmp_path, "wb") as f:
        f.write(file_bytes)

    try:
        # 1. Load PDF
        docs: list[Document] = PyPDFLoader(tmp_path).load()

        # 2. Fail loudly if no extractable text
        total_chars = sum(len(d.page_content.strip()) for d in docs)
        if not docs or total_chars == 0:
            raise ValueError(
                "No text could be extracted from this PDF. "
                "It may be a scanned/image-only PDF (needs OCR)."
            )

        # 3. Split into chunks
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=100,
        )
        chunks: list[Document] = splitter.split_documents(docs)

        if not chunks:
            raise ValueError("Splitting produced no chunks.")

        # 4. Embed + store in-memory
        embeddings = HuggingFaceEmbeddings(
            model_name="BAAI/bge-small-en-v1.5",
            encode_kwargs={"normalize_embeddings": True},
        )

        vectorstore = Chroma.from_documents(
            documents=chunks,
            embedding=embeddings,
        )

        # 5. Save stats for display
        st.session_state["stats"] = {
            "file_name": file_name,
            "pages": len(docs),
            "chunks": len(chunks),
            "chars": total_chars,
        }

        # 6. Retriever
        return vectorstore.as_retriever(
            search_type="mmr",
            search_kwargs={"k": 6, "fetch_k": 15, "lambda_mult": 0.5},
        )

    finally:
        shutil.rmtree(tmp_dir, ignore_errors=True)


# ---------- 3. Prompt + LLM (built once) ----------
prompt: ChatPromptTemplate = ChatPromptTemplate.from_messages([
    (
        "system",
        """You are a helpful AI assistant answering questions about a document.

You have THREE response modes:

1. DIRECT — If the answer is stated in the provided context, answer directly from it.

2. INFERRED — If the answer is NOT literally stated but CAN reasonably be inferred
   from the context (e.g. the document describes skills/experience but doesn't state
   salary — you can still give a well-reasoned estimate), start your reply with:
   "The document doesn't specify this directly, but based on the context:"
   Then give your informed answer.

3. REFUSAL — Only if the question is COMPLETELY unrelated to the document
   (e.g. asking about the weather, sports scores, unrelated trivia), respond with
   exactly:
   "I could not find the answer in the document."

IMPORTANT:
- Use the conversation history to resolve follow-ups like "is he good?" or
  "what about his salary?" — identify who "he" is from prior turns.
- Never fabricate facts as if they were in the document. If you infer, say so.
- Be concise and well-structured.""",
    ),
    MessagesPlaceholder(variable_name="history"),
    (
        "human",
        """Context:
{context}

Question: {query}""",
    ),
])

llm: ChatGroq = ChatGroq(model="openai/gpt-oss-120b")


# ---------- 4. Chat UI ----------
if uploaded_file is not None:
    file_bytes: bytes = uploaded_file.getvalue()
    file_name: str = uploaded_file.name
    file_hash: str = hashlib.sha256(file_bytes).hexdigest()

    try:
        retriever: VectorStoreRetriever = build_retriever(file_hash, file_bytes, file_name)

        stats = st.session_state.get("stats", {})
        if stats:
            st.success(
                f"✅ Indexed **{stats['file_name']}** — "
                f"{stats['pages']} pages, {stats['chunks']} chunks, "
                f"{stats['chars']:,} characters"
            )

    except Exception as e:
        st.error(f"❌ Failed to index PDF: {e}")
        st.stop()

    # Chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Optional clear button
    if st.sidebar.button("🔄 Clear chat"):
        st.session_state.messages = []
        st.rerun()

    # Render past turns
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Input box
    query: str | None = st.chat_input("Ask a question about your PDF...")

    if query:
        # Show user message
        st.session_state.messages.append({"role": "user", "content": query})
        with st.chat_message("user"):
            st.markdown(query)

        # 1. Retrieve chunks for this query
        docs: list[Document] = retriever.invoke(query)

        with st.expander(f"🔍 Retrieved {len(docs)} chunks", expanded=False):
            for i, d in enumerate(docs):
                page = d.metadata.get("page", "?")
                preview = d.page_content[:300].replace("\n", " ")
                st.write(f"**Chunk {i+1} (page {page}):** {preview}…")

        context: str = "\n\n".join(doc.page_content for doc in docs)

        # 2. Build history as proper message objects
        #    (exclude the last message — that's the current query)
        history: list[BaseMessage] = []
        for m in st.session_state.messages[:-1]:
            if m["role"] == "user":
                history.append(HumanMessage(content=m["content"]))
            else:
                history.append(AIMessage(content=m["content"]))

        # 3. Format prompt with history + fresh context
        final_prompt: ChatPromptValue = prompt.invoke({
            "history": history,
            "context": context,
            "query": query,
        })

        with st.expander("🐛 Prompt sent to LLM", expanded=False):
            for m in final_prompt.to_messages():
                st.markdown(f"**{m.type}**: {m.content[:800]}")

        # 4. Generate
        response: AIMessage = llm.invoke(final_prompt)

        # 5. Save + show
        st.session_state.messages.append(
            {"role": "assistant", "content": response.content}
        )
        with st.chat_message("assistant"):
            st.markdown(response.content)