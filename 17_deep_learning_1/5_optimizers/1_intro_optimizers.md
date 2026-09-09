


# Introduction to Optimizers

An **optimizer** is an algorithm that updates a model's weights to **minimize the loss function**.

Once the loss function tells us *how wrong* the model's predictions are, the optimizer decides *how to change the weights* using the gradients to reduce that loss.

Training a neural network is essentially a repeated cycle of:

1. Make a prediction
2. Calculate the loss
3. Use an optimizer to adjust the weights based on gradients
4. Repeat until the loss is minimized

Different optimizers differ in **how** they use the gradient to update the weights.

---

## Cons of Vanilla (Batch) Gradient Descent

### 1. Uses the Entire Dataset for One Update
- Vanilla Gradient Descent computes the gradient using **all training samples** before making a single weight update.
- This makes each update extremely **slow and computationally expensive**, especially for large datasets.

### 2. High Memory Usage
- Since the entire dataset must be loaded to compute one gradient, it requires a lot of **memory**, which becomes impractical for large-scale data.

### 3. Slow Convergence
- Because updates happen only once per full pass over the data, the model takes a long time to converge, especially early in training when a rough direction would already be useful.

### 4. Can Get Stuck in Local Minima / Saddle Points
- Since the gradient is computed precisely (no noise), it can settle into a **local minimum** or get stuck at a **saddle point** with no randomness to help it escape.

### 5. Not Suitable for Online Learning
- Vanilla GD needs the full dataset upfront, so it can't easily update the model as **new data streams in** one sample at a time.

---

## Stochastic Gradient Descent (SGD)

### What Is It?

**Stochastic Gradient Descent** fixes the core speed/memory problem of vanilla GD by updating the weights using **just one randomly chosen training sample** at a time, instead of the entire dataset.

$$
w = w - \eta \cdot \frac{\partial L_i}{\partial w}
$$

- **$w$** → Weight being updated
- **$\eta$** → Learning rate
- **$\frac{\partial L_i}{\partial w}$** → Gradient of the loss computed on a **single sample $i$**

This means the model updates its weights **after every single training example**, making it much faster per update and suitable for very large or streaming datasets.

```python
model.compile(
    optimizer='sgd',
    loss='mse'
)
```

---

## Cons of Stochastic Gradient Descent

### 1. Very Noisy Updates
- Since each update is based on just **one sample**, the gradient direction can vary a lot from step to step, causing the loss to fluctuate instead of decreasing smoothly.

### 2. Unstable Convergence
- Due to the noise, SGD doesn't settle neatly into the minimum — it tends to **oscillate around** the minimum rather than converging precisely to it.

### 3. Doesn't Fully Utilize Hardware Parallelism
- Processing one sample at a time doesn't take advantage of vectorized/batch operations that GPUs are optimized for, making training **computationally inefficient** compared to processing samples in batches.

### 4. Sensitive to Learning Rate
- Because updates are already noisy, a poorly chosen learning rate can make training even more unstable — too high and it diverges, too low and it takes forever with all that noise.

### 5. Same Learning Rate for All Parameters
- Like vanilla GD, standard SGD still applies **one global learning rate** to every parameter, regardless of how much each one actually needs to change.

## Key Idea

Vanilla Gradient Descent is accurate but slow and memory-heavy since it uses the whole dataset per update. SGD fixes the speed problem by using one sample per update, but introduces noisy, unstable convergence in exchange.