

# MAE — Mean Absolute Error

**Mean Absolute Error (MAE)** is a loss function that calculates the average absolute difference between actual and predicted values.

## Formula

$$
MAE = \frac{1}{n}\sum_{i=1}^{n}|y_i-\hat{y}_i|
$$

- **$n$** → Number of observations
- **$y_i$** → Actual value
- **$\hat{y}_i$** → Predicted value
- **$|y_i-\hat{y}_i|$** → Absolute error

## Why Do We Need MAE?

MSE squares the errors:

$$
MSE = \frac{1}{n}\sum_{i=1}^{n}(y_i-\hat{y}_i)^2
$$

Because errors are squared, **large errors and outliers are heavily penalized**.

```text
Error = 2   → MSE = 4
Error = 10  → MSE = 100
```

MAE uses absolute values instead:

```text
Error = 2   → MAE = 2
Error = 10  → MAE = 10
```

Therefore, MAE is less sensitive to outliers than MSE.

## MSE vs MAE

| MSE | MAE |
|---|---|
| Squares errors | Takes absolute errors |
| Highly sensitive to outliers | Less sensitive to outliers |
| Penalizes large errors heavily | Penalizes errors proportionally |
| Smooth gradient | Not differentiable at zero |

## Limitation of MSE

MSE can be strongly affected by outliers because it squares the errors.

## Limitation of MAE

MAE is less sensitive to outliers, but it is not differentiable at zero, which can make gradient-based optimization less convenient.

## MAE as a Loss Function

```python
model.compile(
    optimizer='sgd',
    loss='mae'
)
```

The model tries to minimize MAE during training.

## Key Idea

MSE heavily penalizes large errors, while MAE treats errors proportionally and is more robust to outliers.