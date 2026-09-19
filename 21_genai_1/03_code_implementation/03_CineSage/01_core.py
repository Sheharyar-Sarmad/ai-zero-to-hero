# This file is a small command-line app called CineSage.
# Its job is to take a paragraph about a movie and return a structured
# breakdown of that movie (title, year, cast, plot, summary, etc.).
# It uses an LLM (via Groq) to do the extraction.

# We import load_dotenv so the app can read environment variables
# from a .env file — specifically the GROQ_API_KEY.
from dotenv import load_dotenv

# This line actually reads the .env file and loads its values
# into the environment so the Groq client can find the API key.
load_dotenv()

# We import ChatGroq — a LangChain wrapper that lets us talk to
# Groq's fast, free LLM API using a simple chat-style interface.
from langchain_groq import ChatGroq

    
# We import ChatPromptTemplate — this is the key piece of this file.
# A prompt template lets us define a reusable message structure with
# placeholders (like {paragraph}) that we can fill in at runtime.
from langchain_core.prompts import ChatPromptTemplate

# WHAT IS A PROMPT TEMPLATE?

# A prompt template is a REUSABLE, PARAMETERIZED prompt.
#
# Without a template, you would write your prompt like this every time:
#     "Extract info from: Interstellar is a sci-fi movie..."
#     "Extract info from: Inception is a thriller..."
#     "Extract info from: The Matrix is..."
# That's repetitive, error-prone, and hard to maintain.
#
# WITH a template, you write the prompt ONCE with a placeholder:
#     "Extract info from: {paragraph}"
# Then every time you call it, you only supply the new paragraph.
#
# WHY WE USE IT:
#   1. Reusability — write the instructions once, use them many times.
#   2. Consistency — every call gets the exact same rules and format.
#   3. Separation of concerns — prompt logic lives apart from app logic.
#   4. Easy to update — change the prompt in one place, not fifty.
#
# USE CASES:
#   - Chatbots with a fixed persona ("You are a helpful assistant...")
#   - Extraction tools (what we are building here)
#   - Summarizers, translators, classifiers, Q&A bots
#   - Anything where the structure stays the same but the input changes
# ============================================================


# We create the chat model instance.
# "openai/gpt-oss-120b" is the Groq-hosted model we want to use.
# ChatGroq handles authentication and the HTTP calls for us.
model = ChatGroq(
    model="openai/gpt-oss-120b"
)

# We build the prompt template.
# ChatPromptTemplate.from_messages() takes a list of (role, content) tuples.
# The "system" message sets the model's behavior and rules.
# The "human" message is the user's turn — and it contains our placeholder.
prompt = ChatPromptTemplate.from_messages([
    (
        # "system" = the invisible instructions the model always follows.
        # This is where we define its role, task, rules, and output format.
        "system",
        """
You are a professional Movie Information Extraction Assistant.

Your task:
Extract useful structured information from a movie paragraph and present it
in a clean, readable format.

Rules:
- Do NOT add explanations
- Do NOT add extra commentary
- Follow the exact format
- If information is missing → write NULL
- Keep summary short (2-3 lines max)
- Do NOT guess unknown facts

Output Format:

Movie Title:
Release Year:
Genre:
Director:
Main Cast:
Setting/Location:
Plot:
Themes:
Ratings:
Notable Features:

Short Summary:
"""
    ),
    (
        # "human" = the user's message.
        # {paragraph} is the placeholder that gets filled in at runtime.
        # Whatever the user types will be inserted here.
        "human",
        "{paragraph}"
    )
])

# The commented-out paragraph below is an example input.
# You can uncomment it later if you want to test without typing.
# It's an Interstellar description that the model would parse.
# paragraph: str = """
# Interstellar is a visually stunning science fiction epic directed by
# Christopher Nolan. Released in 2014, the film stars Matthew McConaughey,
# Anne Hathaway, Jessica Chastain, and Michael Caine. The story revolves
# around a group of astronauts who travel through a wormhole near Saturn
# in search of a new home for humanity as Earth faces environmental collapse.
# The movie was widely appreciated for its emotional depth, scientific
# accuracy, and Hans Zimmer’s powerful soundtrack. It holds a rating of
# 8.6 on IMDb and is often considered one of the greatest sci-fi films
# of the 21st century.
# """

# Print an empty line for spacing.
print("")
# Print the app's title banner.
print("  CineSage — Movie Paragraph Extractor")
# Print another empty line.
print("")
# Print the rules header.
print("  Rules:")
# Print rule 1 — tell the user what to do.
print("   - Paste a paragraph about a movie to extract its info.")
# Print rule 2 — tell the user how to exit.
print("   - Type 'exit' at any time to quit the app.")
# Print another empty line for spacing.
print("")

# Start an infinite loop so the user can keep submitting paragraphs
# without restarting the script.
while True:
    # Prompt the user for a paragraph and store it as a string.
    # The input() function pauses execution until the user presses Enter.
    paragraph: str = input("\nEnter your paragraph: ")

    # Format the prompt template with the user's paragraph.
    # This replaces {paragraph} with whatever the user typed,
    # producing a list of properly structured message objects
    # (a system message + a human message).
    messages = prompt.format_messages(
        paragraph=paragraph
    )

    # Invoke the model.
    # We send the formatted messages to Groq, and the model returns
    # an AIMessage containing the extracted movie information.
    response = model.invoke(messages)

    # Print the model's reply.
    # response.content is the actual text the model generated —
    # the clean, structured movie breakdown.
    print(f"\n{response.content}\n")