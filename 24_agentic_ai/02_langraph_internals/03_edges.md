# Edges in LangGraph

## 1. What is an Edge?

An **Edge controls what node runs next.**

```text
[research]
     │
     │ edge
     ▼
[summarize]
```

Nodes do the work. Edges decide the order.

The four core concepts together:

```text
        ┌───────────── GRAPH ─────────────┐
        │                                 │
        │   STATE (shared data)           │
        │   ┌───────────────────────┐     │
        │   │ {"topic": "...",      │     │
        │   │  "summary": "..."}    │     │
        │   └───────────────────────┘     │
        │        ▲            ▲           │
        │        │ read/write │           │
        │    [research] ──edge──► [summarize]
        │      NODE               NODE    │
        └─────────────────────────────────┘

STATE = the data     NODE = does work
EDGE  = what's next  GRAPH = all of them together
```

---

## 2. Normal Edge (always go here)

A normal edge has **one fixed destination**.

```text
START ──► [research] ──► [summarize] ──► END
```

```python
from langgraph.graph import START, END

graph.add_edge(START, "research")
graph.add_edge("research", "summarize")
graph.add_edge("summarize", END)
```

* `START` = where the graph begins
* `END` = where the graph stops
* `add_edge(A, B)` = "after A, always run B"

---

## 3. Conditional Edge (choose where to go)

A conditional edge **picks the next node using a function**.

```text
                    ┌─────────────┐
                    │ route(state)│  ← reads State
                    └──────┬──────┘
                           │ returns a name
              ┌────────────┴────────────┐
              ▼                         ▼
        "summarize"                 "search_more"
```

```python
def route(state):
    if state["enough_info"]:
        return "summarize"
    return "search_more"

graph.add_conditional_edges("research", route)
```

How it works:

```text
[research] ──► route(state) ──► returns "summarize" ──► [summarize]
```

The function returns the **name of the next node**. That's all routing is.

Optional: list the possible targets so the graph is clear.

```python
graph.add_conditional_edges(
    "research",
    route,
    {"summarize": "summarize", "search_more": "search_more"},
)
```

---

## 4. Putting It Together (with a loop)

Edges can point backwards. That creates a loop.

```text
START ──► [research] ──► route?
              ▲            │
              │            ├── not enough ──┐
              │            │                │
              └────────────┼────────────────┘
                           │
                           └── enough ──► [summarize] ──► END
```

```python
graph.add_edge(START, "research")
graph.add_conditional_edges("research", route, {
    "search_more": "research",   # loop back
    "summarize": "summarize",
})
graph.add_edge("summarize", END)
```

**Remember:**

```text
Normal edge       →  A ──► B             (fixed)
Conditional edge  →  A ──► f(state) ──►  B or C   (decided at runtime)
```