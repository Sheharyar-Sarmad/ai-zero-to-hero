



# 📉 Dimensionality Reduction - Complete Notes

## 🌀 Curse of Dimensionality

### What is it?

As the number of features (dimensions) increases, the data becomes sparse and harder to analyze.

### Why it's bad:

- **Data becomes sparse** → Need exponentially more samples
- **Distance metrics fail** → All points become equidistant
- **Overfitting** → Models learn noise instead of patterns
- **Computational cost** → More dimensions = more computation
- **Visualization** → Impossible to visualize beyond 3D

### Why we don't need high dimensions:

- Many features are redundant or correlated
- Only few features actually contribute to the pattern
- Signal-to-noise ratio decreases with more features

---

## 🎯 Feature Selection vs Feature Extraction

### Feature Selection

> **"Choose the best subset of original features"**

| Aspect | Details |
|---|---|
| **What** | Selects subset of existing features |
| **How** | Filter, Wrapper, Embedded methods |
| **Result** | Original features, just fewer |
| **Interpretability** | ✅ High (features remain same) |
| **Example** | Select 3 best features out of 20 |

### Methods:

- **Filter:** Statistical measures (correlation, chi-square)
- **Wrapper:** Forward/Backward selection
- **Embedded:** Lasso, Decision Tree importance

### Feature Extraction

> **"Create new features from combinations of originals"**

| Aspect | Details |
|---|---|
| **What** | Creates new composite features |
| **How** | Transformation (linear/non-linear) |
| **Result** | New features, different from originals |
| **Interpretability** | ⚠️ Lower (features are transformed) |
| **Example** | PCA creates principal components |

---

## 🔬 PCA (Principal Component Analysis) - Simplified

### Core Idea

Find directions (principal components) that capture maximum variance in data.

### Step-by-Step Intuition:

1. Find direction of maximum variance → **PC1**
2. Find perpendicular direction with next max variance → **PC2**
3. Continue → **PC3, PC4, ..., PCn**

### Key Points:

- 📌 PCA is **UNSUPERVISED learning**
- 📌 Works best when features are on same scale
- 📌 Preserves maximum variance in fewer dimensions
- 📌 Reduces data while keeping important patterns

---

## Why We Lose Variance When Merging Two Features (X₁, X₂)

### Original variance:

```python
# Original variance
Var(X₁) + Var(X₂) = 100%

# After averaging (naive merge)
Var((X₁ + X₂)/2) < Var(X₁) + Var(X₂)

# You lose the unique variance of each feature

### Why?

- When you merge two features, you average out their differences
- The unique information in each feature gets diluted
- PCA preserves maximum variance by finding optimal combination

---

## 🧮 Eigen Decomposition - Simply Explained

### What is Eigen Decomposition?

Breaking down a matrix into its eigenvectors (directions) and eigenvalues (importance).

### In PCA Context:

```text
Covariance Matrix (Σ) → Eigen Decomposition
           ↓
    ┌──────────────┐
    │ Eigenvectors │ = Principal Components (directions)
    │ Eigenvalues  │ = Variance explained (importance)
    └──────────────┘

## One Liner Defination: 

**Dimensionality reduction is about finding the right balance between complexity and performance. PCA finds the sweet spot by creating new features that capture the essence of your data while discarding the noise.**