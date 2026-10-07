# Architectural Overview: Subgraphs in LangGraph

## 1. Core Concept
Subgraphs allow nesting a fully compiled `StateGraph` inside a parent graph as a modular node. This encapsulates logic, prevents state namespace pollution, and enables independent testing.

## 2. Integration Patterns
* **Direct Node Addition:** Used when parent and subgraph share identical state keys (data flows automatically through shared channels).
* **Wrapper Function Node:** Used when schemas differ; maps parent keys to subgraph inputs and translates outputs back.