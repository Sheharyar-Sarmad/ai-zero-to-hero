


## Data Preprocessing Steps 

### Common Preprocessing Steps

1. **Lowercasing** - converting all text to lowercase to reduce vocabulary size
   - Example: "Apple" → "apple"

2. **Removing Punctuation** - eliminating punctuation marks that don't add meaning
   - Example: "Hello!" → "Hello"

3. **Removing Stopwords** - filtering out common words that carry little semantic meaning
   - Examples: "the", "is", "a", "an", "of", "and"

4. **Tokenization** - splitting text into smaller units (tokens) like words or sentences
   - Example: "I love NLP" → ["I", "love", "NLP"]

5. **Stemming** - reducing words to their root/base form
   - Example: "running" → "run", "studies" → "studi"

6. **Lemmatization** - converting words to their dictionary/base form (more accurate than stemming)
   - Example: "running" → "run", "studies" → "study"

7. **Removing Special Characters/Noise** - cleaning irrelevant symbols and characters
   - Example: Removing URLs, HTML tags, emojis

8. **Spell Checking/Correction** - fixing misspelled words (optional)

9. **Handling Contractions** - expanding or removing contractions
   - Example: "don't" → "do not"

## Text Cleaning Techniques - Lowercasing, Punctuation Removal, Emoji & Stopword Removal

### Lowercasing
- **What it does:** Converts all text to lowercase
- **Why we do it:** Reduces vocabulary size and ensures "Apple" and "apple" are treated as the same word
- **Example:** 
  - Before: "I Love NLP!"
  - After: "i love nlp!"

### Punctuation Removal
- **What it does:** Removes punctuation marks like .,!?;:'"()[]{} etc.
- **Why we do it:** Punctuation usually doesn't add meaning for most NLP tasks
- **Example:**
  - Before: "Hello, world! How are you?"
  - After: "Hello world How are you"

### Emoji Removal
- **What it does:** Removes or converts emojis from text
- **Why we do it:** Most ML models can't process emojis directly
- **Example:**
  - Before: "I love this! ❤️😊🔥"
  - After: "I love this!"

### Stopword Removal
- **What it does:** Removes common words that carry little meaning (like "the", "is", "and", "of")
- **Why we do it:** These words add noise and don't help in understanding the actual meaning
- **Example:**
  - Before: "The cat is sitting on the mat"
  - After: "cat sitting mat"
