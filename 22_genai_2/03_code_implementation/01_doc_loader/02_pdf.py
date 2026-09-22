# Now the goal is to load PDFs.
# Everything stays the same, only the class name and the file type change.
# You already know the loader theory, this is just the code side of it.

from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document

# Point the loader at the PDF file
data: PyPDFLoader = PyPDFLoader("doc_loader/pythonBOOK.pdf")
docs: list[Document] = data.load()

# Print the content of the fourth page
print(docs[3])

# One document per page, so this shows how many pages the PDF has
print(len(docs))

# People say AI, RAG, and GenAI are extremely tough.
# They are not that tough once you get the domain knowledge and the
# behind the scenes understanding of the architecture.