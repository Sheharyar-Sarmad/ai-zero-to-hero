
# MSE vs Cost Function

| | **MSE** | **Cost Function** |
|---|---|---|
| Full form | Mean Squared Error | Cost Function |
| Purpose | Measures squared prediction error | Measures the overall error/objective of a model |
| Formula | $MSE = \frac{1}{n}\sum_{i=1}^{n}(y_i-\hat{y}_i)^2$ | Depends on the problem |
| Used for | Mainly regression | Regression and classification |
| Examples | MSE | MSE, Binary Cross-Entropy, etc. |

## MSE

**MSE is a specific loss function** that calculates the average squared difference between actual and predicted values.

$$
MSE = \frac{1}{n}\sum_{i=1}^{n}(y_i-\hat{y}_i)^2
$$

## Cost Function

**Cost Function is the overall objective that a model tries to minimize during training.** It can use different loss functions depending on the problem.

- **$J(\theta)$** → Cost function
- **$n$** → Number of observations
- **$y_i$** → Actual value
- **$\hat{y}_i$** → Predicted value
- **$\sum$** → Sum of errors
- **$\frac{1}{n}$** → Average

> **Key idea:** The cost function tells us how wrong the model is overall. The optimizer tries to minimize it.

```text
Regression
    ↓
MSE can be the cost function

Binary Classification
    ↓
Binary Cross-Entropy can be the cost function