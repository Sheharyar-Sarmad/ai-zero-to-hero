

# GridSearchCV

## Definition

**GridSearchCV** is a hyperparameter tuning technique that tries **every possible combination** of given hyperparameter values and evaluates each combination using **Cross-Validation (CV)**.

---

## What is a Grid?

A **grid** contains the hyperparameter values that we want to search.

Example with KNN:

```python
param_grid = {
    "n_neighbors": [1, 3, 5, 7, 9, 11, 13],
    "weights": ["uniform", "distance"],
    "metric": ["manhattan", "euclidean"]
}

Each value is combined with every other possible value.

7 n_neighbors × 2 weights × 2 metrics = 28 combinations
What is CV?

CV = Cross-Validation

cv=5 means every hyperparameter combination is evaluated using 5 cross-validation folds.

Combination
     ↓
Fold 1 → Accuracy
Fold 2 → Accuracy
Fold 3 → Accuracy
Fold 4 → Accuracy
Fold 5 → Accuracy
     ↓
Average Accuracy

The average accuracy becomes the CV score for that combination.

## GridSearchCV Process

Grid
↓
All possible combinations
↓
Cross-Validation for each combination
↓
Accuracy for each fold
↓
Average accuracy for each combination
↓
Compare all average scores
↓
Best average score
↓
Best Hyperparameters

## Example

K = 5, weights = uniform, metric = euclidean

Fold 1 → 83%
Fold 2 → 81%
Fold 3 → 85%
Fold 4 → 84%
Fold 5 → 82%

Average CV Score → 83%

GridSearchCV repeats this process for every combination and selects the combination with the highest average CV score.

Big-O Time Complexity
O(P × K × T)
P → number of hyperparameter combinations
K → number of CV folds
T → training time of the model

- Example:

28 combinations × 5 folds = 140 model fits

## Code

from sklearn.model_selection import GridSearchCV

grid = GridSearchCV(
    model,
    param_grid,
    cv=5,
    scoring="accuracy"
)

grid.fit(X_train, y_train)

grid.best_params_
grid.best_score_
grid.best_estimator_
best_params_ → best hyperparameters
best_score_ → highest average CV score
best_estimator_ → best model

## Key Idea

    Grid = WHAT values to try
    CV = HOW to evaluate them
    GridSearchCV = tries everything and selects the best combination