

# 03 — LLM Foundations

## What an LLM actually is
A stateless function. You send text in, you get text out. It doesn't remember anything between calls — you have to send the whole conversation every time.

## Chat models vs completion models
- **Completion models** (old): you send a prompt, get a completion. No structure.
- **Chat models** (modern): you send a list of messages with roles. Model responds as assistant.

All modern models (GPT-4, Claude, Llama) are chat models.

## The three roles
- **system** — sets the model's behavior. "You are a helpful assistant."
- **user** — what the human says.
- **assistant** — what the model said before.

Every API call sends all three, in order.

## Context window
The maximum number of tokens a model can process in one call — includes input + output. GPT-4o has 128K. Claude Sonnet has 200K.

Cost and latency scale with tokens. Bigger context ≠ better — often worse.

## Why stateless matters
The model has no memory. If you want it to "remember" the conversation, **you** send the full history each time. This is why token cost grows as conversations get longer.

## What you actually pay for
- **Input tokens** — usually cheaper
- **Output tokens** — usually 2–4× more expensive

This is why streaming and caching matter so much.

## Key takeaway
An LLM is a function, not a chat partner. You manage state. You manage history. You manage cost.