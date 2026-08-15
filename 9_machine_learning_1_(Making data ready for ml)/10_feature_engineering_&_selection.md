



# Feature Engineering & Feature Selection - Short Notes

---

## What is Feature Engineering?

**Feature Engineering** = Creating new features or transforming existing ones to improve model performance.

> **Feature Engineering = Making data more informative**

---

## What is Feature Selection?

**Feature Selection** = Choosing the most relevant features and removing irrelevant ones.

> **Feature Selection = Keeping only what matters**

---

## Key Difference

| Feature Engineering | Feature Selection |
|---------------------|-------------------|
| Create new features | Choose existing features |
| Add more information | Remove useless information |
| Increase features | Decrease features |

---

# PART 1: FEATURE ENGINEERING

---

## Why Feature Engineering?

| Reason | Benefit |
|--------|---------|
| Captures patterns | Better learning |
| Handles non-linearity | Complex relationships |
| Domain knowledge | Expert insights |
| Improves accuracy | Better predictions |

---

## Types of Feature Engineering

---

### 1. Feature Creation

**Creating new features from existing data.**

| Method | Example |
|--------|---------|
| **Mathematical** | Ratio, Product, Sum, Difference |
| **Date/Time** | Day, Month, Year, Hour |
| **Text** | Word count, Length, Sentiment |
| **Aggregations** | Mean, Sum, Count, Max, Min |
| **Interaction** | Age × Income |
| **Polynomial** | x², x³, √x |

---

### Mathematical Features
Original: Total Price, Quantity
New: Price per Unit = Total Price / Quantity
New: Discount = Original Price - Selling Price

text

---

### Date/Time Features
Original: Purchase Date: 2024-01-15
New: Day of Week, Month, Quarter, Year, Is Weekend

text

---

### Text Features
Original: "This product is amazing"
New: Word Count: 4, Character Count: 24, Sentiment: 0.85

text

---

### Aggregation Features
Group by Customer:

Total Spend (sum)

Average Order (mean)

Number of Orders (count)

Max Order (max)

text

---

### Interaction Features
Original: Age, Income
New: Age × Income
Why? Effect of age depends on income.

text

---

### Polynomial Features
Original: x = [1, 2, 3, 4]
New: x² = [1, 4, 9, 16], x³ = [1, 8, 27, 64]

text

---

### 2. Feature Transformation

**Changing feature form for better modeling.**

| Method | When to Use | Effect |
|--------|-------------|--------|
| **Log** | Right-skewed data | Reduces skewness |
| **Square Root** | Count data | Reduces variance |
| **Box-Cox** | Skewed data | Makes normal |
| **Square** | Left-skewed data | Increases spread |

---

### Log Transformation Example
Before: [1, 10, 100, 1000] (skewed)
After: [0, 1, 2, 3] (balanced)
✅ Best for: Prices, Income, Population

text

---

### 3. Feature Binning

**Converting continuous to categorical.**
Age: [22, 25, 30, 35, 40, 55, 65]
Bins: Young (18-25), Middle (26-40), Senior (41-60), Elderly (60+)

text

---

### 4. Missing Value Indicators
Original: [25, 30, None, 40]
Imputed: [25, 30, 35, 40]
Indicator: [0, 0, 1, 0]

text

---

# PART 2: FEATURE SELECTION

---

## Why Feature Selection?

| Reason | Benefit |
|--------|---------|
| Reduces Overfitting | Less noise |
| Improves Accuracy | Removes misleading features |
| Faster Training | Less data |
| Better Interpretability | Easier to understand |
| Reduces Memory | Saves storage |

---

## Types of Feature Selection
┌─────────────────────────────────────────┐
│ FEATURE SELECTION │
│ │
│ 1. FILTER METHODS │
│ • Statistical tests │
│ • Fast but less accurate │
│ │
│ 2. WRAPPER METHODS │
│ • Uses ML models │
│ • Accurate but expensive │
│ │
│ 3. EMBEDDED METHODS │
│ • Built into algorithms │
│ • Best of both worlds │
└─────────────────────────────────────────┘

text

---

## 1. Filter Methods

**Statistical tests to select features.**

| Method | How it Works | Best For |
|--------|--------------|----------|
| **Variance Threshold** | Removes low variance | Constant features |
| **Correlation** | Removes highly correlated | Redundancy |
| **Chi-Square** | Tests independence | Categorical |
| **ANOVA** | Tests variance groups | Numeric |
| **Mutual Information** | Measures dependency | Both types |

---

### Variance Threshold
Feature A: [1,1,1,1] → Constant → Remove
Feature B: [1,2,1,2] → Low variance → Remove
Feature C: [1,5,2,8] → High variance → Keep

text

---

### Correlation Method
Correlation Matrix:
Age - Income: 0.65 (correlated)
Income - Spending: 0.70 (correlated)

→ Keep one, remove the other (redundant)

text

---

### Mutual Information
Feature MI Score
Income 0.85 → Most important
Age 0.72 → Important
Education 0.45 → Moderate
City 0.12 → Remove

text

---

## 2. Wrapper Methods

**Use ML models to select features.**

| Method | How it Works |
|--------|--------------|
| **Forward Selection** | Add features one by one |
| **Backward Elimination** | Remove features one by one |
| **RFE** | Train, remove least important, repeat |

---

### Recursive Feature Elimination (RFE)
Train model with all features

Rank by importance

Remove least important

Repeat until optimal
✅ Most popular wrapper method

text

---

## 3. Embedded Methods

**Built into ML algorithms.**

| Method | How it Works |
|--------|--------------|
| **Lasso (L1)** | Shrinks coefficients to zero |
| **Elastic Net** | Combines L1 + L2 |
| **Tree Importance** | Gives importance scores |

---

### Lasso Regression
Lasso makes some coefficients ZERO.
Features with zero coefficients are removed.
✅ Automatic feature selection

text

---

### Tree-based Importance
Feature Importance
Income 0.35 → Most important
Age 0.28 → Important
Education 0.20 → Moderate
City 0.10 → Remove
Gender 0.07 → Remove

text

---

## 4. Hybrid Methods

| Method | How it Works |
|--------|--------------|
| **Boruta** | Random Forest to find important features |
| **Filter + RFE** | Filter first, then RFE |

---

## Summary Flow
┌─────────────────────────────────────────┐
│ RAW DATA │
│ │ │
│ ▼ │
│ FEATURE ENGINEERING │
│ • Create new features │
│ • Transform features │
│ → More features! │
│ │ │
│ ▼ │
│ FEATURE SELECTION │
│ • Remove irrelevant │
│ • Remove redundant │
│ → Fewer features! │
│ │ │
│ ▼ │
│ FINAL DATASET │
│ (Only relevant features) │
└─────────────────────────────────────────┘

text

---

## Quick Reference

| Task | Method |
|------|--------|
| **Create new features** | Math operations, dates, aggregations |
| **Transform data** | Log, sqrt, Box-Cox |
| **Remove constant features** | Variance Threshold |
| **Remove correlated features** | Correlation matrix |
| **Select important features** | Mutual Information, RFE |
| **Automatic selection** | Lasso, Tree Importance |

---

## Checklist

### Feature Engineering
- [ ] Create new features from existing ones
- [ ] Add math operations (ratio, product)
- [ ] Extract date/time features
- [ ] Add text features
- [ ] Create aggregations
- [ ] Apply transformations
- [ ] Bin continuous features

### Feature Selection
- [ ] Remove constant features
- [ ] Remove correlated features
- [ ] Apply filter methods
- [ ] Apply wrapper methods (RFE)
- [ ] Use embedded methods (Lasso, importance)
- [ ] Validate with cross-validation

---

## Common Mistakes

| Mistake | Correct Way |
|---------|-------------|
| Add too many features | Select only important ones |
| Remove features aggressively | Validate with cross-validation |
| Engineer after splitting | Engineer before splitting |
| Use test data for selection | Use only training data |

---

## Bottom Line

> **Feature Engineering = Give your model the ability to learn. Feature Selection = Give your model the ability to learn WELL. Both are essential!**
