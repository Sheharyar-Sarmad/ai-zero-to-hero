


# Backpropagation — Concise Notes

## 1. Why Backpropagation?
A network starts with random weights that produce poor predictions. Training repeatedly adjusts these weights so predictions get better over time. Backpropagation is the step that figures out *how* each weight should change to reduce the error.

```
Input → Forward Propagation → Prediction → Loss → Backpropagation
→ Gradients → Optimizer → Updated Weights → Repeat
```

## 2. Forward Propagation
This is how data flows through the network to produce a prediction: input → output. Each neuron computes a weighted sum of its inputs plus a bias, then passes it through an activation function.

$$ z = x_1w_1 + x_2w_2 + ... + x_nw_n + b, \qquad a = f(z) $$

For binary classification, the output layer commonly uses **sigmoid**, which squashes the result into a probability between 0 and 1:
$$ \hat{y} = \frac{1}{1+e^{-z}} $$
e.g. output 0.85 → 85% chance of class 1.

## 3. Weights & Bias
**Weights** control how much influence each input has on a neuron — bigger weight, stronger effect. **Bias** shifts the output up or down independently of the input, giving the model more flexibility. Training's whole job is to find good values for these.

## 4. Loss
Loss is a single number that measures how wrong a prediction is. A good prediction gives low loss; a bad one gives high loss. For binary classification, we typically use cross-entropy loss:
$$ L = -[y\log(\hat{y}) + (1-y)\log(1-\hat{y})] $$
The entire goal of training is to **minimize this loss**.

## 5. Gradient
A gradient tells us how sensitive the loss is to a small change in a parameter — essentially, "if I nudge this weight, how much does the loss move?"
$$ \frac{\partial L}{\partial w} $$
- Positive gradient → loss increases with the weight → decrease the weight.
- Negative gradient → loss decreases with the weight → increase the weight.
- Larger magnitude → that parameter has more influence on the loss.

## 6. Backpropagation
Backpropagation is the algorithm that computes the gradient of the loss with respect to *every* parameter in the network, layer by layer, moving backward from the output toward the input.

```
Forward:  Input → Layer 1 → Layer 2 → Output → Loss
Backward: Loss → Gradients(Layer 2) → Gradients(Layer 1)
```

Important: backprop does **not** send the original input data backward — it only propagates gradient (error signal) information.

## 7. Chain Rule
Backprop relies on the calculus chain rule to compute gradients across multiple chained operations. If $x \rightarrow z \rightarrow a \rightarrow L$, then:
$$ \frac{dL}{dx} = \frac{dL}{da}\cdot\frac{da}{dz}\cdot\frac{dz}{dx} $$

Applying this to a single weight, where $z = wx+b$ and $a = f(z)$:
$$ \frac{\partial L}{\partial w} = \frac{\partial L}{\partial a}\cdot\frac{\partial a}{\partial z}\cdot\frac{\partial z}{\partial w}, \qquad \frac{\partial z}{\partial w}=x $$
$$ \Rightarrow \frac{\partial L}{\partial w} = \frac{\partial L}{\partial a}\cdot\frac{\partial a}{\partial z}\cdot x $$
This is how the error at the output gets traced back to affect an individual weight deep in the network.

## 8. Updating Weights
Once we have the gradient, the optimizer nudges the weight in the opposite direction to reduce loss:
$$ w_{new} = w_{old} - \eta \frac{\partial L}{\partial w} $$

**Example:** old weight = 0.20, gradient = -1.2, learning rate = 0.1
$$ w_{new} = 0.20 - (0.1)(-1.2) = 0.32 $$

## 9. Learning Rate (η)
The learning rate is a hyperparameter that controls *how big* each update step is.
- **Too small** → learning is very slow, takes many steps to converge.
- **Too large** → updates may overshoot the minimum, causing unstable or divergent training.

## 10. Gradient Descent
Gradient descent is the general optimization strategy: repeatedly move parameters in the direction that reduces loss, guided by the gradient.
$$ W \leftarrow W - \eta\nabla_W L $$
The gradient itself points toward *increasing* loss, so gradient descent moves in the **opposite** direction, step by step, toward the low point of the loss curve.

## 11. Optimizers
An optimizer decides exactly *how* to use the computed gradient to update parameters — it's the strategy layer on top of gradient descent.

| Optimizer | Idea |
|---|---|
| SGD | Uses only the current gradient: $W \leftarrow W-\eta\nabla_W L$ |
| Momentum | Adds a "memory" of past gradients to smooth updates |
| RMSProp | Adapts the step size per parameter based on recent gradient magnitude |
| Adam | Combines momentum + adaptive per-parameter scaling |
| AdamW | Adam with proper weight decay (regularization) |

**Key distinction:** the *gradient* tells you how the loss changes; the *optimizer* decides how to translate that into an actual parameter update.

## 12. Worked Example
Given: $x=2,\ w=0.2,\ b=0,\ y=1$

**Forward pass:**
$$ \hat{y} = wx+b = (0.2)(2) = 0.4 $$

**Loss** (squared error):
$$ L = \tfrac{1}{2}(\hat{y}-y)^2 = \tfrac{1}{2}(0.4-1)^2 = 0.18 $$

**Gradient:**
$$ \frac{\partial L}{\partial w} = (\hat{y}-y)x = (-0.6)(2) = -1.2 $$

**Update** (η = 0.1):
$$ w_{new} = 0.2-(0.1)(-1.2) = 0.32 $$

New prediction: $\hat{y} = (0.32)(2) = 0.64$ — closer to the target of 1.0. This incremental correction, repeated many times, is what "learning" actually is.

## 13. Batch, Iteration & Epoch
- **Batch** — a subset of the training data processed together in one step.
- **Iteration / Step** — one full cycle of forward pass → loss → backward pass → optimizer update, done on one batch.
- **Epoch** — one complete pass through the *entire* training dataset (may consist of many iterations).

**Example:** 1000 samples, batch size 100 → 1000/100 = 10 iterations per epoch, so 1 epoch = 10 forward passes + 10 backward passes + 10 updates. (If the whole dataset were one batch, 1 epoch = just 1 of each.)

## 14. Complete Training Cycle
```
Input → Forward Propagation → Prediction → Loss → Backpropagation
→ Gradients → Optimizer → Updated Weights → Next Batch
→ Next Iteration → Next Epoch → Repeat
```

## 15. Core Mental Model
| Stage | Question it answers |
|---|---|
| Forward Propagation | What does the network predict? |
| Loss | How wrong is that prediction? |
| Backpropagation | How does the loss depend on each parameter? |
| Gradient | Which direction should each parameter move? |
| Learning Rate | How large should that move be? |
| Optimizer | How should the gradient actually be applied? |
| Updated Weights | Make the next, hopefully better, prediction |

**Final goal:** find the parameters that minimize the loss.

**In one line:**
`Forward → Loss → Backprop → Gradients → Optimizer → Updated Weights → Repeat`