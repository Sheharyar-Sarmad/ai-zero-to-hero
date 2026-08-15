


# Overfitting & Underfitting - Linear Regression

## 1. Basic Concepts

### Linear Regression
y = β₀ + β₁x₁ + β₂x₂ + ... + βₙxₙ

text

### Bias-Variance Tradeoff
Total Error = Bias² + Variance + Irreducible Error

text

---

## 2. Underfitting

**Model too simple → Fails to learn patterns**

| Aspect | Description |
|--------|-------------|
| **Symptoms** | High train error, High test error |
| **Bias** | High |
| **Variance** | Low |
| **Causes** | Too few features, too simple model, over-regularization |

**Fixes:**
- Add polynomial features
- Increase model complexity
- Decrease regularization (λ)
- Add more relevant features
- Train longer

---

## 3. Overfitting

**Model too complex → Learns noise, fails to generalize**

| Aspect | Description |
|--------|-------------|
| **Symptoms** | Very low train error, High test error |
| **Bias** | Low |
| **Variance** | High |
| **Causes** | Too many features, insufficient data, complex model |

**Fixes:**
- Regularization (L1/L2)
- Reduce model complexity
- Increase training data
- Feature selection
- Cross-validation
- Early stopping

---

## 4. Regularization Techniques

### Ridge (L2)
Cost = MSE + α∑βᵢ²

text
- Shrinks coefficients
- Keeps all features

### Lasso (L1)
Cost = MSE + α∑|βᵢ|

text
- Feature selection
- Can zero out coefficients

### Elastic Net
Cost = MSE + α(ρ∑|βᵢ| + (1-ρ)∑βᵢ²)

text
- Combination of L1 + L2

---

## 5. Quick Diagnosis

| Metric | Underfitting | Overfitting | Good Fit |
|--------|--------------|-------------|----------|
| Train Error | High | Very Low | Low |
| Test Error | High | High | Low |
| Error Gap | Small | Large | Small |

**Learning Curves:**
- Underfit: Both curves converge high
- Overfit: Large gap between curves
- Good fit: Both converge low
