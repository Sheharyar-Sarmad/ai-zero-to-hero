# Linear Regression

## Definition

**Linear Regression** models the linear relationship between one or more independent variables (**features**) and a dependent variable (**target**). It is primarily used to predict **continuous numerical outputs**.

---

## Core Equation

### Simple Linear Regression

$$
y = \beta_0 + \beta_1x + \epsilon
$$

### Multiple Linear Regression

$$
y = \beta_0 + \beta_1x_1 + \beta_2x_2 + \cdots + \beta_nx_n + \epsilon
$$

### Terms

- **$y$** → Target / dependent variable
- **$\beta_0$** → Intercept
- **$\beta_i$** → Coefficients / feature weights
- **$x_i$** → Input features
- **$\epsilon$** → Error / noise

---

## Objective

The goal of Linear Regression is to find the best values for the coefficients that minimize the **Sum of Squared Errors (SSE)**.

$$
SSE = \sum_{i=1}^{n}(y_i - \hat{y}_i)^2
$$

Where:

$$
\hat{y}_i = \beta_0 + \beta_1x_{i1} + \beta_2x_{i2} + \cdots + \beta_nx_{in}
$$

- $y_i$ → Actual value
- $\hat{y}_i$ → Predicted value
- $y_i - \hat{y}_i$ → Error / residual

---

## Solving Methods

| Method | Approach | When to Use |
|---|---|---|
| **OLS (Normal Equation)** | $\beta = (X^TX)^{-1}X^Ty$ | Small datasets, exact solution |
| **Gradient Descent** | Iterative parameter updates | Large datasets |

### Normal Equation

$$
\beta = (X^TX)^{-1}X^Ty
$$

### Gradient Descent Update

$$
\beta_j = \beta_j - \alpha \frac{\partial SSE}{\partial \beta_j}
$$

Where:

- **$\beta_j$** → Model parameter
- **$\alpha$** → Learning rate
- **$\frac{\partial SSE}{\partial \beta_j}$** → Gradient of the error with respect to the parameter

---

## Key Assumptions

### 1. Linearity

There should be a linear relationship between the features ($X$) and the target ($y$).

### 2. Independence

Observations should be independent of one another.

### 3. Homoscedasticity

The variance of the errors should remain approximately constant across different predicted values.

### 4. Normality

The errors should be approximately normally distributed, especially when performing statistical inference.

---

## Evaluation Metrics

| Metric | Formula | Meaning |
|---|---|---|
| **$R^2$** | $1 - \frac{SSE}{SST}$ | Percentage of variance explained by the model |
| **MSE** | $\frac{1}{n}\sum(y_i-\hat{y}_i)^2$ | Average squared prediction error |
| **RMSE** | $\sqrt{MSE}$ | Average error in the same units as $y$ |

### Total Sum of Squares (SST)

$$
SST = \sum_{i=1}^{n}(y_i-\bar{y})^2
$$

Where:

- **$y_i$** → Actual value
- **$\bar{y}$** → Mean of actual target values

---

## Coefficient Interpretation

### Slope / Coefficient ($\beta_i$)

A coefficient represents the expected change in the target ($y$) for a **1-unit increase** in feature $x_i$, while holding all other features constant.

> Example: If $\beta_1 = 5$, then increasing $x_1$ by 1 unit increases the predicted $y$ by 5 units, assuming other features remain constant.

### Intercept ($\beta_0$)

The predicted value of $y$ when all features are equal to 0.

---

## Regularization

Regularization adds a penalty to the loss function to reduce overfitting.

| Type | Penalty | Effect |
|---|---|---|
| **Ridge (L2)** | $\lambda\sum\beta_i^2$ | Shrinks coefficients toward zero |
| **Lasso (L1)** | $\lambda\sum|\beta_i|$ | Can shrink some coefficients exactly to zero |

### Ridge Regression

Uses the **L2 penalty**:

$$
\lambda\sum_{i=1}^{n}\beta_i^2
$$

Ridge usually keeps all features but reduces the size of their coefficients.

### Lasso Regression

Uses the **L1 penalty**:

$$
\lambda\sum_{i=1}^{n}|\beta_i|
$$

Lasso can make some coefficients exactly **zero**, effectively performing feature selection.

---

## Pros and Cons

| Pros | Cons |
|---|---|
| ✅ Simple and interpretable | ❌ Assumes a linear relationship |
| ✅ Fast to train | ❌ Sensitive to outliers |
| ✅ Easy to understand | ❌ Cannot naturally capture complex patterns |
| ✅ Requires little tuning | ❌ Can be affected by multicollinearity |

---

## Key Takeaway

> **Linear Regression finds the best-fit line or hyperplane by minimizing the difference between actual and predicted values, usually through squared errors.**

The model learns **coefficients** that represent the relationship between features and the target.

$$
\hat{y} = \beta_0 + \beta_1x_1 + \beta_2x_2 + \cdots + \beta_nx_n
$$

- **$\beta_0$** → Starting point / intercept
- **$\beta_i$** → Influence of each feature
- **$\hat{y}$** → Predicted value

**In simple words:**

> Linear Regression learns how changes in input features are related to changes in a continuous target value.