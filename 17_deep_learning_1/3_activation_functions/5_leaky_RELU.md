

# Leaky ReLU Activation Function

## Definition
f(x) = x, if x > 0
f(x) = αx, if x ≤ 0   (where α is a small constant, commonly 0.01)

Basically the same as ReLU, except instead of flattening negative inputs all the way to zero, it lets a small sliver through.

## Key Properties
- Output range: (-∞, ∞)
- Derivative: 1 for x > 0, α for x ≤ 0
- Almost identical shape to ReLU, just with a slight slope on the negative side instead of a flat line

## Why It Exists

ReLU's big weakness is the "dying neuron" problem — once a neuron's input goes negative, its output and gradient both become zero, and it just stops updating. If that happens for enough neurons, you end up with parts of the network that are permanently switched off and contribute nothing.

Leaky ReLU's fix is simple: instead of a hard zero for negative inputs, allow a small negative slope (like 0.01x). This keeps a tiny gradient alive even when the input is negative, so the neuron isn't completely stuck — it still has a chance to recover and start contributing again.

## Advantages
- Solves (or at least reduces) the dying ReLU problem
- Still cheap to compute, barely more expensive than regular ReLU
- Keeps most of ReLU's benefits (no saturation on the positive side, fast gradient flow)

## Limitations
- The slope α is usually a fixed hyperparameter you pick beforehand — it's not learned, so it might not be optimal for every problem
- Results are inconsistent — sometimes it helps meaningfully, sometimes it's basically the same as regular ReLU
- Introduces one more hyperparameter to tune

## Leaky ReLU vs Regular ReLU

| Aspect | ReLU | Leaky ReLU |
|---|---|---|
| Negative input output | 0 | Small negative value (αx) |
| Dying neuron problem | Yes, common | Reduced |
| Gradient for x < 0 | 0 | α (small, nonzero) |
| Extra hyperparameter | No | Yes (α) |
| Compute cost | Very low | Very low |

## Related Variant
- **Parametric ReLU (PReLU)** — same idea, but instead of fixing α ahead of time, the network learns the best value of α during training.

## Code Reference

**Python (from scratch):**
```python
import numpy as np

def leaky_relu(x, alpha=0.01):
    return np.where(x > 0, x, alpha * x)

def leaky_relu_derivative(x, alpha=0.01):
    return np.where(x > 0, 1, alpha)
```

**PyTorch:**
```python
import torch
leaky_relu_activation = torch.nn.LeakyReLU(negative_slope=0.01)
output = leaky_relu_activation(x)
```

**TensorFlow/Keras:**
```python
import tensorflow as tf
layer = tf.keras.layers.LeakyReLU(alpha=0.01)
```