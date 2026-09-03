

# Bag of Words (BoW) in NLP – Complete Notes

---

## What is Bag of Words (BoW)?

**Bag of Words (BoW)** is a simple and foundational technique used in NLP to convert **text data** into **numerical vectors** (numbers) that machine learning models can understand.

> 💡 **The core idea:**  
> "A text is represented by the **count** of each word it contains — **without caring about the order**."

---

## Why Do We Need BoW?

| Reason | Explanation |
|--------|-------------|
| **ML Models** | Require numerical input, not raw text |
| **Simplicity** | Easy to understand and implement |
| **Baseline Model** | Works well for many basic text classification tasks |
| **Interpretable** | You can see which words contribute most to a prediction |

---

## How BoW Works (Step-by-Step)

### Step 1: Collect All Documents (Corpus)

Doc1: "I love NLP"
Doc2: "I love Python"
Doc3: "NLP is fun"

text

### Step 2: Create a Vocabulary
All unique words from all documents:
["I", "love", "NLP", "Python", "is", "fun"]

text

### Step 3: Count Word Occurrences per Document

| Document | I | love | NLP | Python | is | fun |
|----------|---|---|-----|--------|----|-----|
| Doc1     | 1 | 1   | 1   | 0      | 0  | 0   |
| Doc2     | 1 | 1   | 0   | 1      | 0  | 0   |
| Doc3     | 0 | 0   | 1   | 0      | 1  | 1   |

Each row is a **vector representation** of that document.

---

## 🧪 Python Code Example

```python
from sklearn.feature_extraction.text import CountVectorizer

# Sample corpus
corpus = [
    "I love NLP",
    "I love Python",
    "NLP is fun"
]

# Create BoW model
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)

# Get feature names (vocabulary)
print("Vocabulary:", vectorizer.get_feature_names_out())
# Output: ['I', 'NLP', 'Python', 'fun', 'is', 'love']

# Get BoW vectors (as array)
print("BoW Vectors:")
print(X.toarray())
# Output:
# [[1 1 0 0 0 1]
#  [1 0 1 0 0 1]
#  [0 1 0 1 1 0]]
```

#  Visual Representation

Doc1: "I love NLP"
  ↓
Vector: [1, 1, 0, 0, 0, 1]
         ↑  ↑  ↑  ↑  ↑  ↑
         I NLP Python fun is love

Example:
Unigrams (1-gram): ["I", "love", "NLP"]
Bigrams (2-gram): ["I love", "love NLP"]
Trigrams (3-gram): ["I love NLP"]

# Code:
```python
# Use n-grams (bigrams and trigrams)
vectorizer = CountVectorizer(ngram_range=(1, 3))
X = vectorizer.fit_transform(corpus)
```
# Key Takeaway
BoW is simple, fast, and works — but it treats words as independent and ignores meaning.

Use for: Baseline models, small datasets

**Avoid for: Large datasets, semantic tasks, deep learning**


💬 Summary in One Line
"BoW = Count how many times each word appears — ignoring order and meaning."