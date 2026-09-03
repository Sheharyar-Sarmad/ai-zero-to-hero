

# Vectorization in NLP – Complete Notes

---

## What is Vectorization?

**Vectorization** is the process of converting **text data** into **numerical vectors** (numbers) so that machine learning models can understand and process it.

> **Why?**  
> Machines don't understand words — they understand **numbers**. Vectorization bridges that gap.

---

## Why Do We Need Vectorization?

| Reason | Explanation |
|--------|-------------|
| **ML Models** | Require numerical input |
| **Math Operations** | Vectors allow dot products, distances, etc. |
| **Similarity** | We can measure how similar two texts are |
| **Efficiency** | Numeric data is faster to process |

---

## Common Vectorization Techniques

| Technique | Description |
|-----------|-------------|
| **Bag of Words (BoW)** | Counts word occurrences — ignores order |
| **TF-IDF** | Weighs words by importance in a document |
| **Word Embeddings** | Dense vectors capturing semantic meaning (Word2Vec, GloVe) |
| **One-Hot Encoding** | Binary vector for each word (sparse) |

---

## Bag of Words (BoW)

### What It Does:
- Creates a **vocabulary** of all unique words
- Each document becomes a **vector of word counts**

### Example:
**Corpus:**  
- Doc1: "I love NLP"  
- Doc2: "I love Python"

**Vocabulary:** `["I", "love", "NLP", "Python"]`

**Vectors:**
| Document | I | love | NLP | Python |
|----------|---|---|-----|--------|
| Doc1     | 1 | 1   | 1   | 0      |
| Doc2     | 1 | 1   | 0   | 1      |

### Pros /  Cons
| Pros | Cons |
|------|------|
| Simple & easy | Loses word order |
| Works well for small datasets | Sparse vectors (many zeros) |

---

## TF-IDF (Term Frequency – Inverse Document Frequency)

### What It Does:
- **TF** = How often a word appears in a document
- **IDF** = How rare/important a word is across all documents
- Final score = `TF × IDF`

### Why It’s Better:
- Common words like *"the"*, *"is"* get low scores
- Important/rare words get high scores

---

## Word Embeddings (Word2Vec, GloVe)

### What It Does:
- Maps words to **dense vectors** (e.g., 100–300 dimensions)
- Captures **semantic meaning** — similar words have similar vectors

### Example:

- king - man + woman ≈ queen


### Pros / Cons
| Pros | Cons |
|------|------|
| Captures meaning & context | Needs large corpus |
| Dense vectors (efficient) | Computationally expensive |

---

## One-Hot Encoding

### What It Does:
- Each word becomes a vector with **1 at its index**, rest 0

### Example:
Vocabulary: `["cat", "dog", "bird"]`  
- `"cat"` → `[1, 0, 0]`  
- `"dog"` → `[0, 1, 0]`  
- `"bird"` → `[0, 0, 1]`

### Cons:
- Very sparse (mostly zeros)
- No semantic meaning captured

---

## Comparison Table

| Technique | Captures Meaning | Sparse/Dense | Order Preserved | Use Case |
|-----------|------------------|--------------|-----------------|----------|
| **BoW** | No | Sparse | No | Baseline models |
| **TF-IDF** | Partially | Sparse | No | Search/ranking |
| **One-Hot** | No | Sparse | No | Categorical data |
| **Word2Vec** | Yes | Dense | No | Deep learning, semantic tasks |
| **GloVe** | Yes | Dense | No | NLP tasks |
| **BERT Embeddings** | Yes | Dense | Yes | Advanced NLP |

---

## Python Example (BoW & TF-IDF)

```python
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

corpus = [
    "I love NLP",
    "I love Python"
]

# BoW
bow = CountVectorizer()
bow_vectors = bow.fit_transform(corpus)
print(bow.get_feature_names_out())
print(bow_vectors.toarray())

# TF-IDF
tfidf = TfidfVectorizer()
tfidf_vectors = tfidf.fit_transform(corpus)
print(tfidf.get_feature_names_out())
print(tfidf_vectors.toarray())