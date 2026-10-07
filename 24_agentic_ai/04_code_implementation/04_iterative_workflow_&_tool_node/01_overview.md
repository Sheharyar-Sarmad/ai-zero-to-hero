# Project: Iterative Workflow & Multi-Agent Refinement (LinkedIn Post Engine)

## Overview
A LangGraph state machine that writes LinkedIn posts through cyclical feedback loops, bounded tool use, and parallel multi-agent review. A writer agent drafts the post (optionally grounded by one Tavily web search), two reviewer agents evaluate it in parallel, and the result is looped back to the writer until it is approved or the attempt budget is exhausted.

## Patterns Used
1. **ReAct tool loop (Writer ⇄ Tools):** The writer LLM decides whether to call Tavily web search. Tool use is capped at **1 call per run**; once the budget is spent, the writer switches to an unbound LLM that cannot call tools.
2. **Parallel fan-out / fan-in (Reviewers → Aggregator):** `content_reviewer` and `compliance_reviewer` run in the same superstep and write to disjoint state keys. `aggregate_reviews` merges them: approval = content **AND** compliance.
3. **Evaluator-optimizer loop (Aggregator → Writer):** Combined reviewer feedback is stored in `review_feedback` and fed back to the writer for the next rewrite, capped at **3 attempts**.
4. **Multi-LLM setup:** A larger, creative model writes; a smaller, low-temperature model judges.

| Role | Model | Temperature |
|---|---|---|
| Writer | `openai/gpt-oss-120b` | 0.8 |
| Reviewers | `openai/gpt-oss-20b` | 0.3 |

## Graph Flow
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

## Nodes
| Node | Responsibility |
|---|---|
| `writer` | Writes or rewrites the post using the full message history, so it sees tool results |
| `tools` | Runs the Tavily search (3 results) |
| `extract_draft` | Copies the writer's final text into `draft` |
| `content_reviewer` | Checks hook, takeaway, skimmability, length, CTA, tone |
| `compliance_reviewer` | Checks hashtags and formatting rules |
| `aggregate_reviews` | Fan-in; sets `is_approved` and merges feedback |

## State
`topic`, `messages` (append-only via `add_messages`), `draft`, `content_feedback`, `compliance_feedback`, `review_feedback`, `content_approved`, `compliance_approved`, `is_approved`, `attempts`, `tool_calls_used`.

## Workflow Lifecycle
* **Input State:** The CLI creates a fresh `thread_id` (UUID) per topic and initializes all counters to zero, with `recursion_limit=25` in the graph config.
* **Iterative Execution:** The writer optionally searches once, drafts, then the draft is reviewed in parallel. Rejections route back to the writer through the outer loop.
* **Convergence & Stop Conditions:** Execution ends when both reviewers approve, or when `attempts` reaches `MAX_ATTEMPTS = 3`. The recursion limit acts as a hard safety net.

## Safeguards & Reliability
* **Rate limiting:** One shared `InMemoryRateLimiter` (~24 requests/min) covers every Groq call (writer and both reviewers).
* **Retries and timeouts:** `max_retries=3` with backoff for 429s, and `timeout=60` so calls never hang.
* **Bounded loops:** `MAX_TOOL_CALLS = 1`, `MAX_ATTEMPTS = 3`, `recursion_limit = 25`.
* **Checkpointing:** `MemorySaver` (in-process); a new thread per topic prevents old messages leaking into new runs.

## Known Limitations
* Verdict parsing relies on string matching (structured output would be more robust).
* Hashtag and word-count checks are done by an LLM; deterministic Python checks would be more reliable.
* `MemorySaver` and the rate limiter are per-process only.
* If the final attempt is rejected, the last draft is returned (no best-of selection).