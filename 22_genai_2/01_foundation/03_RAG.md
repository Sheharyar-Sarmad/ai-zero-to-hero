# RAG (Retrieval-Augmented Generation)

## The Problem It Solves

LLMs are powerful, but they have three core limitations.

| Limitation | What it means | Example |
|---|---|---|
| **Knowledge cutoff** | The model only knows what it saw during training | Ask GPT-4 about an event from last week — it has no idea |
| **Hallucination** | The model confidently makes things up when unsure | Ask for a legal citation and it invents a case that doesn't exist |
| **No access to private data** | The model never saw your company's internal docs | Ask "what's our refund policy?" and it can't answer — it never read your wiki |

RAG fixes all three by giving the model **fresh, relevant, external knowledge** at query time — instead of relying only on what's baked into its weights.

## What RAG Actually Is

RAG is a 3-step loop:

1. **Retrieve** — find relevant documents/chunks related to the user's question
2. **Augment** — insert those chunks into the prompt as context
3. **Generate** — let the LLM answer using that context

**Analogy:** A closed-book exam is an LLM answering from memory alone. RAG turns it into an **open-book exam** — the model can look things up before answering.

**One-line summary:** RAG lets an LLM answer using information it was never trained on, by fetching it just-in-time.

## How It Works (Architecture)

There are two pipelines: one to prepare data (offline), one to answer queries (runtime).

```
INDEXING PIPELINE (done once, or on data update)
──────────────────────────────────────────────────
Documents → Load → Split → Embed → Store
   │          │       │       │       │
   │          │       │       │       └─ save vectors in a vector DB
   │          │       │       └───────── convert chunks to embeddings
   │          │       └───────────────── break docs into small chunks
   │          └───────────────────────── read raw files (PDF, docs, etc.)
   └──────────────────────────────────── your knowledge source

QUERY PIPELINE (done every time a user asks something)
──────────────────────────────────────────────────
Query → Embed → Retrieve → Augment → LLM → Answer
  │        │         │          │       │      │
  │        │         │          │       │      └─ final response to user
  │        │         │          │       └──────── model generates using context
  │        │         │          └──────────────── stuff retrieved chunks into prompt
  │        │         └─────────────────────────── find top-k similar chunks in DB
  │        └───────────────────────────────────── convert query to a vector too
  └────────────────────────────────────────────── user's question
```

Each step, one line:

- **Load** — pull raw content from PDFs, websites, databases, etc.
- **Split** — chunk large docs into smaller pieces (so retrieval is precise)
- **Embed** — turn text into numerical vectors capturing meaning
- **Store** — save vectors in a vector database for fast similarity search
- **Retrieve** — find the chunks closest in meaning to the query
- **Augment** — inject those chunks into the LLM's prompt as context
- **Generate** — LLM produces an answer grounded in that context

## RAG vs Fine-Tuning

| Factor | RAG | Fine-Tuning |
|---|---|---|
| **Cost** | Low — no retraining needed | High — requires GPU training runs |
| **Setup time** | Hours to days | Days to weeks |
| **Updating knowledge** | Just update the vector DB | Must retrain the model |
| **Best for** | Fast-changing facts, private docs | Changing behavior, tone, format, style |
| **Hallucination control** | Better — answers are grounded in sources | Doesn't fix hallucination by itself |

**Rule of thumb:**
- Need the model to *know new facts* → **RAG**
- Need the model to *behave differently* (tone, format, domain reasoning) → **Fine-tuning**
- Often, real systems use **both**.

## When To Use RAG

**Good fits:**
- Internal knowledge bases
- Documentation Q&A bots
- Customer support assistants
- Legal/medical research tools
- Search over large private datasets

**Bad fits:**
- Pure creative writing (poems, stories) — no external facts needed
- Casual general chat — retrieval adds latency for no benefit
- Tasks needing behavior/style change, not new facts

## Real-World Examples

- **ChatGPT (file uploads)** — retrieves from your uploaded PDF/docs to answer questions
- **Perplexity AI** — retrieves from the live web, then generates a cited answer
- **Notion AI** — retrieves from your workspace pages to answer "ask my docs" queries
- **GitHub Copilot Chat** — retrieves relevant code from your repo to answer questions about it

All four follow the same loop: retrieve context → stuff it into the prompt → generate.

## Connection to ClipSage (Module 21)

ClipSage already does a mini version of RAG — it retrieves relevant transcript snippets and answers questions using them.

| ClipSage today | With real RAG |
|---|---|
| Retrieves from a single video's transcript, held in memory during the session | Retrieves from a **persistent vector store** holding thousands of videos |
| Memory resets when the session ends | Knowledge stays searchable forever |
| Small, in-memory similarity search | Scalable vector DB (e.g. Chroma, Pinecone, Weaviate) |

The core loop doesn't change. What changes is **scale and persistence** — that's exactly what this module adds.

## What's Next

Head to the `02_RAG` hands-on folder to build the indexing and query pipelines yourself — chunking real documents, generating embeddings, and wiring up a vector store.

You already understand embeddings and LLMs. RAG is just the missing piece that connects them into something genuinely useful — build it once, and you'll see it everywhere.