# GRU — Intuition, Gates & Workflow

## 1. Quick Recap — What LSTM Did

LSTM fixed the vanishing gradient problem by adding a cell state (long-term memory) plus 3 gates to control it. It worked great... but it's heavy — 3 gates and 2 memories to manage at every single step.

## 2. What GRU Is

GRU = Gated Recurrent Unit.

One-line definition: GRU is a simplified LSTM. It uses 2 gates instead of 3, and 1 memory instead of 2.

Introduced by Cho et al. in 2014, as a faster alternative to LSTM. Same goal though — solve vanishing gradients and control the flow of memory.

## 3. The Big Idea — Simplification

LSTM has:
- Hidden state (h)
- Cell state (C)
- 3 gates: forget, input, output

GRU has:
- Only hidden state (h)
- 2 gates: update, reset

No separate cell state. GRU merges both memories into one stream.

Analogy: LSTM is a company with two filing cabinets and three managers. GRU is the same company downsized — one cabinet, two managers. Same job, fewer moving parts.

## 4. The Two GRU Gates (Deep but Simple)

### 4.1 Update Gate (z)

Purpose: decides how much of the OLD memory to keep versus how much NEW info to add. It's basically LSTM's forget gate and input gate fused into one.

Output is a number between 0 and 1 (from a sigmoid):
- 0 = fully replace memory with new info
- 1 = fully keep the old memory

Analogy: think of it like a dimmer switch. "Keep 30% old, add 70% new."

Formula: `z_t = sigmoid(W_z · [h_{t-1}, x_t])`

In plain English: take the previous hidden state and the current input, mash them together, pass them through a small learned filter (W_z), then squash the result into a 0-to-1 range with sigmoid. That number is your keep-vs-replace dial.

### 4.2 Reset Gate (r)

Purpose: decides how much of the OLD memory to IGNORE when computing the new candidate memory. It lets the model "forget temporarily" so it can focus on the new input without old baggage.

Output is also 0 to 1:
- 0 = ignore all old memory when building the candidate
- 1 = use the full old memory

Analogy: think of it like a filter. "Don't let old context bias this new idea."

Formula: `r_t = sigmoid(W_r · [h_{t-1}, x_t])`

In plain English: same idea as the update gate — combine old hidden state and new input, pass through a learned filter (W_r), squash with sigmoid. This number decides how much of the past gets let through into the new draft memory.

## 5. The Candidate Hidden State

Just like LSTM has a candidate cell state, GRU has a candidate hidden state. Think of it as the "draft" of new memory. The reset gate controls how much old memory is allowed into this draft.

Formula: `h̃_t = tanh(W · [r_t * h_{t-1}, x_t])`

In plain English: first, the reset gate filters the old memory (r_t * h_{t-1}). That filtered memory gets combined with the new input, passed through a learned filter (W), then squashed with tanh into a -1 to 1 range. That's your fresh, candidate version of memory — not final yet, just a draft.

## 6. The Final Hidden State Update

Formula: `h_t = (1 - z_t) * h_{t-1} + z_t * h̃_t`

In plain English:
- (1 - z_t) controls how much OLD memory sticks around
- z_t controls how much of the NEW candidate gets added in
- Add them together and you get the new hidden state

Analogy: imagine mixing two liquids in a jug — old memory and new candidate memory. The update gate decides the exact proportions of the mix.

## 7. GRU Per-Word Workflow (4 Steps)

Step 1: Look at the new input word and the previous hidden state.

Step 2: Compute the update gate — how much old memory to keep versus replace.

Step 3: Compute the reset gate, then use it to build the candidate hidden state — the new info worth considering.

Step 4: Blend the old memory with the candidate memory, using the update gate as the mixing ratio, to get the new hidden state.

Repeat this for every word in the sequence, one step at a time.

## 8. Visual Timeline

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

Compare that to LSTM, which ran two streams side by side — h (short-term) and C (long-term). GRU squashes both into just h. Simpler pipe, same water flowing through it.

## 9. Why GRU Matters

- Fewer gates → faster training and faster inference
- Only one memory stream → smaller memory footprint
- Similar accuracy to LSTM on many real-world tasks
- Great for edge devices and low-compute environments
- Fewer parameters → lower overfitting risk on small datasets

## 10. Summary

- GRU = simplified LSTM with 2 gates and 1 memory
- Update gate = keep old vs add new (combines forget + input)
- Reset gate = how much old memory to ignore when computing the candidate
- Workflow per word: look → update gate → reset gate + candidate → blend into new hidden state
- Faster and lighter than LSTM, with similar accuracy on most tasks