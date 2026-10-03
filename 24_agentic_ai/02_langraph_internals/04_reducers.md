# Reducers

## 1. What is a Reducer?

A reducer defines **how a Node's update is merged into an existing State field**.

```text
Existing State
      │
      ├── messages = [A]
      │
      ▼
 Node returns
 {"messages": [B]}
      │
      ▼
   Reducer
      │
      ▼
New State
messages = [A, B]
```

```text
Without reducer → replace
With reducer    → combine according to the reducer
```

## 2. Overwrite vs Accumulate

**Overwrite (default):**

```python
class State(TypedDict):
    answer: str
```

```text
answer = "old"

Node returns:
{"answer": "new"}

Result:
answer = "new"
```

**Accumulate (with a reducer):**

```python
import operator
from typing import Annotated, TypedDict

class State(TypedDict):
    items: Annotated[list, operator.add]
```

```text
Before: [A]
Update: [B]

Reducer:
[A] + [B]

After:
[A, B]
```

> A reducer is attached to a **State field**, not to a Node.

## 3. Why Reducers Matter

When several nodes update the same field, LangGraph needs a rule for combining those updates.

```text
             ┌── [Node A] ──▶ {"items": [A]}
State ───────┤
             └── [Node B] ──▶ {"items": [B]}
                         │
                         ▼
                      Reducer
                         │
                         ▼
                    [A, B]
```

Without a reducer, one update would simply replace the other.

The most common reducer is `add_messages`, used for chat history:

```python
from langgraph.graph.message import add_messages

class State(TypedDict):
    messages: Annotated[list, add_messages]
```

```text
Old:    [Human("Hi")]
Update: [AI("Hello")]

Result:
[Human("Hi"), AI("Hello")]
```

`add_messages` is message-aware: it appends new messages, and it can also update a message that has the same ID.

## 4. Mental Model

```text
Node
  │
  │ returns update
  ▼
{"messages": [new_message]}
  │
  ▼
Reducer
  │
  ├── overwrite
  ├── add
  └── custom merge rule
  │
  ▼
Updated State
```

```text
State field = data
Reducer     = update rule
Node        = produces the update
Runtime     = applies the rule
```

```text
No reducer:
[A] + [B] → [B]

Reducer:
[A] + [B] → [A, B]
```