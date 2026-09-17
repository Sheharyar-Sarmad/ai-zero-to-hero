# Multi-Head Attention — Many Questions at Once

## What it really is
Multi-head is just asking several experts instead of one. Attention runs several times in parallel, each with its own learned projections. Each expert sees the same sentence but focuses on something different — then you combine their answers.

## The problem with one head
A single attention pattern can only capture one kind of relationship at a time. Softmax forces a single weighted average per query — great for "what agrees with the verb" but bad for also tracking "what does this pronoun refer to" or "what's nearby." One head, one lens.

## The multi-head trick

`head_i = Attention(Q·W_i^Q, K·W_i^K, V·W_i^V)`
Each head gets its own small projection of Q, K, V, so it looks at the sentence through its own lens.

`MultiHead = Concat(head_1..head_h) · W_O`
Stack all the heads' outputs side by side, then mix them with one learned matrix.

## Visual
```
Input embeddings (d_model)
        │
   ┌────┼────┬────┬────┐
   ▼    ▼    ▼    ▼    ▼
 head1 head2 head3 ... headh
  (d_k) (d_k) (d_k)   (d_k)
   │    │    │         │
   └────┴────┴────┴────┘
           │  concat
           ▼
     [ h × d_k = d_model ]
           │
           ▼
          × W_O
           │
           ▼
      final output
```
Each head is narrower than the full model (d_k = d_model / h), so splitting into heads costs nothing extra — it's the same total width, just sliced up.

## What each head learns
There's no fixed assignment — the model discovers specializations during training, nobody hand-designs them. Common patterns that show up empirically: some heads track grammar (subject-verb agreement), some track coreference (pronouns to their referents), some are almost purely positional (attend to the previous or next token). Others look redundant or uninterpretable. That's fine — it's an emergent division of labor, not a spec.

## Why concatenate then project
Concatenation keeps every head's information intact — nothing is averaged away at this stage. `W_O` is what actually learns how to mix them, deciding which combinations of heads matter for the next layer. Skip W_O and you just have h disconnected mini-attentions bolted together.

## The numbers you'll see

| Model | Heads |
|---|---|
| BERT-base | 12 heads |
| GPT-3 | 96 heads |
| Llama-3-70B | 64 heads |

## Cost
Same total compute as single-head attention — the work is just split into narrower parallel pieces instead of one wide one.

## Activation functions
softmax only, applied inside each head to turn scores into attention weights.

## Loss function
None of its own — it's a layer inside the network, trained by whatever loss sits at the end (e.g., cross-entropy).

## Optimizer
Adam, learning rate ~0.001 (often with warmup/decay schedules in practice).

## Common pitfalls
- Thinking heads have fixed, human-labeled roles — they're discovered, not assigned.
- Forgetting the W_O projection — without it, concatenated heads never actually get mixed.
- Assuming multi-head is more expensive than single-head — it's the same width, just parallelized.

## What to remember
- Multi-head = several small attentions in parallel, not one big one repeated.
- Each head gets its own Q/K/V projections, so it can specialize.
- Concat preserves everything; W_O is what blends heads together.
- Specializations (grammar, coreference, position) emerge from training, not design.
- Total cost matches single-head attention of the same model width.