# One thing i want to clear you is that there will be almost tons and tons of documents loader pipelines, you just have to be doc & ai friendly just and need a good base & bts knowledge of all the thing happening in the background just. visit this langchain link for checking much more documents loader tools https://docs.langchain.com/oss/python/integrations/document_loaders.

# See the code now 

from langchain_community.document_loaders import TextLoader # For text loading 

data: TextLoader = TextLoader("doc_loader/neural_networks.txt") # Just provide of the file in it 

from langchain_core.documents import Document # just docs variable's type hint 

print(data) # <langchain_community.document_loaders.text.TextLoader object at 0x00000185B828E120> it will paste this its saying that one object is created successfully

# Now then we again have to load it using its load function
docs: list[Document] = data.load()

print(docs) # print(docs) outputs: list[Document]
# Each Document has 2 parts:
#   .metadata     -> dict, e.g. {'source': 'file.txt'} (where it came from)
#   .page_content -> str, the raw text (what gets split & embedded later)
# Pattern: ALL LangChain loaders return this exact same structure. Learn once, use everywhere.
print(len(docs))