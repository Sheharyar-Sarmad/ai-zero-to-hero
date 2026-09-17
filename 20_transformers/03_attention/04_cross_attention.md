# Cross-Attention — The Bridge Between Two Sequences

## What cross-attention really is
Cross-attention is the same four-step formula from file 03, but the query comes from one sequence while the keys and values come from another. In an encoder-decoder model, this is how the decoder looks back at the encoder at every single generation step, asking "what in the source is relevant right now?"

## Self vs cross — the one-line difference
- Self-attention: Q, K, V all from sequence A.
- Cross-attention: Q from sequence B, K and V from sequence A.

One line: nothing else changes — formula is identical.

## The translation example
Take "I love books" → Urdu. The encoder reads the whole English sentence and produces one output vector per word. Now the decoder starts generating Urdu, word by word. At the moment it's about to emit the verb (کتابیں سے پیار — "love"), its current hidden state forms a query that essentially says "I need a verb next." That query gets dotted against the encoder's keys for "I," "love," and "books." The key for "love" scores highest, so its value dominates the blended output — the decoder pulls in exactly the source information it needs at that step, not the whole sentence undifferentiated.

## Step-by-step walkthrough
1. `Q = decoder_hidden_state · W_q` — the decoder's current state is projected into a query. This says what the decoder is currently looking for.
2. `K = encoder_outputs · W_k`, `V = encoder_outputs · W_v` — the encoder's full output sequence is projected into keys and values, once, and reused for every decoding step.
3. `scores = Q · Kᵀ / √d_k` — the decoder's query is compared against every encoder position, scaled the same way as in file 03.
4. `weights = softmax(scores)` — turned into a distribution over source positions: how much attention to pay to each source word right now.
5. `context = weights · V_enc` — the final output is a weighted blend of encoder values, i.e. the piece of source information most relevant to this decoding step.

## Visual diagram
```
encoder outputs ──────────────→ K, V
                                  │
decoder state ──→ Q ──→ scores ──┤
                                  ▼
                              softmax
                                  │
                                  ▼
                    context for this decoding step
```

## Why this is what makes translation work
Without cross-attention, the decoder would generate blindly, relying only on what it's produced so far and a single compressed summary of the source. Cross-attention lets it ask, at every single step, "what in the source should I look at right now?" — and the answer changes each step, because different source words matter for different output words. That's what lets word order, gender agreement, and long-distance dependencies transfer correctly between languages with very different structures.

## Where cross-attention appears in a transformer block
It sits between masked self-attention and the feed-forward network, inside every decoder layer:
```
decoder layer
├── masked self-attention
├── cross-attention  ← here
└── feed-forward
```
Self-attention first lets the decoder relate its own generated tokens to each other; cross-attention then lets it consult the encoder; the feed-forward network processes the result.

## Encoder-decoder vs decoder-only models
GPT-style models are decoder-only — no separate encoder, so no cross-attention at all; everything runs through masked self-attention on one sequence. T5 and BART are true encoder-decoder models and use cross-attention to connect the two. One line: encoder-decoder is preferred when there's a clear source-to-target mapping (translation, summarization); decoder-only is preferred for open-ended generation where there's no separate "source" sequence to consult.

## Activation functions used
softmax — same as self-attention, the only non-linearity in the mechanism.

## Loss function
None — cross-attention has no loss of its own; it's trained end-to-end by whatever loss sits at the output of the full model.

## Optimizer
Adam, learning rate around 0.001, same as the rest of the transformer.

## Common pitfalls
- Swapping Q and K roles — the query must come from the decoder, not the encoder.
- Forgetting that K and V must come from the SAME sequence (the encoder), never mixed sources.
- Applying a causal mask to cross-attention — it shouldn't have one; the decoder is allowed to see the entire source sequence at every step.

## What to remember
- Cross-attention: `softmax(Q_dec · K_encᵀ / √d) · V_enc` — same formula, different sources.
- Q comes from the decoder; K and V come from the encoder.
- It sits between masked self-attention and the feed-forward layer in each decoder block.
- It's recomputed fresh at every decoding step, using the same fixed encoder K/V each time.
- No causal masking here — the encoder side is fully visible.
- Decoder-only models like GPT skip this mechanism entirely.