# Architectural Overview: Subgraphs & Advanced Streaming in LangGraph

## 1. Subgraphs (Modular Architecture)
Subgraphs allow nesting a fully compiled `StateGraph` inside a parent graph as a modular node. 
* **Benefits:** Encapsulates internal logic, prevents state namespace pollution, and enables isolated testing.
* **Integration Patterns:**
  * **Direct Node Addition:** Used when parent and subgraph share identical state keys (data flows automatically through shared channels).
  * **Wrapper Function Node:** Used when state schemas differ; maps parent keys to subgraph inputs and translates outputs back.

---

## 2. Token-by-Token Streaming (`stream_mode="messages"`)
* **Mechanism:** Taps directly into intermediate LLM token generation across nodes in real-time.
* **Server-Sent Events (SSE):** Intercepts raw token chunks from model execution and formats them into standard SSE protocol strings (`data: <token>\n\n`, terminating with `data: [DONE]\n\n`) for web clients.

---

## 3. Event-by-Event Streaming (`stream_mode="updates"`)
* **Mechanism:** Yields execution control the exact moment any node finishes running.
* **Payload:** Returns only the incremental state update dictionary produced by that specific node.
* **Use Case:** Powers real-time progress trackers, step-by-step logs, and live UI dashboards as multi-agent workflows progress.