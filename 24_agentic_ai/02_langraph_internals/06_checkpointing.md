# Checkpointing

> Flow so far: **State → Nodes → Edges → Reducers → Graph Compilation → Checkpointing**
> You've built and compiled a graph. Now: how do we *save* its progress?

---

## 1. What is Checkpointing?

Checkpointing means **saving the graph's State at points during execution**, so progress isn't lost.

- **State** = the current working information (lives in memory while the graph runs)
- **Checkpoint** = a saved snapshot of that State at a specific moment

```
        State (live, in memory)
   ┌──────────────────────────────┐
   │ messages: [...]              │
   │ step: 2                      │
   └──────────────┬───────────────┘
                  │ snapshot
                  ▼
        Checkpoint (saved copy)
   ┌──────────────────────────────┐
   │ messages: [...]              │
   │ step: 2                      │
   └──────────────────────────────┘
```

State keeps changing. A checkpoint is frozen — a record of what State looked like *then*.

---

## 2. Why Checkpointing is Needed

Agent workflows can be long and multi-step. If State only lives in memory, it disappears when the process stops (crash, deploy, restart).

```
WITHOUT checkpointing              WITH checkpointing

Node A ✔                           Node A ✔ → 💾 saved
Node B ✔                           Node B ✔ → 💾 saved
Node C ✔                           Node C ✔ → 💾 saved
  💥 process stops                   💥 process stops
  ▼                                  ▼
State lost                         Restart
Start over from Node A ❌           Load last checkpoint
                                   Continue after Node C ✅
```

With checkpoints, an agent **survives restarts**: it reloads its last saved State instead of forgetting everything.

---

## 3. How Checkpointing Works

The lifecycle repeats as the graph runs:

```
Graph executes → State changes → Checkpoint saved → Graph continues
       ▲                                                   │
       └───────────────────────────────────────────────────┘
```

- Each saved checkpoint preserves the State at that point, so together they form the **history** of an execution.
- The component that does the saving is the **checkpointer**. You give it to the graph when you compile:

```python
from langgraph.checkpoint.memory import InMemorySaver

checkpointer = InMemorySaver()
graph = builder.compile(checkpointer=checkpointer)
```

| Term | Meaning |
|---|---|
| State | Current working data |
| Checkpoint | Saved snapshot of State |
| Checkpointer | The component that saves/loads checkpoints |

(`InMemorySaver` is just for learning; real persistence uses other checkpointers — covered later.)

---

## 4. Threads / Conversations and Checkpoints

Checkpoints need an address. A **thread** is a unique ID that groups the checkpoints of one conversation or run.

```
User → Thread → Graph execution → Checkpoints → Resume
 │       │            │                │           │
Alice  "thread-1"   runs nodes     saved under   same thread_id
                                    "thread-1"   loads latest one
```

You pass the `thread_id` in the config on every call:

```python
config = {"configurable": {"thread_id": "thread-1"}}

graph.invoke({"messages": ["Hi, I'm Sam"]}, config)
graph.invoke({"messages": ["What's my name?"]}, config)  # remembers Sam
```

- **Same `thread_id`** → continues from previously saved State.
- **New `thread_id`** → fresh, independent conversation.

Without a `thread_id`, the checkpointer doesn't know which saved State belongs to whom.

---

## 5. Mental Model

```
State → Node → State Update → Checkpoint → Next Node
```

And across a restart:

```
Checkpoint → Restart → Resume
```

**Analogy:** a save point in a video game. You play (State changes), the game saves (Checkpoint), you quit (Restart), and later you load your save and continue (Resume). Your *save slot* is the thread.

**Interview-ready points**
- State is live working data; a checkpoint is a saved snapshot of it.
- A checkpointer saves and loads checkpoints; you attach it at `compile()`.
- Checkpointing makes agents persistent and able to survive restarts.
- A `thread_id` identifies one conversation's checkpoints; reuse it to resume.
- Different thread IDs give isolated conversations.