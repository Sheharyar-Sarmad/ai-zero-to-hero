# Project: Conditional Workflow & RAG Integration

## Overview
A multi-path conditional chatbot designed for a college environment supporting three academic branches: **BCA**, **BBA**, and **B COM**[cite: 5]. 

## Conditional Paths & Architecture
1. **Academic RAG Path:** Retrieves answers using the institutional academic PDF[cite: 5].
2. **Fee RAG Path:** Retrieves fee structures and payment policies using the fee PDF[cite: 5].
3. **General Knowledge Path:** Handles standard queries using the LLM's base knowledge[cite: 5].

## Workflow Lifecycle
* **Input State:** User selects a branch and submits a query.
* **Conditional Routing:** Evaluates user intent to direct flow to Academic RAG, Fee RAG, or General LLM.
* **Convergence Node:** All independent execution paths merge back into a single centralized node to deliver the final response[cite: 5].