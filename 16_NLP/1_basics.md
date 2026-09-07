

# NLP Notes

## What is NLP and its applications 

### Definition
- **Natural Language Processing (NLP)** - a subfield of Artificial Intelligence that focuses on the interaction between computers and humans through natural language.

### Key Applications
- **Machine Translation** - translating text between languages (e.g., Google Translate)
- **Sentiment Analysis** - determining sentiment/emotion in text
- **Text Summarization** - generating concise summaries from longer texts
- **Question Answering** - systems that can answer questions posed in natural language
- **Named Entity Recognition** - identifying and classifying named entities (e.g., person names, organizations, dates)
- **Chatbots/Virtual Assistants** - conversational agents like Siri, Alexa, Google Assistant
- **Spam Detection** - identifying unwanted emails or messages
- **Text Classification** - categorizing documents into predefined categories
- **Speech Recognition** - converting spoken language to text
- **Information Extraction** - extracting structured information from unstructured text

---

## Limitations of Rule-based Approaches 

### Problems with Rule-based Systems
- **Scalability Issues** - as language grows, maintaining rules becomes challenging
- **Lack of Flexibility** - cannot handle new/unknown words or phrases effectively
- **Context Understanding** - difficult to capture context and ambiguity in language
- **Coverage Problem** - impossible to write rules for every possible language pattern
- **Domain Dependence** - rules for one domain don't generalize well to others
- **Performance Limitations** - constant updating needed to maintain accuracy

---

## Machine Learning / Statistical Approach to NLP 

### Key Concepts
- **Statistical Models** - using probability and statistics to predict language patterns
- **Data-Driven Approach** - learning from large datasets rather than hand-coded rules
- **Feature Extraction** - converting text into numerical representations that ML algorithms can understand

### Common Techniques
- **Probability-based Models** - using likelihood to predict sequences of words
- **Corpus-based Methods** - learning from large collections of text

### Advantages
- **Generalizability** - can handle new/unseen data
- **Adaptability** - learns patterns directly from data
- **Scalability** - works with large amounts of data
- **Less Manual Effort** - reduces the need for human-crafted rules

### Evolution
- From **Rule-based** → **Statistical** → **Modern Deep Learning Approaches** (Neural Networks, Transformers)

### Modern Methods
- **N-gram Models** - predicting the next word based on previous n-1 words
- **Hidden Markov Models** - used for sequence labeling tasks
- **Neural Networks** - multi-layer architectures for language understanding
- **Word Embeddings** - representing words as dense vectors (e.g., Word2Vec, GloVe)