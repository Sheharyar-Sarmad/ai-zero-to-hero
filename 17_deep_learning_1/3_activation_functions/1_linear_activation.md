

# Linear Activation Function

## Definition
f(x) = x  (or f(x) = a·x, where `a` is a constant)

## Key Properties
- Output is directly proportional to input
- Range: (-∞, ∞)
- Derivative is constant: f'(x) = a (or 1)
- Graph: a straight line through the origin

## Use Cases
- Output layer of regression models (predicting continuous values)
- Rarely used in hidden layers

## Advantages
- Simple, computationally cheap
- No vanishing gradient (constant derivative)
- Good for continuous output problems

## Major Limitation
- **No non-linearity** → stacking multiple linear layers collapses into a single linear transformation, regardless of depth
- Network can't learn complex or non-linear patterns
- This is why it's avoided in hidden layers of deep networks

## Comparison: Linear vs Non-linear

| Aspect | Linear | Non-linear (e.g., ReLU, Sigmoid) |
|---|---|---|
| Hidden layers | Not useful | Essential |
| Output layer (regression) | Common | — |
| Gradient | Constant | Varies |
| Can model complex patterns | No | Yes |

## Code Reference

**Python (from scratch):**
```python
def linear(x, a=1):
    return a * x

def linear_derivative(x, a=1):
    return a
```

**PyTorch:**
```python
import torch
linear_activation = torch.nn.Identity()
output = linear_activation(x)
```

**TensorFlow/Keras:**
```python
import tensorflow as tf
layer = tf.keras.layers.Dense(units=1, activation='linear')
```