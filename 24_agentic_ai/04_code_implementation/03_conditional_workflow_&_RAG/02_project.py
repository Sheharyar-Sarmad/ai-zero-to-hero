import os
from typing import TypedDict, Annotated, Literal
from functools import lru_cache

from dotenv import load_dotenv
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from langgraph.graph.state import CompiledStateGraph
from langgraph.checkpoint.memory import InMemorySaver

from langchain_groq import ChatGroq
from langchain_core.messages import BaseMessage, AIMessage
from langchain_core.documents import Document
from langchain_core.vectorstores import VectorStoreRetriever
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

load_dotenv()  # Load API keys and environment variables from .env

# Convert text into vectors so FAISS can perform semantic similarity search
embeddings_model: HuggingFaceEmbeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

@lru_cache
def build_retriever(pdf_path: str) -> VectorStoreRetriever:
    """Build a FAISS retriever from a PDF and cache it."""
    try:
        if not os.path.isfile(pdf_path):
            raise FileNotFoundError(f"PDF file not found: {pdf_path}")

        loader: PyPDFLoader = PyPDFLoader(pdf_path)  # Load PDF pages
        documents: list[Document] = loader.load()

        # Split large pages into smaller chunks for better retrieval
        splitter: RecursiveCharacterTextSplitter = RecursiveCharacterTextSplitter(
            chunk_size=800,
            chunk_overlap=100
        )

        chunks: list[Document] = splitter.split_documents(documents)

        # Store chunk embeddings in FAISS for semantic search
        vectorstore: FAISS = FAISS.from_documents(chunks, embeddings_model)

        # Return a retriever that returns the 4 most relevant chunks
        return vectorstore.as_retriever(search_kwargs={"k": 4})

    except Exception as err:
        raise Exception(f"Error building retriever: {err}") from err

# Create separate retrievers for academic and fee information
academic_retriever: VectorStoreRetriever = build_retriever("./academics_handbook.pdf")
fee_retriever: VectorStoreRetriever = build_retriever("./fee_structure.pdf")

# LLM is used for classification and final answer generation
llm: ChatGroq = ChatGroq(
    model="openai/gpt-oss-20b",
    max_tokens=1024,
    temperature=0.4
)

class State(TypedDict):
    # Student's selected programme is available throughout the workflow
    programme: str

    # add_messages preserves the conversation history when messages are updated
    messages: Annotated[list[BaseMessage], add_messages]

    # Classifier stores whether the query is academic, fee, or general
    query_type: str

    # Final combined context used by the response node
    retrieved_context: str

    # These fields store results from the parallel academic nodes
    handbook_context: str
    course_context: str
    policy_context: str

def classifier_node(state: State) -> dict[str, str]:
    """Classify the student's query."""
    try:
        query: str = state["messages"][-1].content  # Get the latest user query

        # Ask the LLM to classify the query into one of three workflow branches
        prompt: str = (
            "Classify this student query into exactly one category: "
            "'academic', 'fee', or 'general'.\n\n"
            "academic: attendance, exams, grading, credits, promotion, "
            "course structure, training, degree requirements.\n"
            "fee: tuition, payment, refund, late charges, scholarships, money.\n"
            "general: greetings, casual talk, or unrelated questions.\n\n"
            f"Query: {query}\n\n"
            "Return only: academic, fee, or general."
        )

        response: AIMessage = llm.invoke(prompt)  # Run classification with the LLM
        category: str = response.content.strip().lower()

        # Normalize the LLM output so the router always receives a valid category
        if "academic" in category:
            category = "academic"
        elif "fee" in category:
            category = "fee"
        else:
            category = "general"

        return {"query_type": category}

    except Exception as err:
        raise Exception(f"Error in classifier_node: {err}") from err

def academic_start_node(state: State) -> dict:
    """Start the parallel academic branch."""
    return {}  # This node only triggers the three independent academic nodes

def academic_handbook_node(state: State) -> dict[str, str]:
    """Retrieve general academic information."""
    try:
        query: str = state["messages"][-1].content

        # Search the academic handbook for chunks relevant to the user's question
        docs: list[Document] = academic_retriever.invoke(query)

        # Convert retrieved documents into one context string
        context: str = "\n\n".join(doc.page_content for doc in docs)

        return {"handbook_context": context}

    except Exception as err:
        raise Exception(f"Error in academic_handbook_node: {err}") from err

def course_structure_node(state: State) -> dict[str, str]:
    """Retrieve course-related information."""
    try:
        query: str = state["messages"][-1].content

        # Add course-specific keywords to guide this parallel retrieval branch
        search_query: str = f"{query} course subjects curriculum credits programme"

        docs: list[Document] = academic_retriever.invoke(search_query)

        # Store this branch's retrieved information separately
        context: str = "\n\n".join(doc.page_content for doc in docs)

        return {"course_context": context}

    except Exception as err:
        raise Exception(f"Error in course_structure_node: {err}") from err

def academic_policy_node(state: State) -> dict[str, str]:
    """Retrieve academic policy information."""
    try:
        query: str = state["messages"][-1].content

        # Add policy-specific keywords to focus this retrieval branch
        search_query: str = f"{query} policy rules attendance examination requirements"

        docs: list[Document] = academic_retriever.invoke(search_query)

        # Store the policy retrieval result separately before fan-in
        context: str = "\n\n".join(doc.page_content for doc in docs)

        return {"policy_context": context}

    except Exception as err:
        raise Exception(f"Error in academic_policy_node: {err}") from err

def merge_academic_node(state: State) -> dict[str, str]:
    """Merge parallel academic results."""
    try:
        # Fan-in combines the three independently retrieved contexts
        context: str = "\n\n".join([
            f"HANDBOOK INFORMATION:\n{state.get('handbook_context', '')}",
            f"COURSE INFORMATION:\n{state.get('course_context', '')}",
            f"POLICY INFORMATION:\n{state.get('policy_context', '')}"
        ])

        return {"retrieved_context": context}

    except Exception as err:
        raise Exception(f"Error in merge_academic_node: {err}") from err

def fee_rag_node(state: State) -> dict[str, str]:
    """Retrieve fee information."""
    try:
        query: str = state["messages"][-1].content

        # Search only the fee structure document for fee-related questions
        docs: list[Document] = fee_retriever.invoke(query)

        context: str = "\n\n".join(doc.page_content for doc in docs)

        return {"retrieved_context": context}

    except Exception as err:
        raise Exception(f"Error in fee_rag_node: {err}") from err

def general_node(state: State) -> dict[str, str]:
    """Handle queries that do not need retrieval."""

    # This marker tells response_node to use the LLM without RAG context
    return {"retrieved_context": "NO_RETRIEVAL_NEEDED"}

def response_node(state: State) -> dict[str, list[tuple[str, str]]]:
    """Generate the final response."""
    try:
        query: str = state["messages"][-1].content
        programme: str = state.get("programme", "Unknown")
        context: str = state["retrieved_context"]

        # General questions do not need information from the college documents
        if context == "NO_RETRIEVAL_NEEDED":
            prompt: str = (
                f"You are a friendly college assistant helping a {programme} student.\n\n"
                f"Question: {query}\n\n"
                "Answer naturally and clearly."
            )
        else:
            # RAG questions use the context collected by the previous nodes
            prompt: str = (
                f"You are a college assistant helping a {programme} student.\n\n"
                "Use the official college information below to answer accurately.\n\n"
                f"College context:\n{context}\n\n"
                f"Question: {query}\n\n"
                f"Give a clear answer relevant to {programme}. "
                "Do not invent information that is not supported by the context."
            )

        response: AIMessage = llm.invoke(prompt)  # Generate the final answer
        answer: str = response.content.strip()

        # Return an AI message so add_messages updates conversation history
        return {"messages": [("ai", answer)]}

    except Exception as err:
        raise Exception(f"Error in response_node: {err}") from err

def route_query(state: State) -> Literal["academic_parallel", "fee_rag", "general"]:
    # Return the graph route based on the classifier's result
    if state["query_type"] == "academic":
        return "academic_parallel"

    if state["query_type"] == "fee":
        return "fee_rag"

    return "general"

graph: StateGraph[State] = StateGraph(State)  # Create the graph using our State schema

# Register every function as a node in the workflow
graph.add_node("classifier", classifier_node)
graph.add_node("academic_start", academic_start_node)
graph.add_node("academic_handbook", academic_handbook_node)
graph.add_node("course_structure", course_structure_node)
graph.add_node("academic_policy", academic_policy_node)
graph.add_node("merge_academic", merge_academic_node)
graph.add_node("fee_rag", fee_rag_node)
graph.add_node("general", general_node)
graph.add_node("response", response_node)

graph.add_edge(START, "classifier")  # Every query starts with classification

# Conditional routing chooses exactly one major branch
graph.add_conditional_edges("classifier", route_query, {
    "academic_parallel": "academic_start",
    "fee_rag": "fee_rag",
    "general": "general"
})

# Fan-out: one academic task starts three independent retrieval tasks
graph.add_edge("academic_start", "academic_handbook")
graph.add_edge("academic_start", "course_structure")
graph.add_edge("academic_start", "academic_policy")

# Fan-in: response waits for all three academic branches to finish
graph.add_edge("academic_handbook", "merge_academic")
graph.add_edge("course_structure", "merge_academic")
graph.add_edge("academic_policy", "merge_academic")

# All major branches eventually reach the same response node
graph.add_edge("merge_academic", "response")
graph.add_edge("fee_rag", "response")
graph.add_edge("general", "response")

graph.add_edge("response", END)  # Final response ends the workflow

# Checkpointer stores graph state for each conversation thread
checkpointer: InMemorySaver = InMemorySaver()
app: CompiledStateGraph = graph.compile(checkpointer=checkpointer)

# These are the programmes the CLI accepts
ALLOWED_PROGRAMMES: tuple[str, ...] = ("BCA", "BBA", "B.Com(H)")

def get_programme() -> str:
    """Get a valid programme from the user."""
    while True:
        print("\nSelect your programme:")
        print("1. BCA")
        print("2. BBA")
        print("3. B.Com(H)")
        print("Type 'exit' to quit.")

        programme: str = input("Programme: ").strip()

        if programme.lower() == "exit":
            raise SystemExit

        if programme in ALLOWED_PROGRAMMES:
            return programme

        print("Invalid programme. Choose BCA, BBA, or B.Com(H).")

def main() -> None:
    """Run the CLI application."""
    print("College RAG Assistant")

    programme: str = get_programme()  # Ask the student for their programme

    print(f"\nProgramme: {programme}")
    print("Ask your question or type 'exit'.")

    # thread_id keeps each conversation's checkpoint state separate
    config: dict = {
        "configurable": {
            "thread_id": f"student-{programme.lower()}"
        }
    }

    while True:
        query: str = input("\nYou: ").strip()

        if query.lower() == "exit":
            print("Goodbye.")
            break

        if not query:
            print("Please enter a question.")
            continue

        # Build the initial state that enters the LangGraph workflow
        state: State = {
            "programme": programme,
            "messages": [("human", query)],
            "query_type": "",
            "retrieved_context": "",
            "handbook_context": "",
            "course_context": "",
            "policy_context": ""
        }

        try:
            # Execute the complete graph from START to END
            result: State = app.invoke(state, config)

            # The last message is the assistant's final answer
            print(f"\nAssistant: {result['messages'][-1].content}")

        except Exception as err:
            print(f"Error: {err}")

if __name__ == "__main__":
    main()  # Run the application