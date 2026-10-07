# Architectural Overview: HITL LinkedIn Content Agent

## 1. System Topology
* **Inner ReAct Loop (`writer` <-> `tools`):** Dynamically invokes Tavily search to fetch context before drafting content.
* **Parallel Fan-Out/Fan-In:** Evaluates drafts concurrently through `content_reviewer` and `compliance_reviewer`, aggregating results.
* **Governance Gate (`human_review`):** Pauses graph execution to enforce human oversight.

## 2. Human-in-the-Loop (HITL) Mechanism
The system uses two core primitives for interactive governance:

1. **`interrupt(some_data)`**
   * Placed inside the `human_review` node to freeze graph execution instantly.
   * Transmits the current draft and feedback payload up to the CLI runtime.
   * Halts execution and waits for operator input.

2. **`Command(resume=value)`**
   * Injected into `app.stream()` after a pause.
   * Resumes graph execution by passing operator approval or revision feedback directly back into the suspended node.