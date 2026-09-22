# Full pipeline for storing a PDF into ChromaDB
# Load PDF, split into chunks, embed locally, persist to disk, and set up a retriever

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
from dotenv import load_dotenv
from langchain_core.vectorstores import VectorStoreRetriever

load_dotenv()

# Load the PDF. PyPDFLoader returns one Document per page.
data: PyPDFLoader = PyPDFLoader("01_doc_loader/deep-learning.pdf")
docs: list[Document] = data.load()

# Split the pages into smaller chunks.
# Recursive splitter keeps paragraphs and sentences intact where possible.
# chunk_overlap ensures no idea gets cut in half at a chunk boundary.
splitter: RecursiveCharacterTextSplitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks: list[Document] = splitter.split_documents(documents=docs)

# Load the embedding model.
# This uses the default local model (all-MiniLM-L6-v2), which runs on your machine.
# No API key, no rate limit, no cost.
embedding_model: HuggingFaceEmbeddings = HuggingFaceEmbeddings()

# Embed every chunk and store them in ChromaDB.
# persist_directory saves the index to disk so you do not re-embed on every run.
vector_store: Chroma = Chroma.from_documents(
    documents=chunks,
    embedding=embedding_model,
    persist_directory="chroma_db"
)

# Convert the vector store into a retriever.
# A retriever is an object, not a list. It has an invoke method you can call
# with a natural language query to fetch the most relevant chunks.
retriever: VectorStoreRetriever = vector_store.as_retriever()

# Query the retriever. This is the payoff of the whole pipeline.
# It returns a list of Document objects whose content is closest in meaning
# to the question, not just keyword matches.
results: list[Document] = retriever.invoke("What is deep learning?")

# Print the retrieved chunks with their source metadata
for doc in results:
    print("\n")
    print(doc.page_content)
    print(doc.metadata)