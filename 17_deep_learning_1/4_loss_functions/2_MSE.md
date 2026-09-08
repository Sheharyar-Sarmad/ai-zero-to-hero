

# MSE — Mean Squared Error

**Mean Squared Error (MSE)** is a loss function commonly used for **regression problems**. It measures the average squared difference between the actual values and the predicted values.

## Formula

$$
MSE = \frac{1}{n}\sum_{i=1}^{n}(y_i-\hat{y}_i)^2
$$

## Explanation of the Formula

- **$n$** → Total number of observations/data points.
- **$i$** → Index of the current observation, starting from 1.
- **$y_i$** → Actual value for the $i$-th observation.
- **$\hat{y}_i$** → Predicted value for the $i$-th observation.
- **$(y_i-\hat{y}_i)$** → Difference between the actual and predicted value, also called the **error**.
- **$(y_i-\hat{y}_i)^2$** → Squared error.
- **$\sum$** → Adds all the squared errors together.
- **$\frac{1}{n}$** → Divides the total squared error by the number of observations to calculate the average.