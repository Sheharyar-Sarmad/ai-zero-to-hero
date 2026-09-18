# Training and Testing a Transformer

## What training means here
Training is adjusting millions (or billions) of weights so the model's predictions match reality. It's a giant game of trial and error, repeated billions of times.

## The training loop
1. Feed a batch of text.
2. Model predicts the next token at every position.
3. Compare predictions to the true next tokens → loss.
4. Backpropagate → gradients.
5. Optimizer updates the weights.
6. Repeat for millions of batches.

That loop, on repeat, is all of training.

## Teacher forcing (for encoder-decoder models)
During training, the decoder is fed the TRUE previous token, not its own prediction. This makes training faster and more stable — errors don't compound across a sequence. But it creates "exposure bias": the model never learns to recover from its own mistakes, since it never sees them during training.

## Masking during training
A causal mask prevents the decoder from peeking at future tokens. Without it, the model would trivially cheat — copying the answer instead of learning to predict it — and learn nothing useful.

## Loss function — cross-entropy
```
L = -Σ y_true · log(y_pred)
```
For the correct next token, take the model's predicted probability and penalize it for being low. Sum this penalty across the vocabulary, though only the true token's term matters.

This is the standard loss for language modeling because it directly rewards putting high probability on the right answer. Lower loss means the model assigns higher probability to the actual next tokens — it's less "surprised" by real text.

## Optimizer — Adam with warmup
Adam adapts the learning rate per parameter, speeding up or slowing down updates based on recent gradient history. Warmup slowly ramps the learning rate up from near-zero at the start of training to avoid early instability. Warmup is not optional for transformers — without it, training often diverges in the first few hundred steps.

## Learning rate schedule
Training typically moves through three phases: warmup → peak → decay. This shape works because early gradients are noisy (small steps keep things stable), the middle needs speed (large steps make progress), and late training needs precision (small steps settle into a good minimum). Common peak values for transformers are 0.0001 to 0.0005.

## Regularization
- **Dropout** — randomly zero out activations to prevent overfitting.
- **Weight decay** — small penalty on large weights.
- **Early stopping** — stop when validation loss starts rising.

## Training cost — the honest picture
Frontier LLMs cost $10M–$100M+ in compute. That's trillions of tokens × billions of parameters × thousands of GPUs × weeks. For you, this means most engineers fine-tune existing models — they don't pre-train from scratch.

## Testing / inference
At inference, there's no teacher forcing. The model feeds its own predictions back in, one token at a time. This is called autoregressive generation.

## The inference loop
1. Start with a prompt (or `<sos>` token).
2. Model predicts a probability distribution over the vocabulary.
3. Pick a token (greedy / beam / sampling — see next section).
4. Append it to the input.
5. Repeat until `<eos>` or max length.

## Decoding strategies
- **Greedy** — always pick the highest-probability token. Fast, but can be repetitive.
- **Beam search** — keep the top-k sequences alive at each step. Better quality, more compute.
- **Sampling** — temperature, top-k, top-p. Controlled randomness, used for creative output.

## Evaluation metrics
- **Perplexity** — how "surprised" the model is by real text. Lower is better.
- **BLEU** — measures translation quality against reference translations.
- **ROUGE** — measures summarization quality against reference summaries.
- **Human evaluation** — used when automated metrics aren't enough to judge quality.

## Overfitting vs underfitting
Underfit: the model hasn't learned enough — training loss stays high. Overfit: the model memorized training data but fails on new data — training loss keeps dropping while validation loss rises. Watching both curves together tells you which one you're facing.

## The full training pipeline
```
raw data
   ↓
tokenize
   ↓
batch
   ↓
model forward pass
   ↓
loss
   ↓
backprop
   ↓
optimizer step
   ↓
checkpoint
   ↓
evaluate
   ↓
(loop)
```

## What a checkpoint is
A saved snapshot of model weights + optimizer state at a point in training, used to resume training or deploy the model.

## Activation functions recap
Softmax lives at the output layer, turning scores into a probability distribution. GELU/ReLU live inside the feed-forward network, adding non-linearity. Nothing new here — just a reminder of where each lives.

## Common pitfalls
- Skipping warmup, leading to early divergence.
- Overfitting on small datasets without enough regularization.
- Evaluating on training data instead of a held-out set.

## What to remember
- Training = predict → loss → backprop → update, repeated.
- Teacher forcing speeds up training but creates exposure bias.
- Cross-entropy is the standard loss.
- Adam + warmup + decay is the standard optimizer setup.
- Inference is autoregressive — no teacher forcing.

## Where this leaves you
You now have the full picture of how a transformer is built, trained, and used — from attention to backprop to autoregressive generation. The next module moves to GenAI: building with these models instead of training them.