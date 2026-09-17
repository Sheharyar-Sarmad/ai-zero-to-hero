# Positional Encoding — Teaching Order to Attention

## The problem
Attention doesn't know time. It's order-blind by design — "dog bites man" and "man bites dog" produce the exact same set of word vectors to attend over, just relabeled. Without help, the model has no idea what came first, second, or last. We have to inject position info ourselves.

## The fix
The fix is simple: add a position vector to each word embedding before it enters the encoder. Positional encoding is the clock you bolt onto each word so the model knows "this came first, that came third."

`final_input = word_embedding + position_encoding`
Each word's vector gets nudged by a pattern that depends only on where it sits in the sequence.

## What position encoding looks like
Each position gets its own unique vector, the same length as the word embedding, so it can just be added on. The classic approach (from the original Transformer paper) builds this vector out of sine and cosine waves of different frequencies.

## The formula (simplified)
`PE(pos, 2i)   = sin(pos / 10000^(2i/d))`
`PE(pos, 2i+1) = cos(pos / 10000^(2i/d))`
Sine for even dimensions, cosine for odd, with different frequencies per position. That's really all you need to take away — no need to trace the math further.

## Why sine and cosine
- Every position ends up with a unique fingerprint vector.
- The same formula works for any sequence length, even ones longer than training saw.
- Relative positions come out linear — position 5 relates to position 3 the same way position 50 relates to position 48.

## The visual
```
dimension →
        d0   d1   d2   d3   d4   d5 ...
pos 0 [ 0.0  1.0  0.0  1.0  0.0  1.0 ]
pos 1 [ 0.8  0.5  0.2  0.9  0.1  0.9 ]
pos 2 [ 0.9 -0.4  0.4  0.7  0.2  0.9 ]
pos 3 [ 0.1 -0.9  0.6  0.5  0.3  0.8 ]
  ...
```
Picture this as a heatmap: y-axis = position, x-axis = dimension, each cell a value between -1 and 1. Rows form smooth wave patterns — low dimensions oscillate fast, high dimensions oscillate slow.

## Learned vs fixed
The original transformer used fixed sine waves — no training needed, just math. Many modern models instead learn a position embedding table like any other parameter. Trade-off: fixed generalizes better to unseen lengths, learned can fit the training distribution more precisely.

## Rotary (a modern alternative)
RoPE (Rotary Position Embedding) — used by Llama, Mistral, and friends — takes a different approach: instead of adding a position vector, it rotates the query and key vectors by an angle that depends on position. This bakes relative position directly into the attention score itself, which makes it noticeably better behaved for long context windows.

## Activation functions
sine/cosine — the only non-learned, deterministic operation in this whole layer (when using fixed encoding).

## Loss function
None of its own — position encoding just shapes the input; the loss comes from the task at the end.

## Optimizer
Adam, learning rate ~0.001 (only relevant if the position encoding is learned).

## Common pitfalls
- Forgetting to add it — without it, the model is a bag-of-words machine no matter how many layers it has.
- Adding it after attention instead of before — position info needs to be in the input, not bolted on afterward.
- Assuming it's the same across models — fixed sine, learned embeddings, and RoPE are all genuinely different mechanisms.

## What to remember
- Attention alone has no sense of order — positional encoding fixes that.
- It's added to word embeddings before the encoder sees them.
- Classic version: sine/cosine waves at different frequencies per dimension.
- Modern alternative: RoPE rotates Q/K vectors instead of adding a vector.
- Fixed encodings generalize to new lengths; learned ones fit training data better.