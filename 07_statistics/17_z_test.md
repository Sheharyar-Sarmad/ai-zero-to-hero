# Z-Test Notes (Statistics)

> Complete Beginner-to-Advanced Notes for Statistics, Data Science, Machine Learning, and AI

---

# Table of Contents

1. Introduction
2. What is a Z-Test?
3. Why Do We Use a Z-Test?
4. When Should We Use a Z-Test?
5. Conditions for Using a Z-Test
6. Population vs Sample
7. Population Mean and Sample Mean
8. Population Standard Deviation
9. Null and Alternative Hypotheses
10. Types of Z-Tests
11. Z-Test Formula
12. Understanding Every Symbol
13. Standard Error
14. Steps of Performing a Z-Test
15. Decision Rule
16. Critical Value Method
17. P-value Method
18. One-Tailed vs Two-Tailed Tests
19. Z Critical Values
20. Complete Solved Example
21. Interpretation
22. Assumptions
23. Advantages
24. Limitations
25. Common Mistakes
26. Interview Questions
27. Summary

---

# 1. Introduction

A **Z-Test** is a statistical hypothesis test used to determine whether there is a significant difference between a sample statistic and a population parameter.

It helps answer questions like:

- Is the sample mean different from the population mean?
- Did a new process improve production?
- Is a medicine effective?
- Is a machine producing correct weights?

---

# 2. What is a Z-Test?

A Z-Test is a hypothesis test that uses the **Standard Normal Distribution (Z-distribution)**.

It converts the sample result into a **Z-score**, which tells us how many standard deviations the sample mean is from the population mean.

---

# 3. Why Do We Use a Z-Test?

We use a Z-Test to determine whether an observed difference is:

- Due to random chance
- OR statistically significant

---

# 4. When Should We Use a Z-Test?

Use a Z-Test when:

- Population standard deviation (σ) is known.
- Sample size is greater than or equal to 30.
- Sample is randomly selected.
- Observations are independent.
- Population is approximately normal (or sample size is large enough for the Central Limit Theorem).

---

# 5. Conditions for Using a Z-Test

✅ Population standard deviation is known

✅ Sample size ≥ 30

✅ Random sampling

✅ Independent observations

✅ Population approximately normal

---

# 6. Population vs Sample

Population

Entire group you want to study.

Example:

All students in a university.

Represented by:

μ (Population Mean)

σ (Population Standard Deviation)

---

Sample

A small portion of the population.

Represented by:

x̄ (Sample Mean)

s (Sample Standard Deviation)

n (Sample Size)

---

# 7. Population Mean vs Sample Mean

Population Mean

Symbol:

μ

True average of the entire population.

---

Sample Mean

Symbol:

x̄

Average calculated from the sample.

Formula

x̄ = Σx / n

---

# 8. Population Standard Deviation

Symbol

σ

Measures the spread of the population.

A Z-Test requires the population standard deviation to be known.

---

# 9. Hypotheses

## Null Hypothesis (H₀)

Represents no change or no difference.

Example

H₀ : μ = 100

---

## Alternative Hypothesis (H₁)

Represents a difference or change.

Examples

H₁ : μ ≠ 100

H₁ : μ > 100

H₁ : μ < 100

---

# 10. Types of Z-Tests

## One-Sample Z-Test

Compare one sample mean with a known population mean.

Example:

Is the average battery life 10 hours?

---

## Two-Sample Z-Test

Compare two population means.

Example:

Company A vs Company B.

---

## Z-Test for Population Proportion

Used to compare proportions.

Example:

Is the defect rate below 5%?

---

# 11. Z-Test Formula

Z = \frac{\bar{x} - \mu}{\sigma / \sqrt{n}}

---

# 12. Meaning of Symbols

| Symbol | Meaning |
|---------|----------|
| Z | Test Statistic |
| x̄ | Sample Mean |
| μ | Population Mean |
| σ | Population Standard Deviation |
| n | Sample Size |
| √n | Square Root of Sample Size |

---

# 13. Standard Error

Standard Error measures how much the sample mean varies from sample to sample.

Formula

SE = σ / √n

Smaller Standard Error means more reliable estimates.

---

# 14. Steps of Performing a Z-Test

### Step 1

State the hypotheses.

H₀

H₁

---

### Step 2

Choose significance level.

Usually

α = 0.05

---

### Step 3

Collect sample.

---

### Step 4

Calculate sample mean.

---

### Step 5

Calculate Standard Error.

SE = σ / √n

---

### Step 6

Calculate Z-score.

Use the Z-Test formula.

---

### Step 7

Find p-value or compare with critical value.

---

### Step 8

Make decision.

Reject H₀

OR

Fail to Reject H₀

---

# 15. Decision Rule

Using p-value

If

p ≤ α

Reject H₀

Otherwise

Fail to Reject H₀

---

# 16. Critical Value Method

Instead of p-value, compare the calculated Z-score with the critical Z value.

If

|Z| > Critical Value

Reject H₀

Otherwise

Fail to Reject H₀

---

# 17. P-value Method

A p-value tells us how likely the observed sample result is if the null hypothesis is true.

Decision

p ≤ α

Reject H₀

p > α

Fail to Reject H₀

---

# 18. One-Tailed vs Two-Tailed Tests

## Left-Tailed

H₁ : μ < μ₀

Reject only on the left side.

---

## Right-Tailed

H₁ : μ > μ₀

Reject only on the right side.

---

## Two-Tailed

H₁ : μ ≠ μ₀

Reject on both sides.

---

# 19. Common Critical Values

| Confidence Level | α | Critical Z |
|------------------|----|-----------|
| 90% | 0.10 | ±1.645 |
| 95% | 0.05 | ±1.96 |
| 99% | 0.01 | ±2.576 |

---

# 20. Complete Example

A company claims the average weight of its cereal boxes is **500 g**.

Sample Size

n = 64

Sample Mean

x̄ = 495 g

Population Standard Deviation

σ = 16 g

Test

H₀ : μ = 500

H₁ : μ ≠ 500

Step 1

Calculate Standard Error

SE = 16 / √64

SE = 16 / 8

SE = 2

Step 2

Calculate Z-score

Z = (495 − 500) / 2

Z = -2.5

Step 3

Critical Value

95%

±1.96

Step 4

Decision

Since

|-2.5| > 1.96

Reject H₀

Conclusion

The average cereal box weight is significantly different from 500 g.

---

# 21. Interpretation

Large positive Z

Sample mean is much larger than the population mean.

Large negative Z

Sample mean is much smaller.

Z close to 0

Sample mean is very close to the population mean.

---

# 22. Assumptions

- Random sample
- Independent observations
- Known population standard deviation
- Sample size ≥ 30
- Population approximately normal

---

# 23. Advantages

- Easy to calculate
- Accurate for large samples
- Widely used
- Based on the standard normal distribution

---

# 24. Limitations

- Requires known population standard deviation
- Not suitable for small samples
- Sensitive to non-random sampling

---

# 25. Common Mistakes

❌ Using a Z-Test when σ is unknown and n is small.

Use a **t-Test** instead.

---

❌ Confusing the sample standard deviation with the population standard deviation.

---

❌ Forgetting to check assumptions.

---

❌ Interpreting "Fail to Reject H₀" as "Accept H₀."

---

# 26. Interview Questions

### Q1. What is a Z-Test?

A statistical hypothesis test used to compare sample and population means when σ is known.

---

### Q2. When do we use a Z-Test?

When the population standard deviation is known and the sample size is at least 30.

---

### Q3. What is the Z-score?

The number of standard deviations the sample mean is from the population mean.

---

### Q4. What is the difference between a Z-Test and a t-Test?

| Z-Test | t-Test |
|---------|---------|
| σ known | σ unknown |
| Large sample | Small sample |
| Uses Z-distribution | Uses t-distribution |

---

### Q5. What happens if p < 0.05?

Reject the Null Hypothesis.

---

# 27. Quick Summary

| Concept | Description |
|---------|-------------|
| Purpose | Compare sample mean with population mean |
| Formula | Z = (x̄ − μ) / (σ / √n) |
| Distribution | Standard Normal Distribution |
| Population SD | Must be known |
| Sample Size | Usually n ≥ 30 |
| Decision | Reject H₀ if p ≤ α or |Z| > Critical Value |
| Common α | 0.05 |
| Test Statistic | Z-score |
| Alternative Test | t-Test (when σ is unknown) |

---

# Key Takeaways

- A Z-Test is used to determine whether a sample mean differs significantly from a known population mean.
- It requires a known population standard deviation and a sufficiently large sample.
- The Z-score indicates how many standard deviations the sample mean is from the hypothesized population mean.
- Decisions are made using either the **critical value method** or the **p-value method**.
- If the assumptions of a Z-Test are not met, especially when σ is unknown and the sample is small, use a **t-Test** instead.
- We will use z-test when the **sample size** is **greater than or equals to 30** and for z-test we must know the **variance or standard deviation of the population**
- It checks that the **sample mean** is **significantly different** from the **population mean**
- There are two ways of solving the question one is using **Critical Values** and another one is using **P values**.

# Formula:

Z = (​xˉ - μ) / (σ / under-root(n))​

Meaning of each symbol
x bar= Sample mean — the average from your sample
μ = Population mean — the claimed/known average of the whole population
σ = Population standard deviation — how spread out the population data is
n = Sample size — number of observations in your sample

# Problem Solving: 

🧪 Z-Test Word Problem

A company claims that the average battery life of its laptops is 50 hours. The population standard deviation is known to be 8 hours.

A researcher randomly selects 64 laptops and finds that their average battery life is 52 hours.

Question: Using the Z-test formula, calculate the Z-score.

# Data

Population Mean(μ) = 50
Sample Mean(xˉ) = 52
Standard Deviation(σ) = 8
Number Of Samples = 64

# Formula

Z = (xˉ - μ) / (σ / under-root(n))

# Solution

Z = (52 - 50) / (8 / under-root(64))
Z = 2 / (8 / 8)
Z = 2 / 1

# Answer
Z = **2**