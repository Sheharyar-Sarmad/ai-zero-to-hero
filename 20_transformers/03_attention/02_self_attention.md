# Self-Attention — Every Token Looks at Every Other

## What self-attention really is
Self-attention is a group chat. Every token sends a message (query), every token advertises what it knows (key), and every token ends up with a weighted blend of everyone else's content (values). The Q, K, and V here all come from the *same* sequence — nothing external is involved.

## The aha example
"The animal didn't cross the street because it was too tired."

What does "it" refer to — the animal or the street? You know instantly. A model doesn't, unless something lets "it" look back across the sentence and pull in context from "animal." That's the job of self-attention: every word gets to check every other word before deciding what it means here.

## Q, K, V — all from the same sequence
Same input sequence, three different learned views of it:

```
input tokens
     │
     ├──> × W_Q ──> Q
     ├──> × W_K ──> K
     └──> × W_V ──> V
```

`W_Q`, `W_K`, `W_V` are learned weight matrices.
The model figures out during training what makes a good "question," "label," and "content" for each token.

## Step-by-step walkthrough

1. `score_ij = q_i · k_j`
   How relevant is token j to token i? Dot product measures alignment between i's query and j's key.

2. `score_ij = score_ij / √d`
   Scale it down. Keeps the numbers from exploding as vector size `d` grows, which keeps training stable.

3. `weights = softmax(scores)`
   Turn raw scores into a clean probability distribution — one row per token, values between 0 and 1, summing to 1.

4. `output_i = Σ weight_ij · v_j`
   Token i's new representation is a weighted blend of everyone's values, weighted by how relevant they were.

Compressed: `attention = softmax(Q·Kᵀ/√d)·V`

## The attention matrix (visual)
For 3 tokens, rows = queries, columns = keys:

```
        k1    k2    k3
q1  [ 0.7   0.2   0.1 ]   → sums to 1.0
q2  [ 0.1   0.6   0.3 ]   → sums to 1.0
q3  [ 0.2   0.2   0.6 ]   → sums to 1.0
```

Each row tells you where that token is "looking."

With a causal mask (lower triangle only — can't see the future):

```
        k1    k2    k3
q1  [ 1.0   0     0   ]
q2  [ 0.3   0.7   0   ]
q3  [ 0.2   0.3   0.5 ]
```

Decoders mask because they generate one token at a time and shouldn't peek ahead; encoders skip the mask because the whole input is already available at once.

## Multi-head — a teaser
Instead of running this once, transformers run it several times in parallel, each with its own `W_Q`, `W_K`, `W_V`. Each "head" can specialize — one might track grammar, another might track coreference like our "it" example. Full mechanics live in `04_transformer_architecture.md`.

## Why it works (intuition)
Every token talks directly to every other token in a single step — no relay race. The "distance" between any two tokens, no matter how far apart in the sentence, is always 1 hop. That's what lets the model link "it" back to "animal" across several words instantly.

## Self-attention vs recurrence
- RNNs trickle information through time, one step at a time — long-range links can fade before they arrive.
- Self-attention sees the entire sequence at once — every pair connects directly.
- The cost is O(n²) — every token compares against every other token, so long sequences get expensive fast.

## Activation functions used
softmax — converts raw attention scores into a normalized probability distribution over tokens.

## Loss function
Self-attention has no loss of its own — it's a component trained end-to-end, usually via cross-entropy on whatever the full model is predicting.

## Optimizer
Adam, typically with a learning rate around 0.001 (often warmed up and decayed in practice).

## Common pitfalls
- Forgetting the causal mask in a decoder and letting it "see the future."
- Treating the attention matrix as directly human-interpretable — high weight doesn't always mean intuitive meaning.
- Ignoring the O(n²) cost until sequence length makes training or inference painfully slow.

## What to remember
- Self-attention = same sequence supplies Q, K, and V.
- Formula: `attention = softmax(Q·Kᵀ/√d)·V`.
- Each row of the attention matrix is a probability distribution summing to 1.
- Causal masking blocks future tokens — needed for decoders, not encoders.
- Every token reaches every other token in one step — distance is always 1.
- Multi-head just means doing this several times in parallel with different projections.