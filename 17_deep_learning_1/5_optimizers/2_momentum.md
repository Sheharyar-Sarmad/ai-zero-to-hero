

# Momentum Optimizer

## Physics Analogy

$$
\text{Momentum} = \text{mass} \times \text{velocity}
$$

In physics, a heavier or faster-moving object keeps moving in its direction due to accumulated momentum. The Momentum optimizer borrows this idea: past gradient updates build up a "velocity" that carries forward into future updates, instead of each step being decided fresh.

---

## Vanilla Gradient Descent Update Rule

$$
w_{new} = w_{old} - \eta \frac{\partial L}{\partial w_{old}}
$$

In time-step notation:

$$
w_{T+1} = w_T - \eta \, \Delta w
$$

This update relies **only on the current gradient** — it has no memory of past steps.

---

## Momentum's Update Rule

$$
w_{T+1} = w_T - V_t
$$

Instead of subtracting the raw gradient directly, we subtract $V_t$ — a **velocity term** that accumulates past gradients.

### Velocity Term

$$
V_t = \beta \times V_{t-1} + \eta \, \Delta w_t
$$

- **$\beta$** → Momentum coefficient (commonly ~0.9)
- **$V_{t-1}$** → Velocity from the previous step
- **$\eta \, \Delta w_t$** → Current gradient term (scaled by learning rate)

So $V_t$ is a **running weighted average of all past gradients**, not just the current one.

---

## What Is "Noise" and Why Does SGD Suffer From It?

**Noise** means the update direction **fluctuates wildly** from step to step instead of moving smoothly toward the minimum.

### Why SGD Has This Problem
- SGD computes the gradient using **just one random sample** at a time.
- A single sample isn't representative of the whole dataset — its gradient can point quite differently from the "true" overall gradient (over the full dataset).
- So at every step, SGD's direction can swing — sometimes toward the minimum, sometimes almost sideways or backward — causing the path to **zig-zag** rather than move smoothly downhill.
- Each update fully trusts the current, noisy gradient, so there's nothing smoothing it out.

### Why Momentum Doesn't Have This Problem
- Momentum doesn't rely purely on the current step's gradient. It computes $V_t$ as a **weighted average of the current gradient AND all previous velocities** (via the $\beta \times V_{t-1}$ term).
- Since past gradients still contribute (weighted by $\beta$), a single noisy/off-direction gradient from one bad sample gets **diluted** — it can't suddenly swing the update in a completely different direction.
- This acts like a **smoothing/averaging filter** over the gradient history, so the overall path curves smoothly toward the minimum instead of zig-zagging.
- Physically: like a ball with mass rolling downhill — it has built-up velocity, so a small bump or push in a slightly wrong direction doesn't instantly change its course; it keeps moving mostly in the direction it's already going.

---

## Global Minima vs Local Minima

- **Global Minimum** → The point where the loss function has its **absolute lowest value** across the entire loss landscape. This is the ideal point we want the optimizer to reach.
- **Local Minimum** → A point where the loss is **lower than all nearby points**, but **not** the lowest possible value overall. The loss landscape can have many such "dips" that aren't the true minimum.

### Why This Matters for Optimizers
- Vanilla Gradient Descent, since it only follows the current gradient exactly, can get "trapped" once it reaches a local minimum — the gradient there is zero (or near zero) in all directions, so it stops updating even though a better (lower) minimum exists elsewhere.
- **Momentum helps here too**: because it carries **accumulated velocity** from previous steps, it can "coast" through a shallow local minimum or a flat region (like a ball rolling over a small dip) instead of getting stuck, potentially continuing on to find a better minimum.

## Key Idea

Momentum smooths out SGD's noisy, sample-to-sample gradient fluctuations by blending in a memory of past gradients (velocity), which not only produces a more stable path to the minimum but also gives it enough "carry-through" to escape shallow local minima that vanilla Gradient Descent can get stuck in.