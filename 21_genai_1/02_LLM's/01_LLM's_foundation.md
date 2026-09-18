# LLM Foundations — Quick-Fire Glossary

> One line (or 3-4 words) per term. No fluff. Read top to bottom = the whole LLM pipeline.

---

## What is an LLM? (The Basics)

**Definition:** An LLM (Large Language Model) is a giant neural network trained to do one simple job — **predict the next word** — and it does that job so well, across so much text, that it ends up able to write, reason, summarize, code, and chat.

**Analogy:** Imagine a person who has read almost the entire internet — every book, article, Wikipedia page, forum post — and their only party trick is: *"give me a sentence, and I'll guess what word comes next."* Turns out, if you get insanely good at that one trick, you accidentally become good at writing essays, answering questions, and holding conversations too.

**In 3-4 words:** *"Next-word prediction machine."*

---

## How LLMs Are Trained (3 Stages)

### Stage 1 — Pre-training (the "read everything" phase)

**What happens:** The model reads massive amounts of raw text (books, websites, code) and repeatedly plays "guess the next word," adjusting its internal numbers (weights) a tiny bit every time it's wrong.

**Analogy:** Like a student who reads millions of pages and, after every sentence, covers up the next word and guesses it — then checks the answer and adjusts their intuition slightly. Do this billions of times → they develop a deep, general sense of language and facts.

**3-4 words:** *"Guess, check, adjust — repeat billions of times."*

### Stage 2 — Fine-tuning / Instruction-tuning (the "become helpful" phase)

**What happens:** The raw next-word-predictor gets trained on examples of good question-answer pairs and instructions, so it learns to actually be *helpful* rather than just autocomplete random internet text.

**Analogy:** The well-read student now goes through **customer-service training** — they already know everything, but now they learn how to answer politely, follow instructions, and stay on-topic instead of rambling like a random Reddit thread.

**3-4 words:** *"Teach it to listen."*

### Stage 3 — RLHF / Alignment (the "be safe and likeable" phase)

**What happens:** Humans rate multiple model responses (better vs. worse), and the model is nudged (via reinforcement learning) to produce more responses like the ones humans preferred — safer, more honest, more useful.

**Analogy:** Like a chef who cooks several versions of a dish, a food critic tastes and ranks them, and the chef adjusts their recipe to match what the critic liked best — repeated over and over until the chef reliably makes crowd-pleasing food.

**3-4 words:** *"Humans rank the output."*

---

## A Few Core Truths About LLMs

| Idea | Quick Explanation |
|---|---|
| **It's all prediction** | Every "capability" (writing, coding, reasoning) is just really good next-word guessing. |
| **No real memory (by default)** | The model doesn't "remember" past chats unless the conversation is fed back in as text. |
| **Size = parameters** | "Large" refers to billions of tunable numbers (weights) inside the network. |
| **It learns patterns, not facts** | It doesn't "look things up" — it recalls patterns baked into its weights during training. |
| **Context window** | The max amount of text (tokens) it can "see" at once — it's blind to anything outside this window. |
| **Hallucination** | Confidently generating wrong info, because the model is optimizing for "plausible next word," not "verified truth." |
| **Emergent abilities** | Skills (like basic math or reasoning) that weren't directly trained for but "emerge" once the model gets big enough. |

> **Mantra:** *"Read everything → predict the next word → get taught manners → get ranked by humans → repeat until helpful."*

---

## The Pipeline (in order)

| # | Term | One-Line Meaning |
|---|---|---|
| 1 | **Tokenization** | Chopping text into small pieces (Legos). |
| 2 | **Token ID** | Number label for each Lego piece. |
| 3 | **Embedding** | Turning a token ID into a meaning-vector. |
| 4 | **Positional Encoding** | Stamping "position #" onto each token. |
| 5 | **Query (Q)** | The question a token is asking. |
| 6 | **Key (K)** | The label a token advertises. |
| 7 | **Value (V)** | The actual content a token delivers. |
| 8 | **Attention Score** | Q·K = how relevant two tokens are. |
| 9 | **Scaling (÷√d_k)** | Shrinking scores so they don't explode. |
| 10 | **Softmax** | Turning scores into clean percentages. |
| 11 | **Attention Output** | Percentages × Values = blended info. |
| 12 | **Multi-Head Attention** | Many attentions run in parallel. |
| 13 | **W_O** | Matrix that blends all heads into one. |
| 14 | **Causal Mask** | Blindfold from seeing future words. |
| 15 | **Padding Mask** | Blindfold from seeing filler tokens. |
| 16 | **Residual Connection** | Keep original signal, add it back. |
| 17 | **Layer Norm** | Resets numbers to a stable range. |
| 18 | **Add & Norm** | Residual + LayerNorm, one combo step. |
| 19 | **Feed-Forward (FFN)** | Each token thinks alone, briefly. |
| 20 | **Layer / Block** | One full attention + FFN unit. |
| 21 | **N Layers (Depth)** | Stack the block N times = deeper model. |
| 22 | **Logits** | Raw output scores over the vocabulary. |
| 23 | **Softmax (final)** | Turns logits into next-word probabilities. |
| 24 | **Training** | Parallel guess, blindfolded from future. |
| 25 | **Autoregressive (Testing)** | Write one word, feed it back, repeat. |

---

## Even Faster — 3-4 Word Recall

- Tokenization → **"Text into Legos."**
- Embedding → **"Legos get meaning."**
- Positional Encoding → **"Stamp the order."**
- Q, K, V → **"Ask, Advertise, Deliver."**
- Attention Score → **"How relevant, dot-product."**
- Scaling → **"Shrink before softmax."**
- Softmax → **"Scores to percentages."**
- Multi-Head → **"Many angles, parallel."**
- W_O → **"Blend the heads."**
- Causal Mask → **"No peeking ahead."**
- Padding Mask → **"Ignore the filler."**
- Residual → **"Keep the original."**
- LayerNorm → **"Reset the scale."**
- FFN → **"Think alone, briefly."**
- Training → **"All at once, masked."**
- Autoregressive → **"One word, then repeat."**

---

## One Fire Rule

**"Chop → Paint → Stamp → Ask/Answer/Deliver → Score → Blindfold → Blend → Reset → Think alone → Repeat one word at a time."**