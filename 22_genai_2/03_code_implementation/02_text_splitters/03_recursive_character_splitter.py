# We have seen character based and tiktoken based splitting.
# In real world RAG systems we will mostly use the recursive text splitter.
# For intuition, you can play with this site: https://chunkviz.up.railway.app/

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

data: TextLoader = TextLoader("01_doc_loader/neural_networks.txt")
docs: list[Document] = data.load()

# Only the import and the class name change. The pattern stays the same.
# Recursive splitter tries to split by paragraph first, then line, then word, then character.
# It only gets more aggressive when a chunk is still too big.
# This is why it keeps meaning intact instead of cutting sentences in half.

splitter: RecursiveCharacterTextSplitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=100
)

chunks: list[Document] = splitter.split_documents(docs)

print(len(chunks))

# Print each chunk to see how the recursive splitter cut the text
for i in chunks:
    print("\n" * 3)
    print(i.page_content)
    print("\n" * 3)

# See we are just changing the imports the code is not hard at all you can get it from the ai agents and docs easily you just needs 
# base behind knowledge.