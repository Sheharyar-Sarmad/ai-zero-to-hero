# Prompt Engineering (For Developers)

You already know how to *connect* to an LLM (see `02_using_LLM.md`). Now let's talk about how to *talk* to it.

Prompt Engineering is not about being polite to a robot. It's about **reducing ambiguity** so the model's output is predictable, parseable, and production-ready. Every technique below is a lever you pull to reduce variance in the output.

We'll use the standard chat format everywhere:

```python
messages = [
    {"role": "system", "content": "..."},
    {"role": "user", "content": "..."},
    {"role": "assistant", "content": "..."}  # optional, used for history or few-shot
]
```

---

## 1. System vs. User Prompts

The **system** prompt is not just "context" — treat it as a **configuration object**. It should define:
- Persona (who is the model?)
- Rules (what it must/must never do)
- Output format (how should it respond?)
- Boundaries (what topics/actions are off-limits?)

The **user** prompt should contain the actual task/query — nothing else. Don't mix configuration into the user turn; it gets lost or ignored on longer inputs.

```python
messages = [
    {
        "role": "system",
        "content": (
            "You are a senior backend engineer reviewing pull requests. "
            "Rules:\n"
            "1. Only comment on bugs, security issues, and performance problems.\n"
            "2. Never comment on code style or naming conventions.\n"
            "3. If the code has no issues, respond with exactly: 'LGTM'.\n"
            "4. Keep every comment under 2 sentences."
        )
    },
    {
        "role": "user",
        "content": "def get_user(id):\n    return db.execute(f\"SELECT * FROM users WHERE id={id}\")"
    }
]
```

**Why it matters:** the system prompt has stronger "weight" in most models and persists across the whole conversation, so it's the right place for anything that shouldn't change turn-to-turn.

---

## 2. Zero-Shot Prompting

Just ask. No examples, no demonstration. Works well for simple, well-known tasks (classification, translation, summarization) where the model already has strong priors.

```python
messages = [
    {"role": "system", "content": "You are a sentiment classifier. Respond with only one word: Positive, Negative, or Neutral."},
    {"role": "user", "content": "The delivery was late but the product quality is amazing."}
]
```

**When it fails:** custom formats, company-specific logic, or niche domains. That's when you move to Few-Shot.

---

## 3. Few-Shot Prompting

Give the model 2-3 `input -> output` examples so it learns the **pattern**, not just the instruction. This is the single most effective way to control output *format* and *style*.

Two ways to implement it:

### Option A: Inline in the user prompt (simplest)

```python
prompt = """Convert the following support tickets into a category label.

Ticket: "My payment failed twice today."
Category: Billing

Ticket: "The app crashes when I upload a photo."
Category: Bug

Ticket: "How do I change my email address?"
Category: Account

Ticket: "I was charged twice for the same order."
Category:"""

messages = [
    {"role": "system", "content": "You are a support ticket classifier."},
    {"role": "user", "content": prompt}
]
```

### Option B: Using actual conversation turns (often more reliable)

```python
messages = [
    {"role": "system", "content": "You are a support ticket classifier. Respond with only the category name."},
    {"role": "user", "content": "My payment failed twice today."},
    {"role": "assistant", "content": "Billing"},
    {"role": "user", "content": "The app crashes when I upload a photo."},
    {"role": "assistant", "content": "Bug"},
    {"role": "user", "content": "I was charged twice for the same order."}
]
```

> Option B tends to generalize better because the model treats it as a real dialogue pattern, not just text to continue.

---

## 4. Chain of Thought (CoT)

For anything involving math, logic, multi-step reasoning, or decision-making — telling the model to "think first, answer after" measurably improves accuracy. You are forcing it to generate intermediate reasoning tokens instead of jumping straight to a (often wrong) final answer.

```python
messages = [
    {
        "role": "system",
        "content": "You are a careful reasoning assistant. Always think step-by-step before giving your final answer. Put your final answer on the last line, prefixed with 'Answer:'."
    },
    {
        "role": "user",
        "content": "A store had 120 apples. It sold 35% on Monday and 20% of the remainder on Tuesday. How many apples are left?"
    }
]
```

**Trick — "Let's think step by step":** even just appending this phrase to the end of a user prompt (with no other instruction) is a well-documented zero-shot CoT trigger.

```python
messages = [
    {"role": "user", "content": "If a train travels 60km in 45 minutes, what is its speed in km/h? Let's think step by step."}
]
```

**Production tip:** If you don't need to *show* the reasoning to the end user, ask the model to think in a hidden block, then extract only the final answer programmatically (see Section 5).

---

## 5. Structured Outputs (JSON)

Never trust an LLM to "just return JSON" without constraints — you WILL get markdown fences, explanations before/after, or trailing commas in production. Combine **prompt-level instructions** with **API-level enforcement**.

### Technique A: Prompt-based enforcement (works with any provider)

Be explicit about the schema, and forbid extra text.

```python
messages = [
    {
        "role": "system",
        "content": (
            "You extract structured data from text. "
            "Respond with ONLY valid JSON. No markdown, no code fences, no explanations. "
            "Use exactly this schema:\n"
            '{"name": string, "email": string, "intent": "purchase" | "support" | "other"}'
        )
    },
    {
        "role": "user",
        "content": "Hi, I'm John Doe (john@example.com), my order never arrived, can you help?"
    }
]
```

Always parse defensively:

```python
import json

def safe_json_parse(raw_text: str):
    # Strip accidental markdown fences some models still add
    cleaned = raw_text.strip().removeprefix("```json").removeprefix("```").removesuffix("```").strip()
    return json.loads(cleaned)
```

### Technique B: API-level enforcement (preferred when available)

Modern APIs let you *guarantee* JSON at the transport level instead of hoping the prompt works.

**OpenAI (JSON mode):**
```python
response = client.chat.completions.create(
    model="gpt-4o",
    response_format={"type": "json_object"},  # forces valid JSON
    messages=messages
)
```

**OpenAI (Structured Outputs w/ strict schema — even stronger):**
```python
response = client.chat.completions.create(
    model="gpt-4o",
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "extract_contact",
            "schema": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "email": {"type": "string"},
                    "intent": {"type": "string", "enum": ["purchase", "support", "other"]}
                },
                "required": ["name", "email", "intent"]
            }
        }
    },
    messages=messages
)
```

**Anthropic / Gemini:** don't have a hard "JSON mode" flag in the same way — rely on Technique A (strong prompt constraints) or use their native **tool-calling / function-calling** feature to force a schema, which is effectively the same trick as OpenAI's structured outputs.

> **Rule of thumb:** if the API offers schema enforcement, use it. Prompt instructions are a *fallback*, not a guarantee.

---

## 6. Common Pitfalls

- **Prompt Injection** — if you insert untrusted user/web content into a prompt, an attacker can write "ignore previous instructions and..." inside that content. Never treat user-supplied text as trustworthy just because it's wrapped in your own prompt template. Isolate untrusted input with delimiters and instruct the model explicitly to treat it as *data, not instructions*.
- **Token Limits** — few-shot examples, chat history, and system prompts all consume the context window. Long few-shot prompts can silently truncate your actual user query if you're not tracking token counts.
- **Ambiguous Instructions** — "make it better" or "summarize this" have no fixed output shape. The model will guess, and guesses are inconsistent across calls. Always specify: length, tone, format, and edge-case behavior.
- **Instruction Conflict** — contradicting yourself between system and user prompt (e.g., system says "always answer in English," user says "responde en español") causes unpredictable behavior. Keep instructions consistent across turns.
- **Overloading a single prompt** — asking for 10 different things in one instruction reduces accuracy on all of them. Split into multiple calls or a single well-structured schema instead.

---

## 7. Best Practices (Golden Rules)

1. **Assign a Role** — "You are a senior X" primes the model into a narrower, more consistent behavior distribution than a generic instruction.
2. **Be Specific, Not Polite** — "Summarize in 3 bullet points, max 15 words each" beats "please summarize this nicely."
3. **Use Delimiters** — wrap untrusted or long input in triple backticks, XML tags, or `---` so the model clearly knows where instructions end and data begins.
```python
   content = f"""Summarize the text between the triple backticks.

   \`\`\`{user_input}\`\`\`
   """
```
4. **Show, Don't Just Tell** — one well-crafted few-shot example is often worth more than three paragraphs of instructions.

---

## 🔥 One Fire Rule

> **If you can't describe the exact shape of the output you want, the model can't produce it reliably either.**

Every technique in this file — roles, few-shot examples, CoT, JSON schemas — exists to answer one question before you hit "send": *what, exactly, should the response look like?* Answer that first. The prompt writes itself after.