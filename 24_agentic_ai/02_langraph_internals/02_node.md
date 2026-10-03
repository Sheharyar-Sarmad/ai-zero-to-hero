# Node In Langraph

## 1. What is a Node?

A Node is a **named unit of work**. It receives the current State, does something, and returns a **partial State update**.

```text
Current State
     │
     ▼
   NODE
     │
     ▼
State Update
```

```python
def greet(state):
    return {"message": "Hello"}
```

- `state` is the input: the current State.
- The function does its work (here, trivial).
- The returned dict is an *update*, not the whole State.

---

## 2. Nodes Inside a Graph

```text
START
  │
  ▼
[research]
  │
  ▼
[summarize]
  │
  ▼
 END
```

```python
graph.add_node("research", research)
graph.add_node("summarize", summarize)

graph.add_edge(START, "research")
graph.add_edge("research", "summarize")
graph.add_edge("summarize", END)
```

```text
Node  = does the work
Edge  = controls what runs next
Graph = complete workflow
State = information shared between nodes
```

(Edges get their own note next.)

---

## 3. What Happens Inside a Node?

A Node is only the execution unit. What it does inside is up to you:

```text
                 ┌── Python logic
                 │
State ──▶ NODE ──┼── LLM call
                 │
                 ├── Tool / API
                 │
                 └── Database
                      │
                      ▼
                 State Update
```

```python
def call_model(state):
    response = llm.invoke(state["messages"])
    return {"messages": [response]}
```

- An LLM is **not** a Node. A Tool is **not** a Node.
- They *run inside* a Node.
- The Node is the graph's callable execution unit.

---

## 4. How a Node Executes

```text
graph.invoke(input)
       │
       ▼
Runtime reaches Node
       │
       ▼
Node receives State
       │
       ▼
Node executes
       │
       ▼
Node returns update
       │
       ▼
State is updated
       │
       ▼
Next graph step
```

```text
add_node(...)  → registers the node
invoke(...)    → actually runs the graph
```

A Node normally returns a **partial update**: only the keys it wants to change. Keys it doesn't return stay as they were.

```text
State before:  {"topic": "AI", "summary": ""}
Node returns:  {"summary": "AI is ..."}
State after:   {"topic": "AI", "summary": "AI is ..."}
```

*How* an update is merged into State (overwrite vs. append) is decided by Reducers/Channels, which come later.

---

**Roadmap:** Node → Edges → Compilation → Pregel Runtime → Reducers/Channels