# Deep Learning III — Recurrent Neural Networks

From vanishing gradients to gated architectures. Every concept in plain English, every model in working code, every architectural choice explained.

This module covers the full RNN family, the problems they solve, and where they still break down. It ends with a real project — an LSTM that completes quotes.

---

## What's inside

### 1. Basics
- **Why RNNs?** — the limits of feedforward networks on sequential data
- **RNN fundamentals** — hidden state, recurrence, parameter sharing
- **Inputs and sequences** — how sequence data is batched, shaped, and fed in

### 2. Architecture
- **RNN architecture intuition** — the unrolled view
- **Forward and backward pass** — backpropagation through time, step by step
- **Vanishing and exploding gradients** — why long sequences kill vanilla RNNs
- **Bidirectional and deep RNNs** — stacking layers, reading in both directions

### 3. Gated RNNs
- **Problems with vanilla RNNs** — the three failure modes
- **Why LSTM** — the motivation behind gating
- **LSTM intuition and workflow** — cell state as long-term memory
- **LSTM gates** — forget, input, output — what each one actually does
- **GRU intuition and workflow** — the lighter alternative
- **LSTM vs GRU** — when to pick which

### 4. Project — Quote Completion
A full-stack AI application. Trains a from-scratch LSTM on 3,038 famous quotes, exports it to TFLite, serves it through a FastAPI backend, and completes real quote fragments in a Next.js frontend with Groq and voice.

**Live:** https://quote-lab-dun.vercel.app
**Repo:** https://github.com/Sheharyar-Sarmad/Quote-Lab

---

## Structure

```
19_deep_learning_3/
├── 1_basics/
│ ├── 1_why_RNN.md
│ ├── 2_RNN.md
│ └── 3_rnn_inputs_&sequences.md
├── 2_architecture/
│ ├── 1_rnn_architecture_intuition.md
│ ├── 2_forward_backward_pass.md
│ ├── 3_vanishing_exploding_gradients.md
│ └── 4_bidirectional_and_deep_rnn.md
├── 3_gated_rnns/
│ ├── 1_problems_with_RNN.md
│ ├── 2_why_LSTM.md
│ ├── 3_LSTM_intuition&workflow.md
│ ├── 4_lstm_gates.md
│ ├── 5_GRU_intuition&_workflow.md
│ └── 6_LSTM_vs_GRU.md
├── notebooks/
│ └── RNN_Implementation.ipynb
└── projects/
└── quote_completion/
```


---

## Key takeaways

**The vanishing gradient problem is the whole reason gated RNNs exist.** As sequences get longer, gradients multiplied through backpropagation through time either shrink to zero or explode. LSTMs solve this with a cell state that carries information across time steps largely unmodified — the forget gate decides what to keep.

**LSTM vs GRU is a tradeoff, not a winner.** GRUs have fewer parameters and train faster. LSTMs have more expressive power and dominate on long sequences. For most modern tasks, benchmark both.

**Bidirectional layers double the context.** If your task doesn't require causal reasoning (i.e., you don't need to predict the next token in real time), running a second RNN backward through the sequence can capture meaning the forward pass misses.

**RNNs are no longer state-of-the-art.** Transformers replaced them for almost every NLP task. But RNNs are still the clearest way to learn sequence modelling — and the intuitions from LSTM gating carry directly into understanding attention.

---

## What's next

**Transformers** — self-attention, positional encoding, multi-head attention, and the architecture behind GPT, Claude, and every modern LLM. The same sequence-modelling problem, solved without recurrence.

---

## Stack

Python · TensorFlow · Keras · NumPy · Pandas · Jupyter · FastAPI · Next.js
