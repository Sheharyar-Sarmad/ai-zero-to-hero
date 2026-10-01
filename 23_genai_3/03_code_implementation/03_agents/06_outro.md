# Outro: Where We Are and What Comes Next

Congratulations on finishing the agents module. This is a good place to stop and look at what you can now do.

## What we covered

- Tools: turning plain Python functions into tools an LLM can call with `@tool`.
- Hard coded agents: building the tool calling loop by hand, so you understand what happens underneath.
- `create_agent`: letting LangChain run that loop for you (`04_autonomous_agent.py`).
- Middleware: adding human approval before a tool runs, and why it must be registered with the agent.
- Runnables: chaining steps together with the pipe operator, so input, agent and output parsing stay clean.
- A Streamlit UI: wrapping the agent in a real interface with chat history, tool call details and approve or reject buttons (`05_autonomous_agent_ui.py`).
- Memory with a checkpointer, so the agent remembers the conversation.

## What we did not cover: LangGraph

We built our agents with LangChain, and that is the right place to start. For simple agents it is fast and enough.

LangGraph is what the industry prefers when a workflow gets complex. It gives you full control over how an agent thinks and moves between steps.

- State: one shared object that every step can read and update.
- Nodes and edges: each step is a node, and edges decide what runs next.
- Conditional routing: branch, loop, or retry based on what the agent finds.
- Persistence: save progress, pause, and resume long running workflows.
- Human in the loop: stop at any node and wait for a person.
- Multi agent systems: several specialised agents working together under one graph.

You have already used it without knowing. `create_agent` returns a LangGraph graph, and the pause and resume approval flow in our UI is a LangGraph feature. Learning LangGraph means opening the box you have been using.

## What comes next

Now we move from learning to building. One or two projects are coming, and they are the most important part of this course.

- Each project will be built end to end, not as a small demo.
- They will use the ideas from this module: tools, agents, memory and human approval.
- They are designed so you can put them on your resume and talk about them in interviews.

Employers do not hire you for the tutorials you watched. They hire you for what you built and can explain. A few strong projects, with clean code and a working demo, will do more for your career than any certificate.

## Before the projects

- Re-run every file in this folder and change something each time.
- Add a third tool to the city agent, such as currency rates or a travel tip.
- Break the code on purpose, read the error, and fix it.
- Push your work to GitHub with a clear README.

## Key takeaway

- LangChain gets you a working agent quickly.
- LangGraph gives you control when the workflow becomes complicated.
- Projects turn both of them into proof that you can build.

See you in the projects. Build something you are proud of.