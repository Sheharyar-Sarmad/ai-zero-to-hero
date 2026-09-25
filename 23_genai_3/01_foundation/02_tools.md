# 🛠️ Tools in AI Agents: A Beginner's Guide

An **AI Agent** without tools is like a smart person locked in a room without a phone or internet—they can think and speak, but they can't check today's weather or turn on the lights.

**Tools** are the "apps" or "hands" you give to an LLM so it can take real actions in the real world.

---

## 💡 The Core Idea: How Tools Work

1. **You ask a question**: *"What is the weather in Paris?"*
2. **LLM looks at its Tools**: It sees a tool named `get_weather`.
3. **LLM generates a Tool Request**: It doesn't answer directly. Instead, it says: *"Please run `get_weather(city='Paris')`"*.
4. **Your Python Code Runs the Tool**: Python calls the Weather API and gets `"18°C and Sunny"`.
5. **LLM gives the Final Answer**: *"The current weather in Paris is 18°C and sunny."*

---

## 1. Creating Your First Tool (Simple Example)

The easiest way to make a tool in LangChain is using the `@tool` decorator. 

> ⚠️ **Important:** The docstring (the text inside `""" ... """`) is **what the LLM reads** to decide whether to use the tool!

```python
from langchain_core.tools import tool

@tool
def add_numbers(a: int, b: int) -> int:
    """Adds two integers together. Use this when you need basic addition."""
    return a + b

@tool
def count_letters(text: str) -> int:
    """Counts the total number of characters in a given string."""
    return len(text)