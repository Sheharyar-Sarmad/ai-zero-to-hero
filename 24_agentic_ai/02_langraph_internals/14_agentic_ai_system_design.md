# Agentic AI System Design: Architecting, Scaling, Securing and Operating Production Agents

> **Scope:** this file is about the *system around* the agent: architecture, scaling, safety, operations. It does not re-teach LangGraph syntax. LangGraph is used as the main orchestration example, but every pattern here applies to any agent runtime (custom loops, other frameworks, durable-workflow engines).

**Contents**
1. What is Agentic AI System Design?
2. High-Level Production Architecture
3. Agent Runtime and Execution Architecture
4. Memory, State, and Persistence
5. Scaling and Performance of Agentic Systems
6. Reliability, Safety, and Failure Handling
7. Observability, Cost, and Evaluation
8. Complete Production Agentic AI Design + Interview Framework

---

## 1. What is Agentic AI System Design?

### 1.1 The progression

```text
User
 ↓
LLM                         one prompt → one completion
 ↓
LLM + Tools                 model can request actions (function calling)
 ↓
Agent                       loop: decide → act → observe → decide …
 ↓
Agent + State               the loop carries structured working data
 ↓
Agent + Memory              knowledge survives beyond one run
 ↓
Multi-step workflow         explicit control flow, branches, approvals
 ↓
Production Agentic System   all of the above + scale, safety, ops, cost control
```

Each step adds capability **and** a new class of engineering problem. Tools add side effects. Loops add unbounded cost. State adds persistence. Memory adds privacy. Workflows add versioning. Production adds everything else.

### 1.2 Five terms people mix up

| Term | What it is | Key question it answers | Example |
|---|---|---|---|
| **LLM application** | App that calls a model; fixed, developer-defined flow | "Can the model produce text for this step?" | Summarise a document; RAG Q&A with a fixed retrieve → generate pipeline |
| **Agent** | A loop where the *model chooses* the next action from available tools until it decides it is done | "Who decides what happens next?" (the model) | Research assistant that picks between search, SQL and calculator |
| **Multi-agent system** | Several agents (often with different prompts/tools/models) that delegate to or coordinate with each other | "Should responsibility be split?" | Supervisor routes to "researcher", "coder", "reviewer" |
| **Agentic workflow** | Predefined graph/steps where LLMs handle *some* nodes or decisions; control flow is mostly developer-defined | "How much autonomy do I actually need?" | Triage → classify → (if refund) approval → execute |
| **Production agentic platform** | The surrounding system: auth, tenancy, queues, persistence, streaming, safety, observability, evaluation, cost controls | "Can this run reliably for thousands of users, safely and affordably?" | The thing this whole file designs |

**Agent vs workflow** is the most important distinction: in a **workflow** the *code* decides the path; in an **agent** the *model* decides the path. Most real systems sit on a spectrum, with deterministic skeletons and agentic "pockets" where flexibility is worth the risk.

```text
Fully deterministic ◄────────────────────────────────────► Fully autonomous
  pipeline      workflow w/ LLM nodes     agent + tools      multi-agent
  cheap, testable, predictable            flexible, costly, risky, harder to test
```

> **Design rule:** use the *least autonomy that solves the problem*. Every degree of autonomy you add is paid for in latency, cost, test difficulty and risk.

### 1.3 How agentic systems differ from traditional web apps

| Property | Traditional web app | Agentic system | Consequence |
|---|---|---|---|
| Behaviour | Deterministic: same input, same output | **Non-deterministic**; may be wrong confidently | Need evals, guardrails, output validation; unit tests alone are insufficient |
| Side effects | Code you wrote and reviewed | **Tool calls chosen at runtime** by a model | Permission model, approvals, idempotency |
| Execution shape | One request → one response (ms) | **Multi-step** loops (seconds to hours) | Request/response timeout model breaks; need async execution |
| Duration | Short | **Long-running** | Queues, workers, durable state, resumability |
| State | Mostly in DB/session | **Rich evolving state** per run | State schema design, checkpointing, versioning |
| Memory | User profile/history | **Learned/retrieved context** injected into prompts | Privacy, relevance, summarisation, deletion |
| Response delivery | Single payload | **Streamed** tokens and events | SSE/WebSocket, long-lived connections, cancellation |
| Dependencies | DB, a few services | **LLM providers + many tools + search + APIs** | Failure surface multiplies; rate limits everywhere |
| Cost model | Roughly per request/CPU | **Per token, per tool call, per step** with huge variance | Budgets, step limits, cost attribution |
| Latency | Predictable, low variance | **High variance** (a request may take 2 s or 90 s) | Percentiles, timeouts, progress UI |
| Failure | Crash or error | Also **silent quality failure** (hallucination, wrong tool) | Evaluation is part of operations |

A traditional app mostly fails *loudly*. An agent can fail *quietly*: HTTP 200, plausible answer, wrong content. That is why observability and evaluation (Section 7) are first-class parts of the architecture rather than add-ons.

---

## 2. High-Level Production Architecture

### 2.1 The full picture

```text
                    USER
                      │
                      ▼
                Frontend / API
                      │
               Auth / Rate Limit
                      │
                 Load Balancer
                      │
                Agent API Layer
                      │
              ┌───────┴────────┐
              ▼                ▼
         Agent Runtime      Queue
              │                │
              ▼             Workers
        Agent / Graph
              │
      ┌───────┼────────┐
      ▼       ▼        ▼
    LLMs    Tools    Memory
      │       │        │
      │       │        ├── Redis
      │       │        ├── SQL
      │       │        └── Vector DB
      │       │
      │       ├── Web
      │       ├── APIs
      │       ├── Search
      │       └── Internal services
      │
      ▼
 Checkpoints / Persistence
      │
      ▼
 Streaming / Events
      │
      ▼
 Monitoring / Tracing
```

### 2.2 What each layer solves

| Layer | Architectural reason it exists | What goes wrong without it |
|---|---|---|
| **Frontend / API** | Single contract for clients: start a run, stream events, resume, cancel, fetch history. Hides the agent internals so you can change them freely | Clients coupled to internals; every agent change is a client change |
| **Auth / rate limit** | Establishes *who* is calling and *how much* they may consume. For agents, "how much" means tokens, steps and tool calls, not just requests, because one request can trigger 50 LLM calls | Denial-of-wallet; cross-tenant access; one user starving others |
| **Load balancer** | Spreads traffic across stateless API instances; removes unhealthy ones; terminates TLS. Must support long-lived streaming connections | Single point of failure; dropped SSE streams from short idle timeouts |
| **Agent API layer** | Thin, **stateless** orchestration edge: validate input, create run records, enqueue or start execution, relay events. Contains no agent state in memory | If it holds state, you can't scale horizontally or survive restarts |
| **Agent runtime** | The engine that executes the loop/graph: loads state, runs steps, applies updates, checkpoints, emits events, honours interrupts | Ad-hoc loops with no resume, no limits, no uniform tracing |
| **Queue + workers** | Decouples *accepting* a run from *executing* it. Absorbs bursts, enables retries, lets long runs outlive HTTP connections, scales compute independently | Long runs tied to open connections; spikes cause cascading failure |
| **LLMs** | The decision/generation engine. Behind an abstraction (gateway/router) so you can switch models, add fallbacks, meter cost | Provider lock-in; no fallback; no central cost control |
| **Tools** | The agent's hands: all side effects and external data. Each is an integration with its own latency, auth, failure modes | Uncontrolled side effects; no permission boundaries |
| **Memory: Redis** | Fast, ephemeral: caches, rate-limit counters, pub/sub for streaming, locks, short-term session data | Repeated expensive calls; no fast coordination primitive |
| **Memory: SQL** | Durable, transactional, queryable: users, threads, runs, audit logs, approvals, structured memories | Lost history; no auditing; no consistency for money/approval paths |
| **Memory: Vector DB** | Semantic recall: retrieve *relevant* documents and past facts instead of loading everything | Context overflow or irrelevant recall |
| **Checkpoints / persistence** | Durable snapshots of run state so execution can resume, retry, pause for humans, and be debugged | A worker crash loses the whole run; HITL impossible |
| **Streaming / events** | Convert a slow multi-step process into visible progress (tokens, tool starts, state updates) | Users stare at spinners for 30 s and retry, doubling load |
| **Monitoring / tracing** | Makes a non-deterministic, multi-step system explainable: where time, tokens, money and errors went | Silent quality decay; unexplainable bills and incidents |

### 2.3 Key distinctions at the architecture level

- **Queue vs direct execution:** *Direct* = API process runs the agent while the client waits. Simple and low latency; fine for short, interactive runs. *Queue* = API enqueues, worker executes. Needed for long runs, retries, spike absorption, deploy safety. Many systems support both: interactive path direct/streamed, heavy path queued.
- **Tool vs node:** a *node* is a unit of your orchestration (a step in the workflow; it may call an LLM, run code, or invoke tools). A *tool* is a capability exposed to the model (a function it may *request*). Nodes are control-flow structure you own; tools are actions the model selects. A tool-executing node is where the two meet.
- **Streaming vs normal response:** normal = one payload after completion (simple, cacheable). Streaming = incremental events over a long-lived connection (better *perceived* latency, supports progress and cancellation, but needs connection handling, proxy configuration, and resume logic). Streaming changes perceived latency, not actual total work.

### 2.4 Monolith first

The diagram shows *roles*, not necessarily separate services. A reasonable early deployment is: one API+runtime codebase, Postgres, Redis, a worker deployment of the same codebase, and an LLM provider. Split into more services only when scaling profile, team ownership, or security boundary demands (e.g. a sandboxed code-execution service, a GPU inference service, an ingestion pipeline).

---

## 3. Agent Runtime and Execution Architecture

### 3.1 The end-to-end run

```text
User Request
 ↓
Thread ID                       identifies the conversation/session
 ↓
Load previous checkpoint/state
 ↓
Agent/Graph starts
 ↓
Node executes
 ↓
Tool call
 ↓
Tool result
 ↓
Reducer
 ↓
Updated State
 ↓
Checkpoint
 ↓
Next step
 ↓
Interrupt / Resume if needed
 ↓
Streaming events
 ↓
Final response
```

Think of the runtime as a **durable, step-by-step state machine executor**: for each step it reads state, does work, merges the result, and *persists before moving on*. Everything below elaborates this loop.

### 3.2 Lifecycles, kept separate

```text
THREAD      (days/months)   = a conversation / long-lived identity & partition key
  └── RUN   (seconds–hours) = one execution triggered by one input
        └── STEP            = one node execution (a "super-step")
              └── CHECKPOINT = durable snapshot written after a step
```

| Concept | Lifetime | Purpose | Common confusion |
|---|---|---|---|
| **Thread** | Long | Groups all runs/messages of one conversation; the key for loading state, locking, and partitioning | A thread is *not* a checkpoint; it is the *sequence container* |
| **Run** | Short | One invocation: input → final output (may pause/resume) | A run can span several worker processes if it pauses |
| **State** | Within a run (plus carried forward) | The working data the graph reads/writes right now | State is a *value*; a checkpoint is a *saved copy of it* |
| **Checkpoint** | Persistent | A snapshot of state + "what runs next" at a step boundary | Not conversation memory; it is execution progress |

**State lifecycle:** initialise from thread's latest checkpoint + new input → each node returns a *partial update* → reducers merge updates deterministically → merged state becomes the input to the next step → snapshot persisted → final state returned and retained.

**Why reducers matter architecturally:** they define *how concurrent or repeated updates combine* (append messages, merge dicts, overwrite value). Without defined merge semantics, parallel branches and retries would produce nondeterministic corruption. Reducers are what make parallel fan-out safe.

**Checkpoint lifecycle:** written after each step → used for (1) crash recovery, (2) pause/resume across processes, (3) multi-turn continuity, (4) debugging/time-travel/forking, (5) retry-from-last-good-step. Cost: write amplification (every step writes to the DB) and storage growth, so decide retention (keep latest + N, expire old threads, compact large payloads).

### 3.3 Node execution vs tool execution

```text
Node (orchestration unit)
 ├─ calls LLM → gets: final answer OR "please call tool X with args Y"
 └─ routing decides: if tool requested → Tool node → result → back to LLM node
```

The model never *executes* anything. It emits a **request**; your runtime validates it, enforces permissions/limits, executes the tool, and feeds the result back. This gap between "model asked" and "system did" is where **all safety controls live** (Section 6).

Tool execution responsibilities:
1. **Validate** arguments against a schema (reject malformed model output).
2. **Authorise** against the *end user's* permissions, not a global one.
3. **Apply timeout and concurrency limits.**
4. **Execute** with idempotency key if it has side effects.
5. **Normalise** result/error into something the model can read (truncated, structured).
6. **Record** the call for tracing and audit.

### 3.4 Control-flow patterns at runtime

| Pattern | What happens | Production concern |
|---|---|---|
| **Conditional routing** | After a step, code (or the model) selects the next node | Keep routing logic deterministic where possible; unit-test it; log the chosen branch |
| **Loops** | Agent cycles LLM → tool → LLM until done | **Must be bounded** (max steps, max tokens/cost, wall-clock timeout); detect repetition |
| **Parallel execution (fan-out/fan-in)** | Several branches or tool calls run at once; results merged by reducers | Bounded concurrency; partial-failure policy (fail all vs continue with partial results); merge semantics |
| **Interrupt** | Runtime pauses at a defined point, persists state, **releases compute** | The wait may be days; no open connections/processes; needs notification channel |
| **Resume** | An external event (human input, webhook, timer) continues from the checkpoint, possibly on a *different worker* | Idempotent resume; verify the resumer is authorised; handle expiry |
| **Streaming** | Events emitted while running (tokens, step start/end, tool start/end, state updates) | Event schema, ordering, replay after reconnect, cancellation propagation |

**Concurrency vs parallelism, concretely:** *Concurrency* = one worker process juggling many agent runs while each awaits LLM/tool I/O (async). *Parallelism* = one agent run executing several branches/tool calls *at the same time*. Agent systems are overwhelmingly I/O-bound, so you need lots of **concurrency** per worker; **parallelism** inside one run is a latency optimisation that also multiplies burst load on your tools.

### 3.5 Where the loop executes: three execution models

```text
A. Inline in API process            B. Dedicated worker (queue)          C. Durable workflow engine
Client ↔ API(runs agent)            Client → API → Queue → Worker        API → engine (Temporal etc.)
                                                                          engine schedules steps, retries,
                                                                          timers, resumes natively
```

| Model | Pros | Cons | Fits |
|---|---|---|---|
| **A. Inline** | Simplest; lowest latency; streaming is trivial | Run dies with the process/deploy; ties up API capacity; hard to retry | Short interactive chat, prototypes |
| **B. Queue + workers** | Survives deploys (with checkpoints); independent scaling; retries; backpressure | More moving parts; status/streaming relay needed | Most production agents |
| **C. Durable engine** | Strongest guarantees for very long/complex flows | Extra platform to run/learn; overlap with checkpoint features | Multi-day, compliance-heavy, many-system orchestration |

### 3.6 Run lifecycle states (design them explicitly)

```text
queued → running → ┬→ completed
                   ├→ failed (retryable / terminal)
                   ├→ interrupted (waiting for human/event) → running (on resume)
                   ├→ cancelled (user/system)
                   └→ timed_out / budget_exceeded
```

Store this in SQL (not only in the framework's checkpoint tables) so your API, UI, billing and alerts can query run status without understanding framework internals.

### 3.7 Concurrency on a single thread

If two runs hit the same thread simultaneously (double-click, two tabs, retry race), they may load the same checkpoint and write conflicting successors. Options: **serialise per thread** (queue partition keyed by thread ID or a lock with expiry), **reject** with `409 run already active`, or **enqueue the second input** behind the first. Pick explicitly; never leave it undefined.

---

## 4. Memory, State, and Persistence

### 4.1 Definitions that must stay separate

| Term | What it is | Scope | Stored in |
|---|---|---|---|
| **State** | Working data of the *current execution* (messages so far, plan, tool results, flags) | One run | In memory during run; snapshotted into checkpoints |
| **Checkpoint** | Durable snapshot of state at a step boundary | Resume/recovery | Checkpoint store (Postgres/Redis) |
| **Thread** | Identifier + ordered history of runs/checkpoints for one conversation | One conversation | Thread/run tables + checkpoint store |
| **Conversation history** | The raw record of messages exchanged | One thread | SQL/NoSQL message store |
| **Short-term memory** | What the agent can "see" *within the current thread* (recent messages, summary, scratchpad) | Thread | State/checkpoints |
| **Long-term memory** | Knowledge persisted *across threads* (user preferences, facts, past outcomes) | User/org | SQL (structured), vector DB (semantic), KV |
| **Vector memory** | Long-term memory stored as embeddings for semantic retrieval | User/org/corpus | Vector DB / pgvector |
| **Database persistence** | The system of record for business data (orders, users, audit) | Application | SQL/NoSQL |
| **Cache** | Disposable, speed-oriented copies of computed or fetched results | Short TTL | Redis |

**Memory vs persistence:** *memory* is a **purpose** (information the agent can use to behave better). *Persistence* is a **mechanism** (data survives restarts). A checkpoint is persistence *without* being memory (it is execution progress). A user-preference fact is both. A cache entry is neither (it can vanish).

**State vs memory:** state is the *scratchpad for this run*; memory is *what is kept and recalled later*. Information moves from state into memory only through a deliberate step (summarise, extract, write).

### 4.2 The data flow

```text
Current execution
      ↓
State                       (working data, this run)
      ↓
Checkpoint                  (durable snapshot per step)
      ↓
Thread history              (all checkpoints/messages of this conversation)
      ↓
Long-term storage           (extracted facts, summaries, user profile, vectors)
```

```text
          ┌────────────────────────── per request ─────────────────────────┐
 Input ──►│ load thread state ──► + retrieve relevant long-term memory ──►  │
          │ build prompt (system + summary + recent msgs + retrieved facts) │
          │ LLM / tools / reducers ──► new state ──► checkpoint             │
          └──────────────────────────────┬──────────────────────────────────┘
                                         ▼ (async, after run)
                          extract memories / update summary / index
                                         ▼
                              long-term store (SQL + vector)
```

### 4.3 Which store for what

| Store | Best for | Strengths | Weaknesses | Typical agent use |
|---|---|---|---|---|
| **Redis** | Hot, ephemeral data | Microsecond reads, TTL, pub/sub, locks, counters | Memory-bound cost; durability optional/weaker | Rate limits, response/embedding/tool caches, streaming fan-out, short session data, distributed locks |
| **PostgreSQL** | Durable, relational, transactional data | ACID, constraints, rich queries, JSONB, pgvector, mature ops | Scaling writes needs effort | Users/tenants, threads, runs, approvals, audit logs, **checkpoints**, structured long-term memory |
| **MongoDB** (document) | Flexible-schema documents read as a unit | Schema flexibility, easy horizontal scale | Weaker joins/transactions; schema drift risk | Conversation transcripts, heterogeneous tool outputs, if the team already runs it |
| **Vector database** | Similarity search over embeddings | Fast ANN search, metadata filters | Eventual freshness; re-embedding cost; not a system of record | Semantic recall of documents, past conversations, learned facts |
| **Object storage** | Large blobs | Cheap, durable, huge capacity | No querying; higher latency | Uploaded files, large tool outputs, state attachments, trace payloads, exported reports |

**Practical default:** *Postgres for almost everything durable (including checkpoints and pgvector at moderate scale), Redis for speed and coordination, object storage for blobs.* Add MongoDB or a dedicated vector DB only when a measured requirement justifies the extra system.

**Keep state small:** put large artifacts (documents, big tool results) in object storage and keep a *reference* in state. Every checkpoint copies state, so bloated state means bloated writes, slow resume, and high storage cost.

### 4.4 Why not dump the whole conversation into every prompt?

```text
Turn 1:   [sys][1]                         ~1K tokens
Turn 20:  [sys][1…20]                      ~15K tokens
Turn 200: [sys][1…200]                     ~150K tokens  ← too big / slow / costly / noisy
```

| Problem | Why it hurts |
|---|---|
| **Context limits** | Hard ceiling; beyond it the call fails or you truncate blindly |
| **Cost** | You pay for input tokens on *every* LLM call, and an agent loop makes many calls per turn, so the cost multiplies |
| **Latency** | Longer prompts slow time-to-first-token |
| **Quality** | Irrelevant history dilutes attention; models can miss details buried mid-context; stale or contradictory facts mislead |
| **Privacy/safety** | Old sensitive content and injected instructions keep resurfacing |

### 4.5 Better approaches (they combine)

```text
                 Full history (stored in DB, never lost)
                          │
        ┌─────────────────┼───────────────────┬────────────────────┐
        ▼                 ▼                   ▼                    ▼
  Sliding window     Summarisation     Memory extraction    Relevant-history retrieval
 (last N messages)  (rolling summary   (durable facts:      (embed query → fetch only
                     of older turns)    "prefers metric")    related past snippets)
        └─────────────────┴─────────┬─────────┴────────────────────┘
                                    ▼
                  Compact, relevant prompt context
```

- **Sliding window / trimming:** keep recent turns verbatim. Simple, but forgets older detail.
- **Summarisation:** compress older turns into a rolling summary. Cheap context, but lossy; summaries can drift or encode errors; do it asynchronously or at thresholds.
- **Memory extraction:** an LLM (or rules) distils *durable facts/preferences/decisions* into structured records. Compact and precise; requires deduplication, conflict resolution ("moved from Paris to Berlin"), confidence and user control.
- **Relevant-history retrieval:** embed the current query and fetch the most related past messages/facts. Scales to unbounded history; recall depends on retrieval quality.
- **Tool-output trimming:** large tool results are the biggest prompt bloat. Summarise or store externally and pass references/snippets.

**Memory write policy matters:** decide *what* is worth remembering, *who consents*, *how it is corrected or deleted* (privacy rights), *how it expires*, and *how it is isolated per tenant*. Bad memory is worse than no memory: it makes the agent confidently wrong across sessions.

### 4.6 Retention and cost of persistence

| Data | Suggested lifecycle |
|---|---|
| Latest checkpoint per thread | Keep while thread is active |
| Historical checkpoints | Keep last N or short window; archive for debugging/audit if needed |
| Raw messages | Per compliance and product needs; archive to cheap storage |
| Summaries / extracted memories | Long-lived, user-editable, deletable |
| Caches | Short TTL, disposable |
| Traces | Sampled retention; redact PII |

---

## 5. Scaling and Performance of Agentic Systems

### 5.1 Why this is different from scaling a REST API

A typical CRUD request: ~10 to 100 ms, CPU/DB-bound, predictable. An agent run: **multiple LLM calls (each 1 to 20 s) + multiple tool calls + waiting**, mostly **idle waiting on remote systems**, with wildly varying duration and cost.

| Dimension | REST API | Agentic system |
|---|---|---|
| Request duration | ms | seconds → minutes → hours |
| Bottleneck | CPU / DB | **LLM throughput & rate limits, tool latency, concurrency slots, queue** |
| Work per request | Fixed | **Variable** (model decides number of steps) |
| Connections | Short | **Long-lived** (streams) |
| Cost per request | Near-constant | **Highly variable** (tokens × steps) |
| Capacity unit | Requests/second | **Concurrent in-flight runs**, tokens/minute |
| Failure external | Rare | **Constant** (providers, tools) |

Use **Little's Law** to size capacity: `concurrent runs ≈ arrival rate × average run duration`. If 50 runs/s arrive and each lasts 20 s, you need ~1,000 runs in flight. Per-run time is dominated by waiting, so each worker should hold hundreds of runs concurrently via async I/O.

### 5.2 What one run looks like

```text
                1 user
                  ↓
              Agent run
                  ↓
       ┌──────────┼──────────┐
       ▼          ▼          ▼
      Web        ArXiv     Database       ← parallel tool calls
       │          ▼          │
       └──────────┼──────────┘
                  ▼
             LLM reasoning
```

Time budget of such a run (illustrative):

```text
LLM plan      ████ 3s
Tools (parallel; slowest wins)  ██████ 5s
LLM synthesise (streaming)      ████████ 6s
                                  ≈ 14s total, ~95% waiting on others
```

**Where can the bottleneck be?** Pick *each* and know its symptom:

| Candidate | Symptom | Typical fix |
|---|---|---|
| **Model** (provider limits, slow generation) | 429s, high time-to-first-token, tokens/min ceiling | Smaller/faster model for easy steps, routing, caching, batching, provisioned throughput, fallback provider |
| **Tools** | One slow API dominates latency or throttles you | Timeouts, caching, parallelism, circuit breakers, per-tool concurrency caps |
| **Database** | High connection count, slow checkpoint writes | Pooling/PgBouncer, indexes, smaller state, replicas for reads, partitioning |
| **Network** | Cross-region hops, DNS/TLS overhead | Keep-alive/HTTP2, co-locate services, regional deployment |
| **Queue** | Growing depth/age | More workers, priority lanes, admission control |
| **Your application** | Event-loop blocked, sync code in async path, GC, serialisation of huge state | Profile, remove blocking calls, shrink payloads |

> **The bottleneck in an agentic system may be the model, tool, database, network, queue, or your own application, not necessarily the API server.** Measure with traces before scaling anything.

### 5.3 Techniques

**Stateless API servers.** API nodes hold no run state, so you can add or kill them freely. State lives in Postgres/Redis; streaming events flow through Redis pub/sub or a stream so *any* API node can serve any client's stream.

**Queue-based execution + worker pools.**
```text
API ──enqueue run──► Queue ──► Worker pool (N × M concurrent runs, async)
                        ▲               │ autoscale on queue depth/age
                        └── retries/DLQ ┘
```
Workers are disposable. Autoscale on **queue depth and oldest-message age**, not CPU (CPU stays low while waiting on the network). Use **priority queues** (interactive vs batch) and **per-tenant fairness** so one large customer cannot starve others.

**Horizontal scaling and partitioning.** Add API and worker instances. Partition work by `thread_id`/`tenant_id` where ordering or isolation matters.

**Connection pooling.** Workers × concurrent runs × DB connections explode quickly. Use bounded pools and a pooler (PgBouncer). Reuse HTTP clients with keep-alive to LLM providers and tools. Check pool saturation as a core metric.

**Caching** (details in Section 4 and 2):
| Cache | Key | Caution |
|---|---|---|
| Embeddings | content hash + model | Safe, high value |
| LLM response | prompt + params (deterministic calls) | Only for `temperature≈0`, non-personalised |
| Semantic cache | query embedding similarity | Risk of wrong hits; strict threshold |
| Provider prompt-prefix caching | stable prefix first | Keep system prompt/tool schemas stable and at the front |
| Tool results | args + TTL | Only idempotent, read-only tools |

**Parallel tool calls.** Cut latency (total ≈ slowest tool, not the sum) but *multiply burst load* on downstream services. Always cap per-run and per-tool concurrency.

**Rate limiting (several layers).**
```text
Per user/tenant (requests, tokens, runs)  ← protects fairness and wallet
Per tool / per downstream API             ← protects dependencies, respects their quotas
Global LLM budget (tokens/min)            ← respects provider limits; shared token bucket in Redis
```

**Backpressure.** When capacity is exceeded, push back deliberately rather than collapse: reject with `429/503 + Retry-After`, queue with bounded length, degrade (cheaper model, skip optional steps), or shed lowest-priority work. Unbounded queues just move failure to latency: users wait 20 minutes, then retry, which makes things worse.

**Timeouts at every layer** (LLM call, tool call, step, whole run, queue wait). A missing timeout turns one hung dependency into exhausted workers. Remember that timeouts should nest: tool < step < run.

**Request cancellation.** The user closes the tab or presses *stop*: propagate cancellation to the runtime, abort in-flight LLM streams and tool calls where possible, mark the run `cancelled`, and stop paying for tokens. Also handle *client disconnect* separately from *user cancel*: for background runs, disconnect should *not* cancel (the user can return), while explicit cancel should.

### 5.4 Scaling vs performance (not the same thing)

- **Performance:** how fast/cheap *one* run is (prompt size, model choice, caching, parallel tools, fewer steps).
- **Scaling:** whether the system keeps working as the *number* of runs grows (stateless APIs, queues, pools, rate limits).
Optimise performance first where cheap (shorter prompts and fewer steps help *both*), but do not mistake a fast single run for a scalable system.

### 5.5 Evolution with load

```text
1 user
 ↓
100 users
 ↓
10,000 users
 ↓
1,000,000 users
```

| Scale | Typical shape | What becomes the problem |
|---|---|---|
| **1 user** | One process, inline execution, local DB or SQLite checkpointer, one LLM provider | Correctness, prompt quality, tool reliability |
| **100 users** | API + Postgres + Redis; basic rate limits; streaming; simple caching; tracing on | LLM provider rate limits; unbounded loops; first cost surprises; thread race conditions |
| **10,000 users** | Stateless API fleet + **queue + autoscaled workers**; PgBouncer; per-tenant limits; response/embedding caches; model routing; fallback provider; run status in SQL | Concurrency slots, tool quotas, DB connections, queue fairness, cost per tenant |
| **1,000,000 users** | Multi-AZ/multi-region; separate services where profiles diverge (ingestion, retrieval, sandbox, gateway); read replicas; **partitioned checkpoint/message tables**, sharding by tenant/thread *only if measured necessary*; negotiated or provisioned LLM capacity; aggressive caching and routing; cell-based isolation | Checkpoint write volume, hot tenants, cost governance, regional compliance, provider capacity |

**The evolution rule:**

```text
Simple
→ cache
→ async workers
→ queues
→ horizontal scaling
→ distributed services
→ partitioning/sharding where actually necessary
```

Climb one rung only when metrics show the current rung failing. Premature distribution adds failure modes without adding capacity you need.

**Note on cost at scale:** at 1M users the dominant constraint is often **LLM spend and provider capacity**, not servers. Architecture decisions such as routing, caching and step limits are often *scaling* decisions in disguise.

---

## 6. Reliability, Safety, and Failure Handling

### 6.1 The failure model

```text
Agent
 ↓
LLM
 ├── timeout
 ├── rate limit (429)
 ├── provider failure (5xx / outage)
 ├── malformed output (bad JSON, wrong tool args)
 └── bad content (hallucination, refusal)

Tools
 ├── API failure
 ├── invalid response
 ├── timeout
 ├── rate limit
 └── partial/duplicate side effect

Database / Infra
 ├── connection failure
 ├── overload / pool exhaustion
 └── worker crash mid-run

Human / Orchestration
 ├── approval never arrives
 ├── runaway loop
 └── stale graph version on resume
```

Classify failures first: **transient** (retry helps: timeouts, 429, 503), **permanent** (retry won't help: invalid args, 4xx auth, bad request), **semantic** (call "succeeded" but the content is wrong). Only the first class benefits from blind retries.

### 6.2 Reliability toolkit

| Technique | What it does | Agent-specific notes |
|---|---|---|
| **Retries** | Re-attempt transient failures | Cap attempts; never retry non-idempotent writes blindly; retried LLM calls cost money |
| **Exponential backoff + jitter** | Spread retries (1 s, 2 s, 4 s … + randomness) | Prevents retry storms that hammer a recovering provider; respect `Retry-After` |
| **Timeouts** | Bound waiting | Per call/step/run; surface a typed error to the agent |
| **Fallback models/providers** | Switch to alternative on failure | Test the fallback (prompts behave differently across models); log which model answered; consider quality drop |
| **Tool fallback** | Alternate tool/source (secondary search API, cached result) | Tell the model what failed so it can adapt; keep fallbacks equivalent in contract |
| **Circuit breaker** | After N failures, stop calling a dependency for a cooldown, then probe | Prevents burning tokens and time on a known-dead tool; return a fast, explicit "unavailable" |
| **Idempotency** | Same operation repeated = same effect once | Essential because *steps can replay after a crash* (side effect done, checkpoint not yet written); use idempotency keys derived from `run_id + step + tool_call_id` |
| **Graceful degradation** | Reduced but useful service | Skip reranker, use smaller model, answer without optional tool, return partial results with disclosure |
| **Dead-letter / retry queue** | Park repeatedly failing runs for inspection/replay | Preserve full state and trace for replay; alert on DLQ growth |
| **Human approval** | Gate risky actions | Reliability *and* safety: a human is the fallback when automation is uncertain |

**Reliability vs availability:** *availability* = the system answers requests (is it up?). *Reliability* = it answers **correctly and consistently** (does it do the right thing, including after failures?). An agent that always responds but sometimes triggers the wrong refund is *available but unreliable*. Fallback models can raise availability while *lowering* reliability if the backup model is worse, so measure both.

### 6.3 Mapping failures to graph-level recovery

```text
Tool failure
 ↓
Error handling            (tool node catches; classify transient/permanent)
 ↓
Retry / fallback / recovery node
 ↓
State update              (record attempt count, error summary, fallback used)
 ↓
Continue                  (or route to escalation / human / graceful end)
```

```text
            ┌────────── retry (transient, attempts < N, backoff) ──┐
            ▼                                                      │
 Tool node ──ok──► LLM node                                        │
     │                                                             │
     └─error─► Classify ──transient──────────────────────────────┘
                  │
                  ├─permanent/invalid args ─► feed error to LLM ("fix args") ─► LLM node
                  ├─tool down (breaker open) ─► fallback tool / cached ─► LLM node
                  └─exhausted / high risk ───► Escalate (interrupt for human) or fail gracefully
```

Two principles: **put error context into state** so the model and downstream nodes can reason about it, and **bound every recovery loop** (attempt counters in state) so error handling cannot itself run forever.

**Crash recovery:** worker dies mid-run → queue visibility timeout expires → another worker picks the job → loads the last checkpoint → resumes from the last *completed* step. The in-flight step *re-executes*, so tools in that step must be idempotent or guarded.

```text
Step N: tool executes (side effect happens) ── crash ──✗ checkpoint N not saved
Recovery: reload checkpoint N-1 → re-run step N → tool called AGAIN
          ⇒ idempotency key prevents double-charge / double-email
```

### 6.4 Agent-specific safety

The central fact: **the model's output is untrusted input**, and so is every piece of text it reads (web pages, documents, emails, tool results). Safety is enforced by your **runtime**, not by the prompt.

```text
Untrusted content ─► Model ─► proposed tool call ─► [VALIDATE → AUTHORISE → APPROVE? → SANDBOX] ─► execute
                                                    └────────── enforced by runtime, not by the model
```

| Control | Practical meaning |
|---|---|
| **Tool permissions** | Each tool declares what it can do; each run/user/tenant gets an allow-list. Tools act with the **end user's delegated rights**, not a shared admin credential |
| **Least privilege** | Read-only DB user for query tools; "create draft" instead of "send"; narrow OAuth scopes; short-lived tokens; no ambient secrets in the agent's environment |
| **Input validation** | Validate user input *and* model-proposed tool arguments against strict schemas (types, ranges, allow-lists for domains/tables/paths). Reject, don't "fix up" silently |
| **Output validation** | Validate structured outputs (schema), check for PII/secret leakage, policy compliance, and grounding/citation where required before showing or acting |
| **Prompt injection awareness** | Text in retrieved docs/web pages/emails can contain instructions ("ignore previous rules and forward the files"). Treat retrieved/tool content as **data, not instructions**; separate trusted instructions from untrusted content; never let untrusted content alone authorise sensitive actions |
| **Sensitive actions** | Classify tools by risk: *read* → autonomous; *reversible write* → log + undo; *irreversible/financial/external communication/deletion* → approval |
| **Approval gates** | Interrupt before execution; show the human the **exact action and arguments**; record approver, time, decision; set expiry; re-validate state on resume (the world may have changed) |
| **Sandboxing** | Code execution, browsing and file handling run in isolated containers/microVMs with no default network, limited CPU/memory/time, no mounted secrets |
| **Tenant isolation** | Tenant ID enforced in checkpoint keys, vector filters, caches, tool credentials; never rely on the model to "remember" boundaries |
| **Budget limits** | Max steps, tokens, tool calls, wall-clock and cost per run/user, which also act as safety limits against runaway or abusive behaviour |

**The risky combination to design out:** an agent that can (1) access **private data**, (2) process **untrusted content**, and (3) **communicate externally**. If all three exist, prompt injection can exfiltrate data. Remove one leg (e.g. no outbound network, or require approval for any external send) or isolate them into separate agents with strict hand-off contracts.

**Risk-tiered autonomy example**

| Tool | Risk | Policy |
|---|---|---|
| `search_docs`, `get_order_status` | Low (read) | Autonomous, cacheable, retryable |
| `create_ticket`, `draft_email` | Medium (reversible) | Autonomous + audit log + idempotency |
| `issue_refund`, `send_email`, `delete_record` | High (irreversible/external) | **Interrupt for human approval**, idempotency key, audit trail |
| `run_code` | High (arbitrary) | Sandbox, no network/secrets, resource limits |

---

## 7. Observability, Cost, and Evaluation

### 7.1 Four signals

```text
Logs     → discrete facts: "tool X failed with 503 at step 4" (structured, with run_id/thread_id/tenant_id)
Metrics  → aggregated numbers over time: p95 latency, error rate, tokens/min, queue depth
Traces   → one run as a tree of timed spans: where time, tokens and errors went
Events   → business/lifecycle occurrences: run_started, approval_requested, run_completed, fallback_used
```

You need **all four** because each answers a different question: metrics say *something is wrong*, traces say *where*, logs say *what exactly*, events say *what the user-visible story was*.

### 7.2 Anatomy of a trace

```text
User Request
 ↓
Agent Run  [run_id, thread_id, tenant, model versions, graph version]
 ├── LLM call      (prompt tokens, completion tokens, latency, model, cost)
 ├── Tool call     (name, args hash, latency, status, retries)
 ├── LLM call
 ├── Tool call
 └── Final response
        ↓
   Trace / Metrics
```

Attach a **correlation ID** from gateway → API → queue → worker → tool calls so a single complaint can be traced end to end. Redact PII/secrets from traced prompts and tool I/O (or store payloads in access-controlled object storage with short retention).

### 7.3 What to measure for agents

| Metric | Why it matters | Red flag |
|---|---|---|
| **Agent (end-to-end) latency** (p50/p95/p99) | What users feel | Long tail growing |
| **Time to first token / first event** | Perceived responsiveness | Slow before streaming starts |
| **LLM latency** (per call, by model) | Isolates model slowness from your code | Provider degradation |
| **Tool latency** (per tool) | Finds the slow dependency | One tool dominates |
| **Token usage** (input/output, per call and per run) | Direct cost driver | Input tokens climbing (history bloat) |
| **Cost per request / per tenant / per feature** | Unit economics | Cost per successful task rising |
| **Number of tool calls per run** | Efficiency | Repeated identical calls |
| **Number of reasoning steps per run** | Loop health | Steps near max limit |
| **Error rate** (by type: LLM / tool / infra / validation) | Reliability | Spikes after deploy |
| **Retry rate** | Hidden instability; retries cost money | High retries masking a failing dependency |
| **Completion rate** (finished vs failed/cancelled/timed out/budget-exceeded) | Outcome health | Rising abandonment |
| **Cache hit rate** (by cache type) | Cost/latency leverage | Falling hit ratio |
| **Queue depth / age, concurrency utilisation** | Capacity | Age increasing |
| **Approval wait time / rejection rate** (HITL) | Process health and agent quality signal | Many rejections = poor proposals |
| **User feedback** (thumbs, rephrase/retry rate) | Real-world quality proxy | Repeated rephrasing |

**Metric hygiene:** track by **model, tool, tenant, graph version, prompt version**, so you can answer "did the new prompt make things worse?" Avoid high-cardinality metric labels (put IDs in traces/logs).

### 7.4 Cost as an operational metric

```text
cost/run = Σ over LLM calls (input_tokens × in_price + output_tokens × out_price)
         + tool/API fees + compute + storage
```

Cost grows with **steps × prompt size**. Levers:
- Fewer steps (better tools, clearer prompts, step limits, deterministic skeleton).
- Smaller prompts (history strategies, tool-output trimming, stable cached prefixes).
- **Model routing** (small model for classification/extraction, large for hard reasoning).
- Caching (Sections 4 and 5).
- Budgets: per-run hard cap, per-user daily cap, alerts on anomalies (a loop bug can burn money fast).
- Attribute cost to tenants/features for pricing and abuse detection.

Optimise **cost per *successful* task**, not cost per call. A cheaper model that fails twice as often can cost more overall.

### 7.5 Evaluation: does the agent actually work?

```text
Does the agent answer correctly?          → task success / answer quality
Does it choose the right tool?            → tool-selection accuracy
Does it hallucinate?                      → groundedness / faithfulness to sources
Does it waste tool calls?                 → trajectory efficiency
Does it become too expensive?             → cost per success, token budget compliance
Does it recover from failures?            → robustness under injected faults
```

**Evaluate two things:** the **final outcome** (was the answer/action right?) and the **trajectory** (were the intermediate steps sensible: right tools, right order, no loops?). Right outcome via a wasteful or risky path is still a defect.

| Eval type | How | Best for |
|---|---|---|
| **Golden dataset (offline)** | Curated inputs + expected outcomes/tool sequences, run on every prompt/model/graph change | Regression gating in CI |
| **LLM-as-judge** | A model scores answers against rubrics/references | Scalable quality scoring; calibrate against humans; beware judge bias |
| **Rule/programmatic checks** | Schema validity, forbidden tool use, step/cost limits, citation presence | Cheap, deterministic guardrail tests |
| **Human review** | Experts label samples | Ground truth, rubric creation, high-risk domains |
| **Fault-injection tests** | Force tool timeouts, 429s, malformed outputs | Verifies retry/fallback/recovery paths |
| **Adversarial/red-team tests** | Prompt-injection and abuse cases | Safety regression |
| **Online evaluation** | Sample live traffic, user feedback, A/B or canary comparisons | Real-world drift and quality |

**Evaluation loop:**

```text
Production traces ─► sample failures/low-feedback runs ─► add to eval dataset
        ▲                                                         │
        │                                                         ▼
  deploy (canary) ◄── pass thresholds? ◄── run evals on candidate change
```

Observability platforms (LangSmith, Langfuse, OpenTelemetry-based tooling, Arize and others) are examples of tools that capture traces and run evals. The architecture requirement is the *capability* (structured traces, datasets, scoring, comparison across versions), not a particular vendor.

**Alert on symptoms:** SLO burn (completion rate, p95 latency, error rate), cost anomalies, queue age, DLQ growth, guardrail-violation spikes. Keep runbooks per failure type.

---

## 8. Complete Production Agentic AI Design + Interview Framework

### 8.1 Final architecture

```text
                           USERS
                             │
                             ▼
                    CDN / WAF / Gateway
                             │
                             ▼
                       Load Balancer
                             │
                    ┌────────┴────────┐
                    ▼                 ▼
                API Server        API Server
                    │                 │
                    └────────┬────────┘
                             ▼
                       Agent Runtime
                             │
                   ┌─────────┼─────────┐
                   ▼         ▼         ▼
                 State      Queue     Cache
                   │         │         │
                   ▼         ▼         ▼
              LangGraph   Workers    Redis
                   │
          ┌────────┼──────────┐
          ▼        ▼          ▼
        LLMs     Tools      Memory
          │        │          │
          │     ┌──┼──┐       ├── SQL
          │     ▼  ▼  ▼       ├── Vector DB
          │    Web APIs       └── Object Storage
          │
          ▼
      Checkpoints
          │
          ▼
     Stream / Events
          │
          ▼
       Frontend

              ↓
      Observability / Tracing
```

**Reading the diagram as roles:** the edge (CDN/WAF/gateway) filters and authenticates. Stateless API servers translate requests into runs. The runtime executes durable steps. Queue and workers provide elasticity and fault isolation. Redis gives speed and coordination. SQL + vector + object storage hold durable truth. Checkpoints make runs resumable. Events turn slow work into visible progress. Observability spans everything.

### 8.2 Full request lifecycle

```text
User request
→ authentication
→ thread lookup
→ state/checkpoint restoration
→ agent execution
→ tool calls
→ reducers/state updates
→ checkpoint
→ retries/recovery
→ streaming
→ final response
```

Expanded as a sequence:

```text
Client         Gateway/API         Queue/Worker         Runtime/State        LLM/Tools         Stores
  │ POST /threads/{id}/runs │            │                    │                  │               │
  ├──────────►│ authN/authZ, tenant,     │                    │                  │               │
  │           │ rate/budget check        │                    │                  │               │
  │           │ validate input           │                    │                  │               │
  │           │ thread lookup/lock ──────┼────────────────────┼──────────────────┼──► SQL        │
  │           │ create run (queued)      │                    │                  │               │
  │◄── 202 + run_id / open SSE stream    │                    │                  │               │
  │           │ enqueue ────────────────►│ worker claims job  │                  │               │
  │           │                          ├───────────────────►│ load latest checkpoint ─────────► │
  │           │                          │                    │ retrieve memory (vector/SQL) ───► │
  │           │                          │                    │ node → LLM ─────►│ plan / tool req│
  │           │                          │                    │ validate+authorise tool call      │
  │           │                          │                    │ tool (idempotency key) ──────────►│
  │           │                          │                    │◄──── result / error (retry/fallback)
  │           │                          │                    │ reducer → new state               │
  │           │                          │                    │ checkpoint ─────────────────────► │
  │◄──────────┼──── events (tokens, tool start/end) via Redis pub/sub ◄──────┤                   │
  │           │                          │                    │ [interrupt? persist, release, wait]
  │           │                          │                    │ [resume: new job, same thread]    │
  │◄── final response + usage            │                    │ finalise: mark run completed      │
  │           │                          │                    │ async: summarise / extract memory │
  │           │                 traces/metrics/events emitted throughout                           │
```

Key properties to point out: API returns quickly; **state is durable after every step**; any worker can continue; retries are guarded by idempotency; events are decoupled from execution; post-run memory work is asynchronous.

### 8.3 Agentic AI System Design Framework (17 steps)

```text
1.  Requirements       2.  Agent boundaries     3.  State design
4.  Tool design        5.  Memory design        6.  Model selection
7.  Execution flow     8.  Persistence          9.  Streaming
10. Concurrency        11. Scaling              12. Reliability
13. Security           14. Observability        15. Cost
16. Evaluation         17. Trade-offs
```

| # | Step | Questions to answer | Typical decision |
|---|---|---|---|
| 1 | **Requirements** | Task types? Users/tenants? Latency expectations? Allowed autonomy? Failure tolerance? Compliance? Budget per task? | Write FR + NFR with numbers; define "success" measurably |
| 2 | **Agent boundaries** | Workflow or agent? One agent or several? What is explicitly *out of scope*? | Start with the least autonomy; split agents only for distinct tools/permissions/models or measurable struggle |
| 3 | **State design** | What must flow between steps? What merges (reducers)? What is large (reference it)? Versioning? | Small, typed, serialisable state; blobs by reference; backward-compatible changes |
| 4 | **Tool design** | Granularity? Schemas? Read vs write? Idempotent? Permissions? Error format? | Few well-described tools; strict schemas; risk tier per tool; errors the model can act on |
| 5 | **Memory design** | What is remembered, by whom, how long? Summarise/extract/retrieve? Deletion? | Window + summary + selective retrieval; explicit write policy and tenant isolation |
| 6 | **Model selection** | Which steps need strong reasoning vs cheap classification? Context size? Fallback? Self-host vs API? | Route by step difficulty; define fallback chain; evaluate before swapping |
| 7 | **Execution flow** | Deterministic skeleton vs free loop? Branching? Parallel steps? Step limits? Where do humans enter? | Graph for predictable parts, agentic pockets for flexible parts, bounded loops |
| 8 | **Persistence** | Checkpoint store? Retention? Run status in SQL? Blob storage? | Postgres for checkpoints/runs; object storage for large artifacts; retention policy |
| 9 | **Streaming** | What events? SSE vs WebSocket? Reconnect/replay? Cancellation? | SSE for one-way tokens/events; persisted event log for replay; propagate cancel |
| 10 | **Concurrency** | Per-thread ordering? Per-run parallelism? Worker concurrency? Tenant fairness? | Thread-keyed serialisation; bounded fan-out; async workers; per-tenant quotas |
| 11 | **Scaling** | Expected concurrent runs? Where is the bottleneck? Burst handling? | Stateless API + queue/workers; autoscale on queue age; pools; caches; partition only when measured |
| 12 | **Reliability** | Failure classes? Retries/fallbacks? Idempotency? Degradation modes? Recovery? | Timeouts + backoff + breakers + idempotency keys + DLQ + defined degraded modes |
| 13 | **Security** | Trust boundaries? Permissions? Injection? Approvals? Sandbox? Tenant isolation? | Least privilege, validated tool calls, risk-tiered approvals, sandboxed execution |
| 14 | **Observability** | Traces? Key metrics? Alerts? Redaction? Correlation IDs? | Trace every run; per-model/tool/tenant metrics; SLO-based alerts |
| 15 | **Cost** | Tokens per step? Steps per run? Budgets? Attribution? | Step/token caps, routing, caching, per-tenant budgets and alerts |
| 16 | **Evaluation** | Golden set? Trajectory checks? Judges? Online sampling? CI gates? | Offline regression suite + fault/adversarial tests + online monitoring |
| 17 | **Trade-offs** | What did you choose, what did it cost, when would you revisit? | State the decision, the cost, and the trigger for change |

### 8.4 Distinctions cheat-sheet

| Pair | The difference in one sentence |
|---|---|
| **State vs memory** | State is this run's working data; memory is information deliberately kept for future use |
| **Memory vs persistence** | Memory is *what the agent may recall*; persistence is *how data survives*. Not all persisted data is memory (checkpoints) |
| **Thread vs checkpoint** | Thread = the conversation container/key; checkpoint = one saved snapshot of execution within it |
| **Tool vs node** | Node = orchestration step you control; tool = capability the model may *request* |
| **Agent vs workflow** | In a workflow the code picks the path; in an agent the model does |
| **Queue vs direct execution** | Direct ties execution to the request; queue decouples accept from execute for durability and elasticity |
| **Streaming vs normal response** | Streaming sends incremental events (better perceived latency, more connection complexity); normal sends one final payload |
| **Concurrency vs parallelism** | Concurrency = many runs interleaved while waiting; parallelism = simultaneous branches within a run |
| **Scaling vs performance** | Scaling = handle more runs; performance = make each run faster/cheaper |
| **Reliability vs availability** | Availability = it responds; reliability = it responds correctly and consistently, including through failure |

### 8.5 Required table: problems and typical approaches

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

> **These are examples, not universal answers.** Each has a cost: caching risks staleness, fallbacks risk quality drops, queues add completion delay, checkpointing adds write load, HITL adds latency, and partitioning adds operational complexity. Always ask what the *requirement* is before reaching for the pattern.

### 8.6 Final mental model

```text
Traditional System
Client
 ↓
API
 ↓
Business Logic
 ↓
Database


Agentic System
Client
 ↓
API
 ↓
Agent Runtime / Graph
 ↓
State
 ↓
LLM ↔ Tools
 ↓
Memory / Databases
 ↓
Checkpoint
 ↓
Retry / Recovery / Interrupt
 ↓
Streaming
 ↓
Response
```

**One-paragraph version:** a traditional system executes *code you wrote* in a short request. An agentic system executes a *durable loop in which a probabilistic model chooses actions*, so you wrap that model in a runtime that **persists every step, bounds every loop, validates every action, isolates every tenant, streams progress, recovers from failure, and measures quality and cost**. The intelligence is the model's; the reliability is your architecture's.

### 8.7 Fifteen interview questions (with hints)

1. **Design a production research agent that browses the web, queries internal databases, and writes reports for 100K users. Walk through the architecture.**
   *Hint: stateless API, queue + workers, durable checkpoints, bounded parallel tools, streaming progress, per-tenant budgets.*

2. **When would you choose a deterministic workflow over a fully autonomous agent?**
   *Hint: predictability, compliance, cost, testability; use autonomy only where flexibility pays for its risk.*

3. **A run takes 10 minutes and the user closes the browser. What should happen?**
   *Hint: background execution, status in SQL, event replay on return, distinguish disconnect from explicit cancel.*

4. **How do you make agent tool calls safe to retry after a worker crash?**
   *Hint: steps replay after the last checkpoint; idempotency keys, check-then-act, separate read vs write tools.*

5. **Explain the difference between state, checkpoint, thread, and long-term memory, and where each is stored.**
   *Hint: run scratchpad vs snapshot vs conversation key vs cross-thread knowledge; Postgres/Redis/vector DB roles.*

6. **Why shouldn't you put the full conversation history in every prompt, and what do you do instead?**
   *Hint: cost multiplies per loop step, latency, context limits, noise; window + summary + extraction + retrieval.*

7. **How would you autoscale agent workers?**
   *Hint: CPU stays low while awaiting I/O; scale on queue depth/age and concurrency utilisation; Little's Law.*

8. **Your p95 latency doubled after a release. How do you find the cause?**
   *Hint: traces by span: LLM vs tool vs DB vs queue wait; compare by model/prompt/graph version; check token growth.*

9. **How do you defend an agent against prompt injection from retrieved documents?**
   *Hint: untrusted content is data; least-privilege tools, validated args, approvals for sensitive actions, break the private-data + untrusted-content + exfiltration triad.*

10. **Design human-in-the-loop approval for refunds, including what happens if the approver responds after three days.**
    *Hint: interrupt releases compute, persist exact action, expiry policy, re-validate state on resume, audit trail.*

11. **How do you handle provider rate limits (429s) across thousands of concurrent runs?**
    *Hint: shared token-bucket in Redis, queueing/backpressure, backoff with jitter, model routing, fallback provider.*

12. **How would you control and attribute cost for an agent platform?**
    *Hint: per-run caps (steps/tokens), tenant budgets, routing, caching, cost per successful task, anomaly alerts.*

13. **How do you evaluate an agent beyond "does the answer look right"?**
    *Hint: outcome + trajectory; golden sets, LLM judges calibrated to humans, fault injection, adversarial tests, online sampling.*

14. **Two requests arrive on the same thread at once. What happens, and what are the options?**
    *Hint: conflicting checkpoint writes; serialise per thread, reject with 409, or queue behind the active run.*

15. **When is multi-agent the wrong choice, and what would make you split into multiple agents or services?**
    *Hint: coordination overhead, multiplied cost, debugging difficulty; split for different tools/permissions/scaling profiles/teams, only after a single agent measurably fails.*

### 8.8 Bonus: common production mistakes

1. Running long agent loops inside the HTTP request with no durable state.
2. No step/token/time budgets, so one bug becomes a large bill.
3. Treating retries as free (non-idempotent writes duplicated).
4. Giving the agent a shared admin credential.
5. Trusting retrieved text or model output without validation.
6. Bloated state and unbounded history in every prompt.
7. Scaling API servers when the bottleneck is the LLM quota or one tool.
8. Shipping prompt/model changes without regression evals.
9. No tracing, so quality failures are invisible until users complain.
10. Adopting multi-agent and distributed services before a single well-bounded agent has been proven insufficient.