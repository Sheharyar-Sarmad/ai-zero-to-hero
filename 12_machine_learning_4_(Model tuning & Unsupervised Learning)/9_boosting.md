

# Boosting

Boosting is an ensemble learning technique where multiple weak models are trained sequentially, and each new model tries to correct the mistakes made by the previous models.

## Simple Example

Imagine we are predicting whether a person will buy a product.

Training Data
      ↓
 Model 1
      ↓
Makes some mistakes
      ↓
 Model 2
      ↓
Focuses on those mistakes
      ↓
 Model 3
      ↓
Corrects remaining mistakes
      ↓
Combine Models
      ↓
Final Prediction

## For example:

Model 1: gets 70% correct.
Model 2: focuses more on the examples Model 1 got wrong.
Model 3: focuses on the remaining difficult examples.
All models are combined to produce the final prediction.
Key Idea
Weak Model
    ↓
Correct Errors
    ↓
Another Weak Model
    ↓
Correct Errors
    ↓
Another Weak Model
    ↓
Strong Model

## In One Line

Boosting combines multiple weak learners sequentially, where each new learner tries to improve the mistakes of the previous learners.