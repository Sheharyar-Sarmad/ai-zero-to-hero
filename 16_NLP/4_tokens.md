

## Token and Tokenization

---

### What is a Token?

> A **token** is the **smallest unit** of text that a model processes. It can be a word, subword, character, or even a punctuation mark.

---

### Examples of Tokens

| Text            | Tokens |
|------           |--------|
| "I love NLP"    | ["I", "love", "NLP"] |
| "Hello World!"  | ["Hello", "World", "!"] |
| "I'm happy"     | ["I", "'m", "happy"] |

---

### What is Tokenization?

> **Tokenization** is the process of **splitting text into smaller units called tokens**.

---

### Types of Tokenization

| Type                       | What it Does              | Example |
|------                      |--------------             |---------|
| **Word Tokenization**      | Splits by words           | "I love NLP" → ["I", "love", "NLP"] |
| **Sentence Tokenization**  | Splits by sentences       | "I love NLP. It's great!" → ["I love NLP.", "It's great!"] |
| **Subword Tokenization**   | Splits into smaller parts | "playing" → ["play", "ing"] |
| **Character Tokenization** | Splits by characters      | "Hi" → ["H", "i"] |

---

### Why Tokenization Matters?

> Machines don't understand text. They understand numbers. Tokenization converts text into tokens that can be turned into numbers.

| Step | What Happens |
|------|--------------|
| 1    | Text → Tokens |
| 2    | Tokens → Numbers |
| 3    | Numbers → Model |

---

### Popular Tokenizers in NLP

| Tokenizer          | Used In       | How it Works |
|-----------         |---------      |--------------|
| **Whitespace**     | Simple tasks  | Splits by spaces |
| **NLTK Tokenizer** | General NLP   | Word and sentence tokenization |
| **Spacy**          | Production    | Fast and accurate |
| **WordPiece**      | BERT          | Subword tokenization |
| **BPE**            | GPT           | Subword tokenization |

---

### Python Code Example

```python
# Word Tokenization
from nltk.tokenize import word_tokenize
text = "I love NLP!"
tokens = word_tokenize(text)
print(tokens)  # ["I", "love", "NLP", "!"]

# Sentence Tokenization
from nltk.tokenize import sent_tokenize
text = "I love NLP. It's amazing!"
sentences = sent_tokenize(text)
print(sentences)  # ["I love NLP.", "It's amazing!"]
```

# Text → Tokenization → Tokens → Numbers → Model

**Example**:
"I love NLP" → ["I", "love", "NLP"] → [1, 2, 3] → Model