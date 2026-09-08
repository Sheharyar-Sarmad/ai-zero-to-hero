

# Where to Use Which Activation Function

A quick decision guide instead of just theory — this is more "which one do I actually pick" than "how does the math work."

---

## Quick Answer (TL;DR)

- **Hidden layers, default choice** → ReLU
- **Hidden layers, ReLU neurons dying on you** → Leaky ReLU or PReLU
- **Hidden layers, deep/modern architectures, willing to pay extra compute** → Swish
- **Hidden layers, RNNs/LSTMs specifically** → Tanh (sometimes sigmoid for gates)
- **Output layer, regression (predicting a number)** → Linear
- **Output layer, binary classification (yes/no)** → Sigmoid
- **Output layer, multi-class classification** → Softmax (not covered in earlier notes, but worth knowing — it's the multi-class version of sigmoid)

---

## Linear

**Use it for:** the output layer when you're predicting a continuous number — house prices, temperature, stock value, anything where the answer isn't a category.

**Don't use it for:** hidden layers. Stacking linear layers just collapses into one linear function no matter how deep the network is — you lose the whole point of having layers.

---

## Sigmoid

**Use it for:** the output layer of a binary classification problem, where you want the result interpreted as a probability between 0 and 1 (e.g. "is this email spam?"). Also shows up inside LSTM/GRU gates, where you specifically want a 0–1 gating value.

**Don't use it for:** hidden layers in a deep network. It saturates on both ends and isn't zero-centered, so gradients shrink fast and training slows down as the network gets deeper.

---

## Tanh

**Use it for:** hidden layers in shallower networks, or in RNNs/LSTMs, where zero-centered output actually matters for how signals combine over time. Also occasionally used when you specifically want output in the (-1, 1) range.

**Don't use it for:** very deep feedforward networks or CNNs — it still saturates at the extremes, so ReLU-family functions usually win there.

---

## ReLU

**Use it for:** hidden layers, basically by default. CNNs, feedforward nets, most standard architectures — start here unless you have a specific reason not to.

**Don't use it for:** situations where you're seeing a lot of dead neurons (outputs stuck at zero, no learning happening). That's your cue to switch to a ReLU variant.

---

## Leaky ReLU

**Use it for:** hidden layers where regular ReLU is causing dying neurons — you're seeing a lot of zero outputs and stalled learning. It's a low-cost, easy swap-in fix.

**Don't use it for:** cases where regular ReLU is already working fine — no need to add complexity if there's no problem to solve.

---

## PReLU

**Use it for:** hidden layers where you want the benefit of Leaky ReLU but don't want to hand-pick the slope value — let the network learn it. Useful on larger datasets where the extra learnable parameters won't easily overfit.

**Don't use it for:** small datasets — the extra learned parameters add overfitting risk without a large enough dataset to justify it.

---

## Swish

**Use it for:** deeper networks or modern architectures (things like EfficientNet use it) where you're chasing a bit more accuracy and can afford the extra compute cost. Worth trying as a drop-in replacement for ReLU if you want to squeeze out better performance.

**Don't use it for:** situations where compute/speed is tight — the sigmoid inside it makes it slower than ReLU, and the accuracy gain isn't guaranteed to be worth it.

---

## Rule of Thumb If You're Unsure

1. Start with **ReLU** for hidden layers. It's the safe, fast default.
2. If training seems stuck or a lot of neurons look dead → try **Leaky ReLU**.
3. If you have the compute budget and want to push accuracy further → try **Swish**.
4. Pick the output layer activation based on the problem type, not preference — linear for regression, sigmoid for binary, softmax for multi-class.