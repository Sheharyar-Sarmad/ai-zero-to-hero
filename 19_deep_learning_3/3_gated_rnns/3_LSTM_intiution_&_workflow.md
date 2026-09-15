# LSTM — Intuition & Workflow

So far we know WHY LSTM exists (previous file). Now let's see HOW it actually works, step by step — without touching the scary math yet. That's for the next file. This one is all about intuition.

---

## 1. The Two Memories of LSTM

LSTM doesn't carry just one memory like plain RNN. It carries **two**, side by side.

- **Hidden state (h)** → short-term memory. Changes almost every step. This is what gets used for the output right now.
- **Cell state (C)** → long-term memory. Changes only when the LSTM *decides* to change it. This is the "important stuff" storage.

Both of these travel forward together, one time step to the next.

### Analogy
- h = your **desk** → messy, always changing, whatever you're working on right now sits here.
- C = your **filing cabinet** → locked, organized, only opened when something truly needs to go in or come out.

You don't rewrite your filing cabinet every five minutes. But your desk? That's chaos, updated constantly. LSTM works the same way.

---

## 2. The Big Picture Workflow (One Time Step)

At every single time step, LSTM quietly does 5 things. In plain English:

- **Step 1: Look** — It looks at the new input (current word) and the previous hidden state (what it remembers so far).
- **Step 2: Decide what to forget** — It checks the cell state and decides what old info is no longer useful.
- **Step 3: Decide what to add** — It decides what new info from this step is worth storing.
- **Step 4: Update the cell state** — Old useless info gets dropped, new useful info gets added in.
- **Step 5: Decide what to show** — It picks what part of the updated cell state should become the new hidden state (the output for this step).

Then this exact process repeats — for every single word in the sequence, one at a time.

---

## 3. The Full Timeline (Visual)

Here's what it looks like when you zoom out and watch it happen across time:

```
Cell State:   C0 ──►── C1 ──►── C2 ──►── C3 ──►── ...
              (mostly carries forward, small edits at each step)

                │        │        │        │
                ▼        ▼        ▼        ▼
Hidden State: h0 ──►── h1 ──►── h2 ──►── h3 ──►── ...

Input:          x1       x2       x3       x4
                (word1)  (word2)  (word3)  (word4)
```

Notice:
- The **top line (C)** runs almost straight across — it's the conveyor belt.
- The **bottom line (h)** also flows forward, but it's more "reactive" — updated fresh at each step.
- At every time step, a little bit of new info hops onto the belt, and a little bit of old info might get dropped off.

---

## 4. The Conveyor Belt Intuition (Expanded)

Think of the cell state as a literal **conveyor belt** running through a factory, from the start of the sequence to the end.

- Information can hop onto the belt at time step 1 and ride all the way to time step 100 — mostly untouched.
- Nothing on the belt changes unless the LSTM specifically decides to add something or remove something.
- It's not being erased and rewritten constantly. It's just... rolling forward.

### Compare this to plain RNN

Plain RNN doesn't have a belt. It has one notebook (hidden state), and at every step, it **erases the whole page and rewrites it**. So anything written on page 1 is basically gone by page 10.

LSTM instead says: "Let's keep the important notes on a separate conveyor belt that nobody erases unless we choose to."

### Analogy Recap
- Plain RNN = rewriting your one notebook every single minute, old notes get lost.
- LSTM = a factory conveyor belt, items ride along calmly, only touched when a worker decides to add or remove something.

---

## 5. Why This Workflow Fixes Vanishing Gradients

Remember the vanishing gradient problem from file 1? Here's why LSTM solves it.

- Since the cell state only changes through small, *controlled* updates (not a full rewrite), gradients can flow backward through time without shrinking to almost nothing.
- The LSTM can literally **choose** to leave a memory untouched for many steps. If nothing touches it, the gradient for that memory doesn't shrink either.
- This is exactly why LSTM can handle sequences of 50–100 steps, while a plain RNN usually struggles after just 10.

Basically: fewer forced rewrites = gradients survive the journey backward = better learning over long sequences.

---

## 6. What "Workflow" Means in Practice

- At every time step, LSTM makes 4 small decisions: forget, add, update, output.
- These decisions are made using the **same learned rules** at every time step — this is the same weight sharing idea from RNNs, it doesn't disappear.
- The LSTM isn't told what to remember or forget by a human. It **learns** this during training, by adjusting its internal rules to reduce error.

So "workflow" just means: the same 4-step decision process runs on repeat, once per word, for the entire sequence.

---

## 6.5 A Peek at the Math (High Level Only)

You don't need the full gate equations yet (that's file 4), but here's the skeleton so the workflow above connects to real formulas later.

At every time step t, the LSTM works with these pieces:

- x_t → input at this step
- h_(t-1) → previous hidden state
- C_(t-1) → previous cell state

The 4 decisions from Section 2 each produce a number between 0 and 1 (like a percentage), using this general shape:

```
decision = sigmoid( W · [h_(t-1), x_t] + b )
```

Where:
- W = learned weights (the model tunes these during training)
- b = learned bias
- sigmoid = squashes the result into a range of 0 to 1 (0 = "forget completely", 1 = "keep completely")

Then the cell state update at a high level looks like this:

```
C_t = (forget_amount × C_(t-1)) + (add_amount × new_candidate_info)
```

In plain English:
- Multiply the old cell state by a number close to 0 or 1 → this is the "forgetting."
- Add in some new scaled information → this is the "storing."
- The result is the updated cell state, C_t.

And the hidden state is just a filtered, squashed view of that updated cell state:

```
h_t = output_amount × tanh(C_t)
```

Where tanh squashes values between -1 and 1, and output_amount decides how much of the cell state to actually reveal as the hidden state.

That's it — no need to memorize this yet. Just notice the pattern: everything is a small, learned percentage (0 to 1) controlling how much old info stays and how much new info gets in. The exact formulas for forget_amount, add_amount, new_candidate_info, and output_amount are what file 4 (4_lstm_gates.md) breaks down one gate at a time.

---

## 7. Summary

- LSTM has two memories: hidden state (short-term) and cell state (long-term).
- At each step, it does 4 things: forget → add → update → output.
- The cell state acts like a conveyor belt — it carries information forward unless the LSTM decides to change it.
- Because changes are small and controlled, gradients can flow much farther back — this solves the vanishing gradient problem.
- Every decision is just a learned number between 0 and 1, controlling how much old info stays and how much new info gets added.
- The actual gates that control forget/add/output are explained in detail in the next file: 4_lstm_gates.md.