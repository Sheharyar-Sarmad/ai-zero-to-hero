# Data Preprocessing - Concise Notes

---

## What is Data Preprocessing?

Converting raw data into a format that machine learning algorithms can understand and work with effectively.

> **Data Preprocessing = Making data ML-ready**

---

## Why Preprocess?

| Reason | Benefit |
|--------|---------|
| Improves accuracy | Better predictions |
| Faster training | Algorithms converge quickly |
| Reduces bias | Features don't dominate others |
| Handles mixed data | Text & numbers become usable |
| Prevents overfitting | Removes noise |

---

## Data Cleaning vs Preprocessing

| Cleaning | Preprocessing |
|----------|---------------|
| Fix errors | Transform data |
| Handle missing values | Encode categories |
| Remove duplicates | Scale features |
| Fix formatting | Split train/test |

---

## Preprocessing Steps Overview
Raw Data → Encode → Scale → Split → Transform → Ready Data

text

---

## Step 1: Encoding Categorical Data

### What is Categorical Data?
Data that represents categories or groups (e.g., Color, Gender, City).

**Why Encode?** ML models understand numbers, not text.

### Encoding Methods

| Method | How it Works | When to Use |
|--------|--------------|-------------|
| **Label Encoding** | Assigns numbers (0,1,2...) | Order matters (ordinal) |
| **One-Hot Encoding** | Creates binary columns | No order (nominal) |
| **Target Encoding** | Replace with mean target | High cardinality |
| **Frequency Encoding** | Replace with count | Many categories |

### Label Encoding Example
Before: Low, Medium, High
After: 0, 1, 2

text
✅ Use when order matters

### One-Hot Encoding Example
Before: Red, Blue, Green
After: Red Blue Green
[1, 0, 0] → Red
[0, 1, 0] → Blue
[0, 0, 1] → Green

text
✅ Use when no order matters
⚠️ Creates many columns

### Target Encoding Example
City → Price
Mumbai → 52500 (mean price)
Delhi → 46500 (mean price)

text
✅ Use for high cardinality
⚠️ Can cause overfitting

---

## Step 2: Scaling Numerical Features

### Why Scale?
- Features with large ranges dominate
- Distance-based algorithms need scaling
- Gradient descent converges faster
- Prevents bias toward large numbers

### Scaling Methods

| Method | Formula | Range | Best For |
|--------|---------|-------|----------|
| **Standardization** | (x - mean) / std | Mean=0, Std=1 | Normal distribution |
| **Min-Max Scaling** | (x - min) / (max - min) | [0,1] | Bounded features |
| **Robust Scaling** | (x - median) / IQR | Median=0 | Data with outliers |
| **MaxAbs Scaling** | x / max(abs(x)) | [-1,1] | Sparse data |

### Standardization (Z-Score)
Before: [20, 30, 40, 50, 60]
After: [-1.41, -0.71, 0, 0.71, 1.41]
Mean=0, Std=1

text
✅ Use for: Linear models, SVM, KNN, Neural Networks, PCA

### Min-Max Scaling (Normalization)
Before: [20, 30, 40, 50, 60]
After: [0, 0.25, 0.5, 0.75, 1]
All values in [0,1]

text
✅ Use for: Neural Networks, KNN, bounded features

### Robust Scaling
Less affected by outliers
Use when data has extreme outliers

text

### Which Scaling for Which Algorithm?

| Algorithm | Scaling Needed |
|-----------|----------------|
| Linear/Logistic Regression | Standardization |
| KNN, SVM, K-Means | Standardization or Min-Max |
| Neural Networks | Min-Max or Standardization |
| Decision Trees, Random Forest | None |
| XGBoost | None |
| PCA | Standardization |

---

## Step 3: Train-Test Split

### Why Split?
- Evaluate on unseen data
- Prevent overfitting
- Measure generalization

### Split Ratios

| Dataset Size | Train | Validation | Test |
|--------------|-------|------------|------|
| Small (<10K) | 60-70% | 15-20% | 15-20% |
| Medium (10K-100K) | 70-75% | 10-15% | 10-15% |
| Large (100K-1M) | 75-80% | 10% | 10% |
| Very Large (>1M) | 80-85% | 7-10% | 5-8% |

### Important Rules
✅ Shuffle data before split
✅ Use stratification for classification
✅ NEVER touch test data until final
✅ Scale AFTER split
✅ Fit on train → Transform test

text

### What is Stratification?
Maintains class distribution across all sets.
Without Stratification:
Training: 80% Class A, 20% Class B (❌ Wrong distribution)
Testing: 20% Class A, 80% Class B (❌ Wrong distribution)

With Stratification:
Training: 90% Class A, 10% Class B (✅ Matches original)
Testing: 90% Class A, 10% Class B (✅ Matches original)

text

---

## Step 4: Handling Imbalanced Data

### What is Class Imbalance?
One class has significantly fewer samples.

**Example:**
Fraud: 1% of transactions
Non-Fraud: 99% of transactions

text

### Why is it a Problem?
- Model becomes biased toward majority class
- High accuracy but useless for minority
- Fails at actual purpose

### Handling Methods

| Method | Type | How it Works |
|--------|------|--------------|
| **Oversampling** | Data | Duplicate minority class |
| **SMOTE** | Data | Create synthetic minority samples |
| **Undersampling** | Data | Remove majority samples |
| **Class Weights** | Algorithm | Penalize misclassifying minority |
| **Focal Loss** | Algorithm | Focus on hard examples |

### Example
Original: 1000 Non-Fraud, 10 Fraud (100:1)

Oversampling: 1000 Non-Fraud, 1000 Fraud (1:1)
Undersampling: 100 Non-Fraud, 10 Fraud (10:1)
SMOTE: 1000 Non-Fraud, 1000 Fraud (synthetic)
Class Weights: Penalize Fraud misclassification more

text

---

## Step 5: Feature Transformation

### Why Transform?
- Make data follow normal distribution
- Reduce skewness
- Handle non-linear relationships

### Common Transformations

| Method | When to Use | Effect |
|--------|-------------|--------|
| **Log** | Right-skewed data | Reduces skewness |
| **Square Root** | Count data | Reduces variance |
| **Box-Cox** | Skewed data | Makes data normal |
| **Square** | Left-skewed data | Increases spread |

### Example
Before: [1, 10, 100, 1000] (highly skewed)
Log: [0, 1, 2, 3] (balanced)

text

---

## Step 6: Dimensionality Reduction

### Why Reduce?
- Prevent overfitting
- Faster training
- Better visualization
- Remove redundant features
- Save memory

### Methods

| Method | Type | Best For |
|--------|------|----------|
| **PCA** | Linear | General purpose |
| **t-SNE** | Non-linear | Visualization |
| **UMAP** | Non-linear | Complex data |
| **LDA** | Supervised | Classification |
| **Autoencoders** | Neural | Deep learning |

### PCA (Principal Component Analysis)
Finds directions of maximum variance
Projects data onto fewer dimensions
Preserves important information

Example: 100 features → 10 features (90% variance preserved)

text

---

## Scaling BEFORE vs AFTER Split

### ✅ Correct Way
Split data → Train/Test

Fit scaler on TRAINING data

Transform TRAINING data

Transform TEST data (use same scaler)

text
> **Prevents data leakage!**

### ❌ Wrong Way
Scale ALL data together

Then split
→ Test data influenced scaling (data leakage!)

text

---

## Common Mistakes

| Mistake | Why Wrong | Correct Way |
|---------|-----------|-------------|
| Scale before split | Data leakage | Scale after split |
| Use same scaler on all | Test influences train | Fit on train, transform test |
| One-Hot on high cardinality | Too many columns | Use target encoding |
| Ignore imbalance | Biased model | Apply SMOTE/class weights |
| No shuffling | Data order matters | Shuffle before split |

---

## Preprocessing Checklist

- [ ] Encode categorical variables
- [ ] Scale numerical features
- [ ] Check for class imbalance
- [ ] Split data (Train/Val/Test)
- [ ] Apply transformations if needed
- [ ] Consider dimensionality reduction
- [ ] Scale AFTER splitting
- [ ] Validate preprocessed data

---

## Quick Reference

| Task | Method |
|------|--------|
| Categorical (ordinal) | Label Encoding |
| Categorical (nominal) | One-Hot Encoding |
| High cardinality | Target Encoding |
| Normal distribution | Standardization |
| Bounded features | Min-Max Scaling |
| Outliers present | Robust Scaling |
| Imbalanced data | SMOTE/Class Weights |
| Skewed data | Log/Box-Cox |
| Too many features | PCA/Feature Selection |

---

## Summary
┌─────────────────┐
│ RAW DATA │
└────────┬────────┘
│
▼
┌─────────────────┐
│ ENCODE │ → Text to numbers
│ CATEGORICAL │
└────────┬────────┘
│
▼
┌─────────────────┐
│ SCALE │ → Different ranges
│ NUMERICAL │ to same range
└────────┬────────┘
│
▼
┌─────────────────┐
│ HANDLE │ → Fix class imbalance
│ IMBALANCE │
└────────┬────────┘
│
▼
┌─────────────────┐
│ SPLIT │ → Train/Val/Test
│ DATA │
└────────┬────────┘
│
▼
┌─────────────────┐
│ TRANSFORM │ → Log, Box-Cox
│ FEATURES │
└────────┬────────┘
│
▼
┌─────────────────┐
│ REDUCE │ → PCA, t-SNE
│ DIMENSIONS │
└────────┬────────┘
│
▼
┌─────────────────┐
│ READY DATA │ → For ML Model
└─────────────────┘

text

---

> **Bottom Line:** Good preprocessing can make a simple model perform well. Bad preprocessing can make a complex model perform poorly. Preprocessing matters MORE than the algorithm!
