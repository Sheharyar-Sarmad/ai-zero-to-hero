# 🔄 Workflows in Agentic AI

In this course, we will focus heavily on **workflows**. But what exactly is a workflow in the context of Agentic AI, and why does it matter?

## 🧩 What is an Agentic Workflow?

A workflow is the **orchestrated sequence of steps** an AI agent takes to achieve a specific goal. 

In traditional software, workflows are rigid and deterministic (e.g., Step A → Step B → Step C). In Agentic AI, workflows are **dynamic**. They combine the reasoning power of LLMs with deterministic code and external tools. This allows the agent to make decisions, loop back, fetch data, and adapt its path based on the current state of the task.

## 🕸️ Workflows in LangGraph

LangGraph models agentic workflows as **State Machines** (or Graphs). Instead of writing a long, messy script with nested `if/else` statements, you define your workflow visually and structurally.

In LangGraph, a workflow consists of:
- **State**: A shared memory that holds the data being passed around (e.g., messages, documents, user info).
- **Nodes**: Python functions or LLM calls that perform work and update the state.
- **Edges**: The connections that tell the graph which node to go to next.
- **Conditional Edges**: Logic that routes the workflow based on the current state (e.g., "If the AI needs more info, go back to the search node").

This graph-based approach gives you **complete control, durability, and visibility** over how your agent thinks and acts.

## 🎯 The 5 Core Workflows We Will Master

Throughout this course, we will build, analyze, and master the 5 foundational workflow types that power every modern AI agent:

### 1. ➡️ Sequential Workflow
**What it is**: A linear, step-by-step execution where the output of one node becomes the input for the next. 
**Example**: A content pipeline where the agent first researches, then writes a draft, then edits it.

### 2. ⚡ Parallel Workflow
**What it is**: Fan-out and fan-in execution. The workflow splits into multiple branches to handle tasks simultaneously, then merges the results back together using **reducers**.
**Example**: A multi-source research agent that queries three different APIs at the same time to save time.

### 3. 🚦 Conditional Workflow
**What it is**: Branching logic. The workflow evaluates the current state and decides which path to take next.
**Example**: A college RAG chatbot that checks if the user's question is about admissions or courses, and routes the query to the correct PDF database.

### 4. 🔄 Iterative Workflow
**What it is**: Self-reviewing loops. The agent generates an output, evaluates it against a set of criteria, and loops back to improve it until the criteria are met.
**Example**: A LinkedIn post generator that writes a post, critiques it, and rewrites it until it passes a quality check.

### 5. 👤 Human-in-the-Loop (HITL) Workflow
**What it is**: Pausing the workflow for human intervention. The agent stops, saves its state, and waits for a human to approve, edit, or reject an action before continuing.
**Example**: A LinkedIn generator that pauses and asks for human approval before publishing the final post.

## 🚀 Course Focus

Our goal is to move beyond basic prompt engineering and simple `create_agent` loops. By mastering these 5 workflow types in LangGraph, you will gain the skills to engineer production-ready, reliable, and scalable agentic systems.