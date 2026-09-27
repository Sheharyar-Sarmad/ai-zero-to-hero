# Agent Abstractions

By now you understand the pieces that make an agent work: the loop, tools, state, and control. This section explains why frameworks wrap those pieces into a single function like `create_agent`, and why that function is not magic.

## 1. What Is an Abstraction?

An abstraction hides the messy details of how something works so you can use it without thinking about every step.

You drive a car without manually controlling the engine combustion process. You press the pedal, and the car deals with fuel injection, ignition timing, and dozens of moving parts. You don't need to know any of that to drive — but a mechanic still needs to.

Abstractions in software work the same way: they let you use something powerful without operating every part of it by hand.

## 2. Why Frameworks Use Abstractions

Every agent needs roughly the same moving parts: a way to call a model, a way to run tools, a way to track state, and a loop that ties them together. Writing this from scratch every time is repetitive and error-prone.

Frameworks package this repeated logic once, test it, and let developers reuse it. This means:

- Less boilerplate code
- Fewer bugs in the "plumbing"
- Faster time from idea to working agent

The tradeoff is that some of the underlying mechanics become less visible.

## 3. Manual Agent

Here is the conceptual loop you'd write by hand:

```
while not finished:
    ask_model()
    inspect_decision()
    execute_tool()
    add_result_to_state()
```

- **ask_model()** — send the current state (conversation, tools, instructions) to the model and get back a decision.
- **inspect_decision()** — check what the model wants to do: answer directly, or call a tool.
- **execute_tool()** — if a tool call was requested, run it and capture the result.
- **add_result_to_state()** — feed that result back into the conversation so the model sees it on the next turn.

This is the entire agent loop. Everything else is refinement around these four steps.

## 4. Framework Agent

A framework agent takes this same loop and wraps it inside a reusable object or function. Instead of writing the `while` loop yourself, you configure the pieces (model, tools, instructions) and the framework runs the loop internally.

Nothing new is happening conceptually — the same four steps still occur. The framework just owns the wiring.

## 5. create_agent

`create_agent` is a conceptual entry point many frameworks provide. Instead of assembling the loop yourself, you hand the framework the ingredients:

```
Model
+
Tools
+
Instructions
+
Agent loop
+
State
```

`create_agent` connects these ingredients into a working agent object. You call it once during setup, then interact with the resulting agent as a whole.

## 6. What create_agent Does NOT Mean

`create_agent` does not magically create intelligence. It is a convenience function, not a source of capability.

The underlying system still depends entirely on:

- **The model** — its reasoning quality is unchanged by the abstraction.
- **The tools** — the agent can still only do what its tools allow.
- **The prompts/instructions** — vague instructions still produce vague behavior.
- **The state** — the agent still needs accurate history to reason well.
- **The execution logic** — tool calls still have to be run and their results still have to be fed back in.

If any of these pieces is weak or missing, wrapping them in `create_agent` does not fix that.

## 7. Manual vs Abstraction

| | Manual Loop | Framework Abstraction |
|---|---|---|
| Control | More control over every step | Less direct control |
| Code | More code to write and maintain | Less code |
| Speed | Slower to build | Faster development |
| Behavior | You define everything explicitly | More built-in behavior |
| Best for | Learning, debugging, custom needs | Production speed, common patterns |

Neither is "better" in all cases — they serve different goals.

## 8. Why Learn the Manual Version First?

If you learn `create_agent` before understanding the loop underneath it, it's easy to treat it as a black box: something you configure by copying examples without knowing why they work.

Once something breaks — a tool doesn't get called, state gets lost, the agent loops forever — you need to know what's actually happening underneath the abstraction to fix it.

Understanding the manual loop first means you use frameworks deliberately, not by cargo-culting patterns you don't understand.

## 9. Conceptual Architecture

```
create_agent(...)
        ↓
Model + Tools + Instructions
        ↓
Agent Runtime
        ↓
Tool Calls
        ↓
State
        ↓
Final Response
```

The runtime is simply running the same loop you built manually — ask the model, inspect the decision, execute tools, update state, repeat until finished.

## 10. Key Takeaways

- `create_agent` is a packaging of the same loop you already understand — not a new concept.
- Abstractions hide complexity; they do not eliminate it.
- The agent's quality still depends on the model, tools, instructions, and state you provide.
- Learning the manual loop first prevents cargo-culting frameworks you don't understand.
- Keep this mental model: **abstraction = convenience, not magic.**