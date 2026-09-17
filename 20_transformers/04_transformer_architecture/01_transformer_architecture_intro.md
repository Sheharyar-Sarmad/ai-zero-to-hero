# Transformer Architecture — The Full Picture

A transformer is Legos. Attention blocks and feed-forward blocks stacked in a pattern. That's all. Encoder stacks, decoder stacks, or both — depending on what you want to build. It's not one model, it's a blueprint that BERT, GPT, and T5 all build from differently.

## The one-page diagram

```
        ENCODER STACK                      DECODER STACK
   (reads the input)                  (writes the output)

   Input Embeddings                   Output Embeddings
         +                                    +
   Positional Encoding                Positional Encoding
         |                                    |
         v                                    v
  +---------------+                  +-------------------+
  | Self-Attention|                  | Masked Self-Attn   |
  +---------------+                  +-------------------+
         |                                    |
  +---------------+                  +-------------------+
  | Feed-Forward  |----------------->| Cross-Attention     |
  +---------------+   (K, V passed)  +-------------------+
         |                (repeat N times)     |
     (repeat N times)                +-------------------+
         |                           | Feed-Forward        |
         v                           +-------------------+
   Encoder Output                            |
                                              v
                                      Output Probabilities
```

## The encoder stack

The encoder is N identical layers stacked on top of each other (N = 6 in the original paper, more in bigger models). Each layer does the same two things: self-attention, then feed-forward. Input embeddings plus positional encoding go in at the bottom, and each layer refines the representation a bit more before passing it up. Nothing decoder-specific happens here — the encoder just builds a rich understanding of the input.

## The decoder stack

The decoder is also N identical layers, but each one has three parts: masked self-attention (so it can't peek at future tokens), cross-attention (so it can look at the encoder's output), then feed-forward. It generates output one token at a time, using what it's already generated plus the encoder's understanding of the input.

## What's inside one layer

```
        input
          |
   +--------------+
   |  Sublayer     |   (Self-Attention or Feed-Forward)
   +--------------+
          |
      Add & Norm  <-- residual connection + layer norm
          |
        output
```

Formula, one line: `output = LayerNorm(input + Sublayer(input))`. In plain English: run the input through attention or feed-forward, add the original input back in, then normalize.

## Residual connections and layer norm

Residual connections are the "+input" part — they let gradients flow straight back through the network instead of vanishing as it gets deeper. Layer norm rescales activations after each sublayer so numbers don't blow up or shrink as they pass through dozens of layers. One line: residual connections prevent vanishing gradients; layer norm keeps activations stable.

## The three families

- **Encoder-only (BERT)** — for understanding text: classification, embeddings, search.
- **Decoder-only (GPT)** — for generating text: chatbots, autocomplete, writing.
- **Encoder-decoder (T5)** — for transforming text: translation, summarization, Q&A.

## Why it won

- **Parallel training** — no recurrence, so every token processes at once, not step by step.
- **Long-range memory** — attention connects any two tokens directly, no matter the distance.
- **Scales with data + compute** — more layers, more data, more GPUs just keeps helping.

## Activation functions

- **ReLU** — `max(0, x)`, zeroes out negatives, cheap and fast.
- **GELU** — a smoother version of ReLU, used in most modern transformers (BERT, GPT).

## Loss function

Cross-entropy loss: compares the predicted next-token probability distribution to the actual next token, penalizing confident wrong guesses hardest.

## Optimizer

Adam, learning rate around 0.001, usually with a warmup period that ramps the learning rate up slowly before decaying it — keeps early training stable.

## Common pitfalls

- Confusing the three families — encoder-only, decoder-only, and encoder-decoder solve different problems.
- Thinking each layer learns something different — the N layers are identical in structure, just with separately learned weights.
- Forgetting residual connections exist — without them, deep stacks simply don't train.

## What to remember

- A transformer = attention blocks + feed-forward blocks, stacked N times.
- Encoders understand, decoders generate, encoder-decoders transform.
- Every sublayer is wrapped in `input + Sublayer(input)`, then normalized.
- The decoder adds masking (no peeking ahead) and cross-attention (look at the encoder).
- The architecture won because it parallelizes, remembers long-range, and scales.