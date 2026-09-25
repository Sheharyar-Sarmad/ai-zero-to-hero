# ⚡ LangChain Runnables & LCEL Quick Reference

Runnables provide a standard, unified interface for executing and chaining components using **LangChain Expression Language (LCEL)**. Any component that implements the Runnable interface — prompts, models, parsers, retrievers, custom functions — can be composed with any other using the same small set of operators and methods.

---

## 1. Unified Execution Methods

Every Runnable, regardless of what it wraps, exposes the same sync and async execution primitives. This consistency is the core value of the Runnable interface: once you know how to call one Runnable, you know how to call all of them.

```python
# 1. Single Execution
result = chain.invoke({"input": "hello"})

# 2. Parallel Batch Execution
results = chain.batch([{"input": "hello"}, {"input": "world"}])

# 3. Streaming Execution
for chunk in chain.stream({"input": "hello"}):
    print(chunk)

# 4. Async Alternatives
result = await chain.ainvoke({"input": "hello"})
```

**Learning notes**
- `batch` runs inputs concurrently (not strictly parallel in the CPU sense, but concurrently via threads/async), which is far faster than looping `invoke` calls one at a time.
- `stream` yields partial output as it's generated — essential for chat UIs where you want tokens to appear incrementally rather than waiting for the full response.
- Every sync method has an async twin prefixed with `a`: `ainvoke`, `abatch`, `astream`. Use the async versions inside async web frameworks (FastAPI, etc.) to avoid blocking the event loop.
- There's also `astream_events` / `astream_log`, which expose fine-grained events (start/end of each step in a chain) — useful for debugging or building detailed progress UIs, not just final output streaming.

---

## 2. Structural Composition

### Sequence Pipe (`|`)

Pipes the output of one component directly into the input of the next, forming a `RunnableSequence`.

```python
chain = prompt | model | parser
```

**Learning notes**
- The `|` operator is just syntactic sugar — `prompt | model` is equivalent to `RunnableSequence(first=prompt, last=model)`.
- Output type of each step must match the expected input type of the next. `prompt` outputs a `PromptValue`, `model` accepts that and outputs an `AIMessage`, `parser` accepts that and outputs whatever the parser extracts (string, JSON, etc.).
- Chains are themselves Runnables, so you can pipe a chain into another chain: `chain | another_step`.

### RunnableParallel

Executes multiple steps simultaneously on the *same* input and combines the results into a dictionary.

```python
from langchain_core.runnables import RunnableParallel

parallel = RunnableParallel({
    "summary": summarize_chain,
    "keywords": keywords_chain
})
```

**Learning notes**
- You can write this with a plain dict literal inside a sequence too — LangChain auto-coerces a dict into a `RunnableParallel` when it appears in a pipe: `{"summary": summarize_chain, "keywords": keywords_chain} | combine_step`.
- Great for fan-out patterns: run multiple independent sub-chains (e.g., summarize + extract keywords + classify sentiment) on the same input in one round trip instead of three sequential calls.
- Execution is concurrent, not sequential — total latency is closer to the slowest branch, not the sum of all branches.

### RunnablePassthrough & `.assign()`

Passes input through unchanged, or dynamically attaches new fields to a dictionary flowing through the pipeline.

```python
from langchain_core.runnables import RunnablePassthrough

# Pass raw input alongside retrieved results
inputs = {
    "context": retriever,
    "question": RunnablePassthrough()
}

# Dynamically append new keys to an existing dictionary input
chain = RunnablePassthrough.assign(
    formatted_context=lambda x: "\n".join(x["context"])
)
```

**Learning notes**
- This is the classic pattern behind RAG chains: the user's raw question needs to flow untouched into the final prompt template *while also* being used to query a retriever. `RunnablePassthrough()` solves that — it just returns whatever it's given.
- `.assign()` differs from a plain dict step: it takes the *existing* input dict and **adds keys to it**, preserving what was already there. A bare `RunnableParallel`/dict step replaces the input entirely with a new dict of only the specified keys.
- `RunnablePassthrough.assign(key=lambda x: ...)` is effectively "map + merge" in one step, which keeps chains flatter and more readable than nesting multiple parallel/lambda steps.

---

## 3. Dynamic Execution & Modifiers

### `.bind()`

Binds fixed keyword arguments to a Runnable ahead of time, so every future call automatically includes them.

```python
# Bind stop tokens or tools to an LLM
model_with_tools = model.bind(tools=[weather_tool])
model_with_stop = model.bind(stop=["\nObservation:"])
```

**Learning notes**
- `.bind()` returns a *new* Runnable — it doesn't mutate the original model object, so you can create several specialized variants (`model_with_tools`, `model_with_stop`, etc.) from the same base model.
- Common uses: attaching tool/function definitions for tool-calling models, setting `stop` sequences (critical for ReAct-style agent loops where you must stop generation at "Observation:"), or fixing `temperature`/`max_tokens` for a specific step in a larger chain without touching global model config.

### `.with_fallbacks()`

Defines backup Runnables to try, in order, if the primary one raises an exception.

```python
# Fallback to an alternative model if the primary API fails
robust_model = primary_llm.with_fallbacks([backup_llm])
```

**Learning notes**
- Fallbacks are evaluated in order on the *whole* input — if `primary_llm` throws, `backup_llm` receives the exact same input and is invoked instead.
- Useful for provider outages, rate limits, or as a "cheap model first, expensive model as backup" cost-saving strategy.
- Can be chained across full sequences too, not just single models: `chain.with_fallbacks([alternative_chain])`.

### `.with_retry()`

Automatically retries a Runnable on transient failures (e.g., rate limits, flaky network errors) using exponential backoff.

```python
# Retry up to 3 times on failure
resilient_chain = chain.with_retry(stop_after_attempt=3)
```

**Learning notes**
- Retry and fallback solve different problems: retry assumes the *same* call might succeed if attempted again (good for transient/rate-limit errors); fallback assumes the primary component itself is unreliable and switches to a different one entirely.
- They compose well together: `chain.with_retry(stop_after_attempt=3).with_fallbacks([backup_chain])`.
- Additional tunable parameters exist beyond `stop_after_attempt`, such as wait multipliers and which exception types trigger a retry.

---

## 4. Custom Logic & Configuration

### RunnableLambda

Wraps a plain Python function so it can participate in a chain like any other Runnable.

```python
from langchain_core.runnables import RunnableLambda

uppercase_step = RunnableLambda(lambda text: text.upper())
chain = prompt | model | parser | uppercase_step
```

**Learning notes**
- In practice you rarely need to call `RunnableLambda` explicitly — LCEL auto-wraps a plain function when it appears in a `|` chain, e.g. `chain | (lambda text: text.upper())` works directly.
- Explicit wrapping is still useful when you need to call `.invoke()`/`.batch()` on the function standalone, or want it to show up cleanly in tracing (e.g., LangSmith) with a name.
- Functions used this way should generally be pure/side-effect-light, since they may be invoked concurrently as part of `batch()` or `RunnableParallel`.

### `@chain` Decorator

Turns a multi-step Python function into a single composite Runnable instance.

```python
from langchain_core.runnables import chain

@chain
def custom_workflow(text: str):
    processed = step_one.invoke(text)
    return step_two.invoke(processed)
```

**Learning notes**
- This is the go-to escape hatch when a chain's logic needs real control flow (conditionals, loops, early returns) that's awkward to express purely with `|` and `RunnableParallel`.
- Once decorated, `custom_workflow` behaves like any other Runnable: it supports `.invoke()`, `.batch()`, `.stream()`, and can itself be piped into other chains.
- Compare with `RunnableBranch` (not shown above), which offers a declarative if/else-style routing between sub-chains — prefer `@chain` when the branching logic is genuinely custom Python, and `RunnableBranch` when it's a simple condition-to-chain mapping.

### Configurable Fields (`.configurable_fields()`)

Allows specific attributes (e.g., `temperature`, `model_name`) to be changed dynamically at runtime via the `config` object, instead of being fixed at chain-build time.

```python
from langchain_core.runnables import ConfigurableField

# Define a model with a configurable temperature
configurable_model = model.configurable_fields(
    temperature=ConfigurableField(id="llm_temp")
)

# Pass runtime options using the config dict
result = configurable_model.invoke(
    "Write a poem",
    config={"configurable": {"llm_temp": 0.9}}
)
```

**Learning notes**
- This is what makes a single deployed chain flexible per-request — e.g., a production API can let each caller specify `temperature` or even swap the underlying `model_name` without rebuilding the chain object each time.
- Related sibling method: `.configurable_alternatives()`, which lets you swap out an *entire component* (e.g., choose between `gpt-4o` and `claude` as the model) at runtime, rather than just tweaking a parameter — same `config={"configurable": {...}}` mechanism, but selecting between predefined named alternatives instead of setting a raw value.
- The `id` passed to `ConfigurableField` is the key you must use inside `config["configurable"]` at call time — it's just a label you choose, not tied to the underlying attribute name.

---

## Quick Mental Model

| Concept | Purpose |
|---|---|
| `\|` | Sequential composition (output → input) |
| `RunnableParallel` / dict | Fan-out: same input, multiple independent branches |
| `RunnablePassthrough` | Carry input through untouched |
| `.assign()` | Add computed keys to an existing dict input |
| `.bind()` | Pre-fix static kwargs (tools, stop tokens) |
| `.with_fallbacks()` | Swap to a backup Runnable on failure |
| `.with_retry()` | Re-attempt the same Runnable on transient failure |
| `RunnableLambda` / auto-wrap | Bring plain functions into a chain |
| `@chain` | Wrap custom multi-step Python logic as one Runnable |
| `.configurable_fields()` | Tune parameters at call time via `config` |