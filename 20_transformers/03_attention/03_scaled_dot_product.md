# Scaled Dot-Product Attention — The Four-Line Formula

## The one equation that runs everything

```
Attention(Q, K, V) = softmax( Q · Kᵀ / √d_k ) · V
```
This one line computes both self-attention and cross-attention — Q, K, V just come from different places depending on which. Self-attention: all three come from the same sequence. Cross-attention: Q comes from one sequence, K and V from another. The formula never changes. Only what you plug in does.

## Breaking it down, one operation at a time

### 1. Q · Kᵀ  — how well do query and key match?
```
scores = Q · Kᵀ
```
Every query row gets dotted against every key row, giving a raw similarity score for every (query, key) pair. Bigger number means the query and key point in a more similar direction.

### 2. / √d_k  — why we scale
```
scaled = scores / √d_k
```
Raw dot products grow larger as the vector dimension d_k grows, just from summing more terms. Dividing by √d_k pulls the scores back into a stable range before softmax sees them.

### 3. softmax(...)  — turning scores into probabilities
```
weights = softmax(scaled)
```
Each row of scores gets turned into a set of positive numbers that sum to 1 — a probability distribution over "which keys matter for this query."

### 4. · V  — blending the values
```
output = weights · V
```
Each query's output is a weighted average of all the value vectors, using the weights just computed. High weight on a key means its value dominates the output.

### 5. Putting it back together
```
output = softmax(Q·Kᵀ/√d_k) · V
```
Match, scale, normalize, blend. That's the whole layer — no hidden steps.

## Why √d_k? (the most-asked question)

Without scaling, dot products grow with d_k, so scores get large, softmax saturates (one weight goes to ≈1, the rest to ≈0), and gradients through it vanish. Dividing by √d_k cancels out that growth and keeps scores in a range where softmax stays soft. One line: it's a variance fix, not a magic constant.

## Worked numeric example

d_k = 2. Two queries, two keys, two values:
```
Q = [[1, 0],
     [0, 1]]
K = [[1, 0],
     [0, 1]]
V = [[10, 0],
     [0, 20]]
```
Step 1 — Q·Kᵀ:
```
[[1, 0],
 [0, 1]]
```
Step 2 — scale by √2 (≈1.414):
```
[[0.707, 0    ],
 [0,     0.707]]
```
Step 3 — softmax each row (e^0.707≈2.03, e^0≈1):
```
row1: [2.03/3.03, 1/3.03] ≈ [0.67, 0.33]
row2: [1/3.03, 2.03/3.03] ≈ [0.33, 0.67]
```
Step 4 — multiply by V:
```
out1 = 0.67*[10,0] + 0.33*[0,20] ≈ [6.7, 6.6]
out2 = 0.33*[10,0] + 0.67*[0,20] ≈ [3.3, 13.4]
```
Query 1 mostly copies value 1, query 2 mostly copies value 2 — the attention pattern found the "matching" key for each query, just as intended.

## Why dot product (and not something else)

- Fast on GPUs: it's just matrix multiplication, which hardware is built to accelerate.
- Learnable via projections: Q, K, V come from learned linear layers, so the model shapes what "similarity" means during training.
- Equivalent to cosine similarity when vectors are normalized — same idea, just scaled by magnitude too.

One line: dot product isn't the only way to score similarity, but it's the one that scales.

## Attention shapes (a diagram)

```
Q: (n_q, d_k)
K: (n_k, d_k)
V: (n_k, d_v)

scores  = Q · Kᵀ        → (n_q, n_k)
weights = softmax(scores) → (n_q, n_k)
output  = weights · V   → (n_q, d_v)
```
n_q = number of query positions, n_k = number of key/value positions, d_k = query/key dimension, d_v = value dimension.

## Masking (how it plugs into the formula)

For decoders, before the softmax step, hidden cells (future positions) get a large negative number (-infinity in theory) added to their score. After softmax, those become 0 — the query simply can't attend to them. One line: masking is a one-line change to the scores, not a separate mechanism bolted on afterward.

## Computational cost

Both time and memory scale with n² because scores is an (n_q, n_k) matrix — every query compares against every key. One line: this quadratic cost is exactly why long-context transformers are hard to scale cheaply.

## Activation functions used

softmax — the only non-linearity in the whole formula, and it lives inside the attention step itself.

## Loss function

None — attention has no loss of its own; it's a building block trained by whatever loss sits at the end of the full model.

## Optimizer

Adam, learning rate around 0.001, same as the rest of the transformer — nothing special for this layer.

## Common pitfalls

- Forgetting to scale by √d_k, which lets softmax saturate and kills gradients.
- Applying softmax over the wrong axis (should normalize over keys, per query row).
- Masking after softmax instead of before — masked positions must be -infinity going in, not zeroed out after.

## What to remember

- One formula, four steps: match (Q·Kᵀ), scale (/√d_k), normalize (softmax), blend (·V).
- Scaling exists purely to stop softmax from saturating as d_k grows.
- Self-attention and cross-attention are the same formula with different inputs.
- Shapes: scores and weights are (n_q, n_k); output is (n_q, d_v).
- Masking is just adding -infinity to scores before softmax — same formula, one extra step.
- Cost grows with n², which is the core scaling bottleneck of attention.