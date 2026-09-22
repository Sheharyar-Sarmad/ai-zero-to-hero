# The SemanticChunker is a different approach from the fixed size splitters.
# Instead of cutting every N tokens or characters, it uses embeddings to
# detect where the topic actually changes, and it splits there.
# This means each chunk is a complete thought, not an arbitrary fragment.

from langchain_experimental.text_splitter import SemanticChunker
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain_core.documents import Document

# Embedding model converts each sentence into a vector
# Note: Hugging Face is technically free to start, but you only get a limited
# amount of free tokens before you have to pay. The local version below uses
# your own machine, so it costs nothing, but it is slower and heavier on RAM.
embeddings: HuggingFaceEmbeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# The breakpoint_threshold_type controls WHERE the chunker cuts.
# percentile is the safest general purpose choice. It splits wherever the
# distance between two sentences is in the top N percent of all distances.
splitter: list[Document] = SemanticChunker(
    embeddings=embeddings,
    breakpoint_threshold_type="percentile",
    breakpoint_threshold_amount=95,
)

# Load the file into Document objects, then split
data = TextLoader("01_doc_loader/neural_networks.txt")
docs: list[Document] = data.load()

chunks: list[Document] = splitter.split_documents(docs)

# Print each chunk with its length so you can compare against other splitters
for i, chunk in enumerate(chunks):
    print(f"Chunk {i} ({len(chunk.page_content)} chars)")
    print(chunk.page_content[:200])
    print()


# If you ever want to use Mistral for the embeddings instead of Hugging Face,
# here is the same setup with Mistral. Note that right now Mistral is throwing
# a 429 rate limit exceeded error on my account, even on the very first request.
# It seems to be a tier 0 restriction that requires phone verification or a
# payment method before the free tier actually works.
#
# from langchain_mistralai import MistralAIEmbeddings
#
# embeddings = MistralAIEmbeddings(
#     model="mistral-embed"
# )
#
# Everything else stays the same.
# Just swap the HuggingFaceEmbeddings line for the MistralAIEmbeddings line.