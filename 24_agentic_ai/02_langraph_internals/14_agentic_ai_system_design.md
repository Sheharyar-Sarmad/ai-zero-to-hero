# Agentic AI System Design

> Focus: the architecture *around* the agent (scale, safety, operations). No LangGraph syntax. LangGraph is the example orchestrator, not a requirement.

---

## 1. What is Agentic AI System Design?

```text
User → LLM → LLM + Tools → Agent → Agent + State → Agent + Memory
     → Multi-step workflow → Production Agentic System
```

| Term | Meaning |
|---|---|
| **LLM application** | Fixed, developer-defined flow that calls a model |
| **Agent** | A loop where the *model* chooses the next action (tool) until done |
| **Multi-agent system** | Several agents with different roles/tools coordinating |
| **Agentic workflow** | Developer-defined graph with LLMs at some nodes; *code* picks the path |
| **Production agentic platform** | All of the above plus auth, queues, persistence, streaming, safety, monitoring, cost control |

**Agent vs workflow:** in a workflow, code decides the path; in an agent, the model does. Use the least autonomy that solves the problem, because every bit of autonomy costs latency, money, testability and safety.

**How it differs from a normal web app:**

- **Non-deterministic:** same input, different output; can fail *quietly* (HTTP 200, wrong answer).
- **Tool calls:** side effects chosen at runtime by a model.
- **Multi-step and long-running:** seconds to hours, so one HTTP request is the wrong container.
- **State and memory:** rich per-run state, plus knowledge kept across sessions.
- **Streaming:** progress must be visible during slow work.
- **External dependencies:** LLM providers and many tools, each with limits and failures.
- **Cost and latency variance:** per token, per step; a run may take 2 s or 90 s.

---

## 2. Production Architecture and Runtime

```text
USER → Frontend/API → Auth/Rate limit → Load balancer → Agent API (stateless)
          ┌───────────────┴───────────────┐
          ▼                               ▼
    Agent Runtime                       Queue → Workers
          │
   ┌──────┼───────┐
   ▼      ▼       ▼
  LLMs   Tools   Memory (Redis / SQL / Vector DB / Object storage)
          │
   Checkpoints → Streaming/Events → Monitoring/Tracing
```

**Why each layer exists**

| Layer | Problem it solves |
|---|---|
| Auth / rate limit | Who is calling, and how much may they consume (tokens and steps, not just requests) |
| Load balancer | Spreads traffic, removes unhealthy nodes, must tolerate long-lived streams |
| Stateless API | Scale and restart freely; holds no run state |
| Queue + workers | Decouples accepting a run from executing it; absorbs bursts, enables retries, lets runs outlive connections |
| Agent runtime | Executes steps uniformly: load state, run, merge, checkpoint, emit events |
| LLM gateway | Model switching, fallback, cost metering |
| Tools | All side effects and external data; the permission boundary |
| Redis | Caches, rate-limit counters, locks, pub/sub for streaming |
| SQL | Durable truth: users, threads, runs, approvals, audit |
| Vector DB | Semantic recall of relevant knowledge |
| Checkpoints | Resume after crash, pause for humans, debug |
| Streaming | Turns slow multi-step work into visible progress |
| Tracing | Explains a non-deterministic system |

**Queue vs direct execution:** direct runs the agent inside the request (simple, low latency, dies with the process). Queue decouples execution (durable, scalable, more moving parts). Short chat can be direct; long or risky work should be queued.

**Tool vs node:** a node is an orchestration step you control; a tool is a capability the model may *request*. The model never executes anything. Your runtime validates, authorises and runs the call.

**The run lifecycle**

```text
Request → Thread ID → load latest checkpoint → graph starts → node executes
→ tool call → tool result → reducer → updated state → checkpoint → next step
→ (interrupt → resume) → streaming events → final response
```

- **Thread:** the conversation container and partition key. **Checkpoint:** one saved snapshot within it. A thread is not a checkpoint.
- **Reducers** define how updates merge, which makes parallel branches and retries safe.
- **Loops** must be bounded (max steps, tokens, cost, wall-clock time).
- **Parallel tool calls** cut latency but multiply burst load downstream, so cap concurrency.
- **Interrupt** persists state and releases compute; **resume** can run on a different worker.
- **Concurrent runs on one thread** can corrupt state. Serialise per thread, reject with 409, or queue behind the active run.
- **Run status** (queued, running, interrupted, completed, failed, cancelled, budget_exceeded) belongs in SQL so your API and UI don't depend on framework internals.

**Concurrency vs parallelism:** concurrency is one worker juggling many runs while they wait on I/O; parallelism is simultaneous branches inside one run. Agents are I/O-bound, so you need lots of concurrency.

---

## 3. State, Memory, and Persistence

| Term | What it is |
|---|---|
| **State** | Working data of the current run |
| **Checkpoint** | Durable snapshot of state at a step boundary |
| **Thread** | Conversation container holding the run/checkpoint history |
| **Short-term memory** | What the agent sees within the thread (recent messages, summary) |
| **Long-term memory** | Knowledge kept across threads (preferences, facts) |
| **Vector memory** | Long-term memory stored as embeddings |
| **Cache** | Disposable speed copy |

```text
Current execution → State → Checkpoint → Thread history → Long-term storage
```

**State vs memory:** state is this run's scratchpad; memory is deliberately kept for later. **Memory vs persistence:** memory is a purpose (what the agent can recall); persistence is a mechanism (data survives). A checkpoint is persistent but is not memory.

**Which store**

| Store | Use for |
|---|---|
| **Redis** | Hot/ephemeral: caches, rate limits, locks, stream fan-out |
| **PostgreSQL** | Durable, transactional: users, threads, runs, audit, checkpoints, structured memory (pgvector at moderate scale) |
| **MongoDB** | Flexible-schema transcripts or heterogeneous tool output, if you already run it |
| **Vector DB** | Semantic retrieval of documents and past facts |
| **Object storage** | Large blobs: files, big tool outputs, exports |

Default: Postgres for durable data, Redis for speed, object storage for blobs. Keep state small: store large artifacts by reference, since every checkpoint copies state.

**Why not dump the whole conversation into every prompt?** An agent makes many LLM calls per turn, so a growing history multiplies cost, slows time-to-first-token, hits context limits, and buries relevant details in noise.

```text
Full history (kept in DB)
  ├─ Sliding window      → recent turns verbatim
  ├─ Summarisation       → rolling summary of older turns (lossy)
  ├─ Memory extraction   → durable facts/preferences (needs dedupe, conflicts, user control)
  └─ Relevant retrieval  → embed query, fetch only related history
        ↓
  Compact, relevant prompt
```

Also trim large tool outputs. Define a memory write policy: what is stored, who consents, how it is corrected or deleted, how it expires, and how tenants stay isolated.

---

## 4. Scaling, Reliability, and Safety

**Why scaling differs from a REST API:** an agent run is several LLM calls and tool calls, mostly waiting, with variable duration and cost. Capacity is concurrent in-flight runs and tokens/minute, not just requests/second. Rough sizing: `concurrent runs ≈ arrival rate × run duration`.

```text
1 user → agent run → [Web | ArXiv | Database] in parallel → LLM reasoning
```

> **The bottleneck may be the model, tool, database, network, queue, or your own application, not necessarily the API server.** Trace before scaling.

**Techniques**

- **Stateless APIs + queue + worker pools:** autoscale workers on queue depth/age, not CPU. Add priority lanes and per-tenant fairness.
- **Connection pooling:** workers × concurrent runs × DB connections explodes; use bounded pools and a pooler.
- **Caching:** embeddings (safe), deterministic LLM responses, tool results (read-only), provider prefix caching (stable prompt prefix first).
- **Rate limiting at three levels:** per tenant, per tool, global LLM budget.
- **Backpressure:** reject with 429/503, bound queues, degrade, or shed low-priority work. Unbounded queues just turn failure into long waits.
- **Timeouts at every layer**, nested: tool < step < run.
- **Cancellation:** explicit user cancel stops the run and the token spend; mere client disconnect should not cancel a background run.

**Scaling vs performance:** performance makes one run faster or cheaper; scaling keeps the system working as run count grows.

**Evolution**

```text
1 user → 100 → 10,000 → 1,000,000

Simple → cache → async workers → queues → horizontal scaling
       → distributed services → partitioning/sharding only where necessary
```

| Scale | Shape | New problem |
|---|---|---|
| 1 user | One process, inline run | Correctness |
| 100 | API + Postgres + Redis, streaming, limits | Provider rate limits, runaway loops |
| 10,000 | Stateless API + queue + autoscaled workers, PgBouncer, routing, fallback provider | Concurrency slots, tool quotas, cost per tenant |
| 1,000,000 | Multi-region, split services, partitioned checkpoint tables, provisioned LLM capacity | Checkpoint write volume, hot tenants, cost governance |

At large scale, LLM spend and provider capacity often dominate, so routing, caching and step limits are scaling decisions.

**Failure model**

```text
LLM:      timeout, 429, provider outage, malformed output, hallucination
Tools:    API failure, invalid response, timeout, rate limit, duplicate side effect
Database: connection failure, overload, pool exhaustion
Runtime:  worker crash mid-run, approval never arrives, runaway loop
```

Classify failures as transient (retry helps), permanent (retry won't), or semantic (call succeeded but content is wrong).

| Technique | Note |
|---|---|
| Retries + exponential backoff + jitter | Cap attempts; retries cost tokens; respect `Retry-After` |
| Fallback models / tools | Test the fallback; it may be lower quality |
| Circuit breaker | Stop calling a dead dependency, fail fast, probe later |
| Idempotency | Steps replay after a crash, so tool calls need keys (e.g. run_id + step + tool_call_id) |
| Graceful degradation | Skip optional steps, use a smaller model, return partial results |
| Dead-letter queue | Park repeatedly failing runs with full state for replay |
| Human approval | Fallback for uncertain or risky actions |

```text
Tool failure → error handling → retry / fallback / recovery node → state update → continue
(bound every recovery loop with an attempt counter in state)

Crash after tool side effect but before checkpoint:
reload previous checkpoint → re-run step → tool called again → idempotency key prevents duplicates
```

**Reliability vs availability:** availability means it answers; reliability means it answers *correctly*, including through failures. A weaker fallback model can raise availability while lowering reliability.

**Agent-specific safety:** model output and everything it reads (web pages, documents, emails) is untrusted. The runtime enforces safety, not the prompt.

```text
Model proposes tool call → VALIDATE → AUTHORISE → APPROVE? → SANDBOX → execute
```

- **Permissions and least privilege:** tools act with the end user's delegated rights; read-only DB users; "draft" instead of "send"; no ambient secrets.
- **Input and output validation:** strict schemas for user input, tool arguments and structured outputs; allow-lists.
- **Prompt injection:** treat retrieved content as data, not instructions. Avoid combining private data access, untrusted content and external communication in one agent without approval.
- **Risk tiers:** read tools autonomous; reversible writes logged; irreversible or external actions need approval showing the exact action and arguments, with audit and expiry.
- **Sandboxing** for code execution and browsing: isolated, no default network or secrets, resource limits.
- **Tenant isolation** in checkpoint keys, vector filters, caches and credentials.

---

## 5. Observability, Evaluation, and the Design Framework

**Four signals:** logs (what happened), metrics (how much/how fast), traces (where time and tokens went), events (lifecycle moments like `approval_requested`).

```text
User Request → Agent Run
  ├── LLM call → Tool call → LLM call → Tool call → Final response
        ↓
   Trace / Metrics   (with a correlation ID from gateway to tools; redact PII)
```

**Measure:** agent, LLM and tool latency; time to first token; token usage; cost per request and per *successful* task; tool calls and steps per run; error rate by type; retry rate; completion rate; cache hit rate; queue age; approval wait and rejection rate. Slice by model, tool, tenant, prompt version and graph version.

**Cost levers:** fewer steps, smaller prompts, model routing, caching, per-run and per-tenant budgets, anomaly alerts.

**Evaluation questions**

```text
Does it answer correctly?        Does it choose the right tool?
Does it hallucinate?             Does it waste tool calls?
Is it too expensive?             Does it recover from failures?
```

Evaluate both the outcome and the trajectory. Methods: golden datasets in CI, programmatic checks (schema, step/cost limits), LLM-as-judge calibrated against humans, fault injection, adversarial tests, and online sampling with user feedback. Feed production failures back into the dataset. LangSmith, Langfuse and OpenTelemetry tooling are examples; the requirement is the capability, not the vendor.

**Complete architecture**

```text
USERS → CDN/WAF/Gateway → Load balancer → API servers → Agent runtime
   ├─ State → LangGraph → LLMs / Tools / Memory (SQL, Vector DB, Object storage)
   ├─ Queue → Workers
   └─ Cache → Redis
Checkpoints → Stream/Events → Frontend      (Observability/Tracing across everything)
```

**Request lifecycle:** user request → authentication → thread lookup → state/checkpoint restoration → agent execution → tool calls → reducers/state updates → checkpoint → retries/recovery → streaming → final response.

**Design framework**

```text
1. Requirements    2. Agent boundaries   3. State design    4. Tool design
5. Memory design   6. Model selection    7. Execution flow  8. Persistence
9. Streaming      10. Concurrency       11. Scaling        12. Reliability
13. Security      14. Observability     15. Cost           16. Evaluation
17. Trade-offs
```

**Problems and typical approaches** (examples, not universal answers)

| Problem | Typical architectural approach |
| --- | --- |
| Slow LLM | streaming / model selection / caching |
| Tool failure | retry / fallback / recovery |
| Long task | queue + worker |
| Many users | horizontal scaling |
| Large history | summarization + retrieval |
| Repeated request | caching |
| Tool overload | rate limiting + concurrency control |
| Need resume | checkpointing |
| Human approval | interrupts + HITL |
| Real-time output | streaming + SSE |
| Huge data | database scaling / partitioning |
| Provider outage | model/provider fallback |
| Expensive agents | caching + model selection + step limits |

**Final mental model**

```text
Traditional System                 Agentic System
Client                             Client
 ↓                                  ↓
API                                API
 ↓                                  ↓
Business Logic                     Agent Runtime / Graph
 ↓                                  ↓
Database                           State → LLM ↔ Tools
                                    ↓
                                   Memory / Databases → Checkpoint
                                    ↓
                                   Retry / Recovery / Interrupt
                                    ↓
                                   Streaming → Response
```

The intelligence is the model's; the reliability is your architecture's.

**15 interview questions**

1. Design a research agent (web + internal DB) for 100K users. *Hint: stateless API, queue + workers, checkpoints, bounded parallel tools, streaming, budgets.*
2. Workflow or autonomous agent? *Hint: predictability, compliance, cost, testability.*
3. A 10-minute run and the user closes the browser. *Hint: background run, status in SQL, event replay, disconnect vs cancel.*
4. Make tool calls safe to retry after a crash. *Hint: steps replay; idempotency keys; read vs write tools.*
5. State vs checkpoint vs thread vs long-term memory. *Hint: scratchpad, snapshot, container, cross-thread knowledge.*
6. Why not put the full history in every prompt? *Hint: cost multiplies per loop step; window, summary, extraction, retrieval.*
7. How do you autoscale workers? *Hint: scale on queue age and concurrency, not CPU.*
8. p95 latency doubled after a release. *Hint: trace spans by LLM, tool, DB, queue; compare versions and token growth.*
9. Defend against prompt injection from documents. *Hint: data not instructions; least privilege; approvals; break the dangerous triad.*
10. Refund approval that returns after three days. *Hint: interrupt releases compute; expiry; re-validate on resume; audit.*
11. Handling 429s across thousands of runs. *Hint: shared token bucket, backpressure, backoff, routing, fallback.*
12. Control and attribute cost. *Hint: per-run caps, tenant budgets, cost per successful task.*
13. Evaluate beyond "looks right". *Hint: outcome plus trajectory; golden sets, judges, fault injection.*
14. Two requests hit one thread at once. *Hint: serialise, 409, or queue behind.*
15. When is multi-agent the wrong choice? *Hint: coordination overhead, cost, debugging; split for tools, permissions or scaling needs.*