# Exploratory Data Analysis (EDA)

## What is EDA?

**EDA** is the process of analyzing and visualizing datasets to understand their main characteristics, find patterns, detect anomalies, and test hypotheses — before building any machine learning model.

> **EDA = Getting to know your data**

---

## Why is EDA Important?

| Purpose | Benefit |
|---------|---------|
| Understand data structure | Know what you're working with |
| Find patterns & trends | Discover useful insights |
| Detect outliers | Handle or remove them |
| Identify missing values | Decide how to handle them |
| Check feature relationships | Find correlations |
| Validate assumptions | Ensure data quality |

---

## Types of EDA

### 1. Univariate Analysis
- Analyzing **one variable at a time**
- Understand distribution of individual features

### 2. Bivariate Analysis
- Analyzing **two variables together**
- Understand relationships between pairs of features

### 3. Multivariate Analysis
- Analyzing **three or more variables**
- Understand complex interactions in data

---

## EDA Techniques

### 📊 Statistical Analysis

| Technique | Purpose |
|-----------|---------|
| **Mean, Median, Mode** | Central tendency |
| **Standard Deviation, Variance** | Spread of data |
| **Skewness, Kurtosis** | Shape of distribution |
| **Min, Max, Quartiles** | Range of values |
| **Correlation Matrix** | Relationships between features |
| **Value Counts** | Frequency of categorical values |

---

### 📈 Visual Analysis

| Visualization | Best For |
|---------------|----------|
| **Histogram** | Distribution of single variable |
| **Box Plot** | Outliers and spread |
| **Bar Chart** | Categorical data frequencies |
| **Scatter Plot** | Relationship between 2 variables |
| **Heatmap** | Correlation matrix |
| **Pair Plot** | All variable relationships |
| **Pie Chart** | Proportion distribution |
| **Density Plot** | Smoothed distribution |
| **Violin Plot** | Distribution + box plot combined |

---

### 🔍 Specific Checks

### Check Missing Values
- Identify columns with null values
- Understand missing data patterns
- Decide: Drop, Impute, or Flag

### Check Outliers
- Use Box plots or Z-score method
- Understand if outliers are errors or genuine
- Decide: Remove, Cap, or Keep

### Check Class Imbalance (Classification)
- Count distribution of target classes
- If imbalanced → use techniques like:
  - Oversampling (SMOTE)
  - Undersampling
  - Class weights

### Check Data Types
- Numerical: int, float
- Categorical: object, category
- Date/Time: datetime
- Ensure proper data types

---

## EDA Process Flow
┌─────────────────────────────────────────────────────────────┐
│ EDA PROCESS │
│ │
│ Step 1: Data Overview │
│ → Check shape, columns, data types, first/last rows │
│ │
│ Step 2: Summary Statistics │
│ → Describe numerical & categorical features │
│ │
│ Step 3: Missing Values Analysis │
│ → Find and visualize missing data │
│ │
│ Step 4: Univariate Analysis │
│ → Analyze each variable individually │
│ │
│ Step 5: Bivariate Analysis │
│ → Analyze relationships between variables │
│ │
│ Step 6: Multivariate Analysis │
│ → Analyze complex interactions │
│ │
│ Step 7: Outlier Detection │
│ → Find and handle outliers │
│ │
│ Step 8: Insights & Documentation │
│ → Document findings for next steps │
└─────────────────────────────────────────────────────────────┘

---

## Common EDA Questions

| Question | How to Answer |
|----------|---------------|
| How large is the dataset? | Check shape (rows, columns) |
| What types of data do I have? | Check dtypes |
| Are there missing values? | Check null counts |
| How are features distributed? | Histograms, density plots |
| Which features are correlated? | Correlation heatmap |
| Are there outliers? | Box plots, scatter plots |
| Is the target balanced? | Value counts, bar charts |
| Which features affect the target? | Pair plots, correlation |

---

## EDA Checklist

- [ ] Load and preview data
- [ ] Check data shape and info
- [ ] Summary statistics
- [ ] Check missing values
- [ ] Analyze target variable
- [ ] Visualize distributions
- [ ] Check correlations
- [ ] Detect outliers
- [ ] Check class imbalance
- [ ] Document key insights

---

## Key Takeaway

> **EDA is NOT about building models. It's about understanding your data so you can build better models.**

Good EDA leads to:
- Better feature engineering
- Correct algorithm selection
- Fewer surprises during training
- More interpretable results
- Faster debugging