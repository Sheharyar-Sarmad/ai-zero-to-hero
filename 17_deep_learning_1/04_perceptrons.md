

# Perceptrons - The Building Block of Neural Networks

## What is a Perceptron?

A **Perceptron** is the simplest type of artificial neural network. It is a building block of deep learning. Think of it as a **single brain cell** that makes a decision.

---

## The Core Formula

The perceptron takes multiple inputs, multiplies each with a weight, adds them up, adds a bias, and passes through an activation function.

Output = Activation( x₁×w₁ + x₂×w₂ + x₃×w₃ + ... + xₙ×wₙ + bias )

**In Simple Math:**

z = x₁·w₁ + x₂·w₂ + x₃·w₃ + ... + xₙ·wₙ + b
Output = f(z) (where f is activation function)

---

## Breaking Down Each Component

| Component | Symbol | Meaning | Analogy |
|-----------|--------|---------|---------|
| **Inputs** | x₁, x₂, x₃,... | The data we feed in | Like ingredients for a recipe |
| **Weights** | w₁, w₂, w₃,... | Importance of each input | Like how much each ingredient matters |
| **Bias** | b (or θ₀) | A threshold to shift decision | Like a minimum passing score |
| **Sum** | z (or net) | Weighted sum of all inputs | Like total score before deciding |
| **Activation** | f(z) | Decision maker | Like a teacher grading pass/fail |

---

## Understanding the Screenshot

In your image:

x₁ ----w₁----
x₂ ----w₂----+----Σ---- Activation ---- Output
x₃ ----w₃----/
↑
bias (b)

**What's happening:**
1. **Inputs (x₁, x₂, x₃)** → The features/data
2. **Weights (w₁, w₂, w₃)** → Each input has a weight
3. **Sum (Σ)** → All values are added together
4. **Bias (b)** → Added to the sum to shift threshold
5. **Activation** → Decides final output (0 or 1)

---

## How Weights are Selected

**Initially:** Random numbers (e.g., 0.2, -0.5, 0.8)

**During Training:** The model **adjusts** weights to minimize errors.

Start with random weights

Calculate prediction

Measure error (how wrong it is)

Update weights to reduce error

Repeat until error is small

Weight Update Rule:
w_new = w_old + learning_rate × error × input


**Analogy:** Like adjusting a volume knob until the sound is perfect.

---

## What is Bias in Output?

> **Bias** is an extra parameter that shifts the activation function left or right.

**Why we need bias:**
- Without bias, the perceptron can only make decisions that pass through the origin (0,0)
- Bias allows the decision boundary to shift anywhere

**Analogy:**
Think of a passing grade:

Without bias:  60% = Pass (fixed)
With bias:     Can be 50% or 70% (adjustable threshold)

**Formula with Bias:**

z = (x₁×w₁ + x₂×w₂ + x₃×w₃) + bias
↑ ↑
Weighted sum Shift threshold

---

## Same Pattern, Different Notation

You might see the same formula written differently. They mean the **same thing**!

| Formula | Same As |
|---------|---------|
| **z = x₁×w₁ + x₂×w₂ + x₃×w₃ + bias** | Same |
| **z = θ₁×x₁ + θ₂×x₂ + θ₃×x₃ + θ₀** | Same! |

**Both formulas:**
- Multiply inputs with weights (or θs)
- Add them up
- Add a constant (bias or θ₀)

> The notation might change, but the **concept is identical!**

---

## The Final Output: 0 or 1

**Why?** Perceptrons are used for **binary classification** (yes/no, true/false, cat/dog).

**How:**

If z > threshold (0): Output = 1 (Fire!)
If z ≤ threshold (0): Output = 0 (Don't fire!)


**In Code:**
```python
# Step function (threshold activation)
def activation(z):
    if z > 0:
        return 1
    else:
        return 0
```