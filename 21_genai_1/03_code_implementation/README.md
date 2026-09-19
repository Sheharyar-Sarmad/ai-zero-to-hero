# 03_code_implementation

## 1. Module Overview

This module is the implementation layer of the `ai-zero-to-hero` roadmap, part of `21_genai_1`. It assumes you have already worked through the theoretical foundation in `01_foundation/` and the model internals covered in `02_LLM's/`. Where those modules explain *how* LLMs and embeddings work, this module is about writing the actual Python code that calls, runs, and wraps them.

The module is split into three folders, and the order is deliberate:

1. **`01_chatmodels`** — the same conversational task implemented four different ways, each one closer to a production pattern: a bare CLI loop, a hosted-API abstraction, a fully local model, and a proper web UI.
2. **`02_embeddingmodels`** — introduces the embedding layer, which is the foundation for retrieval and RAG in later modules.
3. **`03_CineSage`** — a small end-to-end capstone that ties prompting, structured output, and UI together into something that resembles a real deliverable.

By the end of this module you will have written code that calls multiple LLM providers through a single interface, run inference both remotely and locally, generated and compared embeddings, and shipped a structured-output pipeline with a UI on top of it.

## 2. Prerequisites

- **Python 3.10+**
- **Package manager:** `uv` (preferred) or `pip`
- **API keys** for at least Groq and Hugging Face (others optional depending on which files you run — see Section 6 for the full list and where to get each one)
- **Local model support:** `03_localmodel.py` downloads and runs TinyLlama-1.1B locally. This needs about 2.2 GB of disk space and runs fine on CPU — no GPU required, just expect slower inference than the hosted API files.

## 3. Folder Breakdown

### 01_chatmodels

Four files, same underlying task — hold a chat conversation with an LLM — each rebuilding it with more structure than the last:

| File | What it does |
|---|---|
| `01_chat_cli.py` | Simplest possible chatbot: a CLI loop calling Groq's `openai/gpt-oss-120b` directly |
| `02_huggingface.py` | Swaps the direct call for LangChain's `HuggingFaceEndpoint` + `ChatHuggingFace`, using Hugging Face's serverless inference API |
| `03_localmodel.py` | Removes the API dependency entirely — runs TinyLlama-1.1B locally via `HuggingFacePipeline` |
| `04_chatbot.py` | Wraps the chat logic in a Streamlit app with a model picker, temperature slider, editable system prompt, and streaming responses |

The point of this progression is to separate three concerns that are easy to conflate when you're new to this: the **provider** (Groq vs. Hugging Face vs. local), the **abstraction layer** (raw SDK call vs. LangChain wrapper), and the **interface** (CLI vs. web UI). Each file changes exactly one of these at a time.

### 02_embeddingmodels

| File | What it does |
|---|---|
| `01_embedding.py` | Generates embeddings with Hugging Face and compares them against OpenAI's embedding output; also covers why Groq does not offer an embeddings endpoint |
| `02_huggingface_embedding.py` | Generates embeddings in batches using `HuggingFaceEmbeddings` |

Embeddings turn text into vectors that capture semantic meaning, so that "similar" pieces of text end up close together in vector space. This is the mechanism that later powers semantic search and retrieval-augmented generation (RAG) — this module only covers generating and comparing embeddings; retrieval and vector stores come later in the roadmap.

### 03_CineSage

A mini pipeline built around one objective (see `00_objective.txt`): a media intelligence company wants unstructured movie paragraphs turned into structured, queryable data.

| File | What it does |
|---|---|
| `00_objective.txt` | The business spec this capstone is solving |
| `01_core.py` | CLI version using a prompt template, returns free-form text |
| `02_UI.py` | Same logic as `01_core.py`, wrapped in a Streamlit UI, still text output |
| `03_structured_output.py` | CLI version using a Pydantic schema with `with_structured_output`, returns validated JSON |
| `04_structured_UI.py` | Streamlit UI on top of `03_structured_output.py`, with a JSON-first view plus copy/download support |

The evolution across these four files is: **free-text prompt → free-text prompt with a UI → schema-enforced structured output → structured output with a polished UI.** This mirrors a realistic path from prototype to something you could actually hand to a non-technical stakeholder.

## 4. Setup Instructions

```bash
# Clone the repo
git clone https://github.com/Sheharyar-Sarmad/ai-zero-to-hero
cd ai-zero-to-hero/21_genai_1/03_code_implementation

# Create your .env file
cp .env.example .env
# then fill in the keys you need (see Section 6)

# Install dependencies
uv add -r requirements.txt
# or, with pip
pip install -r requirements.txt

# Sanity check
python 01_chatmodels/01_chat_cli.py
```

## 5. Environment Variables

| Variable | Used for | Required for |
|---|---|---|
| `OPENAI_API_KEY` | GPT-4o family, `text-embedding-3-small` | `01_embedding.py` (comparison) |
| `GROQ_API_KEY` | `openai/gpt-oss-120b`, `llama-3.3-70b-versatile` | `01_chat_cli.py`, `04_chatbot.py`, CineSage files |
| `GOOGLE_API_KEY` | Gemini models, Google embeddings | Optional, if you extend files to use Gemini |
| `MISTRAL_API_KEY` | `mistral-small-latest`, `mistral-embed` | Optional, if you extend files to use Mistral |
| `HUGGINGFACEHUB_ACCESS_TOKEN` | Serverless Inference API, model downloads | `02_huggingface.py`, `03_localmodel.py`, embedding files |

## 6. Where to Get Each API Key

### OPENAI_API_KEY
- **Link:** https://platform.openai.com/api-keys
- **Unlocks:** GPT-4o family and `text-embedding-3-small`
- **Steps:** Log in to the OpenAI platform → API keys → Create new secret key → copy it immediately (it's only shown once)
- **Free tier:** No standing free tier — requires purchased credits
- **Best practice:** Never commit this key. Keep it only in `.env`, and confirm `.env` is listed in `.gitignore` before your first commit.

### GROQ_API_KEY
- **Link:** https://console.groq.com/keys
- **Unlocks:** `openai/gpt-oss-120b`, `llama-3.3-70b-versatile`, and Whisper for audio
- **Steps:** Sign in to Groq Console → API Keys → Create API Key → copy it
- **Free tier:** Generous free tier, sufficient for this entire module
- **Best practice:** Same as above — `.env` only, never hardcoded, never committed.

### GOOGLE_API_KEY
- **Link:** https://aistudio.google.com/app/apikey
- **Unlocks:** Gemini models and Google's embedding models
- **Steps:** Open Google AI Studio → Get API Key → Create API key in new or existing project
- **Free tier:** Available, with rate limits
- **Best practice:** Restrict the key's usage in Google Cloud Console if you plan to keep it long-term.

### MISTRAL_API_KEY
- **Link:** https://console.mistral.ai/
- **Unlocks:** `mistral-small-latest`, `mistral-embed`
- **Steps:** Create a Mistral account → API Keys section → generate a new key
- **Free tier:** Free "Experiment" plan, rate-limited but enough for testing
- **Best practice:** Rotate the key if you ever suspect it leaked; Mistral lets you revoke and reissue from the same console page.

### HUGGINGFACEHUB_ACCESS_TOKEN
- **Link:** https://huggingface.co/settings/tokens
- **Unlocks:** Serverless Inference API calls and gated/ungated model downloads
- **Steps:** Log in to Hugging Face → Settings → Access Tokens → New token → give it "Read" scope (sufficient for this module)
- **Free tier:** Free for basic inference and public model downloads
- **Best practice:** Use a "Read"-scope token unless a specific file needs write access — don't default to full-permission tokens.

**General rule across all keys:** never commit `.env`, never paste a raw key into code, and double check `.gitignore` includes `.env` before pushing.

## 7. Dependencies

```
# Core LangChain
langchain
langchain-community
langchain-core
```
LangChain's core packages provide the unified interface this whole module is built around — the abstraction that lets `01_chat_cli.py`, `02_huggingface.py`, and `03_localmodel.py` share the same mental model despite hitting completely different backends. Without these, every provider integration below would need its own bespoke calling code.

```
# Provider integrations
langchain-openai
langchain-groq
langchain-google-genai
langchain-mistralai
langchain-huggingface
```
Each of these is a thin adapter that lets LangChain talk to a specific provider's API in its native format. You only strictly need `langchain-groq` and `langchain-huggingface` to run every file in this module as-is, but the others are included so you can swap providers without changing your code structure.

```
# Local model runtime
transformers
torch
accelerate
sentence-transformers
```
This group is what makes `03_localmodel.py` possible without any external API call. `transformers` and `torch` load and run TinyLlama locally, `accelerate` handles device placement (CPU here), and `sentence-transformers` backs the local embedding paths in `02_embeddingmodels`. Remove these and every "local" file in this module stops working.

```
# Data validation
pydantic
```
Pydantic defines the schemas used in `03_structured_output.py` and `04_structured_UI.py`. It's what turns "the model returned some JSON" into "the model returned data guaranteed to match this exact shape" — without it, `with_structured_output` has nothing to validate against.

```
# UI
streamlit
```
Powers every `*_UI.py` file and `04_chatbot.py`. Without it, those files fall back to being CLI scripts.

```
# Env
python-dotenv
```
Loads the keys from `.env` into the environment at runtime. Without it, every API-backed file in this module fails immediately with an authentication error.

## 8. How to Run Each File

```bash
# From 03_code_implementation/

# 01_chatmodels
python 01_chatmodels/01_chat_cli.py
python 01_chatmodels/02_huggingface.py
python 01_chatmodels/03_localmodel.py
python -m streamlit run 01_chatmodels/04_chatbot.py

# 02_embeddingmodels
python 02_embeddingmodels/01_embedding.py
python 02_embeddingmodels/02_huggingface_embedding.py

# 03_CineSage
python 03_CineSage/01_core.py
python -m streamlit run 03_CineSage/02_UI.py
python 03_CineSage/03_structured_output.py
python -m streamlit run 03_CineSage/04_structured_UI.py
```

## 9. Learning Outcomes

By completing this module, you can:

- Call any supported LLM provider through LangChain's unified interface
- Run inference both via hosted APIs and fully locally, and reason about the trade-offs (cost, latency, control, setup complexity)
- Build both interactive CLIs and Streamlit web UIs on top of the same underlying logic
- Generate embeddings for semantic search and understand why they matter for RAG
- Use prompt templates to keep LLM calls consistent and repeatable
- Enforce structured, validated JSON output from an LLM using Pydantic schemas
- Ship a small end-to-end extraction pipeline, from raw text input to a usable UI
## 10. Next Steps

This module stops at generation and structured extraction. The next parts of the roadmap build directly on it:

- **ClipSage:** the natural successor to CineSage, but for media instead of text. Where CineSage extracts structured info from a movie *paragraph*, ClipSage ingests **audio, video, and images** — transcribing them with Groq Whisper, identifying speakers with Pyannote, and returning a structured summary with a TL;DR, key points, action items, and decisions. It reuses every concept from this module: prompt templates, structured output with Pydantic, Streamlit UI, and provider abstraction across Groq and Hugging Face. The difference is that the *input* is no longer clean text — it's raw media that has to be transcribed, diarized, and merged before the LLM ever sees it.
- **RAG (retrieval-augmented generation):** using the embeddings from `02_embeddingmodels` to retrieve relevant context before generation.
- **Agents and tool use:** letting the model decide when to call external tools or functions.
- **Vector databases:** persisting and querying embeddings at scale, instead of comparing them in memory.
- **FastAPI deployment:** wrapping these scripts into actual served endpoints instead of CLI/Streamlit-only interfaces.