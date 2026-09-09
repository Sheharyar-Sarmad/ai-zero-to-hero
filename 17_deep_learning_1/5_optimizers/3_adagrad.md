

# AdaGrad (Adaptive Gradient) Optimizer

## Problem With Previous Optimizers (GD, SGD, Momentum)

All of them use **one single, global learning rate** ($\eta$) for **every parameter** in the model.

- But not all parameters need the same size of update.
- Some weights are connected to **frequently occurring features** and get updated often — they may need smaller, more careful updates as training progresses.
- Other weights are connected to **rare/sparse features** and get updated rarely — they may need larger updates when they do get a chance, so they can catch up.
- A single fixed learning rate for all parameters can't account for this difference — it treats every weight identically regardless of how often or how strongly it's been updated in the past.

## What Problem Does AdaGrad Solve?

AdaGrad gives **each parameter its own adaptive learning rate**, instead of one global rate shared by all weights.

- Parameters that have received **large/frequent gradients** in the past get their learning rate **shrunk down**.
- Parameters that have received **small/rare gradients** in the past keep a **relatively larger** learning rate.

This is especially useful for **sparse data** (e.g., NLP, one-hot encoded features) where some features appear rarely but are still important.

## Formula

$$
G_t = G_{t-1} + \left(\frac{\partial L}{\partial w}\right)^2
$$

$$
w = w - \frac{\eta}{\sqrt{G_t + \epsilon}} \cdot \frac{\partial L}{\partial w}
$$

- **$G_t$** → Sum of the squares of all past gradients for that specific parameter (accumulated over time)
- **$\eta$** → Global (initial) learning rate
- **$\epsilon$** → Small constant to avoid division by zero
- **$\frac{\partial L}{\partial w}$** → Current gradient

Notice: as $G_t$ grows (because a parameter keeps getting updated with large gradients), the term $\frac{\eta}{\sqrt{G_t+\epsilon}}$ **shrinks** — automatically reducing that parameter's learning rate over time.

## Cons of AdaGrad

### 1. Learning Rate Shrinks Too Aggressively
- $G_t$ is a **cumulative sum** that only ever grows (squared terms are always positive) — it never resets or decays.
- Over many iterations, $G_t$ becomes very large, causing $\frac{\eta}{\sqrt{G_t+\epsilon}}$ to become **extremely small**.

### 2. Learning Can Stall Completely
- Because the effective learning rate keeps shrinking and never recovers, training can slow down so much that the model **stops learning** before it actually reaches the minimum — especially in long training runs.

### 3. No Mechanism to "Forget" Old Gradients
- AdaGrad treats gradients from step 1 and step 10,000 with equal weight in the sum — there's no decay, so old, possibly irrelevant gradient history keeps suppressing the learning rate indefinitely.

This exact problem — the ever-shrinking, non-recoverable learning rate — is what led to the development of **RMSProp**, which fixes it using a decaying average instead of a raw cumulative sum.

## Key Idea

AdaGrad solves the "one learning rate for all parameters" problem by adapting the rate per-parameter based on gradient history, but its cumulative (non-decaying) sum of squared gradients causes the learning rate to shrink too aggressively and can stall training prematurely.