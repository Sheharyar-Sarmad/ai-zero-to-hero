# Import the HuggingFaceEmbeddings class from the langchain_huggingface package
from langchain_huggingface import HuggingFaceEmbeddings

# Import load_dotenv to load environment variables from a .env file
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Initialize the HuggingFaceEmbeddings object with a specific sentence transformer model
embeddings: HuggingFaceEmbeddings = HuggingFaceEmbeddings(
    # Specify the model name to be used for generating embeddings
    model_name="sentence-transformers/all-MiniLM-L6-v2",
)

# Create a list of sample text strings to be embedded
texts: list[str] = [
    # First sample text
    "You are going to learn Gen AI!",
    # Second sample text
    "My name is Sheharyar Sarmad.",
    # Third sample text
    "Deep learnign is more hard than python",
    # Fourth sample text
    "If you choose DSA with c++ and java you are already cooked"
]

# Generate embeddings for the list of texts using the embed_documents method
vector: list[list[float]] = embeddings.embed_documents(texts)

# Print the resulting vector embeddings to the console
print(vector)