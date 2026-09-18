# LangChain Basics

> Prerequisite: You've already made raw API calls to OpenAI, Gemini, and Claude in `02_using_LLM.md`. This file explains why you'd want a framework on top of that, and what's actually inside it.

---

## 1. The Problem: SDK Fragmentation

Every provider ships its own SDK, with its own object shapes, its own auth pattern, and its own way of formatting messages. If you build directly against one, switching providers later means rewriting your core logic — not just swapping a config value.

Here's the same "ask a question" call across three providers:

```python
# --- OpenAI ---
from openai import OpenAI
client = OpenAI(api_key="...")
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Explain gravity in one line."}]
)
print(response.choices[0].message.content)

# --- Google Gemini ---
import google.generativeai as genai
genai.configure(api_key="...")
model = genai.GenerativeModel("gemini-1.5-pro")
response = model.generate_content("Explain gravity in one line.")
print(response.text)

# --- Anthropic Claude ---
import anthropic
client = anthropic.Anthropic(api_key="...")
response = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=100,
    messages=[{"role": "user", "content": "Explain gravity in one line."}]
)
print(response.content[0].text)
```

Notice the pain points:

- **Different client constructors** (`OpenAI()`, `genai.configure()`, `anthropic.Anthropic()`)
- **Different response objects** (`.choices[0].message.content` vs `.text` vs `.content[0].text`)
- **Different required parameters** (Claude forces `max_tokens`; OpenAI and Gemini don't)
- **No shared interface** for prompts, memory, tool-calling, or chaining multiple calls together

If your app needs to try Gemini for cost, fall back to Claude for reasoning, and A/B test GPT-4o — you're maintaining three separate code paths.

**LangChain's core value proposition:** it wraps all of these behind one consistent interface, so your application code stays the same regardless of which model is running underneath.

```python
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_anthropic import ChatAnthropic

# Same method call (.invoke), regardless of provider
llm_openai = ChatOpenAI(model="gpt-4o")
llm_gemini = ChatGoogleGenerativeAI(model="gemini-1.5-pro")
llm_claude = ChatAnthropic(model="claude-3-5-sonnet-20241022")

for llm in [llm_openai, llm_gemini, llm_claude]:
    print(llm.invoke("Explain gravity in one line.").content)
```

One method (`.invoke`), one response shape (`.content`). That's the entire pitch of LangChain in a nutshell — everything else is built on top of this abstraction.

---

## 2. The 6 Core Components

Think of a LangChain application like a **car**. Each component below maps to a part of that car, so you remember not just *what* it does, but *where* it sits in the system.

### Models — The Engine

The engine is what actually generates power (text). LangChain doesn't build its own LLMs — it builds a standard **interface** so any engine (OpenAI, Gemini, Claude, local models via Ollama) can be dropped into the same car.

```python
from langchain_anthropic import ChatAnthropic

llm = ChatAnthropic(model="claude-3-5-sonnet-20241022", temperature=0.7)

response = llm.invoke("Give me one productivity tip.")
print(response.content)
```

Swap `ChatAnthropic` for `ChatOpenAI` or `ChatGoogleGenerativeAI` and the rest of your code doesn't change. That's the whole point of an "engine standard."

---

### Prompts — The Steering Wheel

The steering wheel is how *you* direct the engine's power. Hardcoding f-strings works for a demo, but production apps need **reusable, validated, dynamic templates**. That's what `PromptTemplate` gives you.

```python
from langchain_core.prompts import PromptTemplate

template = PromptTemplate.from_template(
    "You are a {role}. Explain {topic} to a beginner in 2 sentences."
)

prompt = template.invoke({"role": "chemistry teacher", "topic": "oxidation"})
print(prompt.text)
```

Why not just use an f-string? Because `PromptTemplate`:
- Validates that required variables are provided (fails loudly, not silently)
- Plugs directly into Chains (next section) without extra glue code
- Can be composed with system messages, few-shot examples, and chat history

---

### Chains — The Drivetrain

The drivetrain transfers power from the engine to the wheels — it **connects components together** so output flows automatically from one step to the next. A Chain links a Prompt → a Model → an Output Parser.

**Old way (deprecated but still seen in older code): `LLMChain`**

```python
from langchain.chains import LLMChain
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import PromptTemplate

llm = ChatAnthropic(model="claude-3-5-sonnet-20241022")
prompt = PromptTemplate.from_template("Write a tagline for a {product}.")

chain = LLMChain(llm=llm, prompt=prompt)
print(chain.invoke({"product": "eco-friendly water bottle"}))
```

**Modern way: LCEL (LangChain Expression Language)** — uses the `|` pipe operator, similar to Unix pipes:

```python
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = ChatAnthropic(model="claude-3-5-sonnet-20241022")
prompt = PromptTemplate.from_template("Write a tagline for a {product}.")
parser = StrOutputParser()

chain = prompt | llm | parser   # prompt output feeds into llm, llm output feeds into parser
result = chain.invoke({"product": "eco-friendly water bottle"})
print(result)
```

> **Use LCEL for all new code.** `LLMChain` is legacy syntax — you'll see it in older tutorials, but it's being phased out in favor of the pipe (`|`) syntax.

---

### Memory — The Rearview Mirror

An LLM API call is stateless by default — every request is amnesia. The rearview mirror lets the "driver" (the model) see where it's been. `ConversationBufferMemory` stores prior turns and re-injects them into each new prompt.

```python
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain_anthropic import ChatAnthropic

llm = ChatAnthropic(model="claude-3-5-sonnet-20241022")
memory = ConversationBufferMemory()

conversation = ConversationChain(llm=llm, memory=memory)

conversation.invoke("Hi, my name is Sara.")
response = conversation.invoke("What's my name?")
print(response["response"])  # Correctly recalls "Sara"
```

Under the hood, memory just concatenates past exchanges into the prompt context — there's no magic, just automated bookkeeping so you don't manually manage a growing message list.

> Note: `ConversationBufferMemory` and `ConversationChain` are in LangChain's legacy API. For new projects, LangChain recommends `RunnableWithMessageHistory` or LangGraph's built-in state — but the *concept* (re-inject past turns) is identical, and buffer memory is still the fastest way to understand it.

---

### Indexes — The Glovebox

The glovebox holds reference material the driver doesn't have memorized but can pull out when needed. This is **RAG (Retrieval-Augmented Generation)** — giving the model access to your documents instead of relying on what it learned during training.

The RAG pipeline has four steps:

```python
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

# 1. LOAD — pull raw content from a source
loader = TextLoader("company_handbook.txt")
documents = loader.load()

# 2. SPLIT — break into small, retrievable chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(documents)

# 3. EMBED — convert chunks into vectors and store them
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(chunks, embeddings)

# 4. RETRIEVE — fetch the most relevant chunks for a query
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
relevant_chunks = retriever.invoke("What is the vacation policy?")

for chunk in relevant_chunks:
    print(chunk.page_content[:200])
```

Those retrieved chunks then get stuffed into your Prompt template as context, so the Model answers using *your* data instead of guessing. Full deep-dive on RAG is a topic for its own file — this is just the map of the four moving parts.

---

### Agents — The Driver

Everything above is a car that only goes where you point it. An **Agent** is the driver — it uses the LLM to *decide* which tool to use, when to use it, and when to stop, in a loop (this pattern is called **ReAct**: Reason + Act).

```python
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_anthropic import ChatAnthropic
from langchain_core.tools import tool
from langchain_core.prompts import ChatPromptTemplate

@tool
def get_weather(city: str) -> str:
    """Returns the current weather for a given city."""
    return f"It's 22°C and sunny in {city}."

@tool
def multiply(a: int, b: int) -> int:
    """Multiplies two numbers."""
    return a * b

llm = ChatAnthropic(model="claude-3-5-sonnet-20241022")
tools = [get_weather, multiply]

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant with access to tools."),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}"),
])

agent = create_tool_calling_agent(llm, tools, prompt)
executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

result = executor.invoke({"input": "What's the weather in Lahore, and what's 12 times 8?"})
print(result["output"])
```

The model itself decides: "I need `get_weather` for the first part, and `multiply` for the second" — you never hardcoded that logic. This is the shift from *calling* an LLM to *delegating* to one.

---

## 3. Why Use LangChain At All?

You *can* build all of this yourself with raw API calls — dictionaries for memory, string formatting for prompts, if/else trees for tool routing. People do. But for production apps, LangChain earns its place because:

| Concern | Raw API Calls | LangChain |
|---|---|---|
| Switching providers | Rewrite core logic | Change one line |
| Prompt reuse | Copy-pasted f-strings | Versioned, validated templates |
| Multi-step logic | Manual glue code | LCEL pipes (`|`) |
| Conversation history | Manual list management | Built-in memory classes |
| Connecting to your data | Custom vector DB wiring | Standardized loaders/retrievers |
| Tool-using agents | Custom parsing of model output | Built-in agent executors |

The abstraction cost is small (one extra dependency, a slightly different mental model). The abstraction *payoff* is that your business logic stops being tangled with any single vendor's API shape.

---

## 4. Best Practices — 3 Golden Rules

1. **Don't chain what doesn't need chaining.** If your task is "one prompt in, one answer out," a raw `llm.invoke()` call is simpler, faster to debug, and has fewer moving parts than wrapping it in a Chain. Reach for Chains/LCEL when you have *multiple* sequential steps (retrieve → summarize → format, for example).

2. **Prefer LCEL over legacy classes.** `LLMChain`, `ConversationChain`, and similar `Chain` subclasses are legacy. New LangChain code should be built with the `|` pipe syntax and `Runnable` interfaces — they're more debuggable (you can inspect each step) and more composable.

3. **Agents are powerful but unpredictable — cage them.** An agent decides its own execution path, which means it can loop, pick the wrong tool, or burn tokens retrying. Always set `max_iterations`, give tools narrow and well-described purposes, and log every tool call in development before trusting an agent in production.

---

## One Fire Rule

> **LangChain doesn't make your model smarter — it makes your model swappable.** If you're not switching providers, chaining multiple steps, managing memory, retrieving external data, or letting the model choose actions, you don't need LangChain — you need a for-loop and an API call.