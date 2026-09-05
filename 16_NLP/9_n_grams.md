


# N-Grams: Concise Notes

## Definition
Contiguous sequence of **n** items (words/characters) from text(document).

## General Formula

## Probability (MLE)
- P(w_i | w_{i-n+1}...w_{i-1}) = Count(n-gram) / Count(prefix)

## Smoothing Techniques
| Technique | Description |
|-----------|-------------|
| **Add-k** | Add k to all counts (k=1 is Laplace) |
| **Good-Turing** | Re-estimate probabilities using frequency of frequencies |
| **Kneser-Ney** | Uses lower-order distributions for unseen contexts |
| **Interpolation** | Weighted combination of all n-gram orders |
| **Backoff** | Use (n-1)-gram when n-gram count = 0 |

## Evaluation: Perplexity
- Perplexity = exp(- (1/N) * Σ log P(w_i | context))

Lower perplexity = better model

## Trade-offs

| Larger n | Smaller n |
|----------|-----------|
| More context | Less context |
| More sparsity | Denser data |
| Higher memory | Lower memory |
| More specific | More general |

## Practical Guidelines
- **n=3 to 5** for word-level models
- **n=5 to 7** for character-level models
- Always use **smoothing** for unseen n-grams
- Use **log probabilities** to avoid underflow
- Replace rare words with `<UNK>` token

## Applications
- Language modeling
- Text generation
- Machine translation
- Speech recognition
- Information retrieval

## Python Example
```python
from nltk import ngrams
from collections import Counter

text = "this is a sample sentence".split()
n = 3
ngram_list = list(ngrams(text, n))
freq = Counter(ngram_list)
```
## Key Insight

- N-grams balance context (n) vs sparsity.
- Choose n based on data size and task requirements.

