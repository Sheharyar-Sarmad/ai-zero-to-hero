

# RNN Internal Working — Explained With a Real Example (No Scary Math)

Here I willl explains the RNN's internal working using the simplest theory, and then walks through **one real example step by step**, with visuals, so you can *see* the memory being built.

---

## Part 1: The Simple Theory (Recap)

Think of an RNN as **one tiny brain** that:
1. Reads one piece of input at a time (like one word)
2. Keeps a **notebook** (called hidden state) of what it has understood so far
3. Updates the notebook by mixing:
   - What it just read (new input)
   - What it already knew (old notebook)
4. Uses the **same brain and same rules** at every step (no new brain for new words)

In the simplest form (no scary math, just a mixing rule):

```
new_notebook = mix( old_notebook , new_input )
```

That's really it. Now let's see this happen with real numbers.

---

## Part 2: The Problem We'll Solve

**Task:** Predict the next word in the sentence:

```
"I love ___"
```

We will feed the RNN one word at a time: `"I"` then `"love"`, and watch how its internal notebook builds up, until it can guess the next word.

To keep things simple (no scary math), we will represent:
- Each **word** as one simple number (a code for that word)
- The **notebook (hidden state)** as one simple number (its "understanding so far")
- The **mixing rule** as simple addition and averaging (not full RNN math, just the intuition)

| Word | Simple Code (input number) |
|------|------------------------------|
| "I"     | 1 |
| "love"  | 5 |
| "you"   | 9 |
| "pizza" | 9 (also fits "love") |

---

## Part 3: Step-by-Step Walkthrough (With Visuals)

### Step 0 — Before anything happens

The notebook is empty. We'll say empty = `0`.

```
┌─────────────────────┐
│   NOTEBOOK (h0)      │
│        0             │
│  (empty, nothing     │
│   read yet)          │
└─────────────────────┘
```

---

### Step 1 — Read the word "I"

The RNN reads input `x1 = 1` (the code for "I").

It mixes:
- old notebook (`0`)
- new input (`1`)

```
       OLD NOTEBOOK        NEW INPUT
            0        +        1
             \              /
              \            /
               ▼          ▼
            ┌───────────────┐
            │   RNN CELL     │
            │  (mixing rule) │
            └───────┬────────┘
                    │
                    ▼
            NEW NOTEBOOK (h1) = 1
```

```
┌─────────────────────┐
│   NOTEBOOK (h1)      │
│        1             │
│  "I've seen: I"      │
└─────────────────────┘
```

---

### Step 2 — Read the word "love"

The RNN reads input `x2 = 5` (the code for "love").

It mixes:
- old notebook (`h1 = 1`, remembers "I")
- new input (`5`, the word "love")

```
       OLD NOTEBOOK        NEW INPUT
            1        +        5
             \              /
              \            /
               ▼          ▼
            ┌───────────────┐
            │   RNN CELL     │
            │  (mixing rule) │
            └───────┬────────┘
                    │
                    ▼
            NEW NOTEBOOK (h2) = 3
        (simple average: (1+5)/2 = 3)
```

```
┌─────────────────────┐
│   NOTEBOOK (h2)      │
│        3             │
│ "I've seen: I love"  │
└─────────────────────┘
```

Notice: the notebook `3` is **not** just "love" (5), and **not** just "I" (1) — it's a **blend** of both. This is the key trick: the notebook carries a summary of everything so far, not just the latest word.

---

### Step 3 — Predict the next word (no new input, just use memory)

Now we ask: "What comes next?"

The RNN looks only at its notebook (`h2 = 3`) and tries to guess the closest matching word.

```
┌─────────────────────┐
│   NOTEBOOK (h2)      │
│        3             │
└──────────┬──────────┘
           │
           ▼
   ┌───────────────────┐
   │   OUTPUT LAYER     │
   │ (turns memory into │
   │   a word guess)    │
   └──────────┬──────────┘
              │
              ▼
     Closest match: "you" or "pizza"
     (both coded as 9, closer to
      the sentence pattern than
      random words)
```

**Prediction:** "I love **you**" ✅ (or "pizza" — both make sense!)

---

## Part 4: Putting It All Together (Full Visual Timeline)

```
 INPUT:        "I"          "love"           (predict)
                │              │                  │
                ▼              ▼                  ▼
             ┌─────┐        ┌─────┐            ┌─────┐
   h0=0 ────►│ RNN │──h1=1─►│ RNN │──h2=3─────►│ RNN │
             └─────┘        └─────┘            └─────┘
                │              │                  │
                ▼              ▼                  ▼
             (no output    (no output          OUTPUT:
              needed yet)   needed yet)      "you" / "pizza"
```

Same RNN cell. Same rules. Notebook keeps growing and blending as new words arrive.

---

## Part 5: Why This Matters (Connecting Back to Theory)

| What happened in the example | What it means in RNN theory |
|-------------------------------|-------------------------------|
| Notebook started at `0` | This is `h0`, the initial hidden state |
| Notebook updated using old notebook + new word | This is the formula `h_t = f(Wh·h_(t-1) + Wx·x_t + b)` — just without scary letters |
| Same mixing rule used every time | This is **weight sharing** — same Wx, Wh, Wy at every step |
| Final notebook used to guess the word | This is the **output layer** using Wy to turn memory into a prediction |
| "I" got blended into the notebook | This is the **feedback loop** — old memory keeps influencing the future |

---

## Part 6: Summary

1. The RNN keeps one running **notebook (hidden state)** that blends old memory with new input.
2. At each step, it mixes: `new_notebook = mix(old_notebook, new_input)`.
3. It uses the **same brain and rules** at every single step — nothing changes.
4. By the time it reaches the end of the sentence, the notebook holds a **summary of everything read so far**.
5. To predict the next word, it simply looks at the **final notebook**, not the raw words — that's how it "remembers" context.