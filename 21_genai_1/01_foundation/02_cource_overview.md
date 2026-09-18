# Course Overview — Condensed

**Goal:** Build, not just learn. Ship two real projects while picking up GenAI concepts only as needed.

## Projects
- **AI Chatbot**: conversation memory, streaming, UI, multi-provider support, secure API keys. Core loop: input → model → output → state.
- **CineSage AI**: prompt-template-driven film recommender with structured output. Teaches specialization via prompting over fine-tuning.

## Topics Covered
- **Chat model basics**: messages, roles, context windows, LLM as a stateless function.
- **Providers**: OpenAI, Hugging Face, local models — trade-offs in cost/latency/privacy; swapping is config, not rewrite.
- **Project setup**: venv, clean structure, requirements.txt, env vars for keys.
- **Embeddings**: vectors capturing meaning, similarity (cosine/dot product), used in search/RAG/recommendations/clustering — most reused concept in the course.
- **Chatbot mechanics**: message loop, state management, UI, streaming.
- **Prompt templates**: reusable, variable-driven prompts; system prompts; systematic iteration; separating prompt logic from app logic.
- **Structured output**: why raw text breaks pipelines; JSON mode, function calling, Pydantic validation/repair.

## Skills Gained
Set up LLM-agnostic projects, build stateful chat apps, generate/use embeddings, design prompt templates, enforce structured output, stream responses, switch providers, run local models, specialize a general LLM into a product.

## Not Covered
Training models, transformer internals, attention math, research — this is applied engineering only.

## How to Succeed
Code along, extend each project with an untaught feature, read provider docs directly, keep everything on GitHub.

**Prerequisite:** Python + basic NLP + transformer intuition (see `01_prerequisites.md`).