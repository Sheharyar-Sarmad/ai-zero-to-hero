# Tanh (Hyperbolic Tangent) Activation Function

## Definition
f(x) = tanh(x) = (e^x − e^(-x)) / (e^x + e^(-x))

Also can be written in terms of sigmoid:
f(x) = 2 · sigmoid(2x) − 1

## Key Properties
- Output range: (-1, 1)
- S-shaped curve, similar to sigmoid but stretched and shifted
- Zero-centered (outputs can be negative, positive, or zero)
- Derivative: f'(x) = 1 − f(x)²

## Use Cases
- Hidden layers (historically preferred over sigmoid)
- RNNs/LSTMs (often used for cell/hidden state activations)
- Tasks where negative outputs are meaningful

## Advantages
- Zero-centered output → better gradient flow than sigmoid
- Stronger gradients near zero than sigmoid (steeper curve)
- Still smooth and differentiable everywhere

## Limitations
- Still suffers from **vanishing gradient** for large |x| (saturates at -1 and 1)
- Computationally more expensive than ReLU

## Why Tanh is Better Than Sigmoid

| Aspect | Sigmoid | Tanh |
|---|---|---|
| Output range | (0, 1) | (-1, 1) |
| Zero-centered | **No** — always positive | **Yes** — centered at 0 |
| Gradient strength at 0 | 0.25 (max) | 1.0 (max) |
| Convergence speed | Slower | Generally faster |
| Vanishing gradient | Yes | Yes (still occurs at extremes) |

## Why Tanh Actually Wins Over Sigmoid (Explained Simply)

The core problem with sigmoid: it squashes everything into (0, 1) — always positive. So when gradients flow backward through the network, they all push the weights in the same direction (either all up or all down) for a given neuron. This makes learning zig-zag around instead of taking a direct path, which just slows things down.

Tanh fixes half of this: it squashes things into (-1, 1) instead. Now outputs can be negative too, so the gradient updates aren't all forced in one direction. Training tends to move more smoothly and converge faster as a result.

The other reason tanh wins: look at how steep each curve is right around zero. Sigmoid's steepest slope is only 0.25. Tanh's steepest slope is 1.0 — four times steeper. In practice that means when your inputs are near zero (which they often are, especially early in training), tanh gives you a stronger, more useful gradient signal, so weights update more meaningfully instead of barely budging.

So basically: same S-shape, same general vibe, but tanh is centered and steeper — two things that make the network learn faster and with less wasted motion.

**Honest caveat:** tanh still isn't perfect. Once inputs get large (very positive or very negative), it flattens out just like sigmoid, and gradients basically die there too. That's the whole reason ReLU took over as the go-to for hidden layers in modern deep nets — it doesn't saturate on the positive side at all.

## Code Reference

**Python (from scratch):**
```python
import numpy as np

def tanh(x):
    return np.tanh(x)

def tanh_derivative(x):
    return 1 - np.tanh(x)**2
```

**PyTorch:**
```python
import torch
tanh_activation = torch.nn.Tanh()
output = tanh_activation(x)
```

**TensorFlow/Keras:**
```python
import tensorflow as tf
layer = tf.keras.layers.Dense(units=1, activation='tanh')
```