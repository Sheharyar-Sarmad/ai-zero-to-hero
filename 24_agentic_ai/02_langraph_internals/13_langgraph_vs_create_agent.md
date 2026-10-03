# LangGraph vs `create_agent`

> Previous notes: State → Nodes → Edges → Reducers → Compilation → Checkpointing → Interrupts → HITL → Streaming → Subgraphs → Error Handling → When to Use LangGraph.
> This note answers: **should I use `create_agent`, or build the graph myself?**

---

## 1. What is `create_agent`?

`create_agent` (from `langchain.agents`) is a **high-level helper**. You give it a model and some tools, and it returns a ready-to-run agent. You don't wire up nodes and edges yourself.

What you get out of the box:

| Piece | What it does |
|---|---|
| **Model** | The LLM that decides what to do next |
| **Tools** | Functions the model can call |
| **Agent loop** | Repeat: think → act → observe, until done |
| **Tool calling** | Runs the tools the model asks for, feeds results back |
| **Basic execution flow** | Start → loop → final answer |

```
        ┌──────────────────────────────┐
        ▼                              │
 User ─► Model ──tool call?──► Tools ──┘
          │
          └─ no tool call ─► Final answer
```

The goal: **build a working agent without manually constructing every graph component.**

---

## 2. `create_agent` vs LangGraph

They are **not fundamentally different things**. `create_agent` is a higher-level way to build and run an agent workflow, and the agent it returns is a compiled LangGraph graph. So everything you learned (state, checkpointing, streaming, interrupts) still applies to it.

```
create_agent → agent behavior          (you describe WHAT the agent is)
LangGraph    → explicit graph architecture  (you design HOW execution flows)
```

| | `create_agent` | LangGraph |
|---|---|---|
| Abstraction level | Higher | Lower |
| You define | Model, tools, prompt | State, nodes, edges, routing |
| Execution flow | Provided for you | Designed by you |
| Runtime underneath | LangGraph | LangGraph |

The difference is **how much of the structure you write yourself**, not what the runtime can do.

---

## 3. When to Use `create_agent`

Use it when the built-in behavior already matches your need:

- A **standard tool-using agent**
- A **ReAct-style loop** (reason → call tool → observe → repeat)
- **Faster development** and quick prototypes
- **Less custom workflow logic** to write and maintain
- Cases where **built-in behavior is enough**

```python
from langchain.agents import create_agent

def get_weather(city: str) -> str:
    """Get weather for a city."""
    return f"It's sunny in {city}."

agent = create_agent(
    model="openai:gpt-4o",
    tools=[get_weather],
)

agent.invoke({"messages": [{"role": "user", "content": "Weather in Paris?"}]})
```

Tools, loop, and tool execution are all handled for you.

---

## 4. When to Drop Down to LangGraph

Explicit graph control becomes valuable when your workflow no longer looks like one standard agent loop:

| Need | Why explicit graph helps |
|---|---|
| Custom State schema | Track fields beyond messages |
| Multiple specialized agents | Route work between distinct roles |
| Complex branching | Conditional edges you design |
| Loops beyond the standard loop | Retry, critique, refine cycles |
| Parallel execution | Fan-out / fan-in nodes |
| Custom reducers | Control how updates merge |
| Subgraphs | Compose reusable workflows |
| Fine-grained interrupts / HITL | Pause at exact points you choose |
| Custom persistence behavior | Tailor checkpointing |
| Complex recovery and routing | Per-node error paths |

```
create_agent → predefined / high-level agent flow

   Model ⇄ Tools → Answer


LangGraph → developer-designed graph

   Router ─► Researcher ─┐
      │                  ├─► Reviewer ─► (approve?) ─► Output
      └────► Coder ──────┘        ▲           │
                                  └── revise ─┘
```

Note: some customization is possible *inside* `create_agent` (for example middleware and custom state), so dropping down is about needing control over the **graph structure itself**.

---

## 5. Decision Framework + Mental Model

```
Is it a standard agent (model + tools + loop)?
   │
   ├─ Yes ─► create_agent
   │
   └─ No: need custom execution control?
            (branching, parallelism, multi-agent, custom state)
            ─► LangGraph
```

Choosing LangGraph does **not** mean `create_agent` is bad or limited. The choice depends on **how much control your application requires**. Many projects start with `create_agent` and move to LangGraph only if the workflow outgrows it.

**Analogy**
- `create_agent` = **automatic transmission**: the gear changes are handled for you. Great for most everyday driving.
- LangGraph = **manual control over the workflow**: you pick every gear. Useful when the road demands it.

Neither is "better"; they suit different driving conditions.

### Interview-ready points

1. `create_agent` is a **higher-level abstraction** over LangGraph, not a separate system.
2. It provides model, tools, the agent loop, and tool calling out of the box.
3. Use it for standard tool-using / ReAct-style agents and fast development.
4. Use LangGraph directly for custom state, branching, parallelism, multi-agent flows, and fine-grained HITL.
5. The decision is about **required control**, not about good vs. bad.