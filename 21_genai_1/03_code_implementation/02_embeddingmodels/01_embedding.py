# EMBEDDINGS WITH LANGCHAIN — Hugging Face (Free) vs OpenAI (Paid)

# Reality check: Groq does NOT support embeddings via LangChain.
# Use Hugging Face (free, local) or OpenAI (paid).

# Import os module for operating system interactions
import os

# Import load_dotenv to load environment variables from a .env file
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Import init_embeddings to initialize embedding models
from langchain.embeddings import init_embeddings

# Import the base Embeddings class for type hinting
from langchain_core.embeddings import Embeddings

# VERSION 1: Hugging Face (FREE — Use This)

# Why Hugging Face?
#   - Free forever (runs locally on your machine)
#   - Fully supported by LangChain
#   - Small model (~90 MB) downloads once, cached after
#   - No API keys, no rate limits
#
# Why NOT OpenAI?
#   - My OpenAI account has no credits left
#   - I refuse to spend money on embeddings
#   - OpenAI embeddings cost $0.02 per 1M tokens
#
# Why NOT Groq?
#   - LangChain does not support Groq for embeddings
#   - Groq is for chat/generation, not embeddings

# Print a separator line for visual clarity
print("=" * 60)

# Print the header for Version 1
print("VERSION 1: Hugging Face Embeddings (FREE)")

# Print a separator line for visual clarity
print("=" * 60)

# Initialize the Hugging Face embeddings object
hf_embeddings: Embeddings = init_embeddings(
    # Small, fast, well-known embedding model
    # 384 dimensions — small enough to run on any laptop
    model="sentence-transformers/all-MiniLM-L6-v2",
    # LangChain routes this to Hugging Face (runs locally)
    provider="huggingface",
)

# embed_query() → single vector for a single text
hf_vector: list[float] = hf_embeddings.embed_query(
    "You are going to learn Gen AI!"
)

# Print the dimension of the generated vector
print(f"Hugging Face Vector dimension: {len(hf_vector)}")

# Print the first 5 values of the generated vector
print(f"Hugging Face First 5 values:   {hf_vector[:5]}")

# Print an empty line for spacing
print()

# VERSION 2: OpenAI (PAID — Know It, But Don't Pay For It)

# OpenAI is the industry standard for embeddings.
# You should KNOW how to use it, but you don't need to pay for it.
#
# Requires:
#   - OPENAI_API_KEY in .env
#   - At least $5 of credits in your OpenAI account
#
# Cost:
#   - text-embedding-3-small: $0.02 per 1M tokens

# Print the header for Version 2
print("VERSION 2: OpenAI Embeddings (PAID — commented out)")

# Uncomment the lines below ONLY if you have OpenAI credits

# openai_embeddings: Embeddings = init_embeddings(
#     model="text-embedding-3-small",
#     provider="openai",
# )
#
# openai_vector: list[float] = openai_embeddings.embed_query(
#     "You are going to learn Gen AI!"
# )
#
# print(f"OpenAI Vector dimension: {len(openai_vector)}")
# print(f"OpenAI First 5 values:   {openai_vector[:5]}")

# Print a note about the commented out OpenAI code
print("(OpenAI code is commented out — uncomment only if you have credits)")

# Print an empty line for spacing
print()


# THE UNIVERSAL PATTERN (Memorize This)
# Whether you use Hugging Face, OpenAI, Mistral, or Ollama,
# the pattern is ALWAYS the same:
#
#   embeddings = init_embeddings(model="...", provider="...")
#   vector     = embeddings.embed_query("your text")
#
# Only two strings change: model name and provider name.
#
# | Provider      | Model                                     | Cost     |
# |---------------|-------------------------------------------|----------|
# | Hugging Face  | sentence-transformers/all-MiniLM-L6-v2    | Free     |
# | OpenAI        | text-embedding-3-small                    | Paid     |
# | Mistral       | mistral-embed                             | Paid     |
# | Ollama        | nomic-embed-text                          | Free     |
# | Google Gemini | models/embedding-001                      | Free tier|
# | Cohere        | embed-english-v3.0                        | Free tier|


# WHAT IS AN EMBEDDING, ANYWAY?
# An embedding is a list of floating-point numbers that represents
# the "meaning" of a piece of text.
#
# Example (3 dims for simplicity):
#   "cat"  → [ 0.21, -0.45,  0.88]
#   "dog"  → [ 0.19, -0.41,  0.91]   ← similar to "cat"
#   "car"  → [-0.72,  0.33, -0.15]   ← very different
#
# The KEY property: similar meanings → similar vectors.
#
# This is what makes RAG (Retrieval-Augmented Generation) work:
#   1. Embed all your documents → store in a vector database
#   2. Embed the user's question → same vector space
#   3. Find the closest document vectors → relevant chunks
#   4. Feed those chunks + the question to the LLM → it answers
#
# Embeddings are the "search engine" of AI systems.