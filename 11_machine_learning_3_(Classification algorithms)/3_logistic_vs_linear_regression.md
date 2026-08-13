


# Linear Regression

- In Linear Regression, we find the values of **θ₀ (intercept)** and **θ₁ (slope)** to create the **Best Fit Line**.
- The **Cost Function (Mean Squared Error - MSE)** calculates the residual errors, squares them, and computes their average.
- **Gradient Descent** updates θ₀ and θ₁ to minimize the cost function. The goal is to achieve the **minimum possible loss**.

# Logistic Regression

- In Logistic Regression, we also find **θ₀** and **θ₁**, but instead of a straight line, we apply the **Sigmoid Function** to create a **Best Fit Sigmoid (S-shaped) Curve**.
- The **Log Loss (Binary Cross-Entropy)** function measures the prediction error.
- **Gradient Descent** updates θ₀ and θ₁ to minimize the log loss. The goal is to achieve the **minimum possible log loss**.

# Conclusion

- **Linear Regression** predicts continuous numerical values and uses a straight best-fit line with **Mean Squared Error (MSE)** as the cost function.
- **Logistic Regression** predicts probabilities for classification, uses a **Sigmoid Curve**, and minimizes **Log Loss** to make accurate class predictions.
- Both algorithms use **Gradient Descent** to learn the optimal parameters (**θ₀ and θ₁**) by minimizing their respective loss functions.