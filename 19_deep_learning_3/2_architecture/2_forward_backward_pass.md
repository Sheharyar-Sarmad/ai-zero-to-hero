

# Forward Propagation & Backpropagation Through Time (BPTT) — Explained Simply

## 1. What is the "Forward Pass" in an RNN?

The forward pass is simply: **reading the sequence step by step, left to right, and building up memory as you go.**

At each time step, the RNN does 3 things:
1. Takes the current input (e.g., a word)
2. Combines it with the memory from before (hidden state)
3. Produces a new memory + (optionally) a prediction

Analogy: Reading a storybook page by page.
You read page 1, form an idea. You read page 2, update your idea using page 1's idea + new page. This continues until the last page. That whole reading process = the forward pass.

```
Time step:      t1          t2          t3
Input:          x1          x2          x3
                 │           │           │
                 ▼           ▼           ▼
              ┌─────┐     ┌─────┐     ┌─────┐
   h0 ───────►│ RNN │────►│ RNN │────►│ RNN │────► h3
              └─────┘     └─────┘     └─────┘
                 │           │           │
                 ▼           ▼           ▼
                y1          y2          y3
             (prediction) (prediction) (prediction)
```

This left-to-right flow (input → hidden state → output, moving forward in time) is the **forward pass**.

---

## 2. A Tiny Numeric Example (3 Time Steps)

Let's keep the math super simple. We'll pretend:
- Hidden state and inputs are just single numbers
- The mixing rule is: `h_t = (h_(t-1) + x_t) / 2` (simple average — no scary math)

| Time Step | Input (x_t) | Old Memory (h_(t-1)) | New Memory (h_t) |
|-----------|-------------|------------------------|---------------------|
| t1 | 2 | 0 (start) | (0 + 2) / 2 = **1** |
| t2 | 4 | 1 | (1 + 4) / 2 = **2.5** |
| t3 | 6 | 2.5 | (2.5 + 6) / 2 = **4.25** |

```
h0=0 ──x1=2──► h1=1 ──x2=4──► h2=2.5 ──x3=6──► h3=4.25
```

Notice: each hidden state depends on the one before it. This chain is exactly what "forward pass through time" means.

---

## 3. What Does "Loss" Mean Here?

At each time step, the RNN makes a **prediction** (`y_t`). We compare it to the **actual correct answer** (`y_actual_t`).

The difference between them is called the **loss** (or error).

Analogy: Imagine you're guessing the next number in a pattern, and your teacher tells you the real answer. The gap between your guess and the real answer is your "loss" — how wrong you were.

```
Time step:     t1              t2              t3
Prediction:    y1              y2              y3
Actual:        y1_actual       y2_actual       y3_actual
                │                │                │
                ▼                ▼                ▼
             loss1            loss2            loss3

Total loss = loss1 + loss2 + loss3
```

The RNN calculates a loss at **every time step**, then adds them all up to get the **total loss** for the whole sequence.

---

## 4. What is Backpropagation Through Time (BPTT)?

Once we know the total loss (how wrong the RNN was), we need to teach the RNN to do better. This means adjusting the weights (Wx, Wh, Wy).

To do this, we need to know: **"Which weight caused how much of the error?"**

This process is called **backpropagation**. But because RNNs repeat over time steps, we must send the error **backward through every time step** — from the last step back to the first. This special version is called:

> **Backpropagation Through Time (BPTT)**

Analogy: Unrolling a rolled-up carpet.
Normally the RNN loop looks like one small circle (folded). To do BPTT, we "unroll" that circle into a straight line of repeated steps (like unrolling a carpet). Once unrolled, it looks just like a normal deep neural network — and we do **normal backpropagation** on it, just going from the last step back to the first.

```
FORWARD PASS (left to right):
h0 ──► h1 ──► h2 ──► h3
       │      │      │
       ▼      ▼      ▼
       y1     y2     y3

BACKWARD PASS (right to left) — BPTT:
h0 ◄── h1 ◄── h2 ◄── h3
       ▲      ▲      ▲
       │      │      │
     loss1  loss2  loss3
```

The forward arrows show information moving ahead in time.
The backward arrows show the **error signal (gradient)** moving back in time, step by step, correcting the weights.

---


## Summary (5 lines)

1. The **forward pass** reads inputs step by step, updating memory (hidden state) as it goes.
2. **Loss** measures how wrong each step's prediction was, compared to the real answer.
3. **BPTT** "unrolls" the RNN through time and sends the error backward, step by step, to fix the weights.