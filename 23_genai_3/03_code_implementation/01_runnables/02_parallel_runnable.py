# SCRIPT GOAL:
# Demonstrate concurrent (parallel) pipeline execution using LangChain's RunnableParallel.
#
# WHY WE NEED PARALLEL RUNNABLES:
# Standard sequential chains run operations step-by-step (A -> B -> C). If you need 
# multiple independent responses from an LLM (such as a short summary AND an 
# in-depth explanation), running them sequentially causes significant latency overhead 
# because total execution time equals the sum of all response times (T_short + T_long).
#
# RunnableParallel solves this by dispatching multiple sub-chains concurrently across 
# separate threads. Total execution time drops to max(T_short, T_long), drastically 
# cutting response latency and enabling efficient multi-task/map-reduce patterns.

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
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnableLambda 

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
    detailed: str 

# Define independent sequential sub-chains using LCEL pipe operator syntax (|)
# Chain 1: Formats short_prompt -> Sends to LLM -> Parses text string
short_chain = short_prompt | model | parser 

# Chain 2: Formats long_prompt -> Sends to LLM -> Parses text string
long_chain = long_prompt | model | parser 

# Combine sub-chains into a single parallel runnable block using RunnableParallel 
# Incoming inputs are dispatched concurrently to each branch, returning a combined dictionary.
# RunnableLambda is used to extract specific sub-dictionaries ('short' and 'detailed') from the root input payload.
chain: RunnableParallel = RunnableParallel({ 
    "short": RunnableLambda(lambda x: x['short']) | short_chain, 
    "detailed": RunnableLambda(lambda x: x['detailed']) | long_chain 
}) 

# Execute the parallel chain with a single input dictionary 
# Both branches execute concurrently via thread workers inside RunnableParallel
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

