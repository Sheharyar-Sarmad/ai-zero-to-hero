# Hypothesis Testing

## Definition

**Hypothesis Testing** is a statistical method used to determine whether there is enough evidence from a **sample** to support or reject a claim about a **population**.

> **Simple Definition:**  
> Hypothesis testing helps us decide whether a claim about a population is likely to be true based on sample data.

---

# Why Do We Need Hypothesis Testing?

In real life, it is often impossible or expensive to collect data from an entire population. Instead, we collect a sample and use statistical methods to make decisions about the population.

### Examples

- Does a new medicine work better than the old one?
- Has the average salary increased this year?
- Does a new teaching method improve student performance?
- Is a manufacturing machine producing defective products?

---

# Basic Terminology

## Population

The entire group of individuals or items you want to study.

### Examples

- All students in a university
- All voters in a country
- Every smartphone manufactured in a factory

---

## Sample

A subset of the population selected for analysis.

### Examples

- 100 students selected from a university
- 500 voters surveyed
- 50 smartphones tested for quality

---

# What is a Hypothesis?

A **hypothesis** is a statement or claim about a population parameter.

There are two hypotheses in every hypothesis test.

---

# Null Hypothesis (H₀)

The **Null Hypothesis (H₀)** is the default assumption that there is **no effect**, **no difference**, or **no relationship**.

It is assumed to be true unless sufficient evidence suggests otherwise.

### Examples

```
H₀: μ = 70
```

The average exam score is 70.

```
H₀: The new medicine is not more effective than the old medicine.
```

```
H₀: There is no relationship between exercise and weight loss.
```

---

# Alternative Hypothesis (H₁ or Hₐ)

The **Alternative Hypothesis (H₁)** states that there **is an effect**, **difference**, or **relationship**.

This is the claim that the researcher wants to support.

### Examples

```
H₁: μ ≠ 70
```

The average score is not 70.

```
H₁: The new medicine is more effective.
```

```
H₁: Exercise affects weight loss.
```

---

# Types of Alternative Hypotheses

## Two-Tailed Test

Tests whether a value is different.

```
H₀: μ = 100

H₁: μ ≠ 100
```

Used when you only want to know if a difference exists.

---

## Left-Tailed Test

Tests whether the population value is smaller.

```
H₀: μ = 100

H₁: μ < 100
```

---

## Right-Tailed Test

Tests whether the population value is larger.

```
H₀: μ = 100

H₁: μ > 100
```

---

# Significance Level (α)

The **significance level**, denoted by **α (alpha)**, is the probability of rejecting the null hypothesis when it is actually true.

Common values are:

```
0.05
0.01
0.10
```

Most statistical tests use:

```
α = 0.05
```

This means there is a **5% risk of making a Type I Error**.

---

# Test Statistic

A **test statistic** is a numerical value calculated from the sample data that helps determine whether to reject the null hypothesis.

Common test statistics include:

- Z-Statistic
- t-Statistic
- Chi-Square Statistic (χ²)
- F-Statistic

---

# p-value

The **p-value** is the probability of obtaining results at least as extreme as the observed sample result, assuming the null hypothesis is true.

### Decision Rule

If

```
p-value ≤ α
```

Reject the Null Hypothesis.

If

```
p-value > α
```

Fail to Reject the Null Hypothesis.

> **Important:** "Fail to reject H₀" does **not** mean the null hypothesis has been proven true. It simply means there is not enough evidence against it.

---

# Steps of Hypothesis Testing

## Step 1

State the hypotheses.

```
H₀

H₁
```

---

## Step 2

Choose the significance level.

Usually

```
α = 0.05
```

---

## Step 3

Collect sample data.

Example

```
Sample Size = 100
```

---

## Step 4

Calculate the test statistic.

Examples

- Z-Test
- t-Test
- Chi-Square
- F-Test

---

## Step 5

Find the p-value.

---

## Step 6

Compare the p-value with α.

```
p ≤ α
```

Reject H₀.

```
p > α
```

Fail to Reject H₀.

---

# Decision Flow

```
Start
  │
  ▼
State H₀ and H₁
  │
  ▼
Choose α
  │
  ▼
Collect Sample
  │
  ▼
Calculate Test Statistic
  │
  ▼
Find p-value
  │
  ▼
Compare p-value with α
  │
  ├───────────────┐
  ▼               ▼
Reject H₀     Fail to Reject H₀
```

---

# Type I Error

## Definition

Rejecting the Null Hypothesis when it is actually true.

### Also Called

- False Positive

### Probability

```
α
```

### Example

A medical test says a healthy person has a disease.

---

# Type II Error

## Definition

Failing to Reject the Null Hypothesis when it is actually false.

### Also Called

- False Negative

### Probability

```
β
```

### Example

A medical test says a sick person is healthy.

---

# Power of a Test

The **Power of a Test** is the probability of correctly rejecting a false Null Hypothesis.

## Formula

```
Power = 1 − β
```

Higher power means a better statistical test.

---

# Common Hypothesis Tests

| Test | Used For |
|--------|-----------|
| Z-Test | Large sample size or known population standard deviation |
| t-Test | Small sample size and unknown population standard deviation |
| Chi-Square Test | Categorical data and independence |
| ANOVA | Comparing the means of three or more groups |
| F-Test | Comparing variances |

---

# Example

A company claims:

```
Average battery life = 10 hours
```

Take a sample of 80 batteries.

Suppose the calculated p-value is

```
0.03
```

Choose

```
α = 0.05
```

Since

```
0.03 < 0.05
```

Reject the Null Hypothesis.

### Conclusion

There is sufficient statistical evidence that the average battery life is different from 10 hours.

---

# Real-Life Applications

Hypothesis Testing is used in:

- Medical Research
- Machine Learning
- Artificial Intelligence
- Data Science
- Economics
- Manufacturing
- Business Analytics
- Marketing
- Finance
- Psychology
- Education

---

# Memory Trick

## H₀ (Null)

Think:

**No Change**

Keywords:

- No Difference
- No Effect
- No Relationship

---

## H₁ (Alternative)

Think:

**Something Changed**

Keywords:

- Difference
- Effect
- Relationship

---

# Quick Comparison

| Null Hypothesis (H₀) | Alternative Hypothesis (H₁) |
|-----------------------|-----------------------------|
| No Difference | Difference Exists |
| No Effect | Effect Exists |
| No Relationship | Relationship Exists |
| Default Assumption | Research Claim |

---

# Quick Summary

- Hypothesis Testing uses sample data to make decisions about a population.
- H₀ represents no effect or no difference.
- H₁ represents an effect or difference.
- The significance level (α) is commonly 0.05.
- If **p-value ≤ α**, reject H₀.
- If **p-value > α**, fail to reject H₀.
- Type I Error = Rejecting a true H₀.
- Type II Error = Failing to reject a false H₀.
- Power of a Test = **1 − β**.

---

# Exam Definition

> **Hypothesis Testing is a statistical procedure that uses sample data to determine whether there is sufficient evidence to reject a null hypothesis about a population parameter.**