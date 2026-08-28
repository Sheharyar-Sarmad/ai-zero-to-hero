# Stacking

Stacking (Stacked Generalization) is an ensemble learning technique where multiple different models make predictions, and another model called a **meta-model** learns how to combine those predictions into the final prediction.

## Simple Example

Imagine we are predicting whether a person will buy a product.

Input Data
      ↓
Model 1 → Logistic Regression → 0.70
Model 2 → Decision Tree      → 0.80
Model 3 → KNN                → 0.65
      ↓
Predictions
      ↓
Meta-Model
      ↓
Final Prediction

## For example:

Logistic Regression: 70% confidence  
Decision Tree: 80% confidence  
KNN: 65% confidence  

The predictions:

[0.70, 0.80, 0.65]

are given to the **meta-model**, which learns how to combine them and produces the final prediction.

## Key Idea

Different Models
      ↓
Different Predictions
      ↓
Meta-Model
      ↓
Learns How to Combine Them
      ↓
Final Prediction

## Base Models

Base models are the first-level models that learn from the original training data.

Examples:

- Logistic Regression
- Decision Tree
- KNN
- SVM
- Random Forest

Different models can learn different patterns from the same data.

## Meta-Model

The meta-model is the second-level model that learns from the predictions of the base models.

For example:

```text
Base Model 1 ─┐
Base Model 2 ─┼→ Predictions → Meta-Model → Final Prediction
Base Model 3 ─┘