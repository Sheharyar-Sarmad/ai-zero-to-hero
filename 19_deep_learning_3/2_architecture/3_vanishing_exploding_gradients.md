

# Vanishing & Exploding Gradients in RNNs

## 1. Quick Recap

BPTT sends the error signal **backward through time** so the RNN can fix its weights. It's like tracing back your steps to find where you went wrong. This matters because RNNs need to learn from *sequences* — and to learn well, the error signal needs to travel back cleanly, all the way to earlier time steps.

But here's the problem: that signal doesn't always survive the trip.

---

## 2. Why Gradients Get Multiplied on the Way Back

### Chain rule, in plain English
When the error travels backward through time, it doesn't just move — it gets **multiplied** at every single step it passes through. Think of it like a relay race where each runner doesn't just pass the baton, they also **scale** it up or down before handing it off.

- If each step shrinks the signal a little → after many steps, it's basically gone.
- If each step grows the signal a little → after many steps, it's massive.

### The math intuition (no heavy math, promise)
- Multiply numbers **less than 1** again and again → the result keeps getting **smaller** → **vanishing**
- Multiply numbers **greater than 1** again and again → the result keeps getting **bigger** → **exploding**

That's really it. The whole problem comes from **repeated multiplication**.

---

## 3. The Vanishing Gradient Problem 🫥

**What it is:** The error signal shrinks and shrinks as it goes back in time, until it's basically zero.

**What it causes:**
- Early time steps get almost **no update** — they stop learning
- The RNN **forgets long-range context**
- It can only really "remember" recent stuff

**Real impact example:**
> "The cat, which already ate, was full."

The RNN needs to connect **"cat"** to **"was"** (cat *was* full, not "ate" was full). But if the gap between them is long, the gradient shrinks so much by the time it reaches "cat" that the connection is never learned properly.

**Analogy — Telephone Game**
You whisper a message down a long line of people. By the time it reaches the last person, it's faint, garbled, or completely lost. Same thing happens to the gradient — it gets fainter with every step back.

**Simple numbers:**
```
0.5 × 0.5 × 0.5 × 0.5 × 0.5 = 0.03125
```
Just 5 steps back, and the signal is already almost nothing. Imagine 50 steps back!

---

## 4. The Exploding Gradient Problem

**What it is:** The error signal grows bigger and bigger as it travels back.

**What it causes:**
- Weight updates become **huge**
- Training becomes **unstable**
- The network's outputs go crazy (sometimes literally `NaN` — "not a number")

**Analogy — Snowball Rolling Downhill**
A small snowball rolls down a snowy hill, picking up more snow every second. It starts small but ends up a massive, unstoppable boulder of snow. That's your gradient after too many multiplications.

**Simple numbers:**
```
2 × 2 × 2 × 2 × 2 = 32

2^20 = 1,048,576  (over 1 million!)
```
That's what happens when your multiplier is just slightly above 1, over many time steps.

---

## 5. Why Longer Sequences Make It Worse

More time steps = more multiplications = more extreme results.

| Sequence Length | Effect (if multiplier = 0.5) | Effect (if multiplier = 2) |
|---|---|---|
| 5 steps | 0.03 | 32 |
| 10 steps | 0.001 | 1,024 |
| 20 steps | 0.000001 | 1,048,576 |

The longer the sentence or sequence, the worse both problems get. This is exactly why plain RNNs struggle with long text.

---

## 6. Quick Fixes 

**Gradient Clipping** (fixes exploding)
Set a maximum size for gradients — like a **speed limit** on a highway. If the gradient tries to go above the limit, you just cap it.

**Truncated BPTT** (helps both)
Instead of backpropagating through *all* time steps, only go back through the **last N steps**. It's like tasting a cake that turned out bad and only checking the ingredients you added recently, not every ingredient since you started cooking three days ago.

**LSTM & GRU** (teaser )
These are special RNN designs built specifically to fight the vanishing gradient problem. They have "gates" that control what information to keep or forget. We'll cover these in the next module!

---

## 7. Visual Aids

**Vanishing Gradient (shrinking backward):**
```
Time:      t5      t4      t3      t2      t1
Gradient:  █████ ► ████  ► ██   ► █     ► ·
           1.0      0.5     0.25    0.06    0.01
                (getting smaller going backward) ◄
```

**Exploding Gradient (growing backward):**
```
Time:      t1      t2      t3      t4      t5
Gradient:  █   ► ██    ► ████  ► ████████ ► ████████████████
           1        2        4        8              16
                (getting bigger going backward) ◄
```

---

## 8. Summary 

1. **Vanishing gradient** = error signal shrinks to nearly zero as it goes back in time, so early steps stop learning.
2. **Exploding gradient** = error signal grows huge as it goes back in time, making training unstable.
3. Both happen because gradients get **multiplied repeatedly** across time steps.
4. Longer sequences make both problems **worse**.
5. Quick fixes: **Gradient Clipping** (caps exploding gradients) and **Truncated BPTT** (limits how far back you propagate). LSTM/GRU fix vanishing gradients properly — coming up next!

---

## Comparison Table

| | **Vanishing Gradient** | **Exploding Gradient** |
|---|---|---|
| **Cause** | Multiplying many numbers **< 1** | Multiplying many numbers **> 1** |
| **Effect** | Gradient shrinks to ~0, early steps stop learning, RNN forgets long-range info | Gradient grows huge, unstable training, crazy/NaN outputs |
| **Analogy** | Telephone game — message fades away | Snowball rolling downhill — grows out of control |
| **Fix** | Truncated BPTT, LSTM/GRU (next module) | Gradient Clipping, Truncated BPTT |