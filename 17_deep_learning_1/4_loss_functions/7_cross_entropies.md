

# Classification Losses — Binary, Categorical & Sparse Categorical Cross-Entropy

## Why Not Use MSE / MAE / Huber / MSLE for Classification?

All the previous losses (MSE, MAE, Huber, MSLE) are designed for **regression**, where outputs are continuous numbers. In **classification**, the model outputs **probabilities**, and we need a loss that measures how well predicted probabilities match the true class. This is where **cross-entropy** losses come in — they measure the difference between two probability distributions (actual vs predicted).

---

# 1. Binary Cross-Entropy (BCE)

## What Is It?

Used when there are exactly **two classes** (e.g., spam/not spam, cat/dog). The model predicts a **single probability** that the sample belongs to class 1.

## Formula

$$
BCE = -\frac{1}{n}\sum_{i=1}^{n}\Big[y_i \log(\hat{y}_i) + (1-y_i)\log(1-\hat{y}_i)\Big]
$$

- **$n$** → Number of observations
- **$y_i$** → Actual label (0 or 1)
- **$\hat{y}_i$** → Predicted probability of class 1

## Activation Function Used: Sigmoid

Since BCE needs a **single probability between 0 and 1**, the output layer uses the **Sigmoid** activation function:

$$
\sigma(z) = \frac{1}{1+e^{-z}}
$$

- Squashes any real number into the range **(0, 1)**.
- Output represents the probability of the **positive class**.
- The probability of the negative class is simply $1 - \hat{y}$.

```python
model.compile(
    optimizer='adam',
    loss='binary_crossentropy'
)
# Output layer: Dense(1, activation='sigmoid')
```

---

# 2. Categorical Cross-Entropy (CCE)

## What Is It?

Used for **multi-class classification** (more than 2 classes), where labels are **one-hot encoded** (e.g., `[0, 1, 0]` for class 2 out of 3 classes).

## Formula

$$
CCE = -\frac{1}{n}\sum_{i=1}^{n}\sum_{j=1}^{C} y_{ij} \log(\hat{y}_{ij})
$$

- **$n$** → Number of observations
- **$C$** → Number of classes
- **$y_{ij}$** → 1 if sample $i$ belongs to class $j$, else 0 (one-hot)
- **$\hat{y}_{ij}$** → Predicted probability that sample $i$ belongs to class $j$

## Activation Function Used: Softmax

Since CCE needs a **full probability distribution across all classes** (probabilities summing to 1), the output layer uses **Softmax**:

$$
\text{Softmax}(z_i) = \frac{e^{z_i}}{\sum_{j=1}^{C} e^{z_j}}
$$

- Converts raw scores (logits) into probabilities.
- All output probabilities **sum to 1**.
- The class with the highest probability is the predicted class.

```python
model.compile(
    optimizer='adam',
    loss='categorical_crossentropy'
)
# Output layer: Dense(num_classes, activation='softmax')
# Labels must be one-hot encoded, e.g. [0, 0, 1]
```

---

# 3. Sparse Categorical Cross-Entropy (SCCE)

## What Is It?

Mathematically **identical to Categorical Cross-Entropy**, but used when labels are given as **plain integers** (e.g., `2`) instead of one-hot vectors (e.g., `[0, 0, 1]`). It saves you from manually one-hot encoding the labels.

## Formula

Same as CCE, except $y_i$ is the integer class index rather than a one-hot vector:

$$
SCCE = -\frac{1}{n}\sum_{i=1}^{n} \log(\hat{y}_{i, y_i})
$$

- **$y_i$** → True class index (integer) for sample $i$
- **$\hat{y}_{i, y_i}$** → Predicted probability for the correct class $y_i$

## Activation Function to Use: Softmax (same as CCE)

Even though the labels are given as integers instead of one-hot vectors, the model still needs to output a **full probability distribution over all classes** to compute the loss — so the output layer still uses **Softmax**, exactly like Categorical Cross-Entropy.

> The only difference between CCE and SCCE is the **format of the labels** (one-hot vs integer). The activation function, the underlying math, and the model output shape are all the same.

```python
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy'
)
# Output layer: Dense(num_classes, activation='softmax')
# Labels are integers, e.g. 2 (not one-hot)
```

---

## Comparison Table

| Loss | Number of Classes | Label Format | Activation |
|---|---|---|---|
| Binary Cross-Entropy | 2 | 0 or 1 | Sigmoid |
| Categorical Cross-Entropy | > 2 | One-hot encoded | Softmax |
| Sparse Categorical Cross-Entropy | > 2 | Integer class index | Softmax |

## Key Idea

- **Binary Cross-Entropy** → 2 classes → **Sigmoid** → single probability output.
- **Categorical Cross-Entropy** → multi-class, one-hot labels → **Softmax** → probability distribution.
- **Sparse Categorical Cross-Entropy** → multi-class, integer labels → **Softmax** (same as CCE, just avoids manual one-hot encoding).