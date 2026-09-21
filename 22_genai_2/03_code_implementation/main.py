from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage
from langchain_community.document_loaders import TextLoader # For text loading 
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.documents import Document # just docs variable's type hint 

template: ChatPromptTemplate = ChatPromptTemplate.from_messages([
    ("system", "you are an ai that summarizes the text!"),
    ("human", "{data}")
])

data: TextLoader = TextLoader("doc_loader/neural_networks.txt") # Just provide of the file in it 
docs: list[Document] = data.load()
model: ChatGroq = ChatGroq(
    model='openai/gpt-oss-120b'
)

prompt = template.format_messages(data=docs[0].page_content) # this docs[0].page_content means i only want to send the page_content nothing else 

result: AIMessage = model.invoke(prompt)
print(result.content)