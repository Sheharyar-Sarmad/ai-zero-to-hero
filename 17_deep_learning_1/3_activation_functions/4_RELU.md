

# ReLU (Rectified Linear Unit) Activation Function

## Definition
f(x) = max(0, x)

In plain words: if the input is positive, pass it through unchanged. If it's negative, just kill it to zero.

## Key Properties
- Output range: [0, ∞)
- Not smooth — has a sharp corner at x = 0
- Derivative: 1 for x > 0, 0 for x < 0, undefined at x = 0 (usually just set to 0 or 1 in practice)

## Use Cases
- Default choice for hidden layers in most deep networks (CNNs, feedforward nets, etc.)
- Basically the standard unless there's a specific reason to use something else

## Why It Took Over From Sigmoid/Tanh

Sigmoid and tanh both saturate — meaning once the input gets large in either direction, the curve flattens out and the gradient shrinks to almost nothing. Stack enough layers together and gradients vanish completely by the time they reach the earlier layers. Training basically grinds to a halt.

ReLU sidesteps this on the positive side. For any positive input, the gradient is just 1, flat out, no matter how large the input gets. No squashing, no shrinking gradient. This is the main reason deep networks became practical to train — ReLU lets gradients flow through many layers without dying.

It's also just cheap. No exponentials to compute, just a comparison against zero. That adds up when you're doing this across millions of neurons.

## The Catch: Dying ReLU

Here's the tradeoff — for any negative input, the output is 0, and so is the gradient. If a neuron gets stuck outputting negative values for its inputs, it stops learning entirely, because there's no gradient to update it. Multiply this across a big network and you can end up with a chunk of neurons that are just permanently "dead," contributing nothing.

This is why variants exist:
- **Leaky ReLU**: allows a small negative slope instead of a hard zero (f(x) = x if x>0, else 0.01x)
- **Parametric ReLU (PReLU)**: same idea, but the slope is learned instead of fixed
- **ELU / GELU**: smoother alternatives that also try to fix the dying neuron problem

## Quick Comparison

| Aspect | Sigmoid | Tanh | ReLU |
|---|---|---|---|
| Output range | (0, 1) | (-1, 1) | [0, ∞) |
| Zero-centered | No | Yes | No |
| Saturates | Both sides | Both sides | Only negative side |
| Vanishing gradient | Severe | Still there | Mostly avoided (positive side) |
| Compute cost | High (exp) | High (exp) | Very low |
| Main weakness | Slow learning | Slow learning at extremes | Dying neurons |

## Code Reference

**Python (from scratch):**
```python
import numpy as np

def relu(x):
    return np.maximum(0, x)

def relu_derivative(x):
    return np.where(x > 0, 1, 0)
```

**PyTorch:**
```python
import torch
relu_activation = torch.nn.ReLU()
output = relu_activation(x)
```

**TensorFlow/Keras:**
```python
import tensorflow as tf
layer = tf.keras.layers.Dense(units=64, activation='relu')
```