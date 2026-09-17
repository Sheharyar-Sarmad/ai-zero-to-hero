# Decoder Internals — From Start Token to Sentence

## What a decoder really is
The decoder is the half of the model that turns a compressed thought back into words. It generates one token at a time, and — this is the key trick — it feeds its own past output back in as input for the next step. Think of the decoder as a storyteller who has already read the book once. The encoder handed them the plot; now they narrate it back, one word at a time, each word shaping the next.

## The full pipeline at a glance
```
<start> → embedding → decoder cell → linear → softmax → word
                          ▲                                 │
                          └──────── feed back in ◄──────────┘
                                  (repeat until <eos>)
```

## Step 1 — It receives the encoder's context
The decoder never sees raw input words from the source sentence. All it gets is the encoder's final hidden states — the context vector — packaged up and handed over.

```
[encoder final h] ──→ [decoder initial state]
                   └─→ [cross-attention memory]
```

That's the entire handoff. From here on, everything happens inside the decoder.

## Step 2 — The start token
Generation has to begin somewhere, but the decoder hasn't produced anything yet — so we hand it a special placeholder, usually written `<sos>` or `<start>`, with its own token id (e.g. id `1`). This is the only token the decoder ever gets "for free." Every token after it is something the decoder produced itself.

## Step 3 — The feedback loop (the heart of the file)
```
<sos>   → [decoder] → "I"
              ↓
 "I"    → [decoder] → "love"
              ↓
"love"  → [decoder] → "books"
              ↓
"books" → [decoder] → <eos>
              ↓
            STOP
```
At every step, the decoder's own previous output becomes its next input. That loop — output becomes input, again and again — is exactly what "autoregressive" means.

## Step 4 — The decoder cell
The decoder cell is built from the same ingredients as the encoder cell — an RNN, LSTM, GRU, or Transformer block — but with two key differences.

**Masked self-attention** (or a strictly one-directional recurrence): the decoder is only allowed to look at tokens it has already generated, never at tokens that come later.

**Cross-attention**: at every single step, the decoder reaches back and consults the encoder's output, so it never loses track of what it's supposed to be describing.

## Step 5 — Masked self-attention (why the mask matters)
Without a mask, predicting the 3rd token could peek at the 4th and 5th. That's cheating during training and flatly impossible during real inference, since those future tokens don't exist yet. The mask is a triangle that hides the future.

```
token:   I   love  books
  I      ✓    ✗      ✗
  love   ✓    ✓      ✗
  books  ✓    ✓      ✓
```
The ✗ cells are set to -infinity before softmax, so they collapse to zero attention weight.

## Step 6 — Cross-attention (the bridge back to the encoder)
In self-attention, Q, K, and V all come from the same sequence. In cross-attention they split apart: Q comes from the decoder ("what am I trying to produce?"), while K and V come from the encoder ("what did I read?").

```
decoder query  ──┐
                 ├──→ attention ──→ context for this step
encoder keys   ──┤
encoder values ──┘
```
This is the mechanism that lets the model actually stay faithful to the source sentence instead of drifting off on its own.

## Step 7 — Turning the hidden state into a word
Once the decoder cell produces its output vector, a linear layer maps that vector to vocab-size scores (logits). Softmax then turns those scores into probabilities.

```
hidden state (small)  →  logits over vocab       →  softmax  →  probs
                          [3.1, 0.2, 8.4, ...]                  [0.02, 0.001, 0.96, ...]
```
`p = softmax(logits)` — the token with the highest probability is the prediction.

## Step 8 — Picking the next token
**Greedy** — always pick the single highest-probability token; fast, but can lock in mistakes early.
**Beam search** — keep the top-k candidate sequences alive at once; better quality for tasks like translation.
**Sampling** (temperature, top-k, top-p) — introduces randomness; useful when you want creative or varied output.

## Step 9 — Stopping
The decoder stops when it emits `<eos>`, when it hits a max-length cap, or — in beam search — once every beam has ended. Classic flow: `... → "books" → <eos> → STOP`.

## Training vs inference (teacher forcing)

### During training
The full target sentence is fed in, shifted by one position — this is teacher forcing. Even if the model predicts the wrong token at step 3, step 4 is still fed the TRUE token, not the model's guess.

```
step  input     target
 1    <sos>     I
 2    I         love
 3    love      books
 4    books     <eos>
```
This keeps every step's input clean and correct, which makes training faster and much more stable.

### During inference
There's no ground truth to lean on — the model is fed its own previous output, wrong or not. If an early token is off, that error can compound into later steps. This gap between training and inference is called exposure bias.

## Activation functions used
- **tanh** — used inside the decoder hidden state, to squash values into a bounded range.
- **sigmoid** — used inside gates (LSTM/GRU), to decide how much information to let through.
- **ReLU / GELU** — used inside feed-forward sublayers, to add non-linearity.
- **softmax** — used at the very end, to turn logits into token probabilities.

## Loss function
Cross-entropy, same as the encoder side:

`L = -Σ y_true · log(y_pred)`

The target is the true next token; the model's prediction is a probability distribution over the whole vocabulary. The loss penalizes the model for putting low probability on the token that was actually correct.

## Optimizer
Adam, with a learning rate around 0.001. For Transformer decoders in particular, a learning-rate warmup period is often used, since the decoder is the part that suffers most from unstable early training.

## Visual summary
```
[encoder context] ──────────────────────────────┐
                                                  ▼
<sos> → embed → decoder cell (masked self-attn + cross-attn) → linear → softmax → "I"
                                                  ▲                                  │
                                                  └────────────── feed back ─────────┘
                        ... repeats for "love", "books" ...
                                                  ▼
                                               <eos> → STOP
```

## Common pitfalls
- Forgetting the causal mask, which lets the model leak future tokens during training.
- Mismatching the encoder's and decoder's positional encodings.
- Relying only on greedy decoding, which tends to produce repetitive, dull output.

## What to remember
- The decoder generates one token at a time and feeds its own output back in — that's autoregression.
- It receives only the encoder's context vector, never raw source words.
- Masked self-attention blocks the future; cross-attention connects back to the encoder at every step.
- Training uses teacher forcing (true tokens); inference uses the model's own guesses, creating exposure bias.
- Generation stops at `<eos>`, a max-length cap, or when all beams end.