# Error Handling

> **Journey so far:** State → Nodes → Edges → Reducers → Graph Compilation → Checkpointing → Interrupts → HITL → Streaming → Subgraphs → **Error Handling**
>
> Subgraphs made our workflows bigger. Bigger workflows have more places to break, so now we learn how to handle failures.

---

## 1. What is Error Handling?

**Simplest English:** Error handling is deciding *what the graph should do when something goes wrong*, instead of just crashing.

During a run, a node may call an LLM, an API, a database, or a tool. Any of these can fail. If nothing handles the failure, the exception bubbles up and the **whole graph run stops**.

```
Node → Tool/API → ❌ Error → Error Handling → Retry / Fallback / Stop
```

### Expected vs Unexpected Failures

| | Expected failure | Unexpected failure |
|---|---|---|
| **Meaning** | We saw it coming and can recover | A bug or unknown problem |
| **Examples** | Timeout, rate limit, empty search result | Code bug, corrupted state, `KeyError` |
| **What to do** | Handle it: retry, fallback, reroute | Let it surface (stop and report) |

**Rule of thumb:** handle what you can predict; don't hide what you can't. Silencing unknown errors makes bugs harder to find.

### Simple Agentic Example

A research agent calls a `web_search` tool. The search API times out.

- **Without handling:** the whole run crashes, and the user gets nothing.
- **With handling:** retry once, then fall back to a different search tool, then continue the answer.

---

## 2. Types of Failures in Agentic Workflows

```
                ┌─ API / network failure
                ├─ Tool failure
                ├─ Timeout
Graph run ──────┼─ Rate limit
                ├─ Invalid tool input
                ├─ LLM / provider failure
                └─ Database / storage failure
```

| Failure | One-line meaning | Usually... |
|---|---|---|
| **API / network** | Connection dropped or service unreachable | Temporary → retry |
| **Tool failure** | The tool itself raised an error | Depends → retry or fallback |
| **Timeout** | Call took too long | Temporary → retry |
| **Rate limit** | Too many requests (e.g., HTTP 429) | Temporary → retry with a wait |
| **Invalid tool input** | LLM gave bad arguments to a tool | Not temporary → send the error back to the LLM to fix |
| **LLM / provider failure** | Model API is down or errors out | Fallback to another model |
| **Database / storage** | Checkpointer or app DB can't read/write | Retry, or stop; losing state is serious |

**Key idea:** failures are either **temporary** (retrying may work) or **permanent** (retrying won't help). Your strategy depends on which one it is.

---

## 3. Recovery Strategies

| Strategy | Meaning | Use when |
|---|---|---|
| **Retry** | Try the same operation again | Failure is temporary (timeout, network blip, rate limit) |
| **Fallback** | Use another model, tool, provider, or path | The primary option keeps failing or is down |
| **Graceful failure** | Return a controlled error message instead of crashing | Recovery isn't possible, but the user should still get a clear result |
| **Conditional routing** | Send execution to a dedicated recovery node | Different errors need different handling |

### Practical Workflows

**Retry**
```
Agent → Tool → ❌ Error → Retry → ✅ Success
```

**Fallback**
```
Agent → Tool A → ❌ Error → Fallback (Tool B) → ✅ Continue
```

**Graceful failure**
```
Agent → Tool → ❌ Error → Retry ×3 still fails → "Sorry, search is unavailable right now"
```

### Choosing a Strategy (high level)

```
Is the error temporary?
 ├─ Yes → Retry (with a limit!)
 │         └─ Still failing? → Fallback
 └─ No  → Is there an alternative? 
           ├─ Yes → Fallback
           └─ No  → Graceful failure (or stop)
```

> Always **limit retries**. Infinite retries can loop forever and burn money.

---

## 4. Error Handling Inside LangGraph

Errors can be handled at three levels:

| Level | How |
|---|---|
| **Tool level** | Catch the exception inside the tool; return an error message the LLM can read |
| **Node level** | Wrap risky code in `try/except`, or attach a **retry policy** to the node |
| **Workflow level** | Use **conditional edges** to route to a recovery node based on state |

```
Node → Tool → Exception → Catch/Handle → State/Route
```

The pattern: **catch the error → write it into state → let an edge decide where to go next.**

```
          ┌── no error ──→ next_node
call_tool ┤
          └── error ─────→ recover_node (fallback / graceful message)
```

### Tiny Example

```python
from langgraph.types import RetryPolicy

def call_tool(state):
    try:
        return {"result": search(state["query"]), "error": None}
    except TimeoutError as e:
        return {"error": str(e)}          # save the error in state

def route(state):
    return "recover" if state["error"] else "next"

# Retry automatically on unhandled exceptions
builder.add_node("call_tool", call_tool, retry_policy=RetryPolicy(max_attempts=3))
builder.add_conditional_edges("call_tool", route, {"recover": "recover", "next": "next"})
```

> **Heads-up:** a retry policy triggers when the node *raises*. If you catch the exception yourself and return normally, the retry policy won't fire. Choose one approach per failure type.

### Who Does What?

- **LangGraph provides:** graph execution, retry policies on nodes, conditional routing, and checkpointing.
- **You provide:** deciding *which* errors are retryable, *what* the fallback is, and *what message* the user sees. Application-specific recovery logic belongs to the developer.

---

## 5. Best Practices & Summary

### Best Practices

1. **Handle expected errors, surface unexpected ones.** Don't use a blanket `except: pass`.
2. **Retry only temporary failures,** and always set a max attempt limit.
3. **Store errors in state** (e.g., an `error` field) so routing and debugging are easy.
4. **Return tool errors to the LLM** for invalid input so it can correct itself.
5. **Always have a final exit:** a graceful failure message beats a silent crash.
6. **Use checkpointing:** if a run does fail, the saved state lets you resume instead of starting over.

### Quick Summary

```
Failure happens
   ↓
Temporary?  → Retry
Still failing / permanent? → Fallback
Nothing works? → Graceful failure
Unknown bug? → Let it surface
```

| Concept | Remember |
|---|---|
| Expected failure | Handle it |
| Unexpected failure | Surface it |
| Retry | Same operation, again |
| Fallback | Different operation |
| Graceful failure | Controlled error, not a crash |
| Conditional routing | State decides the recovery path |

**Next:** with errors handled, we can look at making graphs more robust and production-ready.