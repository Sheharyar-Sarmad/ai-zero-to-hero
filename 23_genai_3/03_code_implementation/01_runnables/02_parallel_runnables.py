# Load environment variables from the .env file into system environment variables
# This allows ChatGroq to automatically pick up the GROQ_API_KEY environment variable
from dotenv import load_dotenv

load_dotenv()

# Import the ChatGroq model wrapper for LangChain integration
from langchain_groq import ChatGroq

# Import ChatPromptTemplate to build structured input messages for language models
from langchain_core.prompts import ChatPromptTemplate

# Import StrOutputParser to convert model AIMessage outputs directly into clean string variables
from langchain_core.output_parsers import StrOutputParser

# Import LangChain runnable primitives for building sequential and parallel execution pipelines
from langchain_core.runnables import RunnableSequence, RunnableParallel

# Import TypedDict from standard typing library to define precise return structure schemas
from typing import TypedDict

# Define the first prompt template targeting a concise, high-level overview
short_prompt: ChatPromptTemplate = ChatPromptTemplate.from_messages([
    ("human", "Explain {topic} in 1-2 lines")
])

# Define the second prompt template targeting a comprehensive, in-depth explanation
long_prompt: ChatPromptTemplate = ChatPromptTemplate.from_messages([
    ("human", "Explain {topic} in extreme depth and in much detail")
])

# Initialize the ChatGroq model instance with deterministic temperature and token limit controls
model: ChatGroq = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0,
    max_tokens=500,
)

# Initialize the string parser to extract pure text from the raw model response
parser: StrOutputParser = StrOutputParser()

# Define a TypedDict schema representing the structure of the dictionary returned by the parallel chain
class ChainDict(TypedDict):
    short: str
    long: str

# Define independent sequential sub-chains using the pipe operator
short_chain = short_prompt | model | parser
long_chain = long_prompt | model | parser

# Combine sub-chains into a single parallel runnable block using RunnableParallel
# Incoming inputs are dispatched concurrently to each branch, returning a combined dictionary
chain: RunnableParallel = RunnableParallel({
    "short": short_chain,
    "detailed": long_chain
})

# Execute the parallel chain with a single input dictionary
# Both short_chain and long_chain receive the topic input concurrently
result: ChainDict = chain.invoke({
    "short": {"topic": "machine learning"},
    "detailed": {"topic": "deep learning"}
})

# Display the output extracted from the short explanation branch
print("\nShort Answer: \n")
print(result["short"])

# Display the output extracted from the detailed explanation branch
print("\nLong Answer: \n")
print(result["detailed"])