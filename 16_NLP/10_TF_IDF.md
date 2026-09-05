

# TF-IDF (Term Frequency–Inverse Document Frequency)

**TF-IDF** is a technique used in **Natural Language Processing (NLP)** to measure how important a word is in a document compared to the entire corpus.

---

## TF — Term Frequency

Measures how often a word appears in a document.

- More occurrences → Higher TF
- Fewer occurrences → Lower TF

---

## IDF — Inverse Document Frequency

Measures how rare a word is across all documents.

- Common in many documents → Lower IDF
- Rare across documents → Higher IDF

---

## TF-IDF

- TF-IDF = TF × IDF


### What it means:

- Important word → **Higher** TF-IDF score
- Common word → **Lower** TF-IDF score

---

##  Example

**Corpus:**

- Document 1: `I love machine learning`
- Document 2: `I love deep learning`
- Document 3: `I love NLP`

### Analysis:

Words like **"I"** and **"love"** appear in **multiple** documents:

- **Low importance** (low IDF)

Words like:

- `machine`
- `deep`
- `NLP`

appear in **fewer** documents:

- **Higher importance** (high IDF)

---

## BoW vs TF-IDF

| Feature | BoW (Bag of Words) | TF-IDF |
|---------|-------------------|--------|
| What it does | Counts how often words appear | Measures how important words are |

---

## Memory Trick

| Term | Meaning |
|------|---------|
| **TF** = Frequency in **this** document |
| **IDF** = Rarity across the **corpus** |
| **TF-IDF** = Importance of a word |

---

## Summary

- TF-IDF = **TF × IDF**
- Helps identify **important** words in a document
- Reduces weight of **common** words (stopwords)
- Widely used in **information retrieval**, **search engines**, and **text mining**