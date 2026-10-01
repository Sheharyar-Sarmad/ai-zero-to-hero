# Loading environment variables (API keys for Groq, OpenWeather, Tavily)
from dotenv import load_dotenv
load_dotenv()

import os 
import requests
from typing import Any
from functools import lru_cache
from rich import print

# LangChain core imports for tools, messages, and model bindings
from langchain_groq import ChatGroq
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, ToolMessage, BaseMessage
from langchain_core.language_models import LanguageModelInput
from langchain_core.runnables import Runnable
from tavily import TavilyClient

# Define Weather Tool using OpenWeather API
@tool
@lru_cache
def get_weather(city: str) -> str:
    """Get the current weather conditions for a specified city."""
    raw_key = os.getenv("OPENWEATHER_API_KEY", "")
    api_key: str = raw_key.strip().strip("'\"")  # Strip spaces and accidental surrounding quotes
    clean_city: str = city.strip()

    if not api_key:
        return "Error: OpenWeather API key is not configured in environment."

    # Use https and stripped parameters
    url: str = f"https://api.openweathermap.org/data/2.5/weather?q={clean_city}&appid={api_key}&units=metric"

    try:
        response: requests.Response = requests.get(url, timeout=10)
        data: dict[str, Any] = response.json()

        if str(data.get("cod")) != "200":
            return f"Error: {data.get('message', 'Could not fetch weather data.')}"

        temp: float = data["main"]["temp"]
        humidity: int = data["main"]["humidity"]
        desc: str = data["weather"][0]["description"]
        return f"Weather in {clean_city}: {desc.capitalize()}, {temp}°C, Humidity: {humidity}%"

    except Exception as e:
        # Mask the error string to prevent API key leaks in the UI
        return f"Error fetching weather: Unable to connect to OpenWeather service."
    
# Initialize Tavily search client for news retrieval
tavily_client: TavilyClient = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

# Define News Search Tool using Tavily API
@tool
@lru_cache
def get_news(city: str) -> str:
    """Get Latest news about the city!"""

    response: dict[str, Any] = tavily_client.search(
        query=f"latest news in {city}",
        search_depth="basic",
        max_results=3
    )
    
    results: list[dict[str, Any]] = response.get("results", [])

    if not results:
        return f"No news found for {city}"
    
    news_list: list[str] = []
    
    for r in results:
        title: str = r.get("title", "No title")
        url: str = r.get("url", "")
        snippets: str = r.get("content", "")
        news_list.append(
            f"- {title}\n  {url}\n {snippets[:100]}..."
        )

    return f"Latest news in {city}:\n\n" + "\n\n".join(news_list)


# Initialize the LLM via ChatGroq
llm: ChatGroq = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.5,
    max_tokens=700
)

# Store tools in a lookup dictionary mapping tool name string -> tool instance
tools: dict[str, Any] = {
    "get_weather": get_weather,
    "get_news": get_news
}

# Bind tools to the LLM so it receives their JSON schemas
llm_with_tools: Runnable[LanguageModelInput, BaseMessage] = llm.bind_tools(
    [get_weather, get_news]
)

# Main Agent Conversation Loop
def main():
    messages: list[BaseMessage] = []

    print("\nCity Intelligence System")
    print("Type 'exit' to quit!\n")

    while True:
        user_input: str = input("\nYou: ")

        if user_input.lower() == "exit":
            print("\nThank you for using our city intelligence system. Quitting now!\n")
            break

        messages.append(HumanMessage(user_input))

        while True:
            result: BaseMessage = llm_with_tools.invoke(messages)
            messages.append(result)

            if result.tool_calls:
                for tool_call in result.tool_calls:
                    tool_name: str = tool_call["name"]
                    tool_args: dict[str, Any] = tool_call["args"]

                    confirm: str = input(
                        f"\nDo you want to call the tool '{tool_name}' with args {tool_args}? (yes/no): "
                    ).strip().lower()

                    if confirm == "yes":
                        tool_result: str = str(tools[tool_name].invoke(tool_args))
                        messages.append(ToolMessage(content=tool_result, tool_call_id=tool_call["id"]))
                    else:
                        print(f"'{tool_name}' tool execution declined by user.")
                        messages.append(ToolMessage(
                            content=f"Tool '{tool_name}' execution was declined by user.",
                            tool_call_id=tool_call["id"]
                        ))
            else:
                print(f"\nAI: {result.content}")
                break


if __name__ == "__main__":
    main()

    
# While hard-coding the agent loop is great for understanding the underlying mechanics, 
# maintaining and scaling this logic in production becomes extremely difficult. 
# A single edge case or flaw in loop management can easily break the entire workflow. 

# In real-world development, we rely on higher-level abstractions like the ReAct framework 
# and functions like create_react_agent / create_agent to handle reasoning, state, and 
# tool calls dynamically, safely, and at scale.