

# T-Test — Complete Statistics Notes

## 1. What is a T-Test?

A **t-test** is a statistical hypothesis test used to determine whether there is a statistically significant difference between means. When we have **unkown** standard deviation of a **population** then we use **T testing** and sample size can be small than **30** here.

It is especially useful when:

- The sample size is small.
- The population standard deviation is unknown.
- The data is approximately normally distributed.

---

# 2. Basic Idea

Suppose we have:

```text
Sample Data → Calculate Difference → Calculate t-statistic → Calculate p-value

# Degrees of Freedom (df)

## Definition

**Degrees of freedom (df)** is the number of values in a statistical calculation that are free to vary after certain constraints have been applied.

In simple words:

> Degrees of freedom tells us how much independent information is available for estimating a parameter or calculating a statistic.

---

# Simple Example

Suppose we have 3 numbers:

x₁, x₂, x₃

and their mean must be:

Mean = 10

Therefore, their total must be:

x₁ + x₂ + x₃ = 30

We can freely choose two values:

x₁ = 8
x₂ = 12

But the third value is now forced:

x₃ = 10

Therefore:

3 values - 1 constraint = 2 degrees of freedom

## Formula

```text
df = n - 1