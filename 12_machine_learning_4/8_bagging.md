# Bagging

Bagging (Bootstrap Aggregating) is an ensemble learning technique where multiple models are trained independently on different bootstrap samples of the training data, and their predictions are combined.

## Simple Example

Imagine we are predicting whether a person will buy a product.

Original Dataset
      ↓
Bootstrap Sample 1 → Model 1
Bootstrap Sample 2 → Model 2
Bootstrap Sample 3 → Model 3
      ↓
Combine Predictions
      ↓
Final Prediction

## For example:

Model 1: predicts Buy  
Model 2: predicts Don't Buy  
Model 3: predicts Buy  
Model 4: predicts Buy  

Final Prediction: Buy

For classification → majority voting.

For regression → average of predictions.

## Bootstrap Sampling

Bootstrap sampling means randomly selecting rows from the training data **with replacement**.

Original Data:
A B C D E

Sample 1:
A C C E B

Sample 2:
D D A B E

A row can appear multiple times, and some rows may not appear in a sample.

## Key Idea

Different Bootstrap Samples
        ↓
Different Models
        ↓
Independent Training
        ↓
Combine Predictions
        ↓
More Stable Model

## Main Purpose

Bagging mainly helps **reduce variance** and make models more stable.

It is especially useful for high-variance models such as decision trees.

## Bagging vs Boosting

**Bagging:**
Models are trained independently and their predictions are aggregated.

**Boosting:**
Models are trained sequentially, with each new model trying to correct previous errors.

## In One Line

Bagging trains multiple models independently on different bootstrap samples and combines their predictions to reduce variance and improve stability.