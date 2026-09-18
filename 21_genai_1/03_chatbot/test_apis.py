import os
from dotenv import load_dotenv

# Load API keys from .env file
load_dotenv()

# Test OpenAI (Requires paid credits - commented out for now)
# from langchain_openai import ChatOpenAI
# try:
#     llm = ChatOpenAI(model="gpt-4o-mini")
#     print("OpenAI:", llm.invoke("Say 'OpenAI works!'").content)
# except Exception as e:
#     print("OpenAI Error:", e)

# Test Groq (Updated to current working models)
from langchain_groq import ChatGroq
try:
    # For a fast, cheap option:
    llm = ChatGroq(model="openai/gpt-oss-20b")
    # For a more capable option, use: "openai/gpt-oss-120b"
    print("Groq:", llm.invoke("Say 'Groq works!'").content)
except Exception as e:
    print("Groq Error:", e)

# Test Google Gemini (Updated to the current stable model)
from langchain_google_genai import ChatGoogleGenerativeAI
try:
    llm = ChatGoogleGenerativeAI(model="gemini-3.6-flash")
    print("Gemini:", llm.invoke("Say 'Gemini works!'").content)
except Exception as e:
    print("Gemini Error:", e)

# Test Mistral (Wait 60s if rate-limited)
from langchain_mistralai import ChatMistralAI
try:
    # Try "Mistral Small 4" if you have access
    llm = ChatMistralAI(model="mistral-small-latest")
    print("Mistral:", llm.invoke("Say 'Mistral works!'").content)
except Exception as e:
    print("Mistral Error:", e)