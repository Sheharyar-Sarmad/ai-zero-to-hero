# Same pattern as before, but for a web page.
# Instead of a file path, we pass the URL directly to the loader.

from langchain_community.document_loaders import WebBaseLoader
from langchain_core.documents import Document

# The loader will fetch the page and extract the readable text from the HTML
data: WebBaseLoader = WebBaseLoader('https://clipsage-gamma.vercel.app/')
docs: list[Document] = data.load()

# Print the extracted text from the first document
print(docs[0].page_content)

# Usually one document per URL, but printing the length keeps the habit consistent
print(len(docs))