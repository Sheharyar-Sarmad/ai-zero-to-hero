
# Sigmoid Activation Function

## Definition
f(x) = 1 / (1 + e^(-x))

## Key Properties
- Output range: (0, 1)
- S-shaped ("sigmoid") curve
- Smooth and differentiable everywhere
- Derivative: f'(x) = f(x) · (1 − f(x))

## Use Cases
- Output layer for binary classification (interpreted as probability)
- Gates in LSTM/GRU units
- Historically used in hidden layers (less common now)

## Advantages
- Smooth gradient, no jumps in output values
- Output bounded between 0 and 1 → useful for probability
- Clear predictions (values push toward 0 or 1 for large |x|)

## Major Limitations
- **Vanishing gradient**: for large positive/negative x, gradient ≈ 0 → slows/stops learning in deep networks
- **Not zero-centered**: outputs always positive → can cause zig-zagging gradient updates
- Computationally more expensive than ReLU (involves exponential)

## Comparison: Sigmoid vs ReLU

| Aspect | Sigmoid | ReLU |
|---|---|---|
| Output range | (0, 1) | [0, ∞) |
| Vanishing gradient | Yes (severe) | Less (for x>0) |
| Zero-centered | No | No |
| Common use | Output layer (binary) | Hidden layers |
| Computation cost | Higher (exp) | Very low |

## Code Reference

**Python (from scratch):**
```python
import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    s = sigmoid(x)
    return s * (1 - s)
```

**PyTorch:**
```python
import torch
sigmoid_activation = torch.nn.Sigmoid()
output = sigmoid_activation(x)
```

**TensorFlow/Keras:**
```python
import tensorflow as tf
layer = tf.keras.layers.Dense(units=1, activation='sigmoid')
```