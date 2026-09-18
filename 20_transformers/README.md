# Transformers

## Overview
This module covers the transformer architecture from the ground up — the model behind nearly every modern language system. It builds from attention mechanics to the full encoder-decoder pipeline, ending with how these models are actually trained and used.

## What's inside
```
20_transformers/
├── 01_foundation/
├── 02_encoders_decoders/
├── 03_attention/
└── 04_transformer_architecture/
```

| Folder | Files | Topics covered |
|---|---|---|
| 01_foundation | 2 | CNN/RNN/ANN recap, course overview |
| 02_encoders_decoders | 4 | Seq2seq, encoder-decoder workflow, encoder internals, decoder internals |
| 03_attention | 4 | Attention, self-attention, scaled dot-product attention, cross-attention |
| 04_transformer_architecture | 5 | Full architecture, multi-head attention, positional encoding, feed-forward networks, training and testing |

## Learning path
1. **Foundation** — grounds the older architectures (CNN, RNN, ANN) so the leap to transformers makes sense.
2. **Encoders/Decoders** — introduces the seq2seq shape before attention complicates it.
3. **Attention** — the core mechanism, built up piece by piece from plain attention to cross-attention.
4. **Architecture** — assembles everything into the full transformer and closes with training and inference.

## Key concepts covered
- Query, Key, Value (Q/K/V) vectors
- Scaled dot-product attention
- Self-attention vs cross-attention
- Multi-head attention
- Positional encoding
- Feed-forward networks
- Causal masking
- Encoder-decoder vs decoder-only architectures
- Teacher forcing and exposure bias
- Cross-entropy loss
- Adam optimizer with warmup
- Autoregressive decoding (greedy, beam, sampling)
- Perplexity, BLEU, ROUGE

## Notes format
These are personal study notes — written as I learned, revised later as understanding deepened. Not a textbook, not a reference manual. Written for future-me, and shared in case someone else is walking the same path.

## Related projects
QuoteLab, an LSTM-based app paired with Groq for fast inference, is the practical counterpart to this module — a place where the sequence modeling ideas here get applied outside of notes.

## References
These notes follow a deep learning course covering neural network foundations through transformer architecture.

## Next Step
Solid work getting through the whole transformer stack. Next up: GenAI — RAG, agents, tool calling — where all of this stops being theory and starts building things that actually do stuff. This is the fun part. Let's go. 🚀

## Author
Sheharyar Sarmad — AI Full-Stack Engineer in progress. [GitHub](https://github.com/Sheharyar-Sarmad) - [Linkedin](https://www.linkedin.com/in/sheharyar-sarmad-9b7736289/)