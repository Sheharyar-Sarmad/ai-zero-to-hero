# Project: Iterative Workflow & Multi-Agent Refinement

## Overview
An advanced LangGraph state machine featuring cyclical feedback loops, tool integration, and multi-agent coordination for quality-refined content generation[cite: 2].

## Conditional Paths & Architecture
1. **Writer ↔ Tools Loop:** Executes autonomous ReAct-style tool usage with Tavily web search, where the LLM dynamically decides when to query[cite: 2].
2. **Writer → Reviewer Loop:** Employs a dedicated reviewer agent to assess outputs and trigger iterative revisions[cite: 2].
3. **Multi-LLM Setup:** Separates workloads using different LLMs configured with tailored temperatures for creative generation versus analytical judgment[cite: 2].

## Workflow Lifecycle
* **Input State:** Initializes query processing with graph configuration and `recursion_limit` settings[cite: 2].
* **Iterative Execution:** Dynamically routes through backward edges and nested loops for content generation, tool lookup, and critique[cite: 2].
* **Convergence & Stop Conditions:** Terminates execution when approval conditions are met or maximum attempt limits are reached[cite: 2].
