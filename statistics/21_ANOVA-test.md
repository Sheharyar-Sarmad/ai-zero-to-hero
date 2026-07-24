 # ANOVA (Analysis of Variance)

## What is ANOVA?

ANOVA stands for **Analysis of Variance**.

It is a statistical method used to compare the means of **three or more groups**.

Instead of performing many separate t-tests, ANOVA allows us to compare all groups together.

---

## Example

Suppose we want to compare the average marks of students taught by three different teachers:

- Teacher A
- Teacher B
- Teacher C

ANOVA helps us determine whether the difference between their average marks is statistically significant.

---

## Why Not Use Multiple t-tests?

Suppose we have three groups:

- Group A
- Group B
- Group C

We could perform:

- A vs B
- A vs C
- B vs C

But performing many t-tests increases the probability of making a Type I error.

ANOVA solves this problem by testing all groups at the same time.

---

# Types of ANOVA

## 1. One-Way ANOVA

One-Way ANOVA is used when we have:

- One independent variable
- Three or more groups

### Example

Comparing the average salary of employees in:

- Department A
- Department B
- Department C

The independent variable is:

```text
Department