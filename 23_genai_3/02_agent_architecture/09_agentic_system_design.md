# AI Agent System Design

You've spent eight lessons learning individual pieces of the agent puzzle: the LLM, tools, the agent loop, decision making, state, memory, human approval, and safety. Now it's time to put every piece on the table, see the whole picture at once, and get ready to actually build one.

By the end of this lesson, you should be able to look at *any* AI agent — a chatbot, a coding assistant, a support bot — and mentally break it down into the same set of building blocks. And once you can do that, you're ready to start building your own.

---

## 1. From Individual Concepts to a System

Let's quickly remind ourselves what each concept does, and more importantly, how they connect.

- **LLM** — the "brain." It reads text and predicts what should come next. On its own, it can't do anything in the real world — it can only think and talk.
- **Tools** — the "hands." Functions like `get_weather()` or `search_database()` that let the agent actually *do* things or fetch real information.
- **Agent Loop** — the "heartbeat." The repeating cycle of think → act → observe → think again that keeps the agent working until the task is done.
- **Decision Making** — the "judgment." How the LLM decides *whether* to use a tool, *which* tool to use, and *when* it has enough information to answer.
- **State** — the "short-term memory of this task." What's happened so far in this specific conversation or task (messages, tool results, progress).
- **Memory** — the "long-term memory." Facts and preferences that persist *across* conversations, not just within one.
- **Human Approval** — the "safety brake." A checkpoint where a human confirms a risky or irreversible action before it happens.
- **Safety** — the "guardrails." Limits, validation, and restrictions that keep the agent from doing something harmful, wasteful, or wrong.

None of these pieces are impressive alone. A brain with no hands can't act. Hands with no brain can't decide. A loop with no safety brake is dangerous. **An agent system is what happens when you wire all of these together correctly.**

That's the whole point of this lesson — the wiring diagram.

---

## 2. Complete Agent Architecture

Here is the full architecture of a typical agent system:

```
                         User
                          │
                          ▼
                    Application
                          │
                          ▼
                        Agent
                          │
        ┌─────────┬───────────┬──────────┬─────────┐
        │         │           │          │         │
        ▼         ▼           ▼          ▼         ▼
      Model  Instructions   State     Memory     Tools
                                                    │
                                    ┌───────────────┼───────────────┐
                                    │               │               │
                                    ▼               ▼               ▼
                              Weather API      Search API       Database
```

A quick walk-through of each layer:

- **User** — the person typing a request.
- **Application** — the surrounding program (a website, an app, a CLI). This is *not* the agent itself — it's the container that hosts the agent and enforces rules.
- **Agent** — the coordinator that ties together the model, instructions, state, memory, and tools for this specific task.
- **Model** — the LLM doing the thinking.
- **Instructions** — the system prompt: the agent's job description, personality, and rules.
- **State** — this task's working memory.
- **Memory** — long-term, cross-session knowledge.
- **Tools** — the specific capabilities this agent is allowed to use, each connecting out to a real API or database.

Notice that the **User never talks to the Model directly** — everything passes through the Application and Agent first. This matters a lot in Section 6.

---

## 3. Complete Agent Loop

Zooming into the "Agent" box from the diagram above, here is what happens on every single turn:

```
                       User
                        │
                        ▼
              Understand request
                        │
                        ▼
                  Check state
                        │
                        ▼
                 LLM decision
                        │
                        ▼
                  Need tool?
                 ┌──────┴──────┐
                 │             │
                 No           Yes
                 │             │
                 ▼             ▼
          Final answer     Tool call
                                │
                                ▼
                           Validation
                                │
                                ▼
                          Tool execution
                                │
                                ▼
                           Observation
                                │
                                ▼
                          Update state
                                │
                                ▼
                               LLM
                                │
                                ▼
                        Continue / Stop
```

A few important details:

- **"Need tool?"** is a decision made by the LLM based on the request — not a hardcoded rule.
- **Validation** happens *before* execution — the application checks that the tool call is safe and well-formed (correct arguments, allowed action, etc.) before anything runs.
- **Observation** is simply the tool's result being handed back to the LLM as new information.
- **Update state** means the observation gets added to the conversation history, so the LLM's next decision is based on everything that happened so far.
- The loop can repeat many times ("Continue") before it finally reaches "Stop" and gives a final answer.

This loop is the heartbeat of every agent you'll ever build, no matter how complex the system gets around it.

---

## 4. Example: Research Agent

**Request:** *"Find today's weather in Lahore and summarize what I should wear."*

Let's trace this through the full system.

1. **User** sends the request to the **Application**.
2. **Application** passes it to the **Agent**, along with the system instructions ("You are a helpful assistant with access to a weather tool...").
3. **Agent** checks **state** — this is a new conversation, so state is mostly empty.
4. **LLM decision**: the model reads the request and realizes it doesn't know today's weather in Lahore — it needs a tool.
5. **Need tool? → Yes.** The LLM outputs a tool call: `get_weather(city="Lahore")`.
6. **Validation**: the application checks that `"Lahore"` is a valid, well-formed argument, and that this agent is allowed to call the weather tool.
7. **Tool execution**: the application actually calls the Weather API.
8. **Observation**: the API returns something like `{"temp": 34, "condition": "sunny"}`.
9. **Update state**: this result is added to the conversation history.
10. **LLM** now has the weather data and decides it has enough information to answer — **Stop**.
11. **Final answer**: "It's 34°C and sunny in Lahore today — light, breathable clothing and sunglasses would be a good idea!"
12. **Application** sends this final answer back to the **User**.

Notice: the LLM never touched the internet itself. It only *decided* to call a tool. The **application** did the actual calling.

---

## 5. Example: Customer Support Agent

Support agents are a great example because they mix normal actions with sensitive ones.

**Request:** *"Where's my order, and can you cancel it?"*

1. **Understand request** — the LLM sees two parts: a status check, and a cancellation.
2. **Check state** — has this customer been identified in this conversation already?
3. **LLM decision** — it needs customer info first.
4. **Tool call** → `search_customer(email=...)` → **Validation** → **Execution** → **Observation** (customer found).
5. **Update state**, back to **LLM**.
6. **LLM decision** — now it needs the order.
7. **Tool call** → `check_order_status(order_id=...)` → **Validation** → **Execution** → **Observation** (order is "in transit").
8. **Update state**, back to **LLM**.
9. **LLM decision** — the customer also wants to *cancel*. Cancelling an order is irreversible and affects money — this is flagged as a **sensitive action**.
10. **Human approval** — instead of executing immediately, the agent pauses and asks a human (a support supervisor, or even the customer themselves) to confirm: *"Confirm cancellation of Order #4521?"*
11. Only after approval does the **tool execution** for `cancel_order()` happen.
12. **Final answer** to the user: order status shared, and cancellation confirmed (or explained as pending approval).

This example shows why **not every tool should behave the same way**. Read-only tools (like checking status) can run freely. Actions with real consequences (like cancelling an order) need a human checkpoint.

---

## 6. System Boundaries

This is one of the most important ideas in this whole lesson:

> **The LLM should never be in direct control of everything. The application code must remain in control of the system.**

The LLM is excellent at *deciding* — but terrible at being *trusted* with unrestricted power, because it can make mistakes, be tricked, or misunderstand a request.

The **application** — plain, predictable, human-written code — must always control:

- **Authentication** — verifying who the user actually is
- **Permissions** — what this specific user/agent is allowed to do
- **Tool execution** — the LLM requests a tool call, but the application decides whether and how to actually run it
- **Validation** — checking arguments are safe and correctly formed
- **External APIs** — all real network calls happen in application code, never "inside" the model
- **Database operations** — especially writes, deletes, and anything irreversible
- **Safety limits** — rate limits, spending caps, forbidden actions

Think of the LLM as a very smart advisor sitting behind a locked door. It can *suggest* actions all day long, but the application is the only one holding the keys.

---

## 7. Reliability

A working demo is easy. A *reliable* agent system that works day after day requires some unglamorous engineering:

- **Timeouts** — if a tool call takes too long (an API is slow or hanging), don't let the whole agent freeze. Cut it off and handle the failure gracefully.
- **Retries** — some failures are temporary (a flaky network). Retrying a failed tool call once or twice can quietly fix many issues.
- **Validation** — always double-check tool inputs *and* outputs. Never trust that the LLM's arguments are perfectly formed.
- **Error handling** — when something breaks, the agent should not crash silently. It should catch the error and either recover or clearly tell the user something went wrong.
- **Logging** — record what the agent decided, which tools it called, and what happened. This is essential for debugging weird behavior later.
- **Monitoring** — keep an eye on the system in production: how often tools fail, how long things take, how often humans have to intervene.
- **Rate limits** — prevent the agent from calling a tool (or spending money) too many times too quickly, whether from a bug or a runaway loop.

None of these are exciting, but they're the difference between a fun prototype and something you can actually put in front of real users.

---

## 8. Agent Design Checklist

Before shipping any agent, run through this list:

```
[ ] Clear goal
[ ] Appropriate model
[ ] Useful tools
[ ] Tool schemas
[ ] State
[ ] Memory if needed
[ ] Limits
[ ] Validation
[ ] Permissions
[ ] Human approval where needed
[ ] Logging
[ ] Error handling
[ ] Clear stopping condition
```

A short note on each:

- **Clear goal** — can you describe in one sentence what this agent is for?
- **Appropriate model** — does the task need a powerful model, or would a smaller/cheaper one do?
- **Useful tools** — does the agent have exactly the tools it needs (not too few, not too many)?
- **Tool schemas** — are tool inputs/outputs clearly defined so the LLM can use them correctly?
- **State** — is the current task's context being tracked properly?
- **Memory if needed** — does this agent actually need to remember things across sessions, or is that unnecessary complexity?
- **Limits** — are there caps on loops, cost, and tool calls?
- **Validation** — is every tool call checked before it runs?
- **Permissions** — does the agent only have access to what it's supposed to?
- **Human approval where needed** — are risky actions gated behind a human checkpoint?
- **Logging** — can you see what the agent did after the fact?
- **Error handling** — does the system fail gracefully instead of crashing?
- **Clear stopping condition** — does the agent know when it's actually done?

---

## 9. The Complete Mental Model

Here's the whole lesson distilled into one formula:

```
Agent = Model + Instructions + Tools + State + Decision Loop + Control
```

Let's unpack it piece by piece:

- **Model** — the reasoning engine that reads and generates text.
- **Instructions** — the system prompt that shapes how the model behaves and what its job is.
- **Tools** — the capabilities that let the agent affect or query the real world.
- **State** — the memory of what's happened *within* this task.
- **Decision Loop** — the repeating think → act → observe cycle that drives progress toward the goal.
- **Control** — the application-level boundaries, validation, and human checkpoints that keep the whole thing safe and reliable.

**Important note:** this formula is a *teaching tool*, not a formal mathematical or engineering definition. You won't find it in a textbook written with "+" signs. It's simply a memorable way to hold all six ingredients in your head at once. Real agent systems will mix these pieces together in more complex and overlapping ways — but if any one of these six ingredients is completely missing, what you have isn't really a complete agent system yet.

---

## 10. It's Time to Build an Agent

This is the moment all eight previous lessons were leading up to: **you now know enough to design and build a real agent.** Everything from here is about applying this system design, not learning new theory.

Here's how we'll apply it, step by step:

1. **Build tools** — write real functions the agent can call.
2. **Connect tools to an LLM** — give the model the ability to request those functions.
3. **Build a manual agent** — hand-write the loop from Section 3 yourself, so you understand every step.
4. **Build multi-tool agents** — let the agent choose between several tools intelligently.
5. **Add human approval** — implement a real approval checkpoint for sensitive actions.
6. **Use framework abstractions** — see how popular agent frameworks package all of this for you.
7. **Build the complete project** — combine everything into one working, end-to-end agent.

Every one of these steps maps directly back to the architecture diagram and the loop diagram in this lesson — you're not learning new concepts, you're applying the ones you already have.

### Applying the design: a quick walk-through

To make this concrete, let's apply the system design to a brand-new example before we start building: a **"trip planning agent"** that helps a user plan a day out.

**Request:** *"I'm free this afternoon in Lahore — plan something fun for me."*

Applying our mental model:

- **Model** — a capable LLM that can reason about preferences and plans.
- **Instructions** — "You are a local activity planner. Use the weather and search tools to suggest a realistic plan."
- **Tools** — `get_weather(city)`, `search_places(query)`.
- **State** — tracks the user's request and any follow-up answers ("Do you prefer indoors or outdoors?").
- **Decision Loop** — the agent checks the weather first (rain would rule out outdoor plans), then searches for matching places, then reasons over both results together.
- **Control** — the application validates that `search_places` only returns real, safe locations, and caps the agent at a few tool calls so it doesn't loop endlessly.

Running it through the loop from Section 3:

```
Understand request → Check state → LLM decision
   → Need tool? Yes → get_weather("Lahore")
   → Validation → Execution → Observation: "32°C, clear skies"
   → Update state → LLM decision
   → Need tool? Yes → search_places("outdoor afternoon activities Lahore")
   → Validation → Execution → Observation: [list of places]
   → Update state → LLM decision
   → Need tool? No → Final answer
```

**Final answer:** "It's clear and warm this afternoon, so here's an outdoor plan: a walk through Lahore Fort, followed by coffee somewhere shaded nearby."

Notice this example uses *exactly* the same architecture, loop, and boundaries as the weather and support agent examples above — that's the whole point of having one mental model. Once you can apply it to a new scenario like this on your own, you're ready to start building.

---

## 11. Final Summary

1. An agent is not just an LLM — it's an LLM combined with tools, state, memory, and control.
2. The **agent loop** (understand → decide → act → observe → update → repeat) is the heartbeat of every agent.
3. Tools give the agent "hands" to act in the real world; the LLM alone can only think and talk.
4. **State** tracks progress within a single task; **memory** carries knowledge across sessions.
5. Not every tool call should run freely — sensitive or irreversible actions need **human approval**.
6. The **application code**, not the LLM, must always control authentication, permissions, execution, and safety.
7. Validation should happen *before* every tool executes, not after.
8. Reliability (timeouts, retries, logging, error handling) is what separates a demo from a real system.
9. The checklist in Section 8 is a practical tool you can reuse for every agent you design going forward.
10. `Agent = Model + Instructions + Tools + State + Decision Loop + Control` is a simple mental model — not a formal formula — to help you remember all the moving parts.

You now have a complete mental model of an AI agent system — and, as the trip-planning example showed, you can already apply it to a brand-new scenario on your own. That means it's time to stop reading about agents and start building one.