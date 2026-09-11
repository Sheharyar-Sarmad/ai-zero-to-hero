


# CNN Layers

---

## 1. Convolutional Layer

The core building block. A small filter (kernel) slides across the input and computes dot products.

**Key params:** filter size (3×3, 5×5), number of filters, stride, padding

```
Input → [filter slides] → Feature Map
```

- Each filter learns one pattern (edge, curve, texture)
- Multiple filters → multiple feature maps (channels)
- **Weight sharing:** same filter reused across all positions
- Output size = (Input − Filter + 2×Padding) / Stride + 1

---

## 2. Activation Layer (ReLU)

Applied right after convolution. Adds non-linearity.

```
ReLU(x) = max(0, x)
```

- Kills negative values (sets to 0), keeps positives
- Without this, stacked convolutions collapse to one linear operation
- Variants: Leaky ReLU, ELU, GELU — but ReLU is the default

---

## 3. Pooling Layer

Down-samples feature maps. Reduces spatial size, keeps dominant signals.

**Max Pooling (most common):**
```
[9  3]  → 2×2 Max Pool → [9]
[1  7]
```

**Average Pooling:** takes mean instead of max (used in modern architectures like ResNet at the end)

- Reduces computation in subsequent layers
- Provides mild translation invariance
- Typical: 2×2 window, stride 2 → halves spatial dimensions

---

## 4. Batch Normalization Layer

Normalizes the output of a layer across the batch before passing to the next layer.

```
x̂ = (x − μ_batch) / σ_batch
```

- Stabilizes training, allows higher learning rates
- Reduces sensitivity to weight initialization
- Acts as mild regularization
- Usually placed **after Conv, before ReLU** (though order varies)

---

## 5. Dropout Layer

Randomly zeros out a fraction of neurons during training.

```
p = 0.5 → 50% of activations set to 0 each forward pass
```

- Prevents co-adaptation (neurons relying on each other)
- Forces redundant feature learning → better generalization
- Only active during training; disabled at inference
- Typically applied in fully connected layers, less common after Conv

---

## 6. Flatten Layer

Converts the 3D feature map volume into a 1D vector for the dense layers.

```
Feature maps (7 × 7 × 512) → Flatten → (25,088 values)
```

No learnable parameters. Just a reshape operation.

---

## 7. Fully Connected (Dense) Layer

Every neuron connects to every input. Combines all learned spatial features for final prediction.

```
output = activation(W · x + b)
```

- Typically 1–3 dense layers at the end
- High parameter count — often the largest block in older nets
- Modern architectures replace with Global Average Pooling to reduce params

---

## 8. Global Average Pooling (GAP) Layer

Alternative to Flatten + Dense. Averages each entire feature map into a single value.

```
Feature map (7 × 7 × 512) → GAP → (512 values)
```

- Drastically fewer parameters than Flatten + Dense
- More regularization, less overfitting
- Used in ResNet, MobileNet, EfficientNet

---

## 9. Output Layer

Final layer that produces predictions.

```
Softmax  → multi-class probabilities  (sum to 1)
Sigmoid  → binary / multi-label
Linear   → regression
```

Number of neurons = number of classes (or outputs).

---

## Layer Order Summary

```
Input
  ↓
[Conv → BatchNorm → ReLU] × N     ← Feature extraction block
  ↓
[Pool]                             ← Spatial reduction (repeated)
  ↓
[Conv → BatchNorm → ReLU] × N
  ↓
[Global Avg Pool / Flatten]        ← Transition to dense
  ↓
[Dense → Dropout] × 1–2            ← Classification head
  ↓
[Output + Softmax]
```

---

## Quick Reference Table

| Layer | Learnable Params | Purpose |
|---|---|---|
| Convolutional | Yes (filters, bias) | Extract spatial features |
| ReLU | No | Non-linearity |
| Pooling | No | Down-sample |
| Batch Norm | Yes (γ, β) | Stabilize training |
| Dropout | No | Regularize |
| Flatten | No | Reshape |
| Dense | Yes (weights, bias) | Combine features |
| GAP | No | Compact transition |
| Output | Yes (weights, bias) | Predict |

---

## What Each Block "Sees"

```
Early layers  →  Edges, gradients, colors
Mid layers    →  Textures, shapes, corners
Deep layers   →  Parts (eyes, wheels), abstract patterns
Output head   →  "Is this a cat?" → class decision
```