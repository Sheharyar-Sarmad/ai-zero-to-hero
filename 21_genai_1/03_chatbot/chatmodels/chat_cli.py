# Chat Model Demo — Groq Setup
# A simple interactive CLI chatbot using LangChain and Groq.

# Setup:
#     uv add langchain-groq python-dotenv

# .env file must contain:
#     GROQ_API_KEY=gsk_...

#  Load Environment Variables 

from dotenv import load_dotenv
load_dotenv()  # Reads .env and puts GROQ_API_KEY into os.environ

#  Imports 
from langchain_groq import ChatGroq
from langchain_core.language_models import BaseChatModel
from langchain_core.messages import AIMessage

# Model Configuration 
# Groq SDK: provider-specific class (from langchain_groq)
# Model: openai/gpt-oss-120b — Groq's current production model (Aug 2026)
# temperature: 1 = creative/random (0 = deterministic, 2 = chaos)
model: BaseChatModel = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=1,
    # max_tokens=20 # max_tokens is optional, its handles the model's default max token limit automatically
)

# Greeting 
print("\nAI openai/gpt-oss-120b Bot is ready to chat! Type 'exit' to quit.\n")

# Chat Loop 
while True:
    # Get user input 
    user_input: str = input("\nYou: ")

    # Handle empty input 
    if user_input == "":
        print("No input detected. Please try again.")
        continue

    # Handle exit command 
    if user_input.lower() == "exit":
        print("Exiting the chat. Goodbye!")
        break

    # Send to model, get response 
    # model.invoke() sends the prompt and returns an AIMessage
    response: AIMessage = model.invoke(user_input)

    # Extract clean text 
    # Gemini returns a list of blocks, Groq returns a plain string.
    # This handles both cases safely.
    text = response.content[0]['text'] if isinstance(response.content, list) else response.content

    # Print the answer 
    print(f"\nAI openai/gpt-oss-120b Bot: {text}\n")