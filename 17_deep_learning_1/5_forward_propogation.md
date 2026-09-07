

# Forward Propagation 

---

## What is Forward Propagation?

> Forward propagation is the process of passing input data through a neural network from the input layer to the output layer. It's how the network makes predictions.

---

## What Are Hidden Layers?

> **Hidden layers** are layers of neurons between the input and output layers. They are called "hidden" because they are not directly visible from the outside.

| Aspect | Explanation |
|--------|-------------|
| **Position** | Between input and output layers |
| **Function** | Learn complex patterns and features |
| **Depth** | Multiple hidden layers = Deep Learning |
| **Name** | "Hidden" because we don't see their outputs |

**Visual:**

Input → Hidden Layer 1 → Hidden Layer 2 → Output Layer
│ │ │ │
│ ┌──────────┐ ┌──────────┐ │
├────┤ Neuron ├────┤ Neuron ├─────────┤
│ ├──────────┤ ├──────────┤ │
├────┤ Neuron ├────┤ Neuron ├─────────┤
│ ├──────────┤ ├──────────┤ │
├────┤ Neuron ├────┤ Neuron ├─────────┤
│ └──────────┘ └──────────┘ │

---

## The Forward Propagation Process

### Step-by-Step Flow:

Step 1: Input Data → Input Layer
Step 2: Input → Hidden Layer 1 (Weighted sum + Activation)
Step 3: Hidden Layer 1 → Hidden Layer 2 (Weighted sum + Activation)
Step 4: Hidden Layer 2 → Output Layer (Weighted sum + Activation)
Step 5: Output = Prediction

### Mathematical Flow:

Layer 1: z₁ = x × W₁ + b₁ → a₁ = f(z₁)
Layer 2: z₂ = a₁ × W₂ + b₂ → a₂ = f(z₂)

Output: z₃ = a₂ × W₃ + b₃ → Output = f(z₃)

---

## Key Concepts in Forward Propagation

### 1. Weighted 

z = (x₁ × w₁) + (x₂ × w₂) + ... + (xₙ × wₙ) + b

Each input is multiplied by its weight and summed together with bias.

### 2. Activation Function

a = f(z)

The activation function introduces non-linearity, allowing the network to learn complex patterns.

### 3. Layer Output

Each layer's output becomes the input for the next layer
Input → Layer 1 → Layer 2 → Layer 3 → Output

### 4. Batch Processing

Multiple samples processed simultaneously using matrix multiplication
X × W + b

---

## Why Hidden Layers Matter?

| Shallow Network | Deep Network |
|-----------------|--------------|
| One hidden layer | Multiple hidden layers |
| Limited learning capacity | High learning capacity |
| Simple patterns | Complex patterns |
| Fast training | Slow training |

**More hidden layers = More complex patterns the network can learn!**

---

## Activation Functions Used

| Function | Formula | Output Range |
|----------|---------|--------------|
| **Sigmoid** | 1/(1+e⁻ᶻ) | (0, 1) |
| **Tanh** | (eᶻ - e⁻ᶻ)/(eᶻ + e⁻ᶻ) | (-1, 1) |
| **ReLU** | max(0, z) | [0, ∞) |
| **Softmax** | eᶻ/Σeᶻ | (0, 1) |

---

## Forward Propagation vs Backpropagation

| Forward Propagation | Backpropagation |
|---------------------|-----------------|
| **Forward** direction (input → output) | **Backward** direction (output → input) |
| **Makes** predictions | **Updates** weights |
| First step | Second step |
| Uses current weights | Uses gradients |

---

## Why Is It Called "Forward"?

> Because data flows in the **forward direction**:
> 
> Input → Layer 1 → Layer 2 → ... → Output

---

## Summary

| Concept | Explanation |
|---------|-------------|
| **Forward Propagation** | Passing data through the network |
| **Hidden Layers** | Layers between input and output |
| **Weights & Biases** | Parameters that transform data |
| **Activation Functions** | Add non-linearity to the network |

---

## Key Takeaway

> Forward propagation is how neural networks make predictions by passing data through multiple layers, where each layer applies a weighted sum and activation function before passing to the next.

---

**Forward Propagation = Data flowing forward through the network to make a prediction.**