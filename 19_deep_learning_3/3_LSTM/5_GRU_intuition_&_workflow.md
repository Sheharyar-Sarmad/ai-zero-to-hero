# GRU — Intuition & Workflow

## 1. Quick Recap — What LSTM Did

LSTM fixed the vanishing gradient problem by adding a cell state (long-term memory) plus 3 gates to control it. It worked really well... but it's a lot of machinery — 4 gates and 2 memories to update at every single step. That's a lot of managers running one small office.

## 2. What GRU Is

GRU = Gated Recurrent Unit.

One-line definition: GRU is a simpler version of LSTM. It uses 2 gates instead of 3, and 1 memory instead of 2.

It was introduced by Cho et al. in 2014, as a faster, lighter alternative to LSTM. Same mission though — solve vanishing gradients and control what the network remembers.

## 3. The Big Idea — Simplification

LSTM has:
- Hidden state (h)
- Cell state (C)
- 3 gates: forget, input, output

GRU has:
- Only hidden state (h)
- 2 gates: update, reset

No separate cell state. GRU merges the two memories into one stream.

Analogy: LSTM is like a company with two filing cabinets and three managers, each responsible for a different part of the filing process. GRU is the same company, but downsized — one filing cabinet, two managers. Same job gets done, just fewer moving parts to maintain.

## 4. The Two GRU Gates (High Level Only)

Update gate → Decides how much of the OLD memory to keep versus how much NEW info to add. It basically does the job of LSTM's forget gate and input gate combined.

Reset gate → Decides how much of the OLD memory to ignore when figuring out the new candidate memory. It helps the network "forget temporarily" so it can focus on what's relevant right now.

## 5. The GRU Per-Word Workflow (4 Steps)

Step 1: Look at the new input word and the previous hidden state.

Step 2: Compute the update gate — this decides how much old memory to keep versus replace.

Step 3: Compute the reset gate and use it to build a candidate memory — this is the "new info worth considering."

Step 4: Blend the old memory with the candidate memory, using the update gate as the mixing ratio, to get the new hidden state.

Repeat this for every word in the sequence, one step at a time.

## 6. Visual Timeline

    Input:      x1        x2        x3
                 │         │         │
                 ▼         ▼         ▼
              ┌─────┐   ┌─────┐   ┌─────┐
    h0 ──────►│ GRU │──►│ GRU │──►│ GRU │──────► ...
              └─────┘   └─────┘   └─────┘
                 │         │         │
                 ▼         ▼         ▼
                h1        h2        h3

Only ONE memory stream (h) flows through the whole sequence.

Compare that to LSTM, which had two streams running side by side — h (short-term) and C (long-term). GRU squashes both into just h. Simpler pipe, same water flowing through it.

## 7. GRU vs LSTM — Quick Intuition

- GRU: fewer parameters, faster to train, similar accuracy on many tasks
- LSTM: more expressive, sometimes better on very long or complex sequences
- Rule of thumb: try GRU first. If it underperforms on your task, switch to LSTM.

(Full detailed comparison is coming in the next file.)

## 8. Why GRU Matters

- Faster to train and faster at inference — fewer gates to compute
- Uses less memory — only one state to track instead of two
- Performs just as well as LSTM on many real-world tasks
- Great choice for embedded devices or edge hardware where compute is limited

## 9. Summary

- GRU is a simpler LSTM — 2 gates instead of 3, 1 memory instead of 2
- Update gate = keep old vs bring in new; reset gate = what old info to ignore
- 4-step workflow per word: look → update gate → reset gate + candidate → blend into new hidden state
- Faster and lighter than LSTM, with similar accuracy on many tasks
- Try GRU first, upgrade to LSTM only if you actually need the extra power