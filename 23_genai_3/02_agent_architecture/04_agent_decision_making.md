# Agent Decision Making

## 1. What Does "Decision" Mean?

An agent doesn't just respond to text — it receives a **goal** (the user's request) and has to figure out the **next useful action** to move toward completing that goal.

For a simple question, the "next useful action" might just be answering directly. For a more complex request, it might be calling a tool, looking at the result, and then deciding what to do next.

At its core, "decision making" for an LLM agent means: given the request, the conversation so far, and the tools available, what should happen next?

- Answer directly, using what the model already knows
- Call a tool to get information or perform an action
- Call another tool after seeing a previous result
- Ask the user for clarification

This decision is made fresh at each step. The model isn't following a fixed script — it's evaluating the situation each time and picking the most useful next move.

## 2. Simple Examples

**"What is Python?"**
→ Answer directly

This is general knowledge. No external data is needed, and nothing changes over time in a way that matters here. The model can answer from what it already knows.

**"What is the weather?"**
→ Weather tool

Weather is live, changing data. The model has no way of knowing the current weather anywhere — it wasn't trained on real-time conditions. It must call a tool built for this.

**"What is 25 × 50?"**
→ Calculator

This is something the model *could* attempt to answer from its own reasoning, but math is a place where LLMs are prone to small errors, especially with larger numbers. A calculator tool guarantees a correct result, so a well-built agent prefers it for precision.

**"What happened in today's news?"**
→ Search/news tool

News is time-sensitive and happens after the model's training cutoff. There's no way the model could know about events from earlier today — it needs a tool that can fetch current information.

**Why the decisions differ:**
The common thread is that the model asks itself, "Do I already reliably know this, or do I need outside help?" Static knowledge → answer directly. Live, precise, or unknown information → use a tool.

## 3. Tool Descriptions

The model doesn't inspect a tool's internal code. All it has to go on is the tool's **name** and **description**. This description is effectively the model's only window into what a tool does and when to use it.

Example:

```
weather:
"Get the current weather for a city."

calculator:
"Perform mathematical calculations."

search:
"Search the internet for current information."
```

These descriptions matter enormously because:

- They tell the model **when** a tool is relevant (e.g., "current weather" signals this tool applies to live weather questions, not historical climate questions).
- They tell the model **what kind of input** the tool expects (a city, a math expression, a query).
- A vague or misleading description leads to the model picking the wrong tool, or missing a tool it should have used.

A good rule of thumb: if a human reading only the tool's name and description couldn't tell exactly when to use it, the model probably can't either.

## 4. Tool Arguments

Once a tool is chosen, the model has to figure out **what to pass into it**. This means translating natural language into structured input.

Example:

```
User: "What's the weather like in Lahore right now?"
Model calls: weather(city="Lahore")
```

The model has to:

1. Recognize which part of the user's message maps to which argument (`"Lahore"` → `city`).
2. Match the tool's expected format (a string, a number, a specific structure).
3. Fill in only what's needed — no extra guessing beyond what's required.

This mapping step is just as important as picking the right tool. A model can choose the correct tool but still fail if it extracts the wrong argument, leaves one out, or invents a value the user never mentioned.

## 5. Single Tool vs Multiple Tools

Some requests need just one tool call. Others require several steps, where each tool's result feeds into the next decision.

**Single-step:**

```
User → LLM → Tool → Answer
```

Example: "What's the weather in Lahore?" — one tool call, then the model summarizes the result into an answer.

**Multi-step:**

```
User
→ LLM
→ Tool 1
→ Result
→ LLM
→ Tool 2
→ Result
→ LLM
→ Answer
```

Example: "Search for today's weather forecast for Lahore and tell me if I should carry an umbrella, and also convert the temperature to Fahrenheit." This might involve a search tool, then a calculator tool for the conversion, before the model can give a final answer.

The key idea: after *every* tool result, the model re-evaluates. It's not "call all tools upfront" — it's "call one tool, look at what came back, then decide again."

## 6. Decision Process

At a high level, this is the loop the model works through at each step:

```
Understand request
        ↓
Determine required information
        ↓
Check available tools
        ↓
Choose action
        ↓
Generate arguments
        ↓
Execute
        ↓
Observe result
        ↓
Decide again
```

This loop repeats until the model has everything it needs to give a final answer. Each pass through the loop is a fresh decision — the model isn't locked into a plan made at the start; it reassesses based on what it has learned so far.

## 7. What Can Go Wrong?

Agent decision making isn't perfect. Common failure modes include:

- **Wrong tool** — calling a search tool when a calculator was needed, or vice versa.
- **Wrong arguments** — passing an incorrect city name, malformed input, or misreading what the user asked for.
- **Unnecessary tool call** — using a tool for something the model already knows, wasting time and resources.
- **Missing tool** — failing to call a tool when one was actually needed, and guessing or hallucinating instead.
- **Repeated calls** — calling the same tool over and over without making progress, sometimes due to misreading results.
- **Hallucinated information** — inventing an answer instead of admitting it doesn't have the data, or fabricating a plausible-looking tool result.

Understanding these failure modes is important because it shapes how tools and prompts should be designed — clear descriptions, tight argument schemas, and sensible constraints all reduce these errors.

## 8. Deterministic vs Dynamic Workflows

**Deterministic workflows** follow a fixed, predefined sequence of steps every time, regardless of what happens along the way. For example, "always call the weather tool, then always format the result the same way." There's no real decision-making — the path is set in advance by the developer.

**Dynamic workflows** let the model decide the sequence of actions based on the specific request and the results it observes. The number of steps, which tools get used, and in what order, can all change from one request to the next.

Agents are interesting precisely because they use dynamic workflows — the model is doing real-time reasoning about what to do next, rather than following a script. This flexibility is powerful, but it's also why agents can behave unpredictably compared to a fixed pipeline.

## 9. Important Engineering Principle

> **The model makes the decision, but the application controls what the model is allowed to do.**

The LLM decides *which* tool to call and *what* arguments to use, but the surrounding application defines the boundaries:

- Which tools even exist and are exposed to the model
- What permissions those tools have (e.g., read-only vs. read/write)
- Limits on how many tool calls can happen, or what data can be accessed
- Validation and safety checks before a tool actually executes

In other words, the model's "freedom" to decide only exists within the sandbox the application builds around it. Good agent design isn't about trusting the model completely — it's about giving it a well-defined, safe set of options and letting it choose wisely among them.

## 10. Key Takeaways

- Never claim that an LLM has perfect reasoning — it can pick the wrong tool, misread arguments, or hallucinate. Decision making is a best effort, not a guarantee.
- Explain decision-making practically: it's a repeated loop of understanding the request, checking what's needed, and picking the next useful action.
- Keep examples simple: a weather question, a math question, a news question — these are enough to illustrate how and why decisions differ.
- Avoid advanced agent frameworks at this stage. The goal here is to understand the core decision loop, not orchestration systems, planning algorithms, or multi-agent coordination.