

# Huber Loss

## Cons of MSE

- MSE squares the errors, so **large errors and outliers are heavily penalized**.
- A single outlier can dominate the loss and distort the model's training.
- This makes MSE **highly sensitive to outliers**.

## Cons of MAE

- MAE treats all errors proportionally, so it is more robust to outliers than MSE.
- However, MAE is **not differentiable at zero**, which makes gradient-based optimization less smooth and convenient.
- The gradient of MAE is constant regardless of error size, so it doesn't slow down as the model gets closer to the correct answer, which can make convergence less stable.

## What Problem Does Huber Loss Solve?

Huber Loss combines the strengths of both MSE and MAE:

- Like **MSE**, it is smooth and differentiable, which helps with stable gradient-based optimization.
- Like **MAE**, it is **robust to outliers**, since large errors aren't squared.

It solves the trade-off problem: you no longer have to choose between sensitivity to outliers (MSE) and non-differentiability at zero (MAE).

## What Is Huber Loss?

Huber Loss behaves differently depending on the size of the error:

- For **small errors**, it behaves like **MSE** (quadratic) — smooth and differentiable.
- For **large errors**, it behaves like **MAE** (linear) — reducing the influence of outliers.

A threshold parameter, **δ (delta)**, controls the point where the loss transitions from quadratic to linear.

## Formula

$$
L_\delta(y, \hat{y}) =
\begin{cases}
\frac{1}{2}(y - \hat{y})^2 & \text{for } |y - \hat{y}| \leq \delta \\
\delta \cdot \left(|y - \hat{y}| - \frac{1}{2}\delta\right) & \text{for } |y - \hat{y}| > \delta
\end{cases}
$$

- **$y$** → Actual value
- **$\hat{y}$** → Predicted value
- **$\delta$** → Threshold that determines the sensitivity to outliers
- When $|y - \hat{y}| \leq \delta$ → quadratic (like MSE)
- When $|y - \hat{y}| > \delta$ → linear (like MAE)

## Key Idea

Huber Loss is quadratic for small errors and linear for large errors, giving it the smoothness of MSE and the outlier-robustness of MAE.