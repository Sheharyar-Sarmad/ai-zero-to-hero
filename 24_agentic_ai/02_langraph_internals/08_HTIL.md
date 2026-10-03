# Human-in-the-Loop (HITL)

> Flow so far: State → Nodes → Edges → Reducers → Graph Compilation → Checkpointing → Interrupts → **Human-in-the-Loop**

---

## 1. What is Human-in-the-Loop (HITL)?

**HITL means a human takes part in an agent workflow at an important point.** The agent does the work, but a person checks or guides it before it goes further.

Interrupt and HITL are not the same thing:

- **Interrupt** = a *mechanism*. It pauses the graph.
- **HITL** = a *pattern*. It uses that pause to involve a human.

```
 Agent works ──► INTERRUPT (pause) ──► HUMAN decides ──► Agent continues
                 [mechanism]            [HITL pattern]
```

---

## 2. Why HITL is Useful

Full automation is risky when actions are hard to undo, costly, or ambiguous. Common cases:

| Case | Example |
|---|---|
| Approve a sensitive action | Sending an email, making a payment |
| Review a decision or plan | Checking the agent's step-by-step plan |
| Correct information | Fixing a wrong recipient or amount |
| Provide missing information | Agent asks: "Which date do you want?" |

LLMs can be confident and still wrong. A human check keeps mistakes from reaching the real world.

**Example workflow:** a support agent drafts a refund reply → pauses → a human approves → the refund is sent.

---

## 3. How HITL Works with Interrupts

```
Agent ──► Interrupt ──► Pause ──► Human Review ──► Approve / Reject / Edit ──► Resume
```

**What happens to State while paused?**
Nothing changes. The State is saved in a **checkpoint** and stays frozen until the human responds. The graph is not running, so no compute is used while waiting.

```
 Node runs ──► State updated ──► Checkpoint saved ──► interrupt()
                                       │                    │
                                  (State is safe)      graph stops
                                       │                    │
                       Human answers ──┴──► Resume (same thread_id)
                                                    │
                                          continues from the checkpoint
```

Key terms, kept separate:

- **State** – the data the graph is working with.
- **Checkpoint** – a saved snapshot of that State.
- **Interrupt** – the pause point.
- **Thread ID** – the label that says *which* saved run to continue.
- **Resume** – restarts the graph from the checkpoint with the human's answer.

A checkpointer is required. Without a saved checkpoint, there is nothing to resume from.

---

## 4. Approval, Rejection, and Modification

The human's answer becomes the return value of `interrupt()`. Three common decisions:

| Decision | Result |
|---|---|
| **Approve** | Continue as planned |
| **Reject** | Stop, or route to another path |
| **Modify** | Update the data, then continue |

**Example:** an agent plans to email a customer.

```python
from langgraph.types import interrupt, Command

def approval_node(state):
    decision = interrupt({"draft": state["email"]})   # pause here

    if decision["action"] == "approve":
        return {"status": "approved"}
    if decision["action"] == "edit":
        return {"email": decision["email"], "status": "approved"}
    return {"status": "rejected"}                     # reject
```

Resume later with the same thread:

```python
config = {"configurable": {"thread_id": "t1"}}
graph.invoke(Command(resume={"action": "approve"}), config)
```

A conditional edge can then send `"approved"` to the send-email node and `"rejected"` to an end or fallback node.

---

## 5. Mental Model

```
User → Agent → Plan → Interrupt → Human → Decision → Resume → Next Node
```

Inside the broader LangGraph lifecycle:

```
State → Node → Update → Reducer → Checkpoint → Interrupt → Human → Resume
```

**Analogy:** an employee prepares a purchase order but cannot send it until the manager signs. The paperwork waits on the desk (checkpoint), the manager reviews it (human), and the employee continues once it is signed (resume).

**Interview-ready points**

1. HITL is a pattern; interrupt is the mechanism that enables it.
2. Pausing is only possible because State is saved in a checkpoint.
3. The thread ID identifies which paused run to resume.
4. The human can approve, reject, or modify, and the answer returns from `interrupt()`.
5. Use HITL for risky, irreversible, or uncertain actions.