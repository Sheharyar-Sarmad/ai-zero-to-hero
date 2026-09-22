# Load environment variables such as the Groq API key
from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage
from langchain_community.document_loaders import TextLoader
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.documents import Document

# Build the prompt with two roles.
# The system message defines who the AI is.
# The human message holds the raw text we want summarized.
template: ChatPromptTemplate = ChatPromptTemplate.from_messages([
    ("system", "you are an ai that summarizes the text!"),
    ("human", "{data}")
])

# Load the raw text file into LangChain Document objects
data: TextLoader = TextLoader("doc_loader/neural_networks.txt")
docs: list[Document] = data.load()

# Free and fast model on Groq, great for summarization tasks
model: ChatGroq = ChatGroq(
    model='openai/gpt-oss-120b'
)

# We only send page_content, not the metadata, because the AI only needs the text
prompt = template.format_messages(data=docs[0].page_content)

# Send the prompt to the model and get the response back
result: AIMessage = model.invoke(prompt)
print(result.content)