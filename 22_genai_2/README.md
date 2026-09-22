# 🧠 AI Zero to Hero — GenAI Part 2: Retrieval-Augmented Generation (RAG)

Welcome to **Part 2** of the *AI Zero to Hero* series! 🚀 This repository is a hands-on, end-to-end implementation of a **Retrieval-Augmented Generation (RAG)** pipeline — from loading raw documents to chatting with them through a polished Streamlit interface.

Whether you're learning RAG concepts from scratch or looking for a clean reference implementation, this repo walks through every stage of the pipeline in a structured, modular way. 📚

🔗 **Live Demo:** [Streamlit App](https://your-app-name.streamlit.app) *(dummy link — will be updated after deployment)*

## 📁 Module Structure

```
22_genai_2/
├── 01_doc_loader/
├── 02_text_splitters/
├── 03_vector_db/
├── 04_retrievers/
├── src/
├── app.py
├── create_database.py
├── main.py
```

### 🔹 `01_doc_loader/`
Contains scripts and notebooks demonstrating how to load documents from multiple sources — **PDFs, plain text files, and web pages** — using LangChain's document loaders. This is the entry point of the RAG pipeline where raw data is ingested.

### 🔹 `02_text_splitters/`
Explores different **text chunking strategies** (character-based, recursive, token-based, etc.) required to break large documents into manageable, semantically meaningful chunks before embedding.

### 🔹 `03_vector_db/`
Covers setting up and interacting with **Chroma**, the vector database used to store and query document embeddings efficiently.

### 🔹 `04_retrievers/`
Demonstrates **advanced retrieval strategies**, including:
- Maximal Marginal Relevance (MMR)
- Multi-Query Retrieval
- Arxiv Retriever

## ✨ Key Features

- 🔄 **End-to-end RAG pipeline** — from raw documents to conversational answers
- 📄 **Multi-format document loading** — PDF, text, and web pages
- ✂️ **Multiple text splitting strategies** for optimal chunking
- 🗄️ **Vector database powered by Chroma** for fast similarity search
- 🤗 **HuggingFace embeddings** for high-quality vector representations
- 🔍 **Advanced retrievers** — MMR, Multi-Query, and Arxiv retrieval
- 💬 **Streamlit chat application** with an intuitive UI
- ☁️ **Local and Streamlit Cloud ready** — deploy anywhere with minimal config

## 🛠️ Tech Stack

| Category | Technology |
|---|---|
| Language | 🐍 Python |
| Framework | 🦜 LangChain |
| UI | 🎈 Streamlit |
| Vector Store | 🟣 Chroma |
| Embeddings | 🤗 HuggingFace — `BAAI/bge-small-en-v1.5` |
| LLM | ⚡ Groq — `openai/gpt-oss-120b` |
| Package Management | 📦 `uv` / `pip` |

## 🚀 Getting Started

### ✅ Prerequisites

- Python 3.10+
- A [Groq API Key](https://console.groq.com/) for LLM access
- `git` installed on your machine

### 📥 Installation

Clone the repository:

```bash
git clone https://github.com/Sheharyar-Sarmad/ai-zero-to-hero.git
cd ai-zero-to-hero
```

Install dependencies using `uv` (recommended):

```bash
uv sync
```

Or using `pip`:

```bash
pip install -r requirements.txt
```

### 🔑 Environment Variables

Create a `.env` file in the root directory and add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key_here
```

### ▶️ Run the Streamlit App

First, build the vector database:

```bash
python create_database.py
```

Then launch the app:

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501` 🎉

## 💡 Usage

1. Add your source documents (PDFs, text files, or web URLs) to the appropriate loader configuration in `01_doc_loader/`
2. Run `create_database.py` to generate embeddings and persist them in the Chroma vector store
3. Launch `app.py` and start chatting with your documents through the Streamlit interface
4. Explore `04_retrievers/` to experiment with different retrieval strategies (MMR, Multi-Query, Arxiv) for improved answer quality

## 🗺️ Roadmap

This module is part of an ongoing learning series. Coming up next:

- 🔥 A brand-new **banger project** featuring **Next.js**, **FastAPI**, and more modern full-stack AI tooling
- More advanced RAG techniques and production-ready deployment patterns
- Additional GenAI modules building on this foundation

Stay tuned! 👀

## 🤝 Connect with Me

- 👨‍💻 GitHub: [Sheharyar-Sarmad](https://github.com/Sheharyar-Sarmad)
- 💼 LinkedIn: [Sheharyar Sarmad](https://www.linkedin.com/in/sheharyar-sarmad-9b7736289/)

## ⭐ Support

If you found this module helpful for learning RAG or building your own GenAI applications, please consider giving it a **star** ⭐ — it really helps and motivates further open-source contributions!