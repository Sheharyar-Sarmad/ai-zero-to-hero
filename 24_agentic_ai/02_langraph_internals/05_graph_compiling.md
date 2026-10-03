# Graph Compilation

> **Journey so far:** `State → Nodes → Edges → Reducers → Graph Compilation`
> We have the pieces. Now we turn them into something that can actually run.

---

## 0. First, What Exactly is "the Graph"?

Before compiling it, let's be clear about what we are compiling.

A **graph** is just a set of **steps** connected by **arrows**. In LangGraph:

- **Nodes** = the steps (Python functions that do work: call an LLM, run a tool, etc.)
- **Edges** = the arrows (which step runs next)
- **State** = the shared data every node reads from and writes to
- **Reducers** = the rules for merging each node's update into the state

```
   START ──► [ Node A ] ──► [ Node B ] ──► END
                 │              ▲
                 └──── state flows through every node ────┘
```

**Why a graph and not just a simple chain/script?**

| A plain chain | A LangGraph graph |
|---|---|
| Always runs steps in one fixed line | Can **branch** (conditional edges: "if X go here, else there") |
| No going back | Can **loop** (e.g., LLM → tool → LLM until done) |
| Data passed manually between steps | One **shared state** updated at every step |

That ability to branch and loop is exactly what **agents** need: *think → act → observe → think again*.

**The two kinds of edges**

```
 Normal edge:        [A] ─────────► [B]          (always go A → B)

 Conditional edge:           ┌────► [Tool]
                      [LLM] ─┤                   (a function decides
                             └────► END           which way to go)
```

**Building a graph (still just a blueprint!)**

```python
builder = StateGraph(State)            # state schema (with reducers)

builder.add_node("llm", llm_node)      # nodes = steps
builder.add_node("tool", tool_node)

builder.add_edge(START, "llm")         # edges = flow
builder.add_conditional_edges("llm", route)   # branch: tool or END
builder.add_edge("tool", "llm")        # loop back
```

At this point nothing can run yet — `builder` is only a **description** of the workflow. That is the job of **compilation**, which is what the rest of these notes cover.

---

## 1. What is Graph Compilation?

`compile()` is the step that turns your **graph blueprint** into a **runnable graph**.

In simple words: until you call `compile()`, you only have a *description* of a workflow. After `compile()`, you have a *working machine*.

**Building (defining) vs. Compiling**

| | Building / Defining | Compiling |
|---|---|---|
| What you do | `add_node`, `add_edge`, `add_conditional_edges` | `builder.compile()` |
| What it is | Drawing the plan | Validating and preparing the plan |
| Object | `StateGraph` (builder) | Compiled graph (executable) |
| Can you run it? | No | Yes |

**Why is compilation needed?**
- To **catch mistakes early** (e.g., an edge pointing to a node that doesn't exist) *before* anything runs.
- To **prepare the graph for execution** (wire up state, reducers, and the order of steps).
- To give you a **ready-to-use object** with methods like `invoke()` and `stream()`.

```
   DEFINE                       COMPILE                      READY
┌───────────────┐          ┌───────────────┐          ┌─────────────────┐
│  StateGraph   │          │               │          │  Compiled Graph │
│  (blueprint)  │ ───────► │   compile()   │ ───────► │  (executable)   │
│ nodes + edges │          │ check+prepare │          │ invoke / stream │
└───────────────┘          └───────────────┘          └─────────────────┘
```

> Think of it like a **recipe vs. a cooked-ready kitchen**: the recipe (builder) lists the steps; `compile()` checks you have every ingredient and sets up the kitchen so you can start cooking.

---

## 2. What Happens During Compilation?

At a high level, `compile()` **checks and prepares** everything you defined earlier.

```
                    builder.compile()
                           │
        ┌──────────────────┼──────────────────┐
        ▼                  ▼                  ▼
   ┌─────────┐       ┌───────────┐       ┌───────────┐
   │ STRUCTURE│       │   STATE   │       │ EXECUTION │
   │  checks  │       │   setup   │       │   ready   │
   └─────────┘       └───────────┘       └───────────┘
   • Entry point      • State schema      • Graph is
     exists (START)     is read             runnable
   • Edges point      • Reducers are      • Optional extras
     to real nodes      attached to         (e.g. checkpointer)
   • No broken/         each state key       are plugged in
     orphan nodes
```

**How it connects to what we've learned:**

| Concept | What compile does with it |
|---|---|
| **State** | Reads the state schema so the graph knows what keys exist |
| **Nodes** | Confirms every node referenced actually exists |
| **Edges** | Confirms the flow is valid: starts at `START`, connects properly, can reach `END` |
| **Reducers** | Attaches each key's reducer so updates get merged correctly at runtime |

> 💡 If something is wrong with your structure, you'll usually get the error at `compile()` time, **not** halfway through a run.

*(We stop here on purpose — the deep runtime internals are a later topic.)*

---

## 3. `compile()` vs `invoke()`

| | `compile()` | `invoke()` |
|---|---|---|
| Purpose | **Prepares** the graph | **Runs** the graph |
| Called on | The builder (`StateGraph`) | The compiled graph |
| Input | Nothing (just the structure) | Initial state |
| Output | Executable graph | Final state (result) |
| How often | Once | As many times as you like |

**The full lifecycle:**

```
 Define  ──►  Compile  ──►  Invoke  ──►  State Updates  ──►  Result
   │            │            │               │                 │
 nodes,      validate &    pass input     nodes run,        final state
 edges,      prepare       state          reducers          returned
 state                                    merge updates
```

> Compile **once**, invoke **many times** — each `invoke()` is a fresh run of the same workflow.

---

## 4. Compiled Graph as an Executable Workflow

`graph.compile()` returns a **compiled graph** — an object you can run like a program.

```python
graph = builder.compile()                         # blueprint → executable

result = graph.invoke({"messages": ["Hello"]})    # run it with initial state
```

That's it. Two lines:
1. `compile()` → get the runnable graph.
2. `invoke(input_state)` → run the workflow and get the final state back.

**Connecting to an agentic workflow:**

```
 User question
      │
      ▼
 graph.invoke(...)
      │
      ▼
 ┌──────────┐    ┌──────────┐    ┌──────────┐
 │  LLM     │──► │  Tool    │──► │  LLM     │──► Final answer
 │  node    │    │  node    │    │  node    │
 └──────────┘    └──────────┘    └──────────┘
      ▲  State is updated (via reducers) after every node  ▲
```

The compiled graph is your **agent**: it receives input, loops through nodes and edges, updates state at each step, and returns the result.

---

## 5. Mental Model

```
┌─────────┐   ┌─────────┐   ┌─────────┐   ┌───────────┐
│  State  │ + │  Nodes  │ + │  Edges  │ + │ Reducers  │
│ (data)  │   │ (work)  │   │ (flow)  │   │ (merging) │
└────┬────┘   └────┬────┘   └────┬────┘   └─────┬─────┘
     └─────────────┴──────┬──────┴──────────────┘
                          ▼
                    ┌───────────┐
                    │ compile() │   check + prepare
                    └─────┬─────┘
                          ▼
                 ┌──────────────────┐
                 │ Executable Graph │
                 └─────────┬────────┘
                           ▼
                    ┌────────────┐
                    │  invoke()  │   run → state updates → result
                    └────────────┘
```

**One-line summary:** *State holds data, nodes do work, edges set the path, reducers merge updates, `compile()` makes it runnable, `invoke()` runs it.*

### Interview-Ready Points

1. **`compile()` turns a `StateGraph` blueprint into an executable graph.**
2. **Defining ≠ running** — you must compile before you can `invoke()`.
3. **Compilation validates structure early** (missing nodes, bad edges) instead of failing mid-run.
4. **Compile once, invoke many times.**
5. **`invoke()` runs the compiled graph**, applying node updates through reducers and returning the final state.