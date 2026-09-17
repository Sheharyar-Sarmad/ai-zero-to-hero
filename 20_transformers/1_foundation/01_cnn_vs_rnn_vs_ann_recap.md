# 1. CNN vs RNN vs ANN — A Complete Recap

> Each architecture exists because the previous one couldn't handle a specific kind of structure in the data — and seeing that progression side by side is what makes transformers make sense.

## Learning Objectives

- State the core operation, input shape, and main weakness of ANN, CNN, and RNN from memory
- Compare all three architectures directly using shared criteria, not in isolation
- Trace how each architecture emerged specifically to fix the previous one's blind spot
- Walk through the same input sentence and describe how each architecture would actually process it
- Identify the specific gap that remains after RNNs — the gap transformers are built to close

## Prerequisites

- ANN: dense layers, forward propagation, backpropagation, activation functions, optimizers
- CNN: convolution, pooling, weight sharing, translation invariance
- RNN / LSTM / GRU: hidden state, recurrence, gating, vanishing gradients
- Practical experience with a sequence model from your QuoteLab project

## 1.1 Why Revisit the Basics

This is a bridge, not a new lesson. You already know how each of these architectures works internally. What you have not done yet is line them up next to each other and ask "what is each one actually good at, and why did we need the next one." That comparison is the whole point of this file. Once it's sharp in your head, the motivation for transformers in the next lesson will feel obvious rather than assumed.

## 1.2 ANN — Fully Connected Networks

**Core idea.** Every neuron in a layer connects to every neuron in the next layer. There is no assumption built into the architecture about how inputs relate to each other spatially or temporally.

**Input shape.** A flat vector. If your data has structure — pixels arranged in a grid, words in an order — that structure has to be discarded or manually engineered into features before it reaches the network.

**Strengths.** Simple, general-purpose, works fine on tabular data where there is no meaningful notion of "neighboring" features.

**Weaknesses.** No concept of locality or order. Flatten an image into a vector and the network has no idea that two pixels were adjacent. Flatten a sentence into a vector and it has no idea "not" came right before "good."

**When to use it.** Tabular data, simple classification or regression problems, or as the final layers on top of a CNN or RNN once structure has already been extracted.

## 1.3 CNN — Convolutional Neural Networks

**Core idea.** Small filters slide across the input and learn local patterns. The same filter weights are reused at every position — weight sharing — which is what gives CNNs translation invariance: a filter that detects an edge in the top-left corner will detect the same edge if it appears in the bottom-right.

**Input shape.** A grid. Images are the obvious case (2D grid of pixels), but 1D convolutions work over sequences too, sliding over a window of adjacent tokens.

**Strengths.** Very efficient at detecting local structure. Weight sharing keeps parameter counts low relative to a fully connected layer over the same input. Strong default for anything with spatial locality.

**Weaknesses.** The receptive field is fixed by filter size and depth. A single convolutional layer only sees a small local window. To connect information across the whole input, you need to stack many layers, and even then, very long-range dependencies remain hard to capture directly.

**When to use it.** Images, video, and 1D signals where the important patterns are local — audio spectrograms, some genomic sequences, short n-gram-like patterns in text.

## 1.4 RNN — Recurrent Neural Networks

**Core idea.** Process the input one token at a time, maintaining a hidden state that gets updated at every step. Each token's output depends on the current input and everything the hidden state has accumulated so far.

**Input shape.** An ordered sequence. Order is not optional here — it is the entire mechanism by which information flows.

**Strengths.** Naturally suited to sequential data. Can in principle carry information across an arbitrarily long sequence, unlike a CNN's fixed receptive field.

**Weaknesses.** Three specific ones, all covered in depth in your RNN module and worth restating here: processing is strictly sequential so it cannot be parallelized, gradients vanish across long sequences even with LSTM/GRU gating, and encoder-decoder setups compress the whole input into one fixed-size hidden state, which becomes a bottleneck as sequences get longer.

**When to use it.** Language modeling, time series, speech — anything sequential, especially at moderate sequence lengths or when compute is constrained.

## 1.5 The Side-by-Side Comparison

| Architecture | Input type | Core operation | Parallelizable | Handles long-range dependencies | Typical use case | Main weakness |
|---|---|---|---|---|---|---|
| ANN | Flat vector | Dense matrix multiply | Yes | No — no structure at all | Tabular data, simple classification | No notion of order or locality |
| CNN | Grid (2D or 1D) | Convolution with shared weights | Yes | Weak — limited by receptive field | Images, video, local patterns in sequences | Fixed receptive field, needs depth for global context |
| RNN | Ordered sequence | Recurrent hidden-state update | No — strictly sequential | Moderate, degrades over long sequences | Language, time series, speech | Sequential bottleneck, vanishing gradient |

Read the "parallelizable" column carefully. ANN and CNN are both parallelizable across the input — every output can be computed independently given the weights. RNN cannot be, because step `t` depends on step `t-1` by definition. That single difference is a large part of why RNN training is slow relative to the other two, independent of how good its predictions are.

## 1.6 A Concrete Example — One Sentence, Three Architectures

Take the sentence:

```
"The movie was absolutely fantastic"
```

Here is how each architecture would actually handle it.

**ANN** — flatten every word's embedding into one long vector and feed it through dense layers. There is no representation of which word came first, second, or last; "fantastic absolutely was movie the" would produce the exact same input vector if you summed the embeddings, and even with concatenation, the network has no built-in notion that word order carries meaning — it would have to learn any positional pattern from scratch, inefficiently.

```
ANN:  [the] [movie] [was] [absolutely] [fantastic]
              |
              v  flatten + concatenate
      [one long vector] -> Dense -> Dense -> output
```

**CNN** — slide a 1D convolution across windows of adjacent words, picking up local phrase-level patterns like "absolutely fantastic" or "movie was."

```
CNN:  [the] [movie] [was] [absolutely] [fantastic]
              |
              v  1D convolution over 3-word windows
      [the movie was] [movie was absolutely] [was absolutely fantastic]
```

This captures local structure well — "absolutely fantastic" as a unit is exactly the kind of pattern a filter can learn. But if the sentence were longer and the key sentiment word appeared 30 tokens away from a negation, a single convolutional layer would not connect them; you would need to stack many layers to grow the effective receptive field.

**RNN** — process the sentence one word at a time, updating a hidden state at each step.

```
RNN:  [the]        -> h1
      [movie]       -> h2  (built from h1 + "movie")
      [was]         -> h3  (built from h2 + "was")
      [absolutely]  -> h4  (built from h3 + "absolutely")
      [fantastic]   -> h5  (built from h4 + "fantastic")
```

By `h5`, the model has, in principle, accumulated something about the whole sentence — but that "something" is squeezed into one fixed-size vector, and it was built through five sequential steps that cannot run in parallel.

**Transformer** — every word attends to every other word in the same pass, with no sequential dependency.

```
Transformer:
  [the] [movie] [was] [absolutely] [fantastic]
    \      |      |        |          /
     \-----+------+--------+---------/
          every word attends to
          every other word, at once
```

We are not opening up how attention actually computes those connections here — that is the entire subject of the next lesson. For now, just notice the structural difference: no flattening, no fixed window, no sequential chain.

## 1.7 The Progression and the Gap

Each architecture exists to fix a specific limitation in the one before it.

ANN could not represent spatial or sequential structure — everything was a flat, unordered vector.

CNN fixed the spatial case: weight-shared filters gave the network a way to detect local patterns and generalize them across position. But CNN's receptive field is fixed, so it still struggles to connect information across long distances, spatial or otherwise.

RNN fixed the sequential case: an explicit hidden state let the network process order and, in principle, carry information across an arbitrarily long sequence. But it does this at a real cost — one step at a time, with information degrading the further back it has to travel.

The gap that remains after RNN is the one you just watched in the walkthrough above: no way to connect distant tokens directly, and no way to compute the whole sequence in parallel. That gap — direct, parallel access between any two tokens regardless of distance — is exactly what the next lesson opens with.

## Key Takeaways

1. ANN, CNN, and RNN each encode a different assumption about input structure: none, local/spatial, and sequential/ordered, respectively.
2. ANN is parallelizable but structure-blind; CNN is parallelizable and spatially aware but has a fixed receptive field; RNN is sequentially aware but cannot be parallelized.
3. CNN solved ANN's lack of spatial structure through weight-shared local filters.
4. RNN solved the need for sequential order through a recurrent hidden state, at the cost of speed and long-range accuracy.
5. The same sentence processed by all three architectures shows a clear pattern: each adds more structural awareness, but only up to a point.
6. The unresolved gap after RNN — no parallel, direct, long-range connections between tokens — is precisely the motivation for the next lesson.

## Common Misconceptions

- "CNNs can't be used on text at all." False — 1D convolutions over token embeddings are a legitimate technique for capturing local n-gram patterns; they just don't scale to long-range dependencies well.
- "RNNs process the whole sequence at once, they just remember it." False — RNNs process strictly one token at a time; there is no way around this without changing the architecture.
- "A bigger CNN receptive field solves long-range dependency problems." Partially false — stacking layers grows the receptive field, but it grows slowly and adds depth-related training difficulties; it does not give the direct, adaptive connections attention provides.
- "ANN is just a worse version of CNN and RNN." Not quite — ANN is the wrong tool for structured data, but it is still exactly the right tool for genuinely unstructured tabular data, and it is a component inside CNNs and RNNs too, in their final dense layers.

## Next

Continue to `2_introduction_to_transformers.md`