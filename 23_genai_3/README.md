# GenAI Series — Part 3: Runnables, Tools & Agentic AI Architectures

Welcome to **Part 3** of the Generative AI series! This repository contains conceptual guides, architectural deep dives, practical code implementations, and upcoming capstone projects focusing on LangChain Expression Language (LCEL), tool binding, and autonomous AI agents.

---

## 📂 Repository Structure

```text
23_genai_3/
├── 01_foundation/                      # Core theoretical foundations
│   ├── 01_prerequisites.md             # Key concepts & environment pre-requisites
│   ├── 02_runnables.md                 # LCEL Runnable primitives & syntax
│   ├── 03_agentic_ai.md                # Introduction to Agentic AI paradigms
│   └── 03_tools.md                     # Function calling & tool execution mechanics
│
├── 02_agent_architecture/              # In-depth Agent System Design
│   ├── 01_what_is_an_agent.md          # Defining Agents vs standard LLM chains
│   ├── 02_agent_loop.md                # Thought-Action-Observation loops (ReAct)
│   ├── 03_tool_calling.md              # Tool selection, binding & parameter parsing
│   ├── 04_agent_decision_making.md     # Planning, decomposition & strategy
│   ├── 05_state_and_memory.md          # Short-term, long-term & conversational state
│   ├── 06_human_in_the_loop.md         # Interrupts, approvals & safety checkpoints
│   ├── 07_agent_control_and_safety.md  # Guardrails, rate limits & error handling
│   ├── 08_agent_abstractions.md        # Agent frameworks & abstraction layers
│   └── 09_agentic_system_design.md     # End-to-end multi-agent production design
│
├── 03_code_implementation/             # Hands-on Python implementation
│   ├── 01_runnables/                   # Sequence, Parallel & Passthrough chains
│   ├── 02_tools/                       # Built-in, custom @tool, & LLM tool binding
│   ├── 03_agents/                      # Hardcoded vs Autonomous agent scripts & UIs
│   ├── src/                            # Shared utilities and core helpers
│   ├── .env.example                    # Template for environment variables
│   ├── pyproject.toml / requirements.txt
│   └── README.md
│
├── projects/                           # 🚧 IN THE MAKING (Capstone Application)
│   └── [City Intelligence System]      # Streamlit app using Groq, Tavily & OpenWeather
│
└── GenAIvideo3.pdf                     # Reference lecture slides & curriculum map
```

## 📚 What's Covered

### 1. Foundations (`01_foundation/`)
* **LCEL Runnables**: Standardized execution interface (`invoke`, `stream`, `batch`) using `RunnableSequence`, `RunnableParallel`, and `RunnablePassthrough`.
* **Tools**: Declarative schema definitions and LLM function-calling capabilities.

### 2. Agent Architecture (`02_agent_architecture/`)
* Detailed breakdown of autonomous agent loops, memory persistence, human-in-the-loop validation, safety guardrails, and architectural patterns.

### 3. Code Implementation (`03_code_implementation/`)
* Executable Python scripts and Streamlit web interfaces demonstrating ReAct agents, custom tools, chat history retention, and LCEL workflows.

---

## 🚧 Capstone Project — In the Making 🛠️

Inside the `projects/` folder, a production-grade capstone application is currently under active development:

* 🌆 **City Intelligence System**:
  * An interactive **Streamlit** multi-tool dashboard.
  * Powered by **Groq** for high-speed LLM inference.
  * Integrates **Tavily Search API** for real-time web intelligence.
  * Integrates **OpenWeather API** for live weather telemetry.

---

## 🛠 Getting Started

### 1. Environment Setup

Navigate to the code implementation directory and activate your virtual environment:

```bash
cd 03_code_implementation

# Using uv (Recommended)
uv sync

# Or standard Python virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```