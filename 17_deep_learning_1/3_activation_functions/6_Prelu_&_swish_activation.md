

# PReLU and Swish Activation Functions

---

## PReLU (Parametric ReLU)

### Definition
f(x) = x, if x > 0
f(x) = αx, if x ≤ 0   (same as Leaky ReLU, except α is **learned**, not fixed)

### The Idea
Leaky ReLU picks a small slope like 0.01 for negative inputs and just sticks with it for the whole network. But why should that number be the same for every neuron, in every layer, for every dataset? PReLU says: let the network figure out its own best slope during training, just like it learns weights.

So α becomes a trainable parameter — either one shared value, or sometimes a separate value per channel/neuron for more flexibility.

### Advantages
- More flexible than Leaky ReLU — the network adapts the slope to whatever actually helps
- Usually performs at least as well as, and sometimes better than, Leaky ReLU
- Still cheap-ish to compute, only a few extra learnable parameters

### Limitations
- Extra parameters means slightly more risk of overfitting, especially on smaller datasets
- More moving parts to tune/monitor during training
- Gains over Leaky ReLU aren't always huge — depends on the problem

### Code Reference

**PyTorch:**
```python
import torch
prelu_activation = torch.nn.PReLU()
output = prelu_activation(x)
```

**TensorFlow/Keras:**
```python
import tensorflow as tf
layer = tf.keras.layers.PReLU()
```

---

## Swish

### Definition
f(x) = x · sigmoid(x) = x / (1 + e^(-x))

### The Idea
Swish came out of Google research, basically from experimenting with different activation shapes and seeing what trained best. It looks kind of like ReLU but instead of a sharp corner at zero, it's smooth, and it dips slightly below zero for small negative inputs before coming back up.

That small negative dip is actually the interesting part — unlike ReLU, Swish doesn't just kill negative inputs outright. A small negative value can still pass through, which seems to help gradient flow and lets the network express more complex functions.

### Key Properties
- Output range: roughly (-0.28, ∞) — not bounded below at exactly 0 like ReLU
- Smooth everywhere (no sharp corner), which makes optimization a bit nicer
- Self-gated — the sigmoid part acts like a gate controlling how much of x passes through

### Advantages
- Smooth curve helps with gradient-based optimization
- Non-monotonic dip near zero seems to help deeper networks learn richer representations
- Tends to outperform ReLU on deeper networks in practice (shown in the original Swish paper on image classification tasks)

### Limitations
- More expensive to compute than ReLU (involves a sigmoid/exponential)
- Improvement over ReLU isn't guaranteed for every task — sometimes the gain is small
- Behaves less predictably than ReLU since it's not just a simple max operation

### Swish vs ReLU vs PReLU

| Aspect | ReLU | PReLU | Swish |
|---|---|---|---|
| Smooth curve | No (sharp corner) | No | Yes |
| Negative values allowed | No (hard 0) | Yes (learned slope) | Yes (small dip) |
| Learnable parameters | None | Yes (α) | None (in basic form) |
| Compute cost | Very low | Very low | Higher (sigmoid) |
| Common use | Default hidden layers | Alternative to Leaky ReLU | Deeper nets, some modern architectures (e.g. EfficientNet) |

### Code Reference

**Python (from scratch):**
```python
import numpy as np

def swish(x):
    return x * (1 / (1 + np.exp(-x)))
```

**PyTorch:**
```python
import torch
swish_activation = torch.nn.SiLU()  # SiLU = Swish with beta=1
output = swish_activation(x)
```

**TensorFlow/Keras:**
```python
import tensorflow as tf
layer = tf.keras.layers.Dense(units=64, activation='swish')
```