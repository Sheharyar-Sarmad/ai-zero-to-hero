# 🧠 Conceptual Prerequisites: Pre-Requisite Knowledge Check

This module assumes you have completed the earlier sections of the **ai-zero-to-hero** repository[cite: 1]. Before building AI Agents, you should have a solid foundation in the core mathematical, machine learning, and Generative AI concepts listed below.

---

## 1. Mathematical & Programming Foundations

* **Linear Algebra & Calculus**: Vectors, matrix multiplication, dot products (crucial for embeddings and attention mechanisms), and gradient descent concepts.
* **Python & API Integration**: Async Python, data structures, type hints, environment variable management, and making REST API calls (`requests`, `httpx`).
* **Environment Setup**: Handling API keys, managing dependencies, and isolating runtime environments.

---

## 2. Machine Learning, Deep Learning & Transformers

* **ML & DL Core**: Neural network architecture, forward/backward propagation, activation functions, and model evaluation metrics.
* **Transformer Architecture**: Self-attention mechanisms, multi-head attention, encoders/decoders, positional encodings, and tokenization.
* **LLM Foundations**: Context windows, system/user/assistant message roles, temperature setting, and token-based pricing/generation dynamics.

---

## 3. RAG vs. AI Agents (The Conceptual Shift)

From `22_genai_2`, you learned standard Retrieval-Augmented Generation (RAG)[cite: 1]:

```text
[RAG - Deterministic]
User Query ──► Retrieve Vectors ──► Inject Context ──► LLM Answer

[AI Agent - Dynamic]
User Query ──► LLM (Plan) ──► Choose Tool ──► Execute Tool ──► Observe Result ──► Repeat / Answer