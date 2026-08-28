# Data Cleaning

## What is Data Cleaning?

**Data Cleaning** is the process of identifying and correcting errors, inconsistencies, and inaccuracies in raw data to make it ready for analysis and machine learning.

> **Data Cleaning = Making data reliable and consistent**

---

## Why is Data Cleaning Important?

| Reason | Impact |
|--------|--------|
| **Garbage In = Garbage Out** | Bad data leads to bad models |
| **Improves accuracy** | Clean data = Better predictions |
| **Saves time** | Fix issues early, avoid problems later |
| **Builds trust** | Reliable data = Reliable results |
| **Reduces errors** | Avoid misleading insights |

---

## Common Data Problems
┌─────────────────────────────────────────────────────────────┐
│ COMMON DATA PROBLEMS │
│ │
│ ❌ Missing Values │
│ ❌ Duplicate Records │
│ ❌ Outliers (Extreme values) │
│ ❌ Inconsistent Formatting │
│ ❌ Incorrect Data Types │
│ ❌ Typos and Spelling Errors │
│ ❌ Irrelevant Columns │
│ ❌ Data Entry Errors │
└─────────────────────────────────────────────────────────────┘

text

---

## Data Cleaning Process
┌─────────────────────────────────────────────────────────────┐
│ DATA CLEANING STEPS │
│ │
│ Step 1: Handle Missing Values │
│ Step 2: Remove Duplicates │
│ Step 3: Handle Outliers │
│ Step 4: Fix Inconsistent Formatting │
│ Step 5: Correct Data Types │
│ Step 6: Remove Irrelevant Columns │
│ Step 7: Fix Typos & Errors │
│ Step 8: Validate Data Quality │
└─────────────────────────────────────────────────────────────┘

---

## 1. Handling Missing Values

### Types of Missing Data

| Type | Description | Example |
|------|-------------|---------|
| **MCAR** | Missing completely at random | Random survey non-response |
| **MAR** | Missing at random (related to other variables) | Older people skip age question |
| **MNAR** | Missing not at random (related to value itself) | High-income people hide income |

### How to Handle Missing Values

| Method | When to Use | Example |
|--------|-------------|---------|
| **Drop Rows** | Few missing values (<5%) | Delete rows with nulls |
| **Drop Columns** | >60% values missing | Delete entire column |
| **Mean/Median Imputation** | Numerical, normal distribution | Fill age with average |
| **Mode Imputation** | Categorical data | Fill with most common value |
| **Forward/Backward Fill** | Time series data | Fill with previous value |
| **Predictive Imputation** | Important features | Use other features to predict |
| **Flag Missing** | When missing itself is meaningful | Add "is_missing" column |

---

## 2. Removing Duplicates

### Types of Duplicates

- **Exact Duplicates:** All columns identical
- **Partial Duplicates:** Some columns same, others different
- **Near Duplicates:** Slight variations (typos)

### How to Handle

- Identify duplicate rows
- Keep first or last occurrence
- Investigate why duplicates exist
- Remove or merge duplicates

---

## 3. Handling Outliers

### What are Outliers?

**Outliers** are data points that are significantly different from other observations.

### Detection Methods

| Method | How it Works |
|--------|--------------|
| **Box Plot (IQR)** | Values beyond 1.5 × IQR |
| **Z-Score** | Values beyond ±3 standard deviations |
| **Scatter Plot** | Visual detection |
| **Percentile Method** | Values <1% or >99% |

### How to Handle Outliers

| Method | When to Use |
|--------|-------------|
| **Remove** | Genuine errors or measurement mistakes |
| **Cap/Clip** | Keep within reasonable range |
| **Transform** | Log or square root transformation |
| **Impute** | Replace with median/mean |
| **Keep** | Valid extreme values (e.g., high income) |

---

## 4. Fixing Inconsistent Formatting

### Common Formatting Issues

| Issue | Example | Fix |
|-------|---------|-----|
| **Date formats** | 01/02/2023 vs 2023-02-01 | Standardize format |
| **Text case** | "New York" vs "new york" | Convert to same case |
| **Spacing** | "John Doe" vs "John  Doe" | Remove extra spaces |
| **Abbreviations** | "USA" vs "United States" | Standardize values |
| **Units** | "kg" vs "kilograms" | Standardize units |

---

## 5. Correcting Data Types

### Common Data Type Issues

| Issue | Example | Correct Type |
|-------|---------|--------------|
| **Numbers stored as text** | "100" | int/float |
| **Dates stored as text** | "2023-01-01" | datetime |
| **Categories stored as text** | "Red", "Blue" | category |
| **Boolean stored as text** | "Yes"/"No" | boolean |

---

## 6. Removing Irrelevant Columns

### Types of Irrelevant Data

- **ID columns** that don't add value
- **Unused features** for the model
- **Constant columns** (all same value)
- **Highly correlated columns** (redundant)

---

## Data Cleaning Checklist

- [ ] Check for missing values
- [ ] Decide how to handle each missing value
- [ ] Remove duplicate records
- [ ] Detect outliers
- [ ] Handle outliers appropriately
- [ ] Standardize text formatting
- [ ] Standardize date formats
- [ ] Fix data types
- [ ] Remove irrelevant columns
- [ ] Validate data quality

---

## Common Data Cleaning Functions

| Task | What to Do |
|------|------------|
| View data | `head()`, `info()`, `describe()` |
| Check nulls | `isnull().sum()` |
| Fill nulls | `fillna()` |
| Drop nulls | `dropna()` |
| Remove duplicates | `drop_duplicates()` |
| Change case | `str.lower()`, `str.upper()` |
| Remove spaces | `str.strip()` |
| Convert type | `astype()` |
| Change date format | `pd.to_datetime()` |
| Standardize values | `replace()` |

---

## Example Scenario

### Raw Data Issues
Age: [25, -1, 30, 1000, 45, None]
Name: ["John", "JOHN", "John ", "Jane", "Jane"]
Date: ["2023-01-01", "01/02/2023", "2023-01-03", "NaN"]
City: ["NY", "New York", "NYC", "NEW YORK"]

text

### After Cleaning
Age: [25, 25, 30, 45, 45, 30] (handled negatives, outliers, missing)
Name: ["john", "john", "john", "jane", "jane"] (standardized case/spaces)
Date: [2023-01-01, 2023-01-02, 2023-01-03, None] (standardized format)
City: ["New York", "New York", "New York", "New York"] (standardized values)

text

---

## Key Takeaway

> **Clean data = 80% of ML success**

Most ML projects spend **70-80% of time** on data cleaning and preparation. Good cleaning leads to:
- ✅ Better models
- ✅ Faster training
- ✅ Accurate predictions
- ✅ Reliable insights