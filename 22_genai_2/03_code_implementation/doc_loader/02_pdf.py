# Now our goal is to load pdf's everything is same just importing naming differ between each other, you now know the docs loader theory as well as code implementation

from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document

data: PyPDFLoader = PyPDFLoader("doc_loader/pythonBOOK.pdf")
docs: list[Document] = data.load()

print(docs[0].page_content)
print(len(docs))

# Is it really tough, not at all we here from people that oh ai, rag, gen ai these are like extremly tough but not that much see you need the domain knowledge and BTS of the architecture