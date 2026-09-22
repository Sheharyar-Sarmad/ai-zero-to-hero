# MultiQueryRetriever in LangChain
# This retriever uses an LLM to rewrite the user query into multiple variations,
# searches for each variant, and combines the results into one ranked list.

from langchain_core.documents import Document
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_classic.retrievers.multi_query import MultiQueryRetriever
from langchain_groq import ChatGroq
from langchain_core.vectorstores import VectorStoreRetriever

# Small redundant dataset to make the effect of multi-query visible
docs: list[Document] = [
    Document(page_content="Gradient descent is an optimization algorithm used in machine learning."),
    Document(page_content="Gradient descent minimizes the loss function."),
    Document(page_content="Gradient descent is an optimization that minimizes the loss function."),
    Document(page_content="Neural networks use gradient descent for training."),
    Document(page_content="Support Vector Machines are supervised learning algorithms.")
]

# Local embedding model. Free, runs on your machine.
embeddings: HuggingFaceEmbeddings = HuggingFaceEmbeddings()

# Build the underlying vector store
vectorstores: Chroma = Chroma.from_documents(
    documents=docs,
    embedding=embeddings
)

# The base retriever. MultiQueryRetriever wraps this retriever.
# The base retriever is what actually searches the vector store.
# MultiQueryRetriever only improves the queries that go into it.
# Default k is 4. If you want more or fewer results, pass search_kwargs={"k": 3}.
retriever: VectorStoreRetriever = vectorstores.as_retriever()

# The LLM that will generate the query variations.
# Smaller models are usually enough for this task.
# Groq is used here for speed and a generous free tier.
llm: ChatGroq = ChatGroq(model="openai/gpt-oss-20b")

# MultiQueryRetriever wraps the base retriever.
# For every user query, it does three things:
#   1. Uses the LLM to generate N variations of the query (default N is 3).
#   2. Runs the base retriever on each variation separately.
#   3. Merges the results and removes duplicates.
# The final list contains chunks that any of the variations found relevant.
multi_query_retriever: MultiQueryRetriever = MultiQueryRetriever.from_llm(
    retriever=retriever,
    llm=llm
)

# The user query. Keep it short and natural.
# The LLM will rewrite it into multiple interpretations behind the scenes.
query: str = "What is a gradient descent!"

# Invoke the retriever. The output is still a list of Document objects.
# The pattern never changes. Only the strategy changes.
docs: list[Document] = multi_query_retriever.invoke(query)

print("\nMulti Query Retrieved Documents!\n")

for doc in docs:
    print(doc.page_content)