# Local Hugging Face Model Demo
# ------------------------------
# Runs a Hugging Face model locally on your machine using the transformers
# library — no API calls, no internet needed after the first download.

# Setup:
#     uv add langchain-huggingface transformers torch accelerate python-dotenv

# First run downloads the model (~2.2 GB) to:
#     C:\\Users\\Dell\\.cache\\huggingface\\

# Load Environment Variables 
# Not strictly needed for local models, but useful if you later add API keys.
# Import load_dotenv to read environment variables from a .env file
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Imports 
# Import ChatHuggingFace and HuggingFacePipeline from langchain_huggingface
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

# Import AIMessage to type hint the model's response
from langchain_core.messages import AIMessage

# === Load the Model Into a Pipeline ===
# HuggingFacePipeline is the low-level wrapper around Hugging Face's
# `transformers.pipeline()` function. It loads the model into RAM
# and runs inference directly on your machine.
#
# - model_id          : the Hugging Face repo to download and load
# - task              : what the pipeline should do (text-generation here)
# - pipeline_kwargs   : extra arguments passed to transformers.pipeline()
llm: HuggingFacePipeline = HuggingFacePipeline.from_model_id(
    # Small 1.1B model — runs on CPU
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    # Task type
    task="text-generation",
    # Extra arguments passed to transformers.pipeline()
    pipeline_kwargs={
        # Maximum tokens to generate per response
        "max_new_tokens": 512,
        # Deterministic output (no randomness)
        "do_sample": False,
        # Slightly discourage repeating the same words
        "repetition_penalty": 1.03,
    },
)

# Wrap It in a Chat Interface 
# ChatHuggingFace converts chat-style messages (system/user/assistant)
# into the raw text format that HuggingFacePipeline expects.
model: ChatHuggingFace = ChatHuggingFace(llm=llm)

# Send a Prompt 
# model.invoke() runs the pipeline and returns an AIMessage.
# On CPU, this can take 10-30 seconds for the first response.
response: AIMessage = model.invoke("how are you!")

# Print the Answer 
# .content extracts just the text from the AIMessage object.
print(response.content)