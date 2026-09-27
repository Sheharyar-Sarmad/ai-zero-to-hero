# State and Memory

## 1. Why Does an Agent Need State?

Imagine an agent helping you book a flight. In step 1, you tell it your departure city. In step 2, you tell it your travel dates. In step 3, the agent needs to actually search for flights — and to do that, it needs to remember *both* the city and the dates from earlier steps.

If the agent forgot everything after each step, it couldn't combine information gathered over time. It would ask you the same questions over and over, or fail to complete tasks that require more than one step.

This is why an agent needs **state**: a way of holding on to information as it works, so earlier steps can inform later ones.

## 2. Context

**Context** is the information available to the model at the moment it generates a response. It's everything the model can "see" when deciding what to say or do next.

Example:

```
User: "My name is Ali."
...
User: "What is my name?"
```

For the model to correctly answer "Ali," the earlier message ("My name is Ali") must still be included in what's sent to the model on the second turn. Language models don't inherently remember anything between calls — each request is independent. So the application layer takes the earlier conversation and includes it in the prompt sent for the next request.

That's context: previous information made available again, so the model can use it.

## 3. State

**State** is the information an agent is currently maintaining while it works — a snapshot of "everything relevant right now."

Conceptually, you can think of it as a simple object:

```
state = {
    messages,
    current_task,
    tool_results,
    intermediate_data
}
```

- `messages`: the conversation so far
- `current_task`: what the agent is currently trying to do
- `tool_results`: outputs from any tools the agent has called
- `intermediate_data`: anything else the agent computed or gathered along the way

State isn't a specific technology — it's a concept. Different frameworks store it differently (a dictionary, a class, a database row), but the idea is the same: state is the working memory of the agent *during* a task.

## 4. Conversation History

Conversation history is one of the most important parts of state. It's the ordered record of everything that happened in a conversation:

```
User message
Assistant message
Tool call
Tool result
Assistant response
```

Each entry gets added to the history as it happens. When the model is asked to respond again, this history (or a relevant portion of it) is included in the context, which is how the model "remembers" what happened earlier in the same conversation.

## 5. Short-Term Memory

Short-term memory is the agent's ability to remember things *within the current conversation or task*.

Example:

```
User: "I'm planning a trip to Tokyo."
Assistant: "Great! When are you planning to go?"
User: "Next March."
Assistant: "Got it — a trip to Tokyo next March. Would you like hotel suggestions too?"
```

Notice the assistant combines "Tokyo" (mentioned two turns ago) with "next March" (mentioned just now). This works because the conversation history is being carried forward as context — that's short-term memory in action.

Short-term memory usually disappears once the conversation ends or the session resets.

## 6. Long-Term Memory

Long-term memory is information that persists *across* conversations — it survives even after a session ends.

Examples:
- **User preferences** — "I prefer window seats," remembered weeks later
- **Previous interactions** — "Last time we spoke, you were debugging a login issue"
- **Saved information** — facts, notes, or decisions explicitly stored for future use

Unlike short-term memory (which lives in the current conversation's context), long-term memory has to be deliberately saved somewhere and then retrieved later and reintroduced into context when relevant.

We won't go into *how* long-term memory is stored or searched (that's a deeper topic on its own) — the important idea here is simply: **short-term memory lives in the current conversation; long-term memory survives beyond it.**

## 7. State vs Memory

| | State | Memory |
|---|---|---|
| **Lifespan** | Exists during a single task or session | Can persist across sessions (long-term) or within one (short-term) |
| **Purpose** | Tracks what's happening *right now* | Tracks what's worth *remembering later* |
| **Contains** | Messages, current task, tool results, intermediate data | Preferences, past interactions, saved facts |
| **Disappears when** | Task/session ends | Short-term: ends with session. Long-term: persists intentionally |
| **Analogy** | A notepad you use while working on a task | A journal you keep and re-read later |

## 8. Agent State During a Tool Call

Here's how state flows through a single tool-using step:

```
User request
     ↓
State
     ↓
LLM decision
     ↓
Tool call
     ↓
Tool result
     ↓
Updated state
     ↓
LLM
     ↓
Final answer
```

At each stage, the state grows: the tool result gets added to it, and the LLM's next decision is made using this updated state — not just the original request.

## 9. Why State Matters

State isn't just bookkeeping — it's what makes several important agent capabilities possible:

- **Multi-step tasks** — combining information gathered across several steps
- **Tool results** — using the output of one tool call as input to a later decision
- **Conversations** — maintaining coherent, context-aware dialogue
- **Human approval** — pausing mid-task, waiting for a person to confirm something, then resuming with everything still intact
- **Recovery/debugging** — inspecting what the agent knew at each point, to understand why it made a certain decision or to resume after a failure

Without state, an agent would be stuck reacting to only the very last message, with no way to build on anything.

## 10. Common Beginner Confusion

These four terms are related, but not the same thing — and it's easy to mix them up:

- **Chat history** is the raw record of messages exchanged.
- **Context** is whatever is actually sent to the model right now — often built *from* the chat history, but not always all of it.
- **State** is the broader working data of the agent — it includes conversation history, but also task info, tool results, and other intermediate data that may never be shown to the user.
- **Memory** is about *persistence* — short-term memory is state that lasts for the session; long-term memory is information deliberately saved to survive beyond it.

A simple way to keep them straight: chat history is *data*, context is *what the model sees*, state is *everything the agent is tracking*, and memory is *what persists, and for how long*.

## 11. Key Takeaways

- Agents need state to carry information from one step to the next.
- Context is what's actually given to the model at generation time — usually built from history and state.
- State is the agent's full working picture: messages, current task, tool results, and intermediate data.
- Conversation history is the ordered log of messages and tool interactions.
- Short-term memory lasts for the current session; long-term memory persists across sessions.
- State and memory are related but distinct: state is "what's happening now," memory is "what's worth keeping."
- State enables multi-step tasks, tool use, human approval steps, and debugging.