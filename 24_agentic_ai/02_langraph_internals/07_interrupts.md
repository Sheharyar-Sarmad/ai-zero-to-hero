# Interrupts

`State → Nodes → Edges → Reducers → Graph Compilation → Checkpointing → **Interrupts**`

Checkpointing saved our progress. Interrupts are the first big thing we can *do* with it.

---

## 1. What is an Interrupt?

An **interrupt** is a deliberate pause. The graph stops at a chosen point and waits, so a human (or your application) can **inspect, approve, modify, or provide something** before execution continues.

- **Normal execution** → the graph keeps running, node after node, until `END`.
- **Interrupt** → the graph pauses and waits for input.

```
Normal:     [Node A] ──▶ [Node B] ──▶ [Node C] ──▶ END

Interrupt:  [Node A] ──▶ [Node B] ──⏸  (waiting for input...)
                                     └──▶ [Node C] ──▶ END   (only after resume)
```

---

## 2. Why Interrupts are Useful

Agents can act on the real world. Sometimes they should not act alone.

- **Approval before an important action** – "Send this email to 500 customers?"
- **Reviewing a planned action** – the agent shows its plan; you say yes or no.
- **Editing State before continuing** – fix a wrong value the agent produced.
- **Asking for missing information** – "Which date should I book?"

```
User request
     │
     ▼
[Agent drafts email] ──▶ ⏸ Human reviews
                              │
                 ┌────────────┴────────────┐
              approve                    reject / edit
                 ▼                         ▼
          [Send email]             [Revise draft]
```

---

## 3. What Actually Happens During an Interrupt?

```
Node starts → interrupt occurs → execution pauses → State/checkpoint saved → resume later
```

```
 ┌────────┐   interrupt()   ┌────────┐   save   ┌────────────┐
 │  Node  │ ───────────────▶│ PAUSED │ ───────▶ │ Checkpoint │
 └────────┘                 └────────┘          │ (State +   │
                                                │  position) │
                                                └────────────┘
```

How the pieces connect:

- **State** = the data the graph is carrying.
- **Checkpoint** = a saved snapshot of that State *and* where the graph stopped.
- **Interrupt** = the pause that triggers the save and the wait.

The checkpoint is what lets the workflow **remember where it stopped**. Without a checkpointer, an interrupt has nothing to pause *into*, so you must compile the graph with one.

---

## 4. Interrupt → Resume

- **Interrupt = pause**
- **Resume = continue**

You resume by calling the graph again with `Command(resume=...)`. The value you pass becomes the answer the paused node was waiting for.

```python
from langgraph.types import interrupt, Command

def approval_node(state):
    answer = interrupt("Approve this email?")   # pauses here
    return {"approved": answer}                 # runs after resume

graph = builder.compile(checkpointer=checkpointer)
config = {"configurable": {"thread_id": "user-1"}}

graph.invoke({"draft": "Hello!"}, config)       # runs, then pauses
graph.invoke(Command(resume=True), config)      # continues with True
```

**Why `thread_id` matters:** a **thread** is one conversation/execution, and checkpoints are saved per thread. Using the same `thread_id` tells LangGraph *which* paused run to continue. A different `thread_id` would start a separate run.

```
invoke(..., thread_id="user-1") ──▶ ⏸ saved under "user-1"
invoke(Command(resume=...), thread_id="user-1") ──▶ loads that checkpoint ──▶ continues
```

---

## 5. Mental Model

```
Node → Interrupt → Checkpoint → Pause → Resume → Next Node
```

The broader lifecycle:

```
State → Node → Update → Reducer → New State → Checkpoint → Interrupt / Resume
```

**Analogy:** playing a video game. You hit a **save point** (checkpoint), **pause** (interrupt), close the game, and later **load the same save** (thread) and **press continue** (resume).

**Interview-ready points**

1. An interrupt pauses graph execution so a human or app can provide input.
2. Interrupts depend on **checkpointing**; no checkpointer, no pause/resume.
3. The checkpoint stores State and the position where the graph stopped.
4. `Command(resume=...)` continues the run and supplies the awaited value.
5. `thread_id` identifies which paused execution to resume.