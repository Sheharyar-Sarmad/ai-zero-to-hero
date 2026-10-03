# Subgraphs

> Flow so far: State → Nodes → Edges → Reducers → Graph Compilation → Checkpointing → Interrupts → HITL → Streaming → **Subgraphs**

So far, every graph we built was one flat workflow. Now we ask: what if one *node's job* is itself a whole workflow?

---

## 1. What is a Subgraph?

A **subgraph is a graph inside another graph.** It has its own nodes and edges, but the bigger graph uses it like a single step.

```
Main Graph → Subgraph → Nodes + Edges
```

**Why not one huge graph?** A single giant graph becomes hard to read, test, and change. Subgraphs let you split it into small, named pieces.

**Analogy:** A restaurant kitchen. The head chef (main graph) says "prepare the dessert." The pastry station (subgraph) handles mixing, baking, and plating on its own. The head chef doesn't care about those steps, only that dessert comes back.

---

## 2. Why Subgraphs are Useful

- **Modularity:** each workflow lives in its own box.
- **Reusability:** build once, use in many parent graphs.
- **Separation of responsibilities:** research logic stays away from writing logic.
- **Easier testing and maintenance:** run and debug one subgraph alone.
- **Complex systems from small workflows:** big agents are assembled, not written in one piece.

**Practical example:**

```
Main Research Graph
        │
        ▼
Research Subgraph
   ├── Web Search node
   ├── ArXiv node
   └── Wikipedia node
```

Want to add a new source later? Edit only the Research Subgraph. The main graph stays untouched.

---

## 3. How a Subgraph Works Inside a Parent Graph

```
Parent Graph → Subgraph → Subgraph executes → Result returns → Parent Graph continues
```

The parent treats the subgraph as one larger reusable unit. It calls it, waits, and moves on.

| Term | Meaning |
|---|---|
| **Node** | A single unit of work (one function). |
| **Subgraph** | A group of connected nodes and edges forming a smaller workflow. |
| **Parent graph** | The larger workflow that contains or calls the subgraph. |

```
┌──────────────── Parent Graph ────────────────┐
│                                              │
│  [Node A] ──► ┌── Subgraph ──┐ ──► [Node C]  │
│               │ n1 → n2 → n3 │               │
│               └──────────────┘               │
└──────────────────────────────────────────────┘
```

From the outside, the subgraph looks like just another node.

---

## 4. State Between Parent Graph and Subgraph

**State** is the shared data the graph carries. A subgraph can:

1. **Receive** information from the parent's State.
2. **Perform** several internal steps (its own nodes).
3. **Return** updates that the parent merges back into its State.

```
Parent State ──► Subgraph ──► (internal steps) ──► Updates ──► Parent State
```

Parent and subgraph State schemas can be **related but not identical**. They usually overlap on a few keys (like `question` and `answer`), while the subgraph keeps extra private keys for its own work.

```python
class ParentState(TypedDict):
    question: str
    answer: str

class ResearchState(TypedDict):
    question: str          # shared with parent
    answer: str            # shared with parent
    sources: list[str]     # internal to the subgraph

# Compiled subgraph used as a node in the parent
parent.add_node("research", research_subgraph)
```

The shared keys (`question`, `answer`) are the "bridge." `sources` stays inside the subgraph.

---

## 5. Mental Model

```
Parent Graph → Subgraph → Internal Nodes → Internal State/Updates → Result → Parent Graph
```

A realistic agentic architecture:

```
Main Agent
├── Research Subgraph
├── Critic Subgraph
└── Writing Subgraph
```

**Analogy:** A company is the parent graph. Each department (research, review, writing) is a subgraph with its own smaller workflow. Management only receives each department's final result.

**Interview-ready points**

- A subgraph is a compiled graph used as a node inside a parent graph.
- Node = one step; subgraph = a mini-workflow; parent = the larger workflow.
- Subgraphs give modularity, reuse, and easier testing.
- Parent and subgraph communicate through shared State keys.
- Complex agents are built by composing small, focused subgraphs.