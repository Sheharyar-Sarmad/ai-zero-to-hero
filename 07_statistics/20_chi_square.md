# Chi-Square Test (χ² Test)

## 1. What is a Chi-Square Test?

The Chi-Square Test is a statistical hypothesis test used mainly with categorical data.

It compares:

- Observed Frequencies: the values we actually observe
- Expected Frequencies: the values we expect if the Null Hypothesis is true

The test determines whether the difference between observed and expected values is statistically significant.

### Simple Idea

Observed data:

    What actually happened

Expected data:

    What we expected to happen

The Chi-Square Test asks:

> Is the difference between what we observed and what we expected large enough to be statistically significant?

---

# 2. Chi-Square Formula

    χ² = Σ (O - E)² / E

Where:

- χ² = Chi-Square statistic
- O = Observed Frequency
- E = Expected Frequency
- Σ = Sum of all categories

The Chi-Square statistic measures the total difference between observed and expected frequencies.

---

# 3. Understanding the Formula

The formula is:

    χ² = Σ (O - E)² / E

Let's break it down:

## Step 1: Find the Difference

    O - E

This calculates how different the observed value is from the expected value.

---

## Step 2: Square the Difference

    (O - E)²

Squaring removes negative values.

For example:

    (-5)² = 25

    (5)² = 25

---

## Step 3: Divide by Expected Frequency

    (O - E)² / E

This gives the contribution of one category to the total Chi-Square statistic.

---

## Step 4: Add All Contributions

We calculate the value for every category and add them together.

The final result is:

    χ²

---

# 4. Hypotheses in Chi-Square Testing

## Null Hypothesis (H0)

The Null Hypothesis usually states:

> There is no significant difference or relationship.

Examples:

- There is no relationship between gender and product preference.
- The die follows the expected distribution.
- Education level and income are independent.

---

## Alternative Hypothesis (H1)

The Alternative Hypothesis states:

> There is a significant difference or relationship.

Examples:

- There is a relationship between gender and product preference.
- The die does not follow the expected distribution.
- Education level and income are related.

---

# 5. Types of Chi-Square Tests

There are two major types of Chi-Square Tests:

1. Chi-Square Goodness-of-Fit Test
2. Chi-Square Test of Independence

---

# 6. Chi-Square Goodness-of-Fit Test

## Definition

The Chi-Square Goodness-of-Fit Test is used to determine whether observed data follows an expected distribution.

It involves one categorical variable.

---

## Example

Suppose we roll a die 60 times.

If the die is fair, we expect every number to appear approximately the same number of times.

There are 6 possible outcomes:

    1, 2, 3, 4, 5, 6

Expected Frequency:

    Total Rolls / Number of Categories

    E = 60 / 6

    E = 10

Therefore, we expect each number to appear approximately 10 times.

---

## Observed Data

| Number | Observed | Expected |
|--------|----------|----------|
| 1      | 8        | 10       |
| 2      | 12       | 10       |
| 3      | 9        | 10       |
| 4      | 11       | 10       |
| 5      | 10       | 10       |
| 6      | 10       | 10       |

The Chi-Square Test determines whether these differences are due to random chance or whether the die may not be fair.

---

# 7. Chi-Square Test of Independence

## Definition

The Chi-Square Test of Independence determines whether two categorical variables are related.

It is used with a contingency table.

---

## Example

Suppose we want to determine whether gender is related to product preference.

### Observed Frequencies

|          | Product A | Product B | Total |
|----------|-----------|-----------|-------|
| Male     | 30        | 20        | 50    |
| Female   | 20        | 30        | 50    |
| Total    | 50        | 50        | 100   |

The question is:

> Is gender related to product preference?

---

## Hypotheses

### Null Hypothesis

Gender and product preference are independent.

There is no relationship between them.

### Alternative Hypothesis

Gender and product preference are not independent.

There is a relationship between them.

---

# 8. Observed Frequency

Observed Frequency is the actual number of observations.

It is represented by:

    O

Example:

    Male + Product A = 30

Therefore:

    Observed Frequency = 30

---

# 9. Expected Frequency

Expected Frequency is the frequency we would expect if the Null Hypothesis were true.

For a Chi-Square Test of Independence:

    E = (Row Total × Column Total) / Grand Total

---

## Example

For Male and Product A:

    Row Total = 50

    Column Total = 50

    Grand Total = 100

Therefore:

    E = (50 × 50) / 100

    E = 25

The expected frequency is 25.

---

# 10. Expected Frequency Table

Observed Table:

|          | Product A | Product B |
|----------|-----------|-----------|
| Male     | 30        | 20        |
| Female   | 20        | 30        |

Expected Table:

|          | Product A | Product B |
|----------|-----------|-----------|
| Male     | 25        | 25        |
| Female   | 25        | 25        |

The Chi-Square Test compares these two tables.

---

# 11. Complete Chi-Square Calculation

Observed:

| Category | O | E |
|----------|---|---|
| 1        | 30 | 25 |
| 2        | 20 | 25 |
| 3        | 20 | 25 |
| 4        | 30 | 25 |

Formula:

    χ² = Σ (O - E)² / E

For the first category:

    O = 30

    E = 25

    (O - E)² / E

    = (30 - 25)² / 25

    = 5² / 25

    = 25 / 25

    = 1

The same calculation is performed for every category.

Total:

    χ² = 1 + 1 + 1 + 1

    χ² = 4

---

# 12. Degrees of Freedom

Degrees of Freedom are used to determine the correct Chi-Square distribution.

The formula depends on the type of test.

---

## Goodness-of-Fit Test

    df = k - 1

Where:

- k = Number of categories

### Example

If there are 6 categories:

    df = 6 - 1

    df = 5

---

## Test of Independence

    df = (r - 1)(c - 1)

Where:

- r = Number of rows
- c = Number of columns

### Example

For a 2 × 2 table:

    df = (2 - 1)(2 - 1)

    df = 1 × 1

    df = 1

---

# 13. P-Value and Significance Level

The p-value helps us make a decision about the Null Hypothesis.

The commonly used significance level is:

    α = 0.05

This means we are using a 5 percent significance level.

---

## Decision Rule

If:

    p-value < α

Then:

    Reject H0

If:

    p-value >= α

Then:

    Fail to Reject H0

---

# 14. Why Do We Say "Fail to Reject"?

In hypothesis testing, we usually do not say:

    Accept H0

Instead, we say:

    Fail to Reject H0

Why?

Because a statistical test does not prove that the Null Hypothesis is absolutely true.

It only tells us whether we have enough evidence to reject it.

---

# 15. Example of Decision Making

Suppose:

    p-value = 0.03

    α = 0.05

Compare:

    0.03 < 0.05

Therefore:

    Reject H0

Conclusion:

> There is statistically significant evidence of a relationship or difference.

---

## Another Example

Suppose:

    p-value = 0.20

    α = 0.05

Compare:

    0.20 >= 0.05

Therefore:

    Fail to Reject H0

Conclusion:

> There is not enough statistical evidence to conclude that a significant relationship or difference exists.

---

# 16. Chi-Square Critical Value Method

There are two common ways to make a decision.

## Method 1: P-Value Method

Compare:

    p-value with α

Decision:

    p-value < α
    Reject H0

    p-value >= α
    Fail to Reject H0

---

## Method 2: Critical Value Method

Compare:

    Calculated χ² with Critical χ²

Decision:

    Calculated χ² > Critical χ²
    Reject H0

    Calculated χ² <= Critical χ²
    Fail to Reject H0

---

# 17. Relationship Between Chi-Square and P-Value

A larger Chi-Square statistic usually means that the observed values are far from the expected values.

This generally produces a smaller p-value.

The general relationship is:

    Large Difference
          ↓
    Large χ² Statistic
          ↓
    Small p-value
          ↓
    Reject H0

On the other hand:

    Small Difference
          ↓
    Small χ² Statistic
          ↓
    Large p-value
          ↓
    Fail to Reject H0

---

# 18. Assumptions of the Chi-Square Test

## 1. Data Must Be Categorical

Examples:

- Gender
- Country
- Color
- Product Type
- Education Level
- Yes or No
- Pass or Fail

---

## 2. Data Must Be Frequencies or Counts

Chi-Square tests work with counts.

Example:

    Male = 50

    Female = 40

    Pass = 80

    Fail = 20

---

## 3. Observations Should Be Independent

One observation should not influence another observation.

For example, if we are studying people's preferences, one person's answer should not determine another person's answer.

---

## 4. Expected Frequencies Should Not Be Too Small

A common rule is:

> Expected frequency should generally be at least 5.

Very small expected frequencies can make the Chi-Square approximation unreliable.

---

# 19. Chi-Square Distribution

The Chi-Square distribution is:

- Continuous
- Non-negative
- Right-skewed
- Dependent on degrees of freedom

The shape changes as the degrees of freedom change.

---

## Important Properties

The Chi-Square statistic cannot be negative.

Therefore:

    χ² >= 0

Why?

Because the difference is squared:

    (O - E)²

A squared value can never be negative.

---

# 20. Chi-Square Distribution and Degrees of Freedom

When degrees of freedom are small:

    The distribution is strongly right-skewed.

When degrees of freedom increase:

    The distribution becomes more symmetrical.

The Chi-Square distribution is always:

    χ² >= 0

---

# 21. Goodness-of-Fit vs Independence Test

| Feature | Goodness-of-Fit | Independence |
|---------|-----------------|--------------|
| Number of Variables | One | Two |
| Purpose | Compare observed with expected distribution | Test relationship |
| Data Structure | Categories | Contingency Table |
| Example | Is a die fair? | Is gender related to preference? |
| Degrees of Freedom | k - 1 | (r - 1)(c - 1) |

---

# 22. Chi-Square Test vs T-Test

| Feature | Chi-Square Test | T-Test |
|---------|-----------------|--------|
| Data Type | Categorical | Numerical |
| Main Purpose | Compare frequencies | Compare means |
| Statistic | χ² | t |
| Example | Gender vs Preference | Average height |
| Distribution | Chi-Square | t-Distribution |

---

# 23. Chi-Square Test vs Z-Test

| Feature | Chi-Square Test | Z-Test |
|---------|-----------------|--------|
| Main Data | Categorical frequencies | Numerical values or proportions |
| Main Statistic | χ² | z |
| Main Purpose | Test frequency differences or relationships | Test means or proportions |
| Distribution | Chi-Square Distribution | Standard Normal Distribution |

---

# 24. Python: Goodness-of-Fit Test

The SciPy library provides the chisquare function.

```python
from scipy.stats import chisquare

observed = [8, 12, 9, 11, 10, 10]

expected = [10, 10, 10, 10, 10, 10]

chi_stat, p_value = chisquare(
    f_obs=observed,
    f_exp=expected
)

print("Chi-Square Statistic:", chi_stat)
print("P-value:", p_value)