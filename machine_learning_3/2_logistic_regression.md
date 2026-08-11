

# Logistic Regression Notes

> **Machine Learning | Supervised Learning | Classification Algorithm**


# What is Logistic Regression?

Logistic Regression is a **Supervised Machine Learning Algorithm** used for **Classification Problems**. Unlike Linear Regression, Logistic Regression predicts the **probability** that a data point belongs to a particular class. The output is always between: 
**0 and 1**

# Best Fit Line: 

- To create the best fit line the basic formula was this:

**h thetha of x = thetha 0 + (thetha 1 . x of 1)**


# 50% Threshold (Decision Boundary):

- In binary classification, a probability of 50% (0.5) is commonly used as the cutoff point. If the predicted probability is greater than or equal to 50%, the sample is classified as the positive class, if it is less than 50%, it is classified as the negative class.

Example:

- Predicted probability = 0.72 (72%) → Positive class 
- Predicted probability = 0.26 (26%) → Negative class 

- The 50% threshold is the default choice but can be changed depending on the problem (e.g., 70%, 80%, etc., if higher confidence is required).

# Problems:

> Outliers: 

An outlier is a data point that is far away from the rest of the data. A weight of eg 268 kg is unusually high compared to other samples, so it can pull the **best-fit line toward itself and reduce the model's accuracy**. 268 kg is an outlier because it is much larger than the other weights. Outliers can distort the best-fit line and **negatively affect** the **model's predictions**. **Outliers should not be removed automatically**. Remove them only if they are errors or invalid data. If they are genuine observations, keep them, although they may influence the model.

> Results can be negative 0< or positive 1>

The prediction **hθ(x) = θ(0) + θ(1) x(1)** can produce values **less than 0 or greater than 1**. Probabilities must always lie **between 0 and 1**, so these outputs are not valid probabilities. To solve this problem, logistic regression squashes the linear output using the **Sigmoid (Logistic) Function**, which always returns a value between 0 and 1.

Formula of Sigmoid activation is: 
- **h0(x) = g(0(0)+ 0(1) . 0(x))** 
- e is also called as eulars numbers and its mathematical constant whose value is 2.71828. it gives smooth curves to straight line.
- here **g = 1 / 1 + e power -z**
- and z = (0(0) + 0(1) . 0(x))

so the final formual is: **h0(x) = g(1 / 1 + e power(0(0) + 0(1) . x(1)))**

