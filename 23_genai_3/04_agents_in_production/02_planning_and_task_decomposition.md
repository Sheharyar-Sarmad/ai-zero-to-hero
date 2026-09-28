# Planning and Task Decomposition

A language model can answer a question in one step, but it cannot build a product in one step.
**Planning** is how an agent turns a large goal into small actions it can execute, check, and fix.
This chapter uses one running example: **"Build and deploy a full-stack SaaS application."**
The core loop is: decompose the goal, order the pieces, validate the plan, execute it, observe results, and replan when reality disagrees.

## 1. Core Vocabulary

- **Goal**: the outcome we want. Example: "a deployed SaaS app with login and an AI feature."
- **Task**: a unit of work toward the goal. Example: "Build backend."
- **Subtask**: a smaller task inside a task. Example: "Write the `/projects` endpoint."
- **Action**: one executable step, usually a tool call. Example: `write_file("api/projects.py")`.

In short: Goal → Tasks → Subtasks → Actions.

A task is small enough when the agent can do it in a few tool calls and check the result.

## 2. Decomposition and Hierarchy

**Task decomposition** means splitting a big goal into smaller tasks that are individually achievable.
**Hierarchical planning** keeps the plan as a tree, where high-level tasks are refined into lower-level ones.
**Recursive planning** is the algorithm behind it: if a task is not directly executable, split it, then plan each piece the same way.

```text
Build SaaS
├── Architecture
├── Database
├── Backend
│   ├── Design API routes
│   ├── Implement endpoints        ← refined only when needed
│   └── Add validation
├── Frontend
├── Auth
├── AI feature
├── Test
└── Deploy
```

A good decomposition covers the whole goal, has a way to check each task is done, and has little overlap between tasks.

## 3. Dependencies and DAGs

A **dependency** means task B needs task A to finish first. You can't test what isn't built.
A **DAG** (Directed Acyclic Graph) draws tasks as nodes and dependencies as arrows. "Acyclic" means no loops, because if A needs B and B needs A, nothing can ever start.

```text
Architecture ──┬──► Database ──► Backend ──┬──► Auth ──┐
               │                           └──► AI ────┼──► Test ──► Deploy
               └──► Frontend ──────────────────────────┘
```

In Python, a plan can be a dictionary that maps each task to the tasks it waits for:

```python
deps = {
    "architecture": [],
    "database": ["architecture"],
    "backend": ["architecture", "database"],
    "frontend": ["architecture"],           # needs only the API contract
    "auth": ["backend"],
    "ai": ["backend"],
    "test": ["frontend", "auth", "ai"],
    "deploy": ["test"],
}
```

Each key is a task and each list is its prerequisites. An empty list means it can start immediately.
Python's `graphlib.TopologicalSorter(deps)` orders this graph and raises `CycleError` if it contains a loop.

## 4. Preconditions, Postconditions, and Constraints

A **precondition** is what must be true before a task starts. A **postcondition** is what must be true after it succeeds.
A dependency really means "A's postconditions satisfy B's preconditions." Postconditions also give each task a **definition of done**.

```text
Backend   pre:  database schema exists, DB reachable
          post: server starts and /health returns 200
Deploy    pre:  tests pass, DEPLOY_TOKEN set, human approved
          post: production URL returns 200
```

Here is a task type in TypeScript that carries these checks:

```typescript
interface Task {
  id: string;
  description: string;
  dependsOn: string[];        // the DAG edges
  tool?: string;              // which tool executes it
  preconditions: string[];    // must hold before starting
  doneWhen: string[];         // postconditions: the definition of done
  status: "pending" | "running" | "done" | "failed";
  attempts: number;           // used to cap retries
}
```

**Constraints** are limits a plan must respect: budget, deadline, allowed tools, required technologies, safety rules.
The **planning horizon** is how far ahead the agent plans in detail. Planning too far ahead is brittle, and planning too little is aimless.
The usual answer is a **rolling horizon**: plan everything coarsely, plan the next phase in detail, and refine later phases when you reach them.

## 5. Generate → Validate → Execute

Reliable agents keep three phases separate.
**Generate** means the model proposes a plan. **Validate** means cheap checks run before any real work starts. **Execute** means tasks run in order, and each postcondition is verified.

```text
Goal ──► Generate ──► Validate ──► Execute ──► Observe
              ▲           │ invalid       │ failure
              └───────────┴───────────────┘
```

Validation is usually plain code, not another model call, which is why it is trustworthy. It asks:

- Is the graph acyclic, and does every task have a definition of done?
- Do the named tools exist, and are credentials present?
- Does the plan fit the budget and safety rules?

In the SaaS example, validation catches a missing `LLM_API_KEY` before an hour of work is spent on the AI feature.

## 6. Parallelism and Planner–Executor

**Sequential execution** runs one task at a time. **Parallel execution** runs independent tasks at once.
The DAG shows what is safe: tasks with no path between them can run together.

```text
Architecture → (Database ‖ Frontend) → Backend → (Auth ‖ AI feature) → Test → Deploy
```

Parallel work risks conflicts, such as two tasks editing one file. Writing the API contract first lets Frontend run safely beside Database.

The **planner–executor architecture** splits thinking from doing.
The **planner** (usually a strong model) decides what to do. The **executor** carries out tasks and calls tools. The **replanner** is the planner called again with new evidence.

```text
Goal ─► Planner ─► Validator ─► Executor ─► Observations
           ▲                        │              │
           └──────── Replanner ◄────┴── failure ◄──┘
```

This split lets you review a plan before it runs and tell whether a failure came from the plan or the execution.

## 7. Planning with Tools and Under Uncertainty

A **tool** is something the agent can call to act, such as a shell, file editor, API, or database.
Tools define what is executable: "Run migration 001 with `db_tool`" is a valid leaf task, while "Build database" is not.
Tool results also feed back into the plan. A failing `pytest` run becomes a new subtask, "fix the import error."
Verify tool results instead of trusting them, and put irreversible tools behind approval.

**Planning under uncertainty** means planning when some assumptions might be wrong.
For example, "the LLM API supports JSON output" or "the host supports WebSockets."
Three tactics help:

- **Write assumptions down** so they can be checked later.
- **Probe early**: call the LLM API once before building the whole AI feature.
- **Front-load risk**: confirm the deploy target before writing thousands of lines.

## 8. Failure, Replanning, and Backtracking

**Replanning** means creating a new plan from the current state, not from scratch.
**Backtracking** means returning to an earlier decision and choosing a different branch.
Try the cheapest fix first:

```text
failure
  ↓
retry → repair → local replan → backtrack → global replan → human
```

In the SaaS example, two failures need different responses:

```text
Test fails: login returns 500 (code uses `password_hash`, DB column is `password`)
  → a bug, so repair: add subtask "reconcile auth with schema", rerun tests.

Deploy fails: the serverless host can't keep WebSocket connections open
  → a wrong assumption, so backtrack to "deploy on serverless" and replan:
    keep Database, Frontend, Auth, AI (still valid)
    replace Deploy with: Containerize → Provision host → Deploy → Smoke test
```

The main loop, in short Python:

```python
def run_agent(goal, max_replans=2):
    plan = planner.generate(goal)
    for _ in range(max_replans + 1):             # hard cap on replans
        problems = validate(plan)
        if problems:
            plan = planner.revise(plan, problems)    # fix the plan before acting
            continue
        failure = execute(plan)                  # runs in dependency order, checks postconditions
        if failure is None:
            return "goal completed"
        plan = planner.replan(goal, plan, failure)   # completed tasks are kept
    return escalate_to_human()                   # stop safely instead of looping
```

Without limits, agents loop forever. Cap **retries** per task, **replans** per goal, and **decomposition depth** per branch.

## 9. Planning Failure Modes

- **Underplanning**: the agent starts coding with no plan, then finds the API doesn't exist and rewrites everything. Fix: plan architecture and interfaces first.
- **Overplanning**: a 400-step plan that the first failure invalidates. Fix: rolling horizon, detailed near-term and coarse far-term.
- **Goal drift**: the agent slowly optimizes for something else, like polishing the logo instead of deploying. Fix: keep the original goal and definition of done in every planning step, and ask which part of the goal each task serves.
- **Infinite decomposition**: splitting forever ("choose color" → "research color psychology" → ...). Fix: stop when a tool can do the task, and cap the depth.

## 10. Four Ways Agents Plan

- **Reactive**: picks one action at a time from the latest observation. On the SaaS goal it fixes errors quickly but loses the big picture and can't say what "done" is.
- **Workflow**: a human fixed the DAG in advance, so it runs the same eight steps every time. Predictable and cheap, but it stops when something unexpected happens.
- **Planner–executor**: generates and validates a full plan, runs it, and replans explicitly on failure. Good when you want oversight.
- **Dynamic planning**: plans coarsely, refines as it learns (like discovering the WebSocket requirement mid-build), and rewrites the remaining plan constantly. Most flexible, but it needs strong guards against drift and replan loops.

Real systems mix them: a workflow skeleton with dynamic planning inside each stage.

## 11. Production Lessons

1. Plans should be **structured data** (typed tasks and dependencies), not prose.
2. **Validate before execution**, using code rather than the model's own opinion.
3. Every task needs a **definition of done** that can actually be checked.
4. **Track dependencies explicitly** so you know what can run in parallel and what a failure breaks.
5. **Plan near-term details**, not everything.
6. **Bound retries, replans, and decomposition depth.**
7. **Preserve completed work** when replanning.
8. **Keep the original goal fixed** in every planning step.
9. **Verify tool results** instead of assuming an action worked.
10. **Require approval for irreversible actions** like deploys, deletions, and payments.

```text
Goal
 ↓
Decompose
 ↓
Dependencies
 ↓
Plan
 ↓
Validate
 ↓
Execute
 ↓
Observe
 ↓
Replan when necessary
 ↓
Goal completed
```