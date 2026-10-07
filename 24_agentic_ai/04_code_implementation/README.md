# 24 · Agentic AI with LangGraph Code Implementation

Hands-on code implementation of agentic AI workflows using **LangGraph**, **Groq**, and **Tavily**, part of my [ai-zero-to-hero](https://github.com/Sheharyar-Sarmad/ai-zero-to-hero) repository.

---

## Workflows Covered

### 1. Sequential Content Pipeline

**What is a sequential workflow?**
A multi-stage pipeline where data moves in a strict, linear progression from start to end. There are no loops, decision branches, or parallel tasks; each step must finish before the next one begins.

**Project:** An automated system for a content creator who needs to turn raw scripts into polished ones. The output of each node is the exclusive input of the next:

1. **Start:** Receives the raw data.
2. **Editor node:** Cleans up grammar and tone.
3. **Scriptwriter node:** Formats the edited text into an engaging script.
4. **Hinglish node:** Converts the content into Hinglish.
5. **End:** Delivers the final output to the user.

---

### 2. Parallel Workflow & Reducers: AI Content Moderation & Brand Safety Pipeline

Instead of processing text sequentially, the pipeline broadcasts any raw text (a video script, blog draft, or user comment) to **three specialized agents running in parallel**. Each scores the text from 0 to 100 from a different perspective:

* **Toxicity Monitor:** Aggressive language, profanity, hate speech.
* **Copyright Cop:** Plagiarism, trademark violations, unoriginal copy risks.
* **Cultural Guide:** Regional sensitivities and political landmines for a global audience.

**Role of reducers:** When parallel agents return results concurrently, reducers define how those state updates are safely combined, merged, or accumulated into the global state.

---

### 3. Conditional Workflow & RAG Integration

A multi-path chatbot for a college environment supporting three branches: **BCA**, **BBA**, and **B.Com**.

1. **Academic RAG path:** Answers from the institutional academic PDF.
2. **Fee RAG path:** Answers fee and payment questions from the fee PDF.
3. **General knowledge path:** Handles standard queries with the LLM's base knowledge.

**Lifecycle:** The user selects a branch and submits a query. Conditional routing evaluates the intent and directs the flow to Academic RAG, Fee RAG, or the general LLM. All paths then merge into a single convergence node that delivers the final response.

---

### 4. Iterative Workflow & Multi-Agent Refinement: LinkedIn Post Engine

A state machine that writes LinkedIn posts through cyclical feedback loops, bounded tool use, and parallel multi-agent review. A writer drafts the post (optionally grounded by one Tavily search), two reviewers evaluate it in parallel, and the result loops back to the writer until it is approved or the attempt budget is exhausted.

**Patterns used**

1. **ReAct tool loop (Writer ⇄ Tools):** The writer decides whether to call Tavily. Tool use is capped at **1 call per run**; afterwards the writer switches to an unbound LLM that cannot call tools.
2. **Parallel fan-out / fan-in:** `content_reviewer` and `compliance_reviewer` run in the same superstep and write to disjoint state keys. `aggregate_reviews` merges them (approval = content **AND** compliance).
3. **Evaluator-optimizer loop:** Combined feedback is stored in `review_feedback` and fed back to the writer, capped at **3 attempts**.
4. **Multi-LLM setup:** A larger, creative model writes; a smaller, low-temperature model judges.

| Role | Model | Temperature |
|---|---|---|
| Writer | `openai/gpt-oss-120b` | 0.8 |
| Reviewers | `openai/gpt-oss-20b` | 0.3 |

**Graph flow**

```
START → writer ⇄ tools (max 1 Tavily call)
          ↓ (no tool call)
     extract_draft
        ↙       ↘            (parallel)
content_reviewer  compliance_reviewer
        ↘       ↙
     aggregate_reviews
          ↓
 approved or attempts ≥ 3 ? → END
          ↓ no
        writer (with feedback)
```

**Safeguards**

* One shared `InMemoryRateLimiter` (~24 requests/min) across every Groq call
* `max_retries=3` with backoff and `timeout=60`
* Bounded loops: `MAX_TOOL_CALLS = 1`, `MAX_ATTEMPTS = 3`, `recursion_limit = 25`
* Fresh `thread_id` per topic so old messages never leak into new runs
* Streamlit UI with a per-IP limit of 3 posts per day

---

### 5. Human-in-the-Loop (HITL) LinkedIn Content Agent

**System topology**

* **Inner ReAct loop (`writer` ⇄ `tools`):** Invokes Tavily search to fetch context before drafting.
* **Parallel fan-out/fan-in:** Evaluates drafts concurrently through `content_reviewer` and `compliance_reviewer`, then aggregates.
* **Governance gate (`human_review`):** Pauses graph execution to enforce human oversight.

**HITL primitives**

1. **`interrupt(some_data)`**
   * Placed inside the `human_review` node to freeze the graph.
   * Sends the current draft and feedback payload to the CLI runtime.
   * Waits for operator input.
2. **`Command(resume=value)`**
   * Injected into `app.stream()` after a pause.
   * Resumes execution by passing operator approval or revision feedback back into the suspended node.

---

### 6. Subgraphs & Advanced Streaming

**Subgraphs (modular architecture)**
A fully compiled `StateGraph` can be nested inside a parent graph as a node.

* **Benefits:** Encapsulated logic, no state namespace pollution, isolated testing.
* **Integration patterns:**
  * **Direct node addition:** When parent and subgraph share identical state keys, data flows through shared channels automatically.
  * **Wrapper function node:** When schemas differ, the wrapper maps parent keys to subgraph inputs and translates outputs back.

**Token-by-token streaming (`stream_mode="messages"`)**

* Taps into intermediate LLM token generation across nodes in real time.
* Raw token chunks are formatted as Server-Sent Events (`data: <token>\n\n`, ending with `data: [DONE]\n\n`) for web clients.

**Event-by-event streaming (`stream_mode="updates"`)**

* Yields control the moment any node finishes.
* Returns only the incremental state update from that node.
* Powers real-time progress trackers, step-by-step logs, and live UI dashboards.

---

## What's Next

The next step is to build **good, serious-level AI orchestrated workflows**: production-grade multi-agent systems that combine everything covered here (parallelism, conditional routing, tool use, human oversight, subgraphs, and streaming) into real-world applications.

---

## Links

* **This module:** [24_agentic_ai](https://github.com/Sheharyar-Sarmad/ai-zero-to-hero/tree/main/24_agentic_ai)
* **Repository:** [ai-zero-to-hero](https://github.com/Sheharyar-Sarmad/ai-zero-to-hero)
* **GitHub:** [Sheharyar-Sarmad](https://github.com/Sheharyar-Sarmad)
* **LinkedIn:** [Sheharyar Sarmad](https://www.linkedin.com/in/sheharyar-sarmad-9b7736289/)