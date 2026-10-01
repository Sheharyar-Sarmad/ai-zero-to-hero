# LangChain Core — Runnables, Tools & Agents

Welcome to **Part 3** of the GenAI Series Code Implementation! This module bridges theory with practical code implementations, covering LangChain Expression Language (LCEL) Runnables, custom Tool integration, and Autonomous Agentic loops with Streamlit UIs.

---

## 📂 Repository Structure

```text
03_code_implementation/
├── 01_runnables/
│   ├── 01_sequence_runnable.py     # Sequential LCEL chains
│   ├── 02_parallel_runnable.py     # Parallel execution pipelines
│   └── 03_pass_trough_runnable.py  # Data forwarding & prompt binding
├── 02_tools/
│   ├── 01_build_in_tool.py         # Tavily & pre-built tools
│   ├── 02_custom_tool.py           # Custom Python function tools (@tool)
│   ├── 03_tool_with_LLM.py         # Function calling & LLM tool binding
│   └── 04_tool_with_chat_history.py# Conversational tool execution
├── 03_agents/
│   ├── 01_agents_overview.md       # Conceptual foundations of AI Agents
│   ├── 02_hard_code_agent.py       # Deterministic rule-based agent loop
│   ├── 03_hard_code_agent_ui.py    # Streamlit UI for hardcoded agent
│   ├── 04_autonomous_agent.py      # ReAct / Autonomous agent architecture
│   ├── 05_autonomous_agent_ui.py   # Streamlit UI for autonomous agent
│   └── 06_outro.md                 # Summary & key takeaways
├── src/                            # Shared utilities and core helpers
├── .env.example                    # Environment variable template
├── pyproject.toml                  # Project metadata & dependencies
└── requirements.txt                # Pip requirements file
```

## 🚀 Key Topics Covered

* **LCEL Runnables (`01_runnables/`)**:
  * Building pipeline chains with `RunnableSequence`.
  * Executing parallel context gathering with `RunnableParallel`.
  * Modifying data flows on-the-fly using `RunnablePassthrough`.

* **Tool Integration (`02_tools/`)**:
  * Creating custom tools with `@tool` decorators and schema validation.
  * Binding tool definitions directly to LLMs for structured tool calls.
  * Preserving conversational state during tool-assisted execution.

* **Autonomous Agents (`03_agents/`)**:
  * Comparing deterministic (hardcoded) control loops vs. autonomous ReAct reasoning.
  * Interactive CLI and Streamlit interfaces for real-time agent observation.

---

## 🛠 Getting Started

### 1. Environment Setup

Clone/navigate to this directory and activate your virtual environment:

```bash
# Using uv (recommended)
uv sync

# Or standard pip
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt