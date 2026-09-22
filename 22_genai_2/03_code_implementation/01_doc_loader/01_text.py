# One thing to be clear about, there are tons of document loader pipelines out there.
# You just need to be document and AI friendly, and understand the base plus the
# behind the scenes of what is happening. For the full list of loaders, visit:
# https://docs.langchain.com/oss/python/integrations/document_loaders

from langchain_community.document_loaders import TextLoader
from langchain_core.documents import Document

# Just point the loader to the file path
data: TextLoader = TextLoader("doc_loader/neural_networks.txt")

# This only creates the loader object, it does not read the file yet
print(data)

# Calling load reads the file and returns a list of Document objects
docs: list[Document] = data.load()

# Every loader returns the same structure, so learn this once
# .metadata holds info like the source file path
# .page_content holds the raw text that gets split and embedded later
print(docs)

# Shows how many Document objects were returned
print(len(docs))