# Streaming

`State → Nodes → Edges → Reducers → Graph Compilation → Checkpointing → Interrupts → HITL → Streaming`

## 1. What is Streaming?

Streaming means you receive output **while the graph is still running**, instead of waiting for it to finish.

- **Normal execution** (`invoke`): wait until the graph finishes → get the final result.
- **Streaming** (`stream`): get useful pieces of output as they happen.

```
Graph starts → event/update/token → client receives → more events → final result
```

**AI-chat example:** in a chat app, the answer appears word by word. The user starts reading immediately instead of staring at a spinner for 10 seconds.

## 2. What Can LangGraph Stream?

```
              graph.stream() / graph.astream()
                          │
      ┌─────────┬─────────┼─────────┬──────────┐
  messages   updates    values    custom   checkpoints / tasks / debug
```

| Mode | What you get |
|---|---|
| `messages` | LLM token / message chunks |
| `updates` | Only the State changes a node just produced |
| `values` | The full State after each step |
| `custom` | Progress/status events your nodes emit |
| `checkpoints` / `tasks` / `debug` | Execution details for debugging |

**Token streaming vs State/event streaming:**

- **Token streaming** (`messages`) → the *text* the LLM is generating, piece by piece.
- **State/event streaming** (`updates`, `values`, `custom`) → *what the graph is doing*: which node finished, what changed in State, what progress was reported.

LangGraph provides all of this natively through `stream()` / `astream()`.

## 3. How Streaming Works in an Agentic Workflow

```
User → Agent Node → Tool → Agent Node → Final Answer
```

What can be streamed along the way:

```
token → tool event → node update → token → final state
```

**Important:** streaming does **not** change how the graph executes. The same nodes run in the same order. Streaming just lets the consumer *observe* progress as it happens.

```python
for mode, chunk in graph.stream(
    {"messages": [("user", "Weather in Paris?")]},
    stream_mode=["messages", "updates"],
):
    print(mode, chunk)  # tokens and node updates, as they occur
```

Passing a list of modes gives `(mode, chunk)` pairs. Use `astream()` the same way with `async for` in async code.

## 4. LangGraph Streaming → FastAPI → Frontend

LangGraph already handles **graph-level streaming**. You don't need another AI framework just to stream its output. What you need is a **transport** to carry the stream to the browser:

```
LangGraph → FastAPI → HTTP stream → Next.js/browser
```

- **LangGraph** = *produces* the stream.
- **FastAPI + HTTP** = *delivers* the stream.

**Server-Sent Events (SSE)** is the practical default. It is a one-way stream from server to client, which is exactly what an AI answer or progress feed is. Modern FastAPI has native SSE support via `EventSourceResponse` (check your installed version's docs).

**WebSockets** are for when client and server both need to send messages continuously over one connection (e.g., live collaboration, real-time games).

| | SSE | WebSocket |
|---|---|---|
| Direction | Server → client | Both ways |
| Best for | AI responses, progress updates | Interactive two-way apps |
| Complexity | Low | Higher |

For Next.js + FastAPI + LangGraph projects, a good production architecture is:

```
LangGraph streaming → FastAPI SSE → Next.js client
```

## 5. Mental Model

```
Graph Execution → LangGraph Stream → FastAPI/SSE → Frontend
```

```
Token / State Update / Event → Client receives it immediately
```

**Analogy:** watching a live game vs. waiting for the final score. Streaming is the live broadcast; `invoke` is the scoreboard after the whistle.

**Interview-ready points:**

1. Streaming delivers output during execution; `invoke` returns only at the end.
2. `stream()` / `astream()` are native LangGraph features, with modes like `messages`, `updates`, `values`, and `custom`.
3. Token streaming (`messages`) is different from State/event streaming (`updates`, `values`, `custom`).
4. Streaming doesn't change graph logic; it only exposes progress to consumers.
5. LangGraph produces the stream; FastAPI SSE delivers it. Use WebSockets only when you need two-way communication.