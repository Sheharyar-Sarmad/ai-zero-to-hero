# Prerequisites — What You Need Before GenAI

Before diving into GenAI, it helps to know what's ahead. This file
lists what you'll actually use day-to-day, what you'll only meet in
interviews, and why both matter.

---

## What You'll Actually Use

### 1. Python Programming
You will write Python every single day in GenAI.

Not "maybe" — *every day*. Every LLM API call, every embedding, every
RAG pipeline, every agent loop is Python. If you can't write a
function, read a list comprehension, and handle a dict, you'll be
stuck on the first lesson.

You do NOT need to be an expert. You do NOT need to know async,
decorators, or metaclasses. But you do need:

- Variables, functions, loops, conditionals
- Lists, dicts, sets, tuples
- Reading and writing files
- Installing packages with `pip`
- Basic virtual environments (`venv` or `conda`)
- Calling an HTTP API and parsing JSON

If you have that, you're ready. Everything else you'll pick up.

### 2. Basic NLP Concepts
GenAI is built on top of NLP. You will see these terms in every
lesson, every paper, every library:

- **Corpus** — a collection of text. "The dataset."
- **Token** — a piece of text. Could be a word, subword, or character.
- **Tokenizer** — the tool that splits text into tokens.
- **Vocabulary** — the set of all unique tokens a model knows.
- **Bag of Words (BoW)** — representing text as counts of words,
  ignoring order.
- **TF-IDF** — a way to weight words by how important they are to
  a document relative to the whole corpus.
- **Embeddings** — dense vectors that capture the *meaning* of text.
  The backbone of everything in GenAI.

If you've done any NLP, you already know these. If not, spend one
evening on them — they'll pay back a hundred times.

### 3. Transformers (Conceptual Understanding)
You don't need to implement attention from scratch. But you do need
to understand:

- What a token is (and why cost scales with tokens)
- What a context window is (and why it's limited)
- What attention does (weighted lookup over tokens)
- What a decoder-only model is (GPT, Llama)
- What an encoder-decoder is (T5, BART)
- Why attention is O(n²) — and why that matters for long context

If you've read the `20_transformers/` module, you already have all
of this. If not, skim it once. Don't memorize — just build the
mental model.

---

## What You Won't Use (But Should Still Know)

Here's the honest part: **you will not use classical Machine Learning
or Deep Learning fundamentals in most GenAI work.**

You will not:

- Train a model from scratch
- Write backprop by hand
- Tune XGBoost hyperparameters
- Build a CNN
- Implement gradient descent

You will call APIs. You will prompt models. You will build pipelines.
That's the job.

**BUT** — and this is important — you still need to understand ML
and DL for three reasons:

### Reason 1 — Interviews
Every AI engineer interview includes ML/DL questions. Not because
you'll use them, but because they filter out people who don't
understand what's happening under the hood.

Expect questions like:

- "What's the difference between supervised and unsupervised learning?"
- "What's overfitting, and how do you detect it?"
- "Explain gradient descent."
- "What's a loss function? Why cross-entropy for classification?"
- "What's the bias-variance tradeoff?"
- "Why does dropout help regularize a neural network?"

You can't skip these. They're the entry fee.

### Reason 2 — GenAI Makes More Sense With ML/DL
If you've studied ML and DL, GenAI concepts click *immediately*.

| GenAI concept | You'll understand it faster if you know... |
|---|---|
| Fine-tuning | Transfer learning from classical ML |
| Embeddings | Vector representations from NLP |
| RAG | Retrieval + similarity search from IR |
| Temperature | Sampling from probability distributions |
| Loss curves | Regression training visualization |
| Overfitting in LLMs | The classical bias-variance tradeoff |
| Few-shot prompting | Meta-learning intuition |

Every concept in GenAI is a repackaging of an ML/DL idea you've seen
before. Know the originals and the new versions feel obvious.

### Reason 3 — You'll Be Expected to Reason About Trade-offs
Your job will often require decisions like:

- "Should we fine-tune or use RAG?"
- "Is this a classification task or a generation task?"
- "Do we need a bigger model, or better prompts?"
- "Why is this model hallucinating?"

To answer these well, you need ML intuition — not to code it, but to
think in it.

---

## What You *Don't* Need

To be clear, you do **not** need:

- ❌ A PhD or research background
- ❌ Advanced math (linear algebra proofs, calculus derivations)
- ❌ Distributed training experience
- ❌ Custom CUDA kernels
- ❌ Years of production ML experience

If you have Python + basic NLP + conceptual transformers + classical
ML/DL fundamentals, you're overqualified to start GenAI.

---

## The Minimal Checklist

Before starting GenAI, confirm you can say **yes** to these:

- [ ] I can write a Python function, loop, and dict comprehension
- [ ] I can call an HTTP API and parse the JSON response
- [ ] I know what a token is
- [ ] I know what a corpus is
- [ ] I know what an embedding is
- [ ] I understand what attention does (even at a high level)
- [ ] I know what overfitting is
- [ ] I know what a loss function does
- [ ] I know the difference between classification and regression

If most of these are yes — **start GenAI now.**

If a few are no — spend a weekend on the gaps. You don't need months.
You need the intuition, not mastery.

---

Welcome to GenAI.