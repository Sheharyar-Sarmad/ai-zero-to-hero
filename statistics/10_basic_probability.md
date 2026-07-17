# Probability for Inferential Stats (Crash Notes)

## 1. Probability Basics
- **P(E)** = favorable / total
- Range: **0 to 1** (0 = impossible, 1 = certain)
- **P(A')** = 1 - P(A)

### Key Rules
- **Addition**: P(A∪B) = P(A) + P(B) - P(A∩B)
- **Multiplication (Independent)**: P(A∩B) = P(A) × P(B)
- **Conditional**: P(A|B) = P(A∩B) / P(B)
- **Bayes**: P(B|A) = P(A|B)·P(B) / P(A)

---

## 2. Key Distributions

| Distribution | When to Use |
|--------------|-------------|
| **Z (Normal)** | Known σ, large samples (n≥30) |
| **t** | Unknown σ, small samples |
| **χ²** | Variance, goodness-of-fit |
| **F** | Comparing 2 variances, ANOVA |

### Normal (Z) Properties
- Bell-shaped, symmetric
- Mean=0, SD=1
- **68-95-99.7 Rule**: 1σ, 2σ, 3σ

---

## 3. Probability → Inferential Stats (THE LINK)

| Concept | Role of Probability |
|---------|---------------------|
| **CLT** | Sample means → Normal (regardless of population) |
| **Standard Error** | SE = σ/√n (built on probability theory) |
| **Confidence Interval** | x̄ ± z·SE → z comes from probability distribution |
| **p-value** | P(data \| H₀ is true) → probability |
| **α (Type I Error)** | P(reject H₀ \| H₀ true) |
| **β (Type II Error)** | P(fail to reject H₀ \| H₀ false) |
| **Power (1-β)** | P(correctly reject H₀) |

# Likelihood - Quick Notes

## 1. Definition

**Likelihood** = How **plausible** a parameter value is, given the observed data.
