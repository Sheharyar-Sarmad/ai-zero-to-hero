# Text Splitters — Chopping Documents Without Losing Their Meaning

So you've loaded your documents in `01_document_loaders.md`. Great — you now have a giant blob of text sitting in memory. Here's the problem: **you cannot just throw that entire blob at an LLM.** This chapter is about why, and what to do about it.

---

## 1. The "Why": The Context Window Problem

### ELI5

Imagine you have a friend with a really good memory, but they can only listen to you talk for **60 seconds** before they have to start responding. If you try to read them your entire 50-page book report in one breath, two things happen: it takes forever (and costs you a lot of "energy" to say it all), and by the time you get to the end, they've already forgotten what you said in the first 10 seconds. They'll answer your question, but they might mix up details from the beginning and the end of your speech.

That's basically what happens when you send a giant document to an LLM.

### The Technical Dive

Every LLM has a **context window** — a hard limit on how much text (input + output) it can process in a single call, measured in **tokens**, not words or characters.

**What's a token?**
A token is roughly ¾ of a word in English (e.g., "unbelievable" might split into `un`, `believ`, `able`). A 50-page PDF (~25,000 words) is roughly **33,000–40,000 tokens**. That might technically *fit* in a modern 128k or 200k context window model — but fitting isn't the same as being a good idea. Here's why:

1. **Cost scales with tokens.** Most LLM APIs charge per input token. If you're re-sending that entire 50-page document on *every single query* in a RAG pipeline, you're paying for the same 40,000 tokens over and over, even if the user's question only relates to page 12.

2. **Latency scales with tokens.** More input tokens = more time-to-first-token and more total processing time. Users don't want to wait 30 seconds for an answer.

3. **The "Lost in the Middle" phenomenon.** This is the big one. Research (notably the 2023 paper *"Lost in the Middle: How Language Models Use Long Contexts"*) found that LLMs exhibit a **U-shaped attention curve**: they're great at recalling information at the **beginning** and **end** of a long context, but performance **degrades significantly for information buried in the middle**. So even if your document technically fits, the model might completely miss the critical fact sitting on page 25 while confidently answering using something from page 1.

**The solution:** Instead of sending the whole document, RAG retrieves only the *most relevant small pieces* ("chunks") of text and feeds the model just those. This is only possible if the document has already been broken into small, meaningful, retrievable pieces — which is exactly what **text splitters** do.

---

## 2. Core Parameters: `chunk_size` and `chunk_overlap`

### ELI5

Imagine cutting a long loaf of bread into slices to make sandwiches. `chunk_size` is how thick each slice is. If you cut giant, foot-thick slices, each "sandwich" (chunk) has way too much bread and barely any filling — it's unwieldy and mostly noise. If you slice paper-thin, each sandwich is basically just crumbs — no substance, and you'll need hundreds of slices to make a meal.

`chunk_overlap` is like leaving a little bit of the previous slice attached to the next one, so if a filling (a sentence or idea) happens to sit right at the cut line, it doesn't get sliced in half and ruined in both pieces.

### The Technical Dive

**`chunk_size`** — the maximum length of each chunk, measured in characters or tokens depending on the splitter.

- **Too large:**
  - Retrieval becomes imprecise — a chunk might contain 5 different topics, and your vector search will only vaguely match the *average* semantic meaning of all of them, diluting relevance.
  - You waste context window space on irrelevant text once retrieved.
  - Increases the chance of hitting "Lost in the Middle" issues *within* a single retrieved chunk.

- **Too small:**
  - You lose context. A sentence like "It reduces latency by 40%" is useless without knowing *what* "it" refers to — that information might have been split into a different chunk.
  - You dramatically increase the number of vectors in your database, increasing storage and search cost.
  - Increases the risk of **retrieving fragments that are technically similar but contextually meaningless.**

**`chunk_overlap`** — the number of characters/tokens repeated between consecutive chunks.

Why it matters: Without overlap, if a key idea spans the exact boundary between chunk 1 and chunk 2, splitting it there can destroy the sentence's meaning in *both* resulting chunks. A small overlap (typically **10–20% of `chunk_size`**) acts as a safety buffer, ensuring that boundary-straddling ideas remain intact in at least one chunk.

**Rule of thumb starting point:** `chunk_size=1000`, `chunk_overlap=200` (tokens or characters) is a common, sane default for prose — but you should always tune this based on your data (see Pro-Tips below).

---

## 3. The Splitters: Choosing Your Tool

LangChain gives you several splitter classes, each with different levels of "intelligence" about how they cut text.

### `CharacterTextSplitter` — The Dumb One

**ELI5:** This is like cutting the bread loaf with a ruler and a knife at exact, fixed measurements — completely ignoring whether you're slicing straight through a piece of cheese or a tomato. It doesn't care what's in the way.

**Technical:** Splits text based on a **single separator string** (default: `"\n\n"`), and if a resulting split is still bigger than `chunk_size`, it does **not** recursively try smaller separators — it just leaves it oversized (or hard-cuts it, depending on version/config). This means it can — and often does — slice **mid-sentence or mid-word**, destroying semantic coherence. It's simple, fast, and rarely what you actually want in production.

### `RecursiveCharacterTextSplitter` — The Industry Standard

**ELI5:** Imagine you're told "cut this cake into 8 pieces, but try to cut *between* the frosting flowers first. If you can't get 8 clean pieces that way, then cut between the layers. If that's still not enough, only *then* cut straight through the cake." You always try the "nicest" cut first, and only get more aggressive if you have to.

**Technical:** This splitter takes an **ordered list of separators** (default: `["\n\n", "\n", " ", ""]`) — paragraph breaks, then line breaks, then spaces, then hard character cuts as an absolute last resort. It tries the first separator; if a chunk still exceeds `chunk_size`, it recurses into that chunk using the *next* separator down the list. This preserves natural document structure (paragraphs → sentences → words) as much as possible, which is why it's the **default choice for most RAG pipelines** — it balances simplicity with a strong respect for semantic boundaries.

### `TokenTextSplitter` — The Precise One

**ELI5:** Instead of measuring your bread slices with a regular ruler (characters), you're measuring them with the *exact* ruler the LLM itself uses to "see" your bread (tokens). This means your slices will always be exactly the right size for the model's "mouth" (context window), with zero surprises.

**Technical:** `CharacterTextSplitter` and `RecursiveCharacterTextSplitter` measure `chunk_size` in **characters** by default — but the LLM's context window is measured in **tokens**, and characters-to-tokens ratio is *not* fixed (varies by language, punctuation density, code vs. prose, etc.). `TokenTextSplitter` uses an actual **tokenizer** (like `tiktoken`, OpenAI's tokenizer) to split based on real token counts. This guarantees your chunks precisely fit your model's token budget — critical when you're right up against context limits or need exact cost predictions. The tradeoff: it's more computationally expensive and, without care, can still split mid-sentence since it isn't inherently structure-aware.

### `SemanticChunker` — The Advanced One

**ELI5:** Instead of measuring by size at all, imagine you have a super-smart friend reading the whole book with you, and every time the *topic* changes — like going from talking about dinosaurs to talking about outer space — they say "okay, new chunk starts here," regardless of whether that's after 3 sentences or 30.

**Technical:** `SemanticChunker` (from `langchain_experimental.text_splitter`) doesn't use fixed size rules at all. Instead, it:
1. Splits text into initial sentences.
2. Generates **embeddings** for each sentence (or small group of sentences).
3. Measures the **cosine distance** between consecutive sentence embeddings.
4. Inserts a chunk boundary wherever that distance exceeds a threshold (i.e., wherever the *semantic meaning* shifts significantly).

This produces chunks that are **topically coherent** rather than arbitrarily sized — great for retrieval quality. The tradeoff: it requires an embedding model call for every sentence during the chunking process itself, making it **slower and more expensive** to run at ingestion time. It's a great choice when retrieval quality matters more than ingestion speed/cost, e.g., for high-stakes knowledge bases.

---

## 4. Code Example: The Industry Standard in Action

Here's a runnable example using `RecursiveCharacterTextSplitter` with a mock `Document` object, so you can paste this directly into a script and see the output.

```python
# pip install langchain langchain-text-splitters

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

# --------------------------------------------------------------------
# STEP 1: Create a mock Document (this simulates what 01_document_loaders.md
# would have produced after loading a real PDF/txt/webpage)
# --------------------------------------------------------------------
mock_document = Document(
    page_content="""
    Retrieval-Augmented Generation (RAG) is a technique that combines
    the power of large language models with external knowledge retrieval.

    Instead of relying purely on what the model learned during training,
    RAG systems fetch relevant chunks of information from a knowledge base
    at query time, then feed that information to the LLM as context.

    This solves two major problems: hallucination (the model making things up)
    and outdated knowledge (the model not knowing about recent events or
    private company data it was never trained on).

    A typical RAG pipeline has four stages: loading documents, splitting them
    into chunks, embedding those chunks into vectors, and storing them in a
    vector database for fast semantic retrieval.
    """,
    metadata={"source": "rag_intro.txt", "author": "senior_engineer"}
)

# --------------------------------------------------------------------
# STEP 2: Initialize the RecursiveCharacterTextSplitter
# --------------------------------------------------------------------
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,        # max size of each chunk (in characters here)
    chunk_overlap=40,      # overlap between consecutive chunks
    length_function=len,   # how to measure chunk_size (len = character count)
    separators=["\n\n", "\n", " ", ""],  # tries these in order, top to bottom
)

# --------------------------------------------------------------------
# STEP 3: Split the document into chunks
# --------------------------------------------------------------------
# split_documents() works on a LIST of Document objects and preserves metadata
chunks = text_splitter.split_documents([mock_document])

# --------------------------------------------------------------------
# STEP 4: Inspect the results
# --------------------------------------------------------------------
print(f"Original document split into {len(chunks)} chunks.\n")

for i, chunk in enumerate(chunks):
    print(f"--- Chunk {i + 1} (length: {len(chunk.page_content)}) ---")
    print(chunk.page_content.strip())
    print(f"Metadata: {chunk.metadata}\n")
```

**What to expect when you run this:** You'll see the original text broken into overlapping pieces, each under ~200 characters, with the `metadata` (like `source` and `author`) automatically carried over to every chunk — this is crucial later for **citing sources** in your RAG answers.

---

## 5. Pro-Tips: Choosing Chunk Size for Different Data Types

1. **Prose / Articles / Documentation → Medium-large chunks (500–1500 chars or ~150–400 tokens), overlap ~10-15%.**
   Natural language has redundancy and flows in paragraphs, so it tolerates bigger chunks well. Use `RecursiveCharacterTextSplitter` as your default here — it respects paragraph and sentence boundaries out of the box.

2. **Source Code → Small-to-medium chunks, split by syntax, not characters.**
   Never chunk code with a plain character splitter — it'll slice a function in half and produce garbage. Use LangChain's `RecursiveCharacterTextSplitter.from_language(language=Language.PYTHON, ...)` (it supports many languages), which uses language-aware separators like class/function definitions instead of arbitrary line breaks.

3. **Legal / Medical / Highly Technical Documents → Smaller chunks, larger overlap (20-25%), consider `SemanticChunker`.**
   Precision matters more than efficiency here — a hallucinated interpretation of a contract clause is far more costly than the extra compute cost of semantic chunking. Smaller chunks also reduce the chance of a retrieval mixing two unrelated clauses together.

4. **Chat Logs / Transcripts / Q&A pairs → Split by natural unit (message or turn), not by size at all.**
   Don't force a fixed `chunk_size` on conversational data — instead, treat each message or Q&A pair as its own atomic chunk (or small group of turns). Splitting mid-message destroys conversational context entirely.

5. **When in doubt: measure, don't guess.** Chunking is one of the highest-leverage places to experiment in a RAG pipeline. Build a small evaluation set of realistic questions and test retrieval quality across a few `chunk_size`/`chunk_overlap` combinations before locking in your defaults — what works for prose Wikipedia articles will *not* work well for a codebase or a legal contract.

---

**Next up:** `03_embeddings.md` — turning these chunks into vectors your database can actually search.