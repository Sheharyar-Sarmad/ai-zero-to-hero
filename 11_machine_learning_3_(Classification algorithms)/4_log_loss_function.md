

# Intro:

- Log Loss Function is also called **Binary Cross Entropy** as well. Log Loss is used because it is designed for **probability predictions**, produces a **convex cost function** for efficient optimization, and strongly penalizes confident **incorrect predictions**.

# Log Loss Function:

- Log Loss (Logarithmic Loss), is the cost function used in Logistic Regression to measure the difference between the predicted probability and the actual class label. It penalizes incorrect predictions, especially when the model is highly confident but wrong.

# Case 1: Predicted Probability = 0.99, Actual Label = 1

- The model predicts a **99% probability** for the correct class.
- Since the prediction is almost correct, the **Log Loss is very small (close to 0)**.

# Case 2: Predicted Probability = 0.50, Actual Label = 1

- The model is **50% confident**, meaning it is completely uncertain.
- The Log Loss is **0.693 ≈ 0.69**, which represents a moderate loss.

> **Rule of 0.69:**  
> Whenever the predicted probability is **0.5**, the Log Loss is always **0.693 (≈ 0.69)**.

# Case 3: Predicted Probability = 0.01, Actual Label = 1

- The model predicts only a **1% probability** for the correct class.
- Since the prediction is confidently wrong, the **Log Loss is very high**.

## Why do we need a Penalty?

In Logistic Regression, the model predicts a **probability** between **0 and 1**. We need a way to measure **how wrong** the prediction is. This measurement is called the **penalty (loss)**.

- **Correct prediction with high confidence** → Very Low Penalty
- **Uncertain prediction (50%)** → Moderate Penalty
- **Wrong prediction with high confidence** → Very High Penalty

# Log Loss Formula:

- Here's the actual Log Loss Formula

J(θ) = -(1 / m) ​m ∑ i=1 ​[ y(i) . log(y^​(i)) + (1−y(i)) . log(1−y^​(i)) ]

> m = No. of samples
> y(i) = actual label(0 or 1)
> y^​(i) = predicted probability(in between 0 to 1)

- For Example: 

> y(i) = 1
> y^(i) = 0.54
> Log Loss = 0.616

# Gradient Descent Curve and Global Minima Point: 

- After finding all the losses we will create a **graph** like we do **Linear Regression** as well of **h0(x) and 0(1)** and we create **gradient descent curve** and after creating that curve we have to find that point where loss is lowest possible average Log Loss and that point is called as **Global Minima Point**.