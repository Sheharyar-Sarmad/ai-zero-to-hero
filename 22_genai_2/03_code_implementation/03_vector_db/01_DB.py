from langchain_community.vectorstores import Chroma
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_core.documents import Document
from langchain_core.vectorstores import VectorStoreRetriever

# Sample documents to store in the vector database
docs = [
    Document(page_content="Python is widely used in Artificial Intelligence.", metadata={"source": "AI_book"}),
    Document(page_content="Pandas is used for data analysis in Python.", metadata={"source": "DataScience_book"}),
    Document(page_content="Neural networks are used in deep learning.", metadata={"source": "DL_book"}),
]

# Load the embedding model (runs locally, no API key needed)
embedding_model: HuggingFaceEmbeddings = HuggingFaceEmbeddings()

# Create the vector store and persist it to disk
vectorstore: Chroma = Chroma.from_documents(
    documents=docs,
    embedding=embedding_model,
    persist_directory="chroma_db"
)

# Convert the vector store into a retriever
# A retriever is an object, not a list. It has an invoke method.
retriver: VectorStoreRetriever = vectorstore.as_retriever()

# Query the retriever with a natural language question
result: list[Document] = retriver.invoke("Explain deep learning!")

# Print the retrieved chunks
for d in result:
    print("\n" * 3)
    print(d.page_content)
    print(d.metadata)