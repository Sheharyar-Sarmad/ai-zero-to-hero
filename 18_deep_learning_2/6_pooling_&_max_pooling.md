

# Pooling and Max Pooling

## What is Pooling?

**Pooling** is a downsampling operation that reduces feature map size while preserving important information. It divides the input into small windows and extracts one representative value from each.

---

## Why Use Pooling?

- Reduces computation and memory
- Reduces overfitting
- Makes features robust to small input variations
- Faster training

---

## Max Pooling

**Definition:** Takes the maximum value from each window (typically 2×2).

### Example:
```
Input (4×4):           Output (2×2):
[1  3  2  4]           [5  4]
[5  2  1  2]    →      [8  6]
[6  1  2  3]
[7  8  4  6]
```

**Steps:**
1. Define pool size (usually 2×2) and stride (usually 2)
2. Slide window across feature map
3. Extract maximum value from each window
4. Output smaller feature map (~50% reduction)

---

## Types of Pooling

| Type | Operation | Use Case |
|------|-----------|----------|
| **Max Pooling** | Takes maximum | Most common, edge detection |
| **Average Pooling** | Takes average | Smooth information, noise reduction |
| **Min Pooling** | Takes minimum | Specialized cases |
| **Stochastic** | Random selection | Regularization |

---

## Quick Example

```python
from tensorflow.keras.layers import MaxPooling2D

# Create max pooling layer
pool = MaxPooling2D(pool_size=(2, 2), stride=2)

# Input: (4, 4) → Output: (2, 2)
```

---

## Key Points

✅ Reduces feature map size while keeping important features  
✅ Typical settings: 2×2 pool, stride=2  
✅ Used after convolutional layers  
✅ Improves generalization and training speed  
✅ Best for image classification, object detection  

---

## Summary Table

| Aspect | Value |
|--------|-------|
| Purpose | Downsampling |
| Method | Select max from window |
| Pool Size | 2×2 or 3×3 |
| Stride | Equal to pool size |
| Reduces | Computation, overfitting |
| Framework | Keras, PyTorch, TensorFlow |