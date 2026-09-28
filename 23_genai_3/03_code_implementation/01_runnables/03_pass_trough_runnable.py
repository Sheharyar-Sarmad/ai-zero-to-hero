# Script Goal: Demonstrate sequential chain composition and data transformation using RunnableSequence and RunnableLambda in LangChain.
# Why transformation is needed: The output of step 1 (code_generation_chain) is a raw code string. Step 2 (explanation_chain) expects a dictionary with key 'code'.
# RunnableLambda bridges this gap by intercepting the raw string and wrapping it into the dict payload required by the downstream prompt.

from dotenv import load_dotenv

load_dotenv()

from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda, RunnableSequence

# Initialize model with active Groq endpoint
model: ChatGroq = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=1,
    max_tokens=5000,
)

parser: StrOutputParser = StrOutputParser()

# Define prompt templates for generation and explanation
code_prompt: ChatPromptTemplate = ChatPromptTemplate.from_messages([
    ("system", "You are a code generator"),
    ("human", "{topic}"),
])

explain_prompt: ChatPromptTemplate = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a helpful assistant who explains code in simple terms",
    ),
    (
        "human",
        "Explain the following code in simple words:\n{code}",
    ),
])

# Sub-chain 1: Accepts {'topic': '...'} and returns raw string code
code_generation_chain: RunnableSequence = (
    code_prompt
    | model
    | parser
)

# Sub-chain 2: Accepts {'code': '...'} and returns explanation string
explanation_chain: RunnableSequence = (
    explain_prompt
    | model
    | parser
)

# Sequential chain pipeline
# 1. code_generation_chain receives topic dict and generates raw code string
# 2. RunnableLambda maps the raw code string into {'code': code} payload
# 3. explanation_chain receives mapped dict and generates final explanation
seq: RunnableSequence = (
    code_generation_chain
    | RunnableLambda(lambda code: {"code": code})
    | explanation_chain
)

# Execute the combined sequential chain
result: str = seq.invoke(
    {"topic": "Write a code of palindrome in python"}
)

print("\nPass Through Runnable Example!\n")
print(result)

# Practice exercise notes:
# Q1: What happens if you remove RunnableLambda?
# Removing it causes a schema error because explanation_chain expects a dictionary with key 'code', not a raw string.
# Q2: Pipeline data flow:
# Dict {'topic': ...} -> Prompt 1 -> LLM -> Raw String -> RunnableLambda -> Dict {'code': ...} -> Prompt 2 -> LLM -> String Result