# Encoder Internals — From Word to Context Vector

## What an encoder really is
An encoder is the half of a seq2seq model that reads. It takes a whole input sequence, one token at a time, and compresses everything it has seen into a single dense summary. That summary — the context vector — is meant to carry the *meaning* of the sentence, not its exact words.

## The full pipeline at a glance
```
words        tokens         IDs         embeddings      encoder cells      context
┌─────┐    ┌────────┐   ┌────────┐    ┌──────────┐    ┌─────────────┐   ┌─────────┐
│ raw │ →  │ "i"    │ → │  5     │ →  │ [0.1,..] │ →  │ RNN/LSTM/GRU│ → │  h_final│
│ text│    │ "love" │   │  42    │    │ [0.3,..] │    │  (recurrent)│   │ (context│
│     │    │ "books"│   │  891   │    │ [0.7,..] │    │             │   │  vector)│
└─────┘    └────────┘   └────────┘    └──────────┘    └─────────────┘   └─────────┘
```

## Step 1 — Words become tokens
Models can't work with raw text; they need discrete, consistent units. Tokenization splits a sentence into those units — usually words or sub-words, plus lowercasing and punctuation handling.

Example: `"I love books"` → `["i", "love", "books"]`

## Step 2 — Tokens become numbers (IDs)
Each unique token is assigned an integer ID via a lookup table (the vocabulary). This turns text into something a computer can index into.

| token   | ID  |
|---------|-----|
| "i"     | 5   |
| "love"  | 42  |
| "books" | 891 |
| "<pad>" | 0   |

## Step 3 — IDs become vectors (embeddings)
An embedding is a lookup table of *learnable* vectors — one row per vocabulary ID. Instead of a single number, each token now gets a small vector that can encode shades of meaning.

Example (50-dim, like a small LSTM setup): `"love" → [0.12, -0.87, 0.44, ..., 0.05]` (50 numbers total).

## Step 4 — The encoder cell
Any of these can slot into the same pipeline — they just handle memory differently:

- **Vanilla RNN** — passes the hidden state forward at every step with no special gating. Simple, but memory fades fast over long sequences.
- **LSTM** — adds gates that decide what to keep, forget, and output, giving it a much longer memory.
- **GRU** — a lighter LSTM with fewer gates, often just as effective and cheaper to compute.
- **Bidirectional variants** — run the sequence forward *and* backward, so each position sees context from both directions.

Think of the hidden state as the cell's memory of everything read so far — how it's updated is the only thing that changes between these variants.

## Step 5 — The feedback loop (the hidden state update)
```
word₁ → [cell] → h₁
            ↓
word₂ → [cell] → h₂
            ↓
word₃ → [cell] → h₃
            ↓
           ...
```

`h_t = tanh(W · [h_{t-1}, x_t] + b)`

In words: the new hidden state `h_t` is built from the previous hidden state `h_{t-1}` and the current input `x_t`, combined with learned weights `W` and a bias `b`, then squashed with `tanh`. We don't need the exact dimensions — the shape is what matters.

## Activation functions used
- **tanh** — squashes values to [-1, 1]; used for the hidden state so it stays bounded.
- **sigmoid** — squashes values to [0, 1]; used for gates (LSTM/GRU) since gates need an "how much to let through" value.
- **ReLU** — `max(0, x)`; used inside feed-forward layers to add non-linearity cheaply.
- **softmax** — turns raw scores into a probability distribution; used at the output layer.

## Step 6 — Building the context vector
After the last token is read, the cell's final hidden state *is* the context vector — nothing more is done to it. For a bidirectional encoder, the forward and backward final hidden states are concatenated into one longer vector.

```
h_forward_final  ─┐
                   ├──→ [ h_forward_final ; h_backward_final ] = context vector
h_backward_final ─┘
```

## Step 7 — Handing off to the decoder
The context vector becomes the decoder's starting hidden state — the single handoff point between the two halves of the model.

```
[encoder final h] ──→ [decoder initial state]
```

## Loss function (used during training)
`L = -Σ y_true · log(y_pred)`

In words: for each predicted token, compare the predicted probability distribution to the true next token, and penalize the model more heavily the further off it is. This is cross-entropy loss, the standard choice for any task that predicts a sequence of tokens.

## Optimizer
Adam is the default choice for training these models. It adapts the learning rate per parameter using running averages of past gradients, so some weights update faster than others automatically. A learning rate around 0.001 is the usual starting point.

## Visual summary
```
"I love books"
     │
     ▼
[tokenize] → [i, love, books]
     │
     ▼
[IDs]        → [5, 42, 891]
     │
     ▼
[embeddings] → [v1, v2, v3]
     │
     ▼
[cell]→h1 →[cell]→h2 →[cell]→h3
                              │
                              ▼
                      context vector
                              │
                              ▼
                    → to the decoder →
```

## Common pitfalls
- Forgetting to pad short sequences, causing shape mismatches across a batch.
- Exploding gradients in vanilla RNNs over long sequences.
- Using a fixed-size context vector for very long inputs, which forces too much to be compressed into one vector.

## What to remember
- The encoder's job is to compress a whole sequence into one context vector.
- Tokens → IDs → embeddings is a strict pipeline; each step just changes representation, not meaning.
- The hidden state is the running memory; the update equation is the same shape whether it's a vanilla RNN, LSTM, or GRU.
- The final hidden state *is* the context vector — no extra step needed.
- Bidirectional encoders concatenate forward and backward final states.
- The context vector is the only thing passed to the decoder.