# This is the exact same as 03_recursive_character_splitter.py
# The only difference here is that we send the chunks to an LLM to get a summary.

# We already covered character based and tiktoken based splitting.
# In a real RAG system, RecursiveCharacterTextSplitter is the go to choice.
# Play with this site for intuition: https://chunkviz.up.railway.app/

from dotenv import load_dotenv
load_dotenv()

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage
from langchain_core.prompt_values import ChatPromptValue

# Load the raw file into Document objects
data: TextLoader = TextLoader("01_doc_loader/neural_networks.txt")
docs: list[Document] = data.load()

# Split into chunks. The recursive splitter keeps meaning intact.
splitter: RecursiveCharacterTextSplitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=100
)

chunks: list[Document] = splitter.split_documents(docs)

# System prompt sets the role, human prompt holds the raw text
template: ChatPromptTemplate = ChatPromptTemplate.from_messages([
    ("system", "you are an ai that summarizes the text!"),
    ("human", "{data}")
])

# Fast and free model on Groq, good for summarization
model: ChatGroq = ChatGroq(
    model="openai/gpt-oss-120b"
)

# We only send page_content, not the metadata, because the LLM does not need it
prompt: ChatPromptValue = template.format_messages(data=chunks[0].page_content)

# Send the prompt and get the response
result: AIMessage = model.invoke(prompt)
print(result.content)