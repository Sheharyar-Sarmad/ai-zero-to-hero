# same step for the web base loading as well instead of path paste the web url link

from langchain_community.document_loaders import WebBaseLoader
from langchain_core.documents import Document

data: WebBaseLoader = WebBaseLoader('https://clipsage-gamma.vercel.app/')
docs: list[Document] = data.load()

print(docs[0].page_content)
print(len(docs))