

# Hyperparameter Tuning

## Definition

**Hyperparameter tuning** = finding the best hyperparameter values for a model.

## Methods

* **Manual Search** → Try different values manually and compare model performance.
* **GridSearchCV** → Tests every combination of given hyperparameters using cross-validation.
* **RandomizedSearchCV** → Tests a fixed number of random hyperparameter combinations.

---

## Ridge Regression

**L2 Regularization**

Main hyperparameter:

```text
alpha
```

```python
param_grid = {
    "alpha": [0.01, 0.1, 1, 10, 100]
}

grid = GridSearchCV(Ridge(), param_grid, cv=5, scoring="r2")
grid.fit(X_train, y_train)

grid.best_params_
grid.best_score_
```

---

## Lasso Regression

**L1 Regularization**

Main hyperparameter:

```text
alpha
```

```python
param_grid = {
    "alpha": [0.001, 0.01, 0.1, 1, 10]
}

grid = GridSearchCV(Lasso(), param_grid, cv=5, scoring="r2")
grid.fit(X_train, y_train)
```

Can make coefficients exactly `0`.

---

## Decision Tree

Important hyperparameters:

```text
max_depth
min_samples_split
min_samples_leaf
criterion
```

```python
param_grid = {
    "max_depth": [3, 5, 7, 10, None],
    "min_samples_split": [2, 5, 10],
    "min_samples_leaf": [1, 2, 4]
}

grid = GridSearchCV(
    DecisionTreeClassifier(),
    param_grid,
    cv=5,
    scoring="accuracy"
)
```

`max_depth` controls tree complexity.

---

## KNN

Important hyperparameters:

```text
n_neighbors
weights
metric
```

```python
param_grid = {
    "n_neighbors": [3, 5, 7, 9, 11],
    "weights": ["uniform", "distance"],
    "metric": ["euclidean", "manhattan"]
}

grid = GridSearchCV(
    KNeighborsClassifier(),
    param_grid,
    cv=5,
    scoring="accuracy"
)
```

Small `k` → more complex/noisy.

Large `k` → smoother/simple.

**Scaling is important.**

---

## SVM

Important hyperparameters:

```text
C
kernel
gamma
```

Common kernels:

```text
linear
rbf
poly
sigmoid
```

```python
param_grid = {
    "C": [0.1, 1, 10, 100],
    "kernel": ["linear", "rbf", "poly"],
    "gamma": ["scale", "auto"]
}

grid = GridSearchCV(
    SVC(),
    param_grid,
    cv=5,
    scoring="accuracy"
)
```

`C` → penalty for errors.

`gamma` → influence of individual points.

**Scaling is important.**

---

## Random Forest

Important hyperparameters:

```text
n_estimators
max_depth
min_samples_split
min_samples_leaf
max_features
```

```python
param_grid = {
    "n_estimators": [100, 200, 300],
    "max_depth": [None, 5, 10],
    "min_samples_split": [2, 5],
    "min_samples_leaf": [1, 2]
}

grid = GridSearchCV(
    RandomForestClassifier(),
    param_grid,
    cv=5,
    scoring="accuracy"
)
```

`n_estimators` → number of trees.

More trees → generally more stable but more computation.

---

## Best Model

```python
grid.best_params_       # Best hyperparameters
grid.best_score_        # Best CV score
grid.best_estimator_    # Best trained model
```

## Workflow

```text
Baseline Model
↓
Choose Hyperparameters
↓
GridSearchCV / RandomizedSearchCV
↓
Cross-Validation
↓
Best Parameters
↓
Final Test Evaluation
```
