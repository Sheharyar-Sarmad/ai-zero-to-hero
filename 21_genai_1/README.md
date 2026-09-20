# Module 21 — GenAI Part 1 🌱

> Part of the **[ai-zero-to-hero](https://github.com/Sheharyar-Sarmad/ai-zero-to-hero)** learning series.

A hands-on introduction to **Generative AI** — from the fundamentals of LLMs, to LangChain, embeddings, structured outputs, and finally two full-stack AI apps (CineSage + ClipSage).

This module is the **foundation of my GenAI journey**, and it ends with a **deployed, production-style AI application running entirely on free tiers**.

---

## 📚 Module Structure

```
21_genai_1/
├── 01_foundation/          # Theory & prerequisites
│   ├── 01_prerequisites.md
│   ├── 02_course_overview.md
│   └── 03_genai.md
│
├── 02_LLM's/               # LLM fundamentals & LangChain basics
│   ├── 01_LLM's_foundation.md
│   ├── 02_using_LLM.md
│   └── 03_langchain_basics.md
│
├── 03_code_implementation/ # Hands-on coding notebooks & scripts
│   ├── 01_chatmodels/
│   │   ├── 01_chat_cli.py
│   │   ├── 02_huggingface.py
│   │   ├── 03_localmodel.py
│   │   └── 04_chatbot.py
│   ├── 02_embeddingmodels/
│   │   ├── 01_embedding.py
│   │   └── 02_huggingface_embedding.py
│   └── 03_CineSage/        # 🎬 First mini AI app (movie recommender)
│       ├── 01_core.py
│       ├── 02_UI.py
│       ├── 03_structured_output.py
│       ├── 04_structured_UI.py
│       └── README.md
│
└── 04_ClipSage/            # 🚀 Full-stack AI app (Capstone project)
    ├── api/                # FastAPI backend
    ├── client/             # Next.js frontend
    └── README.md
```

---

## 🎯 What You'll Learn

### 🧠 01 — Foundation
- What Generative AI actually is
- Prerequisites (Python, APIs, environment setup)
- Course roadmap & mental model

### 🤖 02 — LLM Fundamentals
- How Large Language Models work under the hood
- Tokens, context windows, temperature, top-p
- Using hosted LLMs via API (Groq, OpenAI, Hugging Face)
- LangChain basics: chains, prompts, memory, output parsers

### 💻 03 — Code Implementation
- **Chat Models** — CLI chatbot, Hugging Face integration, local model inference
- **Embedding Models** — vector embeddings with Hugging Face & sentence-transformers
- **CineSage** — a mini movie-recommender AI built with structured outputs

### 🚀 04 — ClipSage (Capstone)
A full-stack AI media intelligence app that turns any video, audio, or image into **structured, queryable notes**.

**Stack:** Groq Whisper · LangChain · FastAPI · Next.js · PostgreSQL-ready session layer

- 🔗 **Live App:** [clipsage-gamma.vercel.app](https://clipsage-gamma.vercel.app)
- 🔗 **Backend API:** [clipsage-1t7l.onrender.com](https://clipsage-1t7l.onrender.com)
- 🔗 **Source:** [github.com/Sheharyar-Sarmad/ClipSage](https://github.com/Sheharyar-Sarmad/ClipSage)

---

## 🛠️ Tech Stack Across the Module

| Layer | Tools |
|---|---|
| **Language** | Python 3.12+ |
| **LLM APIs** | Groq, Hugging Face, OpenAI-compatible endpoints |
| **Orchestration** | LangChain, LangChain Groq, LangChain Community |
| **Backend** | FastAPI, Uvicorn, Pydantic |
| **Frontend** | Next.js 14, React, TypeScript, Tailwind CSS, Shadcn UI |
| **AI Features** | Whisper (transcription), embeddings, structured output, grounded Q&A |
| **Deployment** | Vercel (frontend) · Render (backend) |
| **Cost** | 💸 **₹0 — built entirely on free tiers** |

---

## 🚀 Quick Start

```bash
git clone https://github.com/Sheharyar-Sarmad/ai-zero-to-hero.git
cd ai-zero-to-hero/21_genai_1
```

Each subfolder has its own `README.md` and setup instructions. Start with `01_foundation/` and work your way down.

For the capstone (`04_ClipSage/`), see the dedicated README in that folder.

---

## 🧭 Learning Path

```
01_foundation  →  02_LLM's  →  03_code_implementation  →  04_ClipSage
     (theory)      (concepts)      (hands-on code)         (full-stack deploy)
```

Each step builds on the previous one. By the end, you'll have gone from **"what is GenAI?"** to **"I just deployed my own GenAI app."**

---

## 💡 Philosophy

- **Learn by building** — every concept ends with running code
- **Free-tier first** — everything here works with $0 spent
- **Ship it** — don't stop at notebooks; deploy real apps
- **Document as you go** — READMEs are part of the deliverable

---

## 🔗 Links

- 📚 **Repo:** [ai-zero-to-hero](https://github.com/Sheharyar-Sarmad/ai-zero-to-hero)
- 📦 **This Module:** [21_genai_1](https://github.com/Sheharyar-Sarmad/ai-zero-to-hero/tree/main/21_genai_1)
- 🎬 **ClipSage (Capstone):** [github.com/Sheharyar-Sarmad/ClipSage](https://github.com/Sheharyar-Sarmad/ClipSage)
- 🌐 **Live Demo:** [clipsage-gamma.vercel.app](https://clipsage-gamma.vercel.app)
- 🧑‍💻 **GitHub:** [@Sheharyar-Sarmad](https://github.com/Sheharyar-Sarmad)
- 💼 **LinkedIn:** [sheharyar-sarmad](https://www.linkedin.com/in/sheharyar-sarmad-9b7736289/)

---

<p align="center">Built with ❤️ as part of the <b>ai-zero-to-hero</b> series</p>