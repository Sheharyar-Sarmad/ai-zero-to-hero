# Hugging Face Endpoint Demo
# ---------------------------
# Uses the Hugging Face Serverless Inference API to call a hosted model
# without downloading it locally.

# Setup:
#     uv add langchain-huggingface python-dotenv

# .env file must contain:
#     HUGGINGFACEHUB_ACCESS_TOKEN=hf_...

# Load Environment Variables 
# Import os module for reading environment variables
import os

# Import load_dotenv to load environment variables from a .env file
from dotenv import load_dotenv

# Reads .env and loads HUGGINGFACEHUB_ACCESS_TOKEN into os.environ
load_dotenv()

# Imports 
# Import ChatHuggingFace and HuggingFaceEndpoint from langchain_huggingface
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

# Import AIMessage to type hint the model's response
from langchain_core.messages import AIMessage

# Configure the Hugging Face Endpoint 
# HuggingFaceEndpoint is the raw LLM wrapper (low-level interface).
# It knows HOW to send requests to Hugging Face's servers,
# but it doesn't natively support chat-style messages.
llm: HuggingFaceEndpoint = HuggingFaceEndpoint(
    # Model ID on Hugging Face Hub
    repo_id="deepseek-ai/DeepSeek-R1",
    # Required: the model's task type
    task="text-generation",
    # Auth token from .env
    huggingfacehub_api_token=os.environ.get("HUGGINGFACEHUB_ACCESS_TOKEN"),
)

# Wrap It in a Chat Interface 
# ChatHuggingFace is the high-level chat wrapper.
# It converts chat-style messages (system/user/assistant) into whatever
# format the underlying HuggingFaceEndpoint expects.
model: ChatHuggingFace = ChatHuggingFace(
    # Pass the low-level endpoint into the chat wrapper
    llm=llm,
)

# Send a Prompt and Get the Answer 
# model.invoke() sends the prompt and returns an AIMessage object.
response: AIMessage = model.invoke("who are you?")

# Print the Answer 
# .content extracts just the text from the AIMessage object.
print(response.content)