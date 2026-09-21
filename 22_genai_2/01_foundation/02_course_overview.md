# Course Overview — Module 22

A quick map of what this module covers and in what order.

---

##  Goal

Build a **full-stack RAG application** from scratch — from loading documents to serving grounded, source-cited answers through a deployed web app.

**End result:** A working product you can demo, similar to ClipSage but powered by retrieval instead of raw LLM memory.

---

## Topics Covered

| # | Topic | What You'll Learn |
|---|---|---|
| 1 | **Foundations** | What RAG is, why it exists, when to use it |
| 2 | **Document Loaders** | Load PDFs, web pages, text files, directories |
| 3 | **Text Splitters** | Chunk documents intelligently (recursive, semantic) |
| 4 | **Vector Stores** | Store & search embeddings (Chroma, FAISS) |
| 5 | **Retrievers** | Fetch relevant chunks (MMR, multi-query, compression) |
| 6 | **RAG Pipeline** | Combine everything into a query → answer flow |
| 7 | **Capstone** | Deploy a full-stack RAG app (FastAPI + Next.js) |

---

## The RAG Pipeline

```
Documents → Load → Split → Embed → Store
                                     │
                                     ▼
Query → Embed → Retrieve → Augment → LLM → Answer + Citations
```

Every section in this module builds **one piece** of this pipeline.

---

## Structure

```
22_genai_2/
├── 01_foundation/          # Theory + plan
├── 02_RAG's/               # Concept notes
├── 03_code_implementation/ # Runnable code
└── 04_Capstone/            # Full-stack deployed app
```

---

## Stack

- **Backend:** FastAPI + LangChain + Chroma
- **Frontend:** Next.js 14 + TypeScript + Tailwind
- **Embeddings:** HuggingFace (free)
- **LLM:** Groq (free tier)
- **Deployment:** Vercel + Render
- **Cost:** ₨0

---

## By the End You'll Be Able To

- Load and chunk any document set
- Generate and store embeddings at scale
- Build retrieval chains with citations
- Deploy a RAG app end-to-end
- Explain RAG architecture confidently in interviews

---

**Next:** [03_learning_plan.md](./03_learning_plan.md)