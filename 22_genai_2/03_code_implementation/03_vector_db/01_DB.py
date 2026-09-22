# Retriever pipeline with ChromaDB
# This file shows how a retriever relates to the underlying vector database
# Think of the vector store as the database, and the retriever as the query interface

from langchain_community.vectorstores import Chroma
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_core.documents import Document
from langchain_core.vectorstores import VectorStoreRetriever

# These documents are the equivalent of rows in a table.
# page_content is the main column, metadata is like extra columns.
docs: list[Document] = [
    Document(page_content="Python is widely used in Artificial Intelligence.", metadata={"source": "AI_book"}),
    Document(page_content="Pandas is used for data analysis in Python.", metadata={"source": "DataScience_book"}),
    Document(page_content="Neural networks are used in deep learning.", metadata={"source": "DL_book"}),
]

# The embedding model converts each document into a vector.
# This is like indexing a column in a traditional database.
embedding_model: HuggingFaceEmbeddings = HuggingFaceEmbeddings()

# Create the vector store and persist it to disk.
# This is the equivalent of CREATE TABLE and INSERT INTO.
# The persist_directory is the physical storage location, like a data file on disk.
vectorstore: Chroma = Chroma.from_documents(
    documents=docs,
    embedding=embedding_model,
    persist_directory="chroma_db"
)

# Convert the vector store into a retriever.
# The retriever is like a database connection with a prepared query interface.
# It is an object, not a list. It has an invoke method.
# This is the equivalent of creating a cursor or a query builder in SQL.
retriever: VectorStoreRetriever = vectorstore.as_retriever()

# Query the retriever with a natural language question.
# This is the equivalent of SELECT * FROM documents WHERE similarity > threshold.
# Instead of SQL, we use natural language, and the retriever translates it.
# The return value is always list[Document], just like a SQL query returns rows.
result: list[Document] = retriever.invoke("Explain deep learning!")

# Print the retrieved chunks.
# Each Document is like a row, and page_content plus metadata are the columns.
for d in result:
    print("\n" * 3)
    print(d.page_content)
    print(d.metadata)