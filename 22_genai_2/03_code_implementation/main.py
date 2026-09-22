# Prequisites: This is the basic RAG pipeline project you can learn it after the four modules
# Which are fundamentals for the RAG then you can come here to combine the workflow 
# First run the create_database.py in the background once because that will create the db 

from dotenv import load_dotenv

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.vectorstores import VectorStoreRetriever

load_dotenv()

embedding_model: HuggingFaceEmbeddings = HuggingFaceEmbeddings()

vectorstore: Chroma = Chroma(
    persist_directory="chroma_db",
    embedding_function=embedding_model
)

retriever: VectorStoreRetriever = vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k": 4,
        "fetch_k": 10,
        "lambda_mult": 0.7
    }
)

llm: ChatGroq = ChatGroq(model="openai/gpt-oss-120b")

prompt: ChatPromptTemplate = ChatPromptTemplate.from_messages(
    [
        ("system", """You are a helpful AI assistant.

Use ONLY the provided context to answer the question.

If the answer is not present in the context,
say: "I could not find the answer in the document.
     """),
        (
            "human", """Context: 
            {context}

            Question:
            {question}"""
        )
    ]
)

