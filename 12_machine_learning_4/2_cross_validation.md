
# Cross-Validation

## Definition

**Cross-validation** is a model evaluation technique used to measure how well a machine learning model generalizes to unseen data.

---

## K-Fold Cross-Validation

- Dataset is divided into **K folds**.
- Model is trained on `K - 1` folds.
- Remaining fold is used for validation.
- Process is repeated **K times**.
- Each fold is used as validation once.
- Final score = average of all fold scores.

Dataset
   ↓
K Folds
   ↓
Train + Validation
   ↓
Repeat K Times
   ↓
Average Score

##  Advantages

Uses the dataset more efficiently.
Provides a more reliable performance estimate.
Reduces dependence on a single train/validation split.
Helps detect overfitting.
Useful for model comparison.
Useful for hyperparameter tuning.
Every sample gets a chance to be used for validation.

## Disadvantages

More computationally expensive.
Model must be trained multiple times.
Can be slow for large datasets.
Not ideal for time-series data when random folds break temporal order.
Requires careful handling of data preprocessing to avoid data leakage.

## Common Types

K-Fold Cross-Validation
Stratified K-Fold
Leave-One-Out Cross-Validation (LOOCV)
Repeated K-Fold

## Key Point 

Cross-Validation
      ↓
Multiple Train/Validation Splits
      ↓
Multiple Scores
      ↓
Average Score
      ↓
Better Performance Estimate

## Code implentation: 

from sklearn.model_selection import cross_val_score

scores = cross_val_score(X_scaled, y, cv=5, scoring='accuracy')

scores.mean()

score_position: int = 1
score_position_short_form: None | str = None

for score in scores:
  if score_position==1: 
    score_position_short_form = 'st'
  elif score_position==2: 
    score_position_short_form = 'nd'
  elif score_position==3: 
    score_position_short_form = 'rd'
  else: 
    score_position_short_form = 'th'

  print(f"{score_position}{score_position_short_form} Fold Score: {round(score*100,2)}")
  score_position+=1
