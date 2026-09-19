# This file is a small command-line app called CineSage.
# Its job is to take a paragraph about a movie and return a structured
# JSON breakdown of that movie (title, year, cast, plot, summary, etc.).
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

# We import BaseModel and Field from pydantic to define the JSON schema.
from pydantic import BaseModel, Field

# We import Optional and List to type the fields precisely.
from typing import Optional, List

# We import ChatPromptTemplate to build a reusable, parameterized prompt.
from langchain_core.prompts import ChatPromptTemplate


# The Movie model defines the exact JSON shape we want back from the LLM.
# Every field here becomes a key in the final JSON output.
class Movie(BaseModel):
    title: str = Field(description="Movie title")
    release_year: Optional[int] = Field(description="Year the movie was released")
    genre: List[str] = Field(description="List of genres")
    director: Optional[str] = Field(description="Director's name")
    cast: List[str] = Field(description="List of main cast members")
    setting: Optional[str] = Field(description="Where the movie takes place")
    plot: Optional[str] = Field(description="Short plot description")
    themes: List[str] = Field(description="List of themes explored")
    rating: Optional[float] = Field(description="IMDb or similar rating")
    notable_features: Optional[str] = Field(description="Any standout features")
    summary: str = Field(description="Short 2-3 line summary")


# We create the chat model instance.
# "openai/gpt-oss-120b" is the Groq-hosted model we want to use.
# ChatGroq handles authentication and the HTTP calls for us.
model = ChatGroq(
    model="openai/gpt-oss-120b"
)

# We wrap the model so it returns a Movie object directly,
# instead of free-form text. This is the JSON-mode equivalent.
structured_model = model.with_structured_output(Movie)


# We build the prompt template.
# The "system" message sets the model's behavior and rules.
# The "human" message is the user's turn — it contains our placeholder.
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are a professional Movie Information Extraction Assistant.

Your task:
Extract structured information from a movie paragraph and return it as JSON.

Rules:
- Return ONLY valid JSON that matches the given schema
- Do NOT add explanations or extra commentary
- If information is missing, use null (or an empty list for arrays)
- Keep the summary short (2-3 lines max)
- Do NOT guess unknown facts
"""
    ),
    (
        "human",
        "{paragraph}"
    )
])


# Print the app's title banner and rules.
print("")
print("  CineSage — Movie Paragraph Extractor")
print("")
print("  Rules:")
print("   - Paste a paragraph about a movie to extract its info.")
print("   - Type 'exit' at any time to quit the app.")
print("")

# Start an infinite loop so the user can keep submitting paragraphs
# without restarting the script.
while True:
    # Prompt the user for a paragraph.
    paragraph: str = input("\nEnter your paragraph: ")

    # Handle exit command.
    if paragraph.strip().lower() == "exit":
        print("\nExiting CineSage. Goodbye!\n")
        break

    # Skip empty input.
    if paragraph.strip() == "":
        print("No input detected. Please try again.")
        continue

    # Format the prompt with the user's paragraph.
    messages = prompt.format_messages(paragraph=paragraph)

    # Invoke the structured model and get a Movie object back.
    movie: Movie = structured_model.invoke(messages)

    # Print the result as pretty JSON.
    print(f"\n{movie.model_dump_json(indent=2)}\n")