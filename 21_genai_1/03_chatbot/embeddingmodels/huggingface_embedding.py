from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings: HuggingFaceEmbeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
)

texts: list[str] = [
    "You are going to learn Gen AI!",
    "My name is Sheharyar Sarmad.",
    "Deep learnign is more hard than python",
    "If you choose DSA with c++ and java you are already cooked"
]

vector: list[list[float]] = embeddings.embed_documents(texts)
print(vector)