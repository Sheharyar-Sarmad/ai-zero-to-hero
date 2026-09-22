# Working with the token splitter, known as tiktoken in LangChain

from langchain_text_splitters import TokenTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document

# Load the PDF into LangChain Document objects
data: PyPDFLoader = PyPDFLoader("01_doc_loader/pythonBOOK.pdf")
docs: list[Document] = data.load()

# Split by tokens, not characters, so chunks fit LLM context windows exactly
splitter: TokenTextSplitter = TokenTextSplitter(
    chunk_size=100,
    chunk_overlap=10
)

# Each chunk is still a Document, so the pattern stays the same
chunks: list[Document] = splitter.split_documents(docs)

# Check how many chunks the PDF was split into
print(len(chunks))

# It will show the 1st page content 
print(chunks[0])