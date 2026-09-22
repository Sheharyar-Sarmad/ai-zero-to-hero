# If you are here, you have finished the first two modules of GenAI part 2.
# You cannot memorize everything. I will show you the base level idea,
# but for specific work always check the AI agents, docs, and official guides.
# For text splitters, use this link to go deeper:
# https://docs.langchain.com/oss/python/integrations/splitters

from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_core.documents import Document

# Load the raw text file into LangChain Document objects
data: TextLoader = TextLoader("01_doc_loader/neural_networks.txt")
docs: list[Document] = data.load()

# Split the document by characters instead of tokens
splitter: CharacterTextSplitter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=10
)

# Same pattern again, the output is always list[Document]
chunks: list[Document] = splitter.split_documents(docs)

# How many chunks did we end up with
print(len(chunks))

# Print each chunk with spacing so you can read them easily
for i in chunks:
    print("\n\n\n")
    print(i.page_content)
    print("\n\n\n")