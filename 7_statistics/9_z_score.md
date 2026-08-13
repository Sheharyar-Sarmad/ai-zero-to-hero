# Z-Score Notes for Statistics

## 1. What is a Z-Score?
A **Z-score** (also called a **standard score**) measures how many **standard deviations** a data point is from the mean of its distribution.

- It standardizes values from different distributions so they can be compared.
- It tells us whether a value is typical or unusual within its data set.

---

## 2. The Formula

For a population:
\[z = \frac{x - \mu}{\sigma}\]

For a sample:
\[z = \frac{x - \bar{x}}{s}\]

Where:
- \( x \) = individual data value
- \( \mu \) = population mean
- \( \bar{x} \) = sample mean
- \( \sigma \) = population standard deviation
- \( s \) = sample standard deviation

---

## 3. Interpreting Z-Scores

| Z-Score | Interpretation |
|---------|----------------|
| \( z = 0 \) | Exactly at the mean |
| \( z > 0 \) | Above the mean |
| \( z < 0 \) | Below the mean |
| \( |z| < 1 \) | Within 1 standard deviation of the mean (common) |
| \( |z| > 2 \) | Unusual (less than 5% chance in normal distribution) |
| \( |z| > 3 \) | Very unusual (outlier potential) |

---

## 4. Why Use Z-Scores?

✅ **Compare different data sets** (e.g., test scores from two different classes)  
✅ **Identify outliers**  
✅ **Standardize data** for machine learning (feature scaling)  
✅ **Calculate probabilities** using the standard normal distribution  
✅ **Determine relative standing** (percentiles)

---

## 5. Z-Scores and the Normal Distribution

If data is **normally distributed**, the Z-score corresponds to a **percentile**:

| Z-Score | Percentile |
|---------|------------|
| -3.0    | 0.13%      |
| -2.0    | 2.28%      |
| -1.0    | 15.87%     |
| 0.0     | 50.00%     |
| 1.0     | 84.13%     |
| 2.0     | 97.72%     |
| 3.0     | 99.87%     |

> Use **Z-tables** or statistical software to find exact probabilities.

---

## 6. Chebyshev’s Theorem (for any distribution)

For **any** distribution, at least:
- \( 1 - \frac{1}{k^2} \) of data falls within \( k \) standard deviations of the mean.

Examples:
- \( k = 2 \): at least 75% of data within \( \mu \pm 2\sigma \)
- \( k = 3 \): at least 88.9% within \( \mu \pm 3\sigma \)

---

## 7. Z-Score vs T-Score

| Z-Score | T-Score |
|---------|---------|
| Mean = 0 | Mean = 50 |
| SD = 1 | SD = 10 |
| Used for known population parameters | Used for small samples or unknown variance |
| Formula: \( z = (x - \mu)/\sigma \) | Formula: \( T = 10z + 50 \) |

---

## 8. Practical Example

**Problem:**  
A student scores 85 on a test. Class mean = 75, standard deviation = 5.  
What is the Z-score?

**Solution:**  
\[
z = \frac{85 - 75}{5} = \frac{10}{5} = 2.0
\]

**Interpretation:**  
The student scored **2 standard deviations above the mean** – better than ~97.7% of the class (if normally distributed).

---

## 9. Limitations

- Sensitive to **outliers**
- Assumes data is **roughly symmetric** (for meaningful percentile interpretation)
- Not ideal for **skewed distributions** (use IQR or other methods instead)

---

## 10. Quick Reference Card



---

## 11. Python Code Snippet

```python
import scipy.stats as stats

z_score = (x - mean) / std_dev
p_value = stats.norm.cdf(z_score)  # percentile

# Or use stats.zscore() on an array
from scipy import stats
z_scores = stats.zscore(data)

## formula:

z-score = (data point - mean) / standard deviation