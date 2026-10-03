# Interrupts vs Human-in-the-Loop

> Flow so far: ... → Checkpointing → Interrupts → Human-in-the-Loop → **Interrupts vs HITL**

---

## 1. The Core Difference

- **Interrupt** = a *mechanism*. It pauses the graph.
- **HITL** = a *pattern*. It uses that pause to involve a human.

```
Interrupt  →  "Stop here."
HITL       →  "Stop here, ask a human, then continue."
```

An interrupt can exist without a human. HITL cannot exist without an interrupt (or a similar pause).

---

## 2. Side-by-Side

| | Interrupt | HITL |
|---|---|---|
| What it is | A pause in execution | A workflow design |
| Level | Low-level tool | High-level pattern |
| Purpose | Stop the graph | Get human input or approval |
| Needs a human? | Not necessarily | Always |
| Needs a checkpoint? | Yes | Yes (through the interrupt) |
| In code | `interrupt()` | Interrupt + human decision + resume |

---

## 3. How They Fit Together

```
Node runs → State saved (checkpoint) → interrupt() → [PAUSE]
                                                        │
                                          HITL: human reviews
                                                        │
                                   Approve / Reject / Edit
                                                        │
                                  Command(resume=...) → continue
```

- **Checkpoint** saves the State so nothing is lost.
- **Thread ID** says which paused run to continue.
- **Resume** restarts the graph with the human's answer.

---

## 4. Interrupt Without HITL

Interrupts are not only for humans. You might pause to:

- Wait for an external system or event.
- Debug and inspect State at a certain step.
- Hold a run until a condition is met.

No human decision is involved, so this is **not** HITL.

---

## 5. Tiny Example

```python
from langgraph.types import interrupt

def approval_node(state):
    answer = interrupt({"draft": state["email"]})  # interrupt = pause
    return {"approved": answer == "yes"}           # HITL = human's answer used
```

The `interrupt()` call is the mechanism. Using the human's answer to decide what happens next is the HITL pattern.

---

## 6. Analogy

A **red traffic light** is the interrupt: it stops the cars.
A **traffic officer waving cars on** is HITL: a person decides when to go.

---

## 7. Interview-Ready Points

1. Interrupt pauses execution; HITL uses the pause for human involvement.
2. HITL is built on top of interrupts.
3. Both rely on checkpoints, a thread ID, and resume.
4. Not every interrupt is HITL.
5. Use HITL for risky, irreversible, or uncertain actions.