# Load environment variables from the .env file into the system environment
# This allows ChatGroq to automatically detect the GROQ_API_KEY environment variable
from dotenv import load_dotenv

load_dotenv()

# Import the ChatGroq model wrapper designed for LangChain integration
from langchain_groq import ChatGroq

# Import ChatPromptTemplate to structure structured messages for the model
from langchain_core.prompts import ChatPromptTemplate

# Import StrOutputParser to extract raw string content from the model AIMessage output
from langchain_core.output_parsers import StrOutputParser

# Import message types and runnable sequence types for explicit type hinting
from langchain_core.messages import AIMessage, BaseMessage
from langchain_core.runnables import RunnableSequence

# Define a structured prompt template using a system or human message pair
# The placeholder topic will be filled dynamically when the chain is invoked
prompt: ChatPromptTemplate = ChatPromptTemplate.from_messages([
    ("human", "Explain {topic} in simple words")
])

# Initialize the Groq language model with specific generation parameters
# Low temperature enforces deterministic responses, while max_tokens limits generation length
model: ChatGroq = ChatGroq(
    model="qwen/qwen3.8-27b",
    temperature=0,
    max_tokens=500,
)

# Initialize the string output parser to automatically process the response object
parser: StrOutputParser = StrOutputParser()

# Construct a LangChain Expression Language (LCEL) chain using the pipe operator
# Data flows sequentially: input dictionary -> prompt template -> LLM model -> string output parser
chain: RunnableSequence[dict, str] = prompt | model | parser

# Invoke the chain by passing a dictionary where the key matches the template variable topic
# Note: Since the output parser is active, the chain returns a plain string, not an AIMessage object
response: str = chain.invoke({
    "topic": "What is a neural network? Explain with clear analogies and step-by-step structure for a beginner student."
})

# Display the parsed string output directly
print(f"\n{response}\n")