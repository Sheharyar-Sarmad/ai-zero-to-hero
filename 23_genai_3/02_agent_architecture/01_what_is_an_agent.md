# What Is an AI Agent?

## 1. The Simple Definition

Imagine you hire a personal assistant. You don't tell them every single step to do. You just give them a goal:

> "Book me a flight to Lahore next Friday."

Your assistant then:
- thinks about what needs to happen,
- checks flight websites,
- compares prices,
- maybe messages you if something is unclear,
- and finally books the flight.

You didn't write a step-by-step script for them. You gave a **goal**, and they figured out the **steps** themselves, using their own judgment and the tools available to them (phone, browser, payment card).

That is exactly what an **AI agent** is.

**Simple definition:**
An AI agent is a system built around a large language model (LLM) that can look at a goal, decide what to do next, use tools to take action, observe the result, and keep deciding-acting-observing until the goal is done.

**Technical definition:**
An AI agent is a system in which an LLM is placed inside a loop, where the model repeatedly decides — based on the current state and the goal — whether to call a tool, take an action, or produce a final answer, and this continues until a stopping condition is met.

The key difference from a normal script: **the agent decides the path itself.** You don't hardcode "do step 1, then step 2, then step 3." You hardcode the *goal* and the *tools available*, and the model figures out the order.

---

## 2. LLM vs Chain vs Workflow vs Agent

Before understanding agents deeply, you need to clearly separate five related but different ideas: **LLM**, **Chain**, **Workflow**, **Tool**, and **Agent**.

### LLM (Large Language Model)

An LLM is just the "brain" — a model that takes text in and produces text out. On its own, it has no memory of tools, no ability to act in the world, and no loop. It just answers.

```
User → LLM → Answer
```

Example: You ask "What is the capital of France?" and the LLM replies "Paris." That's it. One input, one output.

### Chain

A chain is a **fixed sequence of steps**, where the output of one step becomes the input of the next. The order of steps is decided by *you*, the developer, in advance. The LLM might be used in one or more of those steps, but it never decides "should I skip step 2?" — the path is fixed.

```
Input → Step 1 → Step 2 → Step 3 → Output
```

Example: A chain that (1) takes a raw customer email, (2) summarizes it with an LLM, (3) translates the summary, (4) sends it to Slack. Every run goes through all four steps in that exact order, no matter what.

### Workflow

A workflow is a broader term than "chain." It usually means a sequence of steps that may include branching (if/else logic) or parallel steps, but the branches themselves are still **predefined by the developer**. The LLM might help decide *which* predefined branch to take, but it can't invent a brand-new branch that you didn't design.

Think of a workflow as a flowchart with decision diamonds — but you drew the flowchart in advance.

### Tool

A tool is simply a function the LLM is allowed to call to interact with the outside world — a weather API, a calculator, a database query, a web search. A tool by itself does nothing until something (a chain, a workflow, or an agent) decides to call it.

### Agent

An agent also uses steps, tools, and decisions — but unlike a chain or workflow, **the sequence of steps is not fixed in advance.** The LLM itself decides, at each point, what the next action should be, based on what it has seen so far.

```
User → Agent → Decide → Action → Observe → Decide → Answer
```

Example: You ask an agent "What's the weather in Lahore, and should I carry an umbrella?" The agent decides on its own that it needs to call a weather tool first, looks at the result, and *then* decides it has enough information to answer. Next time, if you ask a question that doesn't need weather data, it might skip the tool call entirely — because it decided to, not because you told it to.

**The core distinction in one line:**
A chain/workflow follows a path you designed. An agent designs its own path, one step at a time, using the tools you gave it.

---

## 3. What Makes Something an Agent?

Not every LLM-based program is an agent. For something to count as an agent, it generally needs all of the following pieces working together:

- **Goal** — a task or outcome the agent is trying to achieve (e.g., "answer the user's weather question").
- **Reasoning / Decision** — the ability to look at the current situation and decide what to do next, rather than following a fixed script.
- **Tools** — functions the agent can call to affect or query the outside world (search the web, run code, query a database).
- **Environment** — the world the agent operates in and gets information from (an API, a filesystem, a website, a chat with a user).
- **Actions** — the actual steps the agent takes (calling a tool, sending a message, writing a file).
- **Observations** — the results the agent receives back after taking an action (a tool's output, an error message, new data).
- **Feedback** — using those observations to update its understanding before deciding the next action.
- **Stopping condition** — a way of knowing when the goal is achieved and it's time to stop and give a final answer.

If a system is missing the "decision" piece — if it always does the same steps in the same order regardless of what happens — it's a chain or workflow, not an agent.

---

## 4. Agent Components

Here is what an agent is built from, at a structural level:

```
Agent
├── Model            → the LLM that does the "thinking"
├── Instructions      → the system prompt / rules that shape its behavior
├── Tools             → functions it is allowed to call
├── State             → memory of what has happened so far in this run
├── Decision logic     → the loop that lets it choose the next step
└── Output            → the final answer or result
```

Let's break each one down simply:

- **Model** — This is the LLM (e.g., a Claude or GPT model). It's the part that actually reads the situation and generates the next decision in natural language or structured form.

- **Instructions** — This is the system prompt: rules like "You are a helpful travel assistant. Always confirm prices before booking. Never share personal data." It shapes *how* the agent behaves, not just what it knows.

- **Tools** — The functions available to the agent: `get_weather()`, `search_web()`, `send_email()`. Each tool usually has a name, a description (so the model knows when to use it), and expected inputs/outputs.

- **State** — A running memory of everything that has happened in the current task: the original question, which tools were called, what they returned, and any intermediate reasoning. Without state, the agent would "forget" what it just did.

- **Decision logic** — The loop itself: the mechanism that keeps asking the model "given everything so far, what's your next move?" and routes the model's choice to the right place (call a tool, or give a final answer).

- **Output** — The final result returned to the user once the agent decides the goal has been met.

---

## 5. Real-World Example

Let's trace through a concrete example: a **weather assistant agent**.

**User asks:**
> "What is the weather in Lahore?"

Here is exactly what happens, step by step:

1. **Perceive** — The agent receives the user's message: "What is the weather in Lahore?"
2. **Decide** — The model reasons: "I don't know today's weather from memory — this needs live data. I have a `get_weather` tool. I should use it."
3. **Act** — The agent calls the tool: `get_weather(city="Lahore")`.
4. **Observe** — The tool returns a result, e.g., `{"temp": 34, "condition": "sunny"}`.
5. **Decide again** — The model looks at this observation and reasons: "I now have enough information to answer the user. No more tools are needed."
6. **Answer** — The agent replies: "It's currently 34°C and sunny in Lahore."

Notice what did *not* happen: nobody hardcoded "always call `get_weather` first." The model decided, based on the question, that it needed the tool. If the user had instead asked "What is 12 times 8?", the same agent would have decided *not* to call the weather tool at all, and might use a calculator tool instead — or just answer directly.

That flexibility — deciding *which* action fits *this* specific input — is the heart of what makes it an agent rather than a fixed chain.

---

## 6. Agent vs Normal Chatbot

| Aspect | Normal Chatbot | AI Agent |
|---|---|---|
| Can use tools | Usually no (just replies with text) | Yes, calls tools when needed |
| Access to live/external data | No — limited to training knowledge | Yes — via tools (APIs, search, databases) |
| Decision-making | Single response, no internal loop | Multi-step loop: decide → act → observe → decide |
| Can take real actions | No (can't send emails, book things, etc.) | Yes, if given the right tools |
| Adapts path per request | No, always "read input → generate output" | Yes, chooses different paths for different inputs |
| Example | Answering "What is Python?" from memory | Checking a live weather API before answering |

---

## 7. Agent vs Chain

A **chain** is like a recipe: step 1, then step 2, then step 3, always in that order, no matter what ingredients you started with. You, the developer, decided the recipe in advance.

An **agent** is like a chef: given a goal ("make dinner for 4 people") and access to a kitchen (tools), the chef decides *in the moment* what to cook, in what order, and whether to improvise if something is missing.

Concretely:
- A **chain** always executes the same fixed sequence of steps for every input. Even if step 2 turns out to be unnecessary for a particular input, the chain will still run it, because the developer wired it that way.
- An **agent** looks at each situation individually and dynamically chooses which steps (tool calls) are actually needed. It might use zero tools for a simple question, or five tools in a loop for a complex one.

This dynamic decision-making is powerful, but it also means agents are less predictable than chains — which is an important engineering trade-off to keep in mind as you build with them.

---

## 8. The Agent Mental Model

The simplest way to hold "agent" in your head is this loop:

```
Perceive → Decide → Act → Observe → Repeat
```

- **Perceive** — The agent takes in the current input: the user's message, or the result of a previous action. This is "what do I know right now?"
- **Decide** — Using the model's reasoning, the agent decides what should happen next: call a tool, ask a clarifying question, or give a final answer.
- **Act** — The agent carries out that decision — usually by calling a tool (a function, an API, a search).
- **Observe** — The agent looks at what came back from that action — the tool's output, any errors, new information.
- **Repeat** — The agent goes back to "Decide" with this new information added to its state, and the cycle continues until it decides the goal has been reached — at which point it stops and produces the final output.

This loop is the engine inside almost every agent framework you will encounter, no matter how it's implemented under the hood.

---

## 9. Important Terminology

- **Agent** — A system where an LLM repeatedly decides its own next action (using tools) in order to reach a goal, rather than following a fixed sequence of steps.
- **Tool** — A function the agent is allowed to call to interact with something outside the model itself (an API, a calculator, a file system, a search engine).
- **Action** — A single step the agent takes, usually a tool call, based on its current decision.
- **Observation** — The result or feedback the agent receives after taking an action (e.g., a tool's return value).
- **State** — The accumulated memory of everything that has happened so far in the current run: inputs, decisions, actions, and observations.
- **Environment** — The outside world the agent operates in and gathers information from — this could be a live API, a codebase, a website, or a conversation with a user.
- **Goal** — The outcome the agent is trying to achieve, usually derived from the user's request.
- **Decision** — The model's judgment, at any given point, about what should happen next.
- **Agent loop** — The repeating cycle of perceive → decide → act → observe that continues until a stopping condition is met.

---

## 10. Beginner Summary

- An AI agent is an LLM placed inside a loop that can decide, act, observe, and repeat until a goal is reached.
- An LLM alone just answers a single prompt — it has no loop and no tools.
- A chain runs a fixed sequence of steps in an order the developer decided in advance.
- A workflow adds branching, but the branches are still predefined by the developer.
- An agent is different because *it* decides which steps to take, not the developer.
- The core building blocks of an agent are: a model, instructions, tools, state, decision logic, and output.
- The mental model to remember is: **Perceive → Decide → Act → Observe → Repeat.**
- Compared to a normal chatbot, an agent can use live tools, take real actions, and adapt its path per request.
- Agents are more flexible than chains, but also less predictable — this trade-off matters a lot in real engineering.
- Before writing any agent code, always be clear on the goal, the available tools, and the stopping condition — these three define how the agent will behave.