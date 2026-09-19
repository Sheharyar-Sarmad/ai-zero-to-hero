# Chat Model Demo — Groq Setup
# A simple interactive CLI chatbot using LangChain and Groq.

# Setup:
#     uv add langchain-groq python-dotenv

# .env file must contain:
#     GROQ_API_KEY=gsk_...

#  Load Environment Variables 

# Import load_dotenv to load environment variables from a .env file
from dotenv import load_dotenv

# Reads .env and puts GROQ_API_KEY into os.environ
load_dotenv()

#  Imports 

# Import ChatGroq to interact with Groq's chat models
from langchain_groq import ChatGroq

# Import the base chat model class for type hinting
from langchain_core.language_models import BaseChatModel

# Import AIMessage to type hint the model's response
from langchain_core.messages import AIMessage

# Model Configuration 
# Groq SDK: provider-specific class (from langchain_groq)
# Model: openai/gpt-oss-120b — Groq's current production model (Aug 2026)
# temperature: 1 = creative/random (0 = deterministic, 2 = chaos)
model: BaseChatModel = ChatGroq(
    # Specify the Groq model to use
    model="openai/gpt-oss-120b",
    # Set the temperature for creativity and randomness
    temperature=1,
    # max_tokens=20 # max_tokens is optional, its handles the model's default max token limit automatically
)

# Greeting 
# Print a welcome message to the user
print("\nAI openai/gpt-oss-120b Bot is ready to chat! Type 'exit' to quit.\n")

# Chat Loop 
# Start an infinite loop to keep the chat running
while True:
    # Get user input 
    # Prompt the user for input and store it
    user_input: str = input("\nYou: ")

    # Handle empty input 
    # Check if the user pressed enter without typing anything
    if user_input == "":
        # Inform the user that no input was detected
        print("No input detected. Please try again.")
        # Skip the rest of the loop and ask again
        continue

    # Handle exit command 
    # Check if the user wants to quit the chat
    if user_input.lower() == "exit":
        # Print a goodbye message
        print("Exiting the chat. Goodbye!")
        # Break out of the while loop to end the program
        break

    # Send to model, get response 
    # model.invoke() sends the prompt and returns an AIMessage
    response: AIMessage = model.invoke(user_input)

    # Extract clean text 
    # Gemini returns a list of blocks, Groq returns a plain string.
    # This handles both cases safely.
    text = response.content[0]['text'] if isinstance(response.content, list) else response.content

    # Print the answer 
    # Display the model's response to the user
    print(f"\nAI openai/gpt-oss-120b Bot: {text}\n")