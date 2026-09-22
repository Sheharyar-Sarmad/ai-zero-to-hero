# RAG Pipeline from Scratch: A Hands-On Implementation

A complete Retrieval-Augmented Generation system built from the ground up, covering document loading, chunking strategies, vector storage, and retrieval methods, wrapped in a working chat application.

## Live Demo

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://docapp-bot-j7v8vovmh8sxbvcsqlnlqr.streamlit.app/)
[![DocQA Bot Repo](https://img.shields.io/badge/Project_Repo-DocQA_Bot-blue?logo=github)](https://github.com/Sheharyar-Sarmad/Docqa-Bot)

## What This Project Demonstrates

* End-to-end RAG pipeline design, from raw documents to grounded LLM responses
* Practical experience with multiple document loaders (text, PDF, web)
* Comparative implementation of four chunking strategies, including semantic chunking
* Local embedding generation using Hugging Face models (no API cost)
* Vector storage and similarity search with ChromaDB
* Three distinct retrieval strategies: Similarity, MMR, and MultiQuery
* A production-style chat interface with conversation history and a 3-mode response system (Direct, Inferred, Refusal)
* Both a CLI and a web UI for interacting with the same underlying pipeline
* Building an entire functional AI system on free-tier tools only

## Architecture Overview

```
   Documents              Chunks              Embeddings
  (PDF, TXT,               (Split            (Local HF
   Web, Arxiv)             Strategy)          Models)

      LOAD         --->      SPLIT      --->     EMBED
        |                                            |
        |                                            v
        |                                         STORE
        |                                       (ChromaDB)
        |                                            |
        v                                            v
   User Query   --------------------------->     RETRIEVE
                                              (Similarity/MMR/
                                               MultiQuery)
                                                     |
                                                     v
                                                 GENERATE
                                              (Groq LLM Inference)
                                                     |
                                                     v
                                              Grounded Answer
```

## Folder Structure

```
22_genai_2/
│
├── 01_doc_loader/
│   ├── text_loader.py
│   ├── pdf_loader.py
│   ├── web_loader.py
│   └── llm_summarization_demo.py
│
├── 02_text_splitters/
│   ├── character_splitter.py
│   ├── token_splitter.py
│   ├── recursive_character_splitter.py
│   ├── semantic_chunker.py
│   └── (each paired with an LLM integration file)
│
├── 03_vector_db/
│   ├── chroma_setup.py
│   └── similarity_search.py
│
├── 04_retrievers/
│   ├── arxiv_loader.py
│   ├── mmr_retriever.py
│   └── multi_query_retriever.py
│
├── app.py                  # Streamlit chat UI
├── create_database.py      # Builds the ChromaDB from source docs
├── main.py                 # CLI-based RAG chatbot
└── README.md
```

## Tech Stack

| Layer | Tool | Purpose |
|---|---|---|
| Orchestration | LangChain (core, community, text-splitters, postgres) | Chains together loaders, splitters, retrievers, and the LLM |
| Embeddings | Hugging Face (`BAAI/bge-small-en-v1.5`, `all-MiniLM-L6-v2`) | Converts text chunks into vectors, run locally, no API cost |
| Vector Store | ChromaDB | Stores and searches embeddings locally |
| LLM Inference | Groq (`openai/gpt-oss-120b`, `openai/gpt-oss-20b`) | Generates the final response from retrieved context |
| Frontend | Streamlit | Chat interface with history and mode switching |
| Backend | FastAPI | Planned next step, will expose the pipeline as an API |
| Runtime | Python 3.13 | Language |
| Package Manager | uv | Fast dependency management |

## The Four Modules Explained

**Document Loaders**
Every RAG system starts with getting raw content into a usable format. This module covers loading plain text, PDFs, and live web pages using LangChain's loader interfaces, along with a demo that summarizes loaded documents using an LLM before they ever reach the retrieval pipeline.

**Text Splitters**
Raw documents are too large to embed directly, so they need to be broken into meaningful chunks. This module implements and compares four approaches: a basic character splitter, a token-aware splitter using tiktoken, a recursive character splitter that respects natural text boundaries, and a semantic chunker that groups text by meaning rather than fixed length.

**Vector Databases**
Once chunks exist, they need to be embedded and stored somewhere searchable. This module sets up ChromaDB as a local vector store and implements similarity search, forming the retrieval backbone for the rest of the pipeline.

**Retrievers**
Storing vectors is only half the job, retrieving the right ones matters just as much. This module explores an Arxiv-based loader for research paper retrieval, an MMR retriever for diverse results, and a MultiQuery retriever that rephrases a single question into multiple queries to improve recall.

## Retrieval Strategies Compared

| Strategy | Best At | Trade-off |
|---|---|---|
| Similarity Search | Fast, straightforward top-k matches | Can return redundant, overly similar chunks |
| MMR (Maximal Marginal Relevance) | Balancing relevance with diversity in results | Slightly slower, needs a tunable lambda parameter |
| MultiQuery | Improving recall on ambiguous or under-specified questions | More LLM calls, higher latency per query |

## Setup and Installation

**1. Clone the repository**

```bash
git clone https://github.com/Sheharyar-Sarmad/ai-zero-to-hero.git
cd ai-zero-to-hero/22_genai_2
```

**2. Install dependencies using uv**

```bash
uv sync
```

**3. Create a `.env` file in the project root**

```
GROQ_API_KEY=your_groq_api_key_here
```

Get a free Groq API key at [console.groq.com](https://console.groq.com).

**4. Build the vector database**

```bash
python create_database.py
```

This loads the source documents, splits them, generates local embeddings, and stores them in ChromaDB.

## How to Run

**Option 1: CLI Chatbot**

```bash
python main.py
```

A terminal-based conversational interface for quick testing of the RAG pipeline without a UI.

**Option 2: Streamlit App**

```bash
streamlit run app.py
```

Launches the full chat interface with conversation history, MMR retrieval, and the 3-mode response system (Direct, Inferred, Refusal).

**Option 3: Rebuild the Database**

```bash
python create_database.py
```

Run this any time the source documents change and the vector store needs to be refreshed.

## A Note on the $0 Stack

Every part of this project runs on free tiers. Embeddings are generated locally using open-source Hugging Face models, so there is no cost per embedding call. ChromaDB runs in-memory on local storage, no hosted database needed. Groq's free tier handles LLM inference at very low latency. And once deployed, the app itself runs on Streamlit Community Cloud at no cost. The entire pipeline, from raw PDF to grounded answer, was built and can be run without spending a single rupee or dollar.

## What I Learned

Building this pipeline end to end taught me that RAG is not one thing, it is a chain of small decisions that each affect the final answer quality. Choosing the wrong text splitter can silently break retrieval, and I did not fully understand why until I compared character-based splitting against semantic chunking on the same documents and saw the difference in retrieved context. Implementing MMR and MultiQuery retrievers side by side also showed me that there is no single best retrieval strategy, only trade-offs suited to different query types. Working entirely with free-tier tools forced me to think carefully about efficiency instead of just throwing API credits at problems. This project moved me from understanding RAG in theory to being able to build, debug, and reason about one from scratch.

## Author and Connect

Built by Sheharyar Sarmad, a self-taught AI engineer from Pakistan.

* GitHub: [github.com/Sheharyar-Sarmad](https://github.com/Sheharyar-Sarmad)
* LinkedIn: [linkedin.com/in/sheharyar-sarmad-9b7736289](https://www.linkedin.com/in/sheharyar-sarmad-9b7736289/)
* Repository: [ai-zero-to-hero/22_genai_2](https://github.com/Sheharyar-Sarmad/ai-zero-to-hero/tree/main/22_genai_2)

If you have feedback or spot something worth improving, feel free to open an issue or reach out directly.
