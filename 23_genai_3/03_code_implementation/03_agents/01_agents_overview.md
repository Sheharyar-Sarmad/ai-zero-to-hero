# 03_agents: City Intelligence Project

## Prerequisites
Before diving into this section, I am assuming that you come here after completing the `23_genai_3/02_agent_architecture` section of the [ai-zero-to-hero](https://github.com/Sheharyar-Sarmad/ai-zero-to-hero) repository. Understanding the underlying architecture is crucial before we start building.

**Note:** This is the most important phase of the `23_genai-3` module! Pay close attention, as we will be putting theory into active practice.

## What We Will Build
In this `03_agents` section, we will be creating a comprehensive **City Intelligence Project**. This project will allow our AI to act as a smart assistant, gathering real-time data about specific cities.

To demonstrate different approaches to building AI agents, we will create two distinct agents:
1. **Hardcoded Agent:** We will build the agentic loop and decision-making logic manually from scratch to understand the mechanics under the hood.
2. **ReAct Library Agent:** We will build a second agent utilizing the ReAct (Reasoning and Acting) framework/library to see how abstractions can streamline the development of complex agents.

## Tools and APIs
To empower our agents with real-world knowledge, we will integrate the following tools:
*   **OpenWeatherMap API:** Used by the agents to fetch real-time weather data and forecasts for the target cities.
*   **Tavily API:** Used as a search tool to browse the web for the latest news, events, and localized information.