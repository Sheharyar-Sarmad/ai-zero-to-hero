

# Bidirectional RNNs and Deep (Stacked) RNNs

We already know how a normal RNN works, how it trains (BPTT), and why it struggles with vanishing/exploding gradients.

Now let's look at two upgrades to the basic RNN. These don't fix the gradient problem — they just make the RNN **smarter about reading** (Bidirectional) and **smarter about understanding** (Deep/Stacked).

---

## PART A — Bidirectional RNNs

### 1. The problem with a normal RNN

A normal RNN is like reading a text message **one word at a time, left to right**, and never looking ahead.

That's a problem for sentences like this:

- "The **bank** of the river was flooded." → bank = riverbank
- "The **bank** approved the loan." → bank = money bank

At the moment the RNN sees the word "bank," it has **no idea** which meaning is correct. It needs to see the words that come *after* "bank" to understand it. But a normal RNN can't peek ahead — it's stuck moving in one direction only.

### 2. What a Bidirectional RNN is

A Bidirectional RNN (BiRNN) fixes this by using **two RNNs instead of one**:

- One RNN reads the sentence **forward** (left → right)
- Another RNN reads the same sentence **backward** (right → left)

At every time step, both RNNs produce their own hidden state. These two hidden states are then **combined** (usually by concatenating them, sometimes by adding them) to make the final output for that word.

Think of it like two friends reading the same book — one starts from page 1, the other starts from the last page — and then they compare notes on every page.

### 3. How it works step by step

For a sentence with words x1, x2, x3:

- **Forward RNN** reads: x1 → x2 → x3
- **Backward RNN** reads: x3 → x2 → x1
- At each position (say x2), we now have:
  - a forward hidden state (knows everything *before* x2)
  - a backward hidden state (knows everything *after* x2)
- Combine them → final representation of x2 has context from **both sides**

### 4. Why this helps

The network now understands each word using its **full context** — past AND future.

This is super useful for:
- **Named Entity Recognition (NER)** — deciding if "Apple" means the fruit or the company
- **Sentiment analysis** — understanding the full meaning of a sentence before judging tone
- **POS tagging** — figuring out if a word is a noun or verb based on the whole sentence

### 5. When NOT to use bidirectional

Bidirectional RNNs need the **entire sequence available at once**. That means they don't work for real-time or streaming tasks.

Example: predicting the next word while someone is **speaking live** — you literally don't know the future words yet, because they haven't been said. It's like trying to guess the ending of a movie that hasn't been filmed yet.

So bidirectional RNNs are great for analyzing complete sentences, but useless for live prediction tasks.

### 6. Diagram — Bidirectional RNN

```
Input:        x1        x2        x3
              │         │         │
              ▼         ▼         ▼
Forward:   ┌─────┐   ┌─────┐   ┌─────┐
   h1 ────►│ RNN │──►│ RNN │──►│ RNN │────► h3
           └─────┘   └─────┘   └─────┘

Backward:  ┌─────┐   ┌─────┐   ┌─────┐
   h1 ◄────│ RNN │◄──│ RNN │◄──│ RNN │◄──── h3
           └─────┘   └─────┘   └─────┘
              │         │         │
              ▼         ▼         ▼
Combine:  [fwd+bwd]  [fwd+bwd]  [fwd+bwd]
              │         │         │
              ▼         ▼         ▼
Output:      y1        y2        y3
```

Each output (y1, y2, y3) is built from **both directions** at once.

---

## PART B — Deep (Stacked) RNNs

### 7. What a Deep RNN is

A Deep RNN (also called a Stacked RNN) is what you get when you take multiple RNN layers and **stack them on top of each other**, like layers in a cake.

- **Layer 1** takes the raw input sequence and processes it
- **Layer 2** takes Layer 1's outputs (not the raw input) and processes those
- **Layer 3** takes Layer 2's outputs, and so on

Each layer passes its sequence of outputs up to the next layer.

### 8. Why depth helps

This is similar to how a school works:

- Lower layers = elementary school → learn simple stuff (letters, basic words, short patterns)
- Higher layers = high school/college → learn complex stuff (phrases, meaning, tone, sentiment)

Or think of it like a company building:
- **Ground floor workers** handle simple, repetitive tasks
- **Top floor executives** make big-picture decisions based on what the lower floors already processed

Each layer builds on the last one, learning increasingly abstract patterns instead of starting from scratch.

### 9. Trade-offs

Stacking layers isn't free. More layers means:

- **More power** — can learn more complex patterns
- **More compute** — slower to train, needs more memory
- **Risk of overfitting** — the model might just memorize the training data instead of learning general patterns
- **Harder to train** — gradients now have to travel through more layers (on top of already traveling through time), making vanishing/exploding gradients even more likely

So depth is a trade-off: more capability, but more cost and more training difficulty.

### 10. Diagram — Deep (Stacked) RNN

```
Layer 3:   ┌─────┐   ┌─────┐   ┌─────┐
           │ RNN │──►│ RNN │──►│ RNN │   (complex patterns: meaning, sentiment)
           └─────┘   └─────┘   └─────┘
              ▲         ▲         ▲
Layer 2:   ┌─────┐   ┌─────┐   ┌─────┐
           │ RNN │──►│ RNN │──►│ RNN │   (mid-level patterns: phrases)
           └─────┘   └─────┘   └─────┘
              ▲         ▲         ▲
Layer 1:   ┌─────┐   ┌─────┐   ┌─────┐
           │ RNN │──►│ RNN │──►│ RNN │   (simple patterns: letters, short words)
           └─────┘   └─────┘   └─────┘
              ▲         ▲         ▲
Input:        x1        x2        x3
```

Information flows **upward** through the layers, and **forward** through time within each layer.

---

## PART C — Combining Both

### 11. Stacked + Bidirectional

You can combine both ideas: build a Deep RNN where **each layer is itself bidirectional**.

So every layer has a forward RNN and a backward RNN, and the combined output of that layer feeds into the next layer (which is also bidirectional).

This "Deep Bidirectional RNN" setup was extremely popular in real-world NLP systems (translation, tagging, question answering) **before Transformers took over**. Models like deep BiLSTMs were the state of the art for years.

---

## Summary

- **Bidirectional** adds future context — the model reads both forward and backward so it understands each word using the whole sentence.
- **Deep (Stacked)** adds hierarchy — lower layers learn simple patterns, higher layers learn complex, abstract patterns.
- Use **Bidirectional** when the full sequence is available upfront (not real-time), like tagging or classifying whole sentences.
- Use **Deep** when the task needs more complex understanding and you have enough data/compute to support it.
- Real-world examples: **Bidirectional** → Named Entity Recognition (e.g. detecting names/places in text). **Deep** → Machine translation (e.g. English to French).

### Comparison Table

| Variant | What it adds | Best for |
|---|---|---|
| Bidirectional | Future context | NER, sentiment, POS |
| Deep | Hierarchical features | Complex NLP, translation |