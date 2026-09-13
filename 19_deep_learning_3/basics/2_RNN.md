

# Recurrent Neural Networks (RNN)

## 1. Architecture

An RNN processes sequential data by maintaining a **hidden state** that gets updated at every time step, carrying information from previous steps forward.

### Core Equations

At each time step `t`:

```
h_t = tanh(W_hh · h_(t-1) + W_xh · x_t + b_h)
y_t = W_hy · h_t + b_y
```

Where:
- `x_t` → input at time step t
- `h_t` → hidden state at time step t
- `h_(t-1)` → hidden state from previous time step
- `y_t` → output at time step t
- `W_hh` → weight matrix (hidden → hidden)
- `W_xh` → weight matrix (input → hidden)
- `W_hy` → weight matrix (hidden → output)
- `b_h`, `b_y` → bias terms

### Key Idea
The **same weights** (`W_hh`, `W_xh`, `W_hy`) are shared/reused across all time steps — this is called **parameter sharing**.

### Unrolled View
An RNN is often visualized "unrolled" through time:

```
x1 → [RNN Cell] → h1 → [RNN Cell] → h2 → [RNN Cell] → h3 → ...
        ↑                  ↑                  ↑
        x1                 x2                 x3
```

Each cell is the same network, just applied repeatedly with updated hidden states.

---

## 2. Types of RNN Architectures (based on input/output structure)

| Type | Description | Example Use Case |
|---|---|---|
| One-to-One | Single input, single output | Standard NN (not really RNN) |
| One-to-Many | Single input, sequence output | Image captioning |
| Many-to-One | Sequence input, single output | Sentiment analysis |
| Many-to-Many (equal length) | Sequence in, sequence out (same length) | POS tagging |
| Many-to-Many (different length) | Sequence in, sequence out (diff length) | Machine translation |

---

## 3. Variants of RNN

### a) Vanilla RNN
- Basic version described above.
- Struggles with long-term dependencies due to **vanishing/exploding gradients**.

### b) LSTM (Long Short-Term Memory)
- Introduces **gates**: forget gate, input gate, output gate.
- Maintains a separate **cell state** (`C_t`) for long-term memory.
- Equations:
```
f_t = σ(W_f · [h_(t-1), x_t] + b_f)     # forget gate
i_t = σ(W_i · [h_(t-1), x_t] + b_i)     # input gate
o_t = σ(W_o · [h_(t-1), x_t] + b_o)     # output gate
C̃_t = tanh(W_c · [h_(t-1), x_t] + b_c)  # candidate cell state
C_t = f_t * C_(t-1) + i_t * C̃_t         # new cell state
h_t = o_t * tanh(C_t)                   # new hidden state
```

### c) GRU (Gated Recurrent Unit)
- Simplified version of LSTM with fewer gates (update gate + reset gate).
- Faster to train, often comparable performance.
```
z_t = σ(W_z · [h_(t-1), x_t])           # update gate
r_t = σ(W_r · [h_(t-1), x_t])           # reset gate
h̃_t = tanh(W · [r_t * h_(t-1), x_t])
h_t = (1 - z_t) * h_(t-1) + z_t * h̃_t
```

### d) Bidirectional RNN (Bi-RNN)
- Processes sequence in both forward and backward directions.
- Combines both hidden states for final output.
- Useful when future context matters (e.g., NLP tasks).

### e) Deep (Stacked) RNN
- Multiple RNN layers stacked on top of each other.
- Output of one RNN layer becomes input to the next.

---

## 4. Training RNNs

### Backpropagation Through Time (BPTT)
- Standard backpropagation applied across unrolled time steps.
- Gradients are calculated by summing contributions from all time steps.

### Common Problems
- **Vanishing Gradient**: gradients shrink exponentially over long sequences → early time steps stop learning.
- **Exploding Gradient**: gradients grow uncontrollably → unstable training.

### Fixes
| Problem | Solution |
|---|---|
| Vanishing gradients | Use LSTM/GRU, ReLU variants, careful init |
| Exploding gradients | Gradient clipping |
| Long sequences | Truncated BPTT |

---

## 5. Usage / Applications

- **Natural Language Processing (NLP)**
  - Text generation
  - Machine translation
  - Sentiment analysis
  - Named Entity Recognition (NER)
- **Speech Recognition**
- **Time Series Forecasting**
  - Stock price prediction
  - Weather forecasting
- **Music Generation**
- **Video Analysis** (frame-by-frame sequential processing)
- **Handwriting Recognition**

---

## 6. Advantages

- Handles variable-length sequential input/output.
- Shares parameters across time steps → fewer parameters than fully separate networks per step.
- Captures temporal/sequential dependencies.

## 7. Limitations

- Vanishing/exploding gradient issues (vanilla RNN).
- Sequential computation → hard to parallelize (slower training compared to Transformers).
- Struggles with very long-term dependencies.
- Largely replaced by **Transformers** in modern large-scale NLP tasks.

---

## 8. Quick Comparison: RNN vs LSTM vs GRU

| Feature | RNN | LSTM | GRU |
|---|---|---|---|
| Gates | None | 3 (forget, input, output) | 2 (update, reset) |
| Memory | Hidden state only | Hidden + Cell state | Hidden state only |
| Long-term dependency handling | Poor | Good | Good |
| Training speed | Fast | Slower | Faster than LSTM |
| Parameters | Fewest | Most | Moderate |

---

## 9. Simple Pseudocode (Vanilla RNN Cell)

```python
def rnn_cell(x_t, h_prev, W_xh, W_hh, W_hy, b_h, b_y):
    h_t = tanh(W_xh @ x_t + W_hh @ h_prev + b_h)
    y_t = W_hy @ h_t + b_y
    return h_t, y_t

# Loop over sequence
h = h0
for x_t in sequence:
    h, y_t = rnn_cell(x_t, h, W_xh, W_hh, W_hy, b_h, b_y)
```