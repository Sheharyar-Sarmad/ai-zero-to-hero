

# Boosting

## Why do we need boosting?

**Boosting** combines multiple weak learners sequentially
to build a stronger model.

> Each new learner focuses on what previous learners handled poorly.

---

## 1. AdaBoost

### Core Concept

**AdaBoost = Adaptive Boosting**

- Trains weak learners sequentially.
- Gives more importance to misclassified samples.
- Later learners focus on difficult examples.
- Combines learners using weighted voting.

### Key Idea

> Focus more on previous mistakes.

---

## 2. Gradient Boosting

### Core Concept

Gradient Boosting builds models sequentially where each new
model tries to reduce the loss of the existing model.

Initial Model
     ↓
Calculate Error
     ↓
Train Next Weak Learner
     ↓
Reduce Loss
     ↓
Repeat

Key Idea

Each new learner moves the model toward lower loss.

## XGBoost

Core Concept

XGBoost = Extreme Gradient Boosting

XGBoost is an optimized and regularized implementation of
gradient boosting.

It provides:

Regularization
Faster training
Efficient tree construction
Learning-rate control
Row/column subsampling
Missing-value handling

## Key Idea

Gradient Boosting + Optimization + Regularization

Quick Comparison

Algorithm	        Core Idea

AdaBoost	        Focus on previous mistakes
Gradient Boosting	Reduce loss using gradients
XGBoost	            Optimized and regularized Gradient Boosting

## Remember

AdaBoost → Focus on mistakes

Gradient Boosting → Reduce loss using gradients

XGBoost → Optimized + regularized Gradient Boosting