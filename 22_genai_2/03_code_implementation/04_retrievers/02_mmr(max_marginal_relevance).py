# Comparing two retrieval strategies in LangChain.
# Similarity search returns the k most similar chunks.
# MMR returns k chunks that are both relevant and diverse from each other.

from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
from dotenv import load_dotenv

load_dotenv() # loading .env file 

# These five documents are intentionally redundant.
# Three of them say nearly the same thing about gradient descent.
# That redundancy is exactly what MMR is designed to handle.
docs: list[Document] = [
    Document(page_content="Gradient descent is an optimization algorithm used in machine learning."),
    Document(page_content="Gradient descent minimizes the loss function."),
    Document(page_content="Gradient descent is an optimization that minimizes the loss function."),
    Document(page_content="Neural networks use gradient descent for training."),
    Document(page_content="Support Vector Machines are supervised learning algorithms.")
]

# Load the local embedding model.
# This runs on your machine. No API key, no rate limit, no cost.
embeddings: HuggingFaceEmbeddings = HuggingFaceEmbeddings()

# Build the vector store from the documents.
# Important: use Chroma.from_documents, not the Chroma constructor.
# The constructor expects a collection name as the first argument.
# Passing a list of documents there causes a TypeError.
# from_documents is the correct method when you have raw documents to embed.
vectorstores: Chroma = Chroma.from_documents(
    documents=docs,
    embedding=embeddings
)

# Similarity retriever.
# Returns the k chunks whose meaning is closest to the query.
# This is the default behavior of as_retriever.
similarity_retriever = vectorstores.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 3}
)

similarity_docs = similarity_retriever.invoke("What is a gradient descent!")

print("\nSimilarity Retriever\n")

for doc in similarity_docs:
    print(doc.page_content)

# MMR stands for Max Marginal Relevance.
# It returns chunks that are relevant to the query but also diverse from each other.
# Without this, the retriever returns three near-identical chunks.
# With MMR and a low lambda_mult, it returns three chunks from different topics.
#
# Arguments explained:
#   k: how many chunks to return at the end
#   lambda_mult: balance between relevance and diversity
#     1.0 means pure relevance, 0.0 means pure diversity, 0.5 is balanced
#   fetch_k (not set here, defaults to 20): how many candidates to consider
#     before MMR selects the final k
mmr_retriever = vectorstores.as_retriever(
    search_type="mmr",
    search_kwargs={"k": 3, "lambda_mult": 0.2}
)

mmr_docs = mmr_retriever.invoke("What is a gradient descent!")

print("\nMMR (Max Marginal Relevance)\n")

for doc in mmr_docs:
    print(doc.page_content)