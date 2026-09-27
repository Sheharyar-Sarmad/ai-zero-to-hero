# Tool Calling

## 1. What Is a Tool?

A **tool** is simply a function that an agent can use to do something the language model itself cannot do on its own — fetch live data, run a calculation, query a database, or call an external service.

Think of tools as the "hands" of the agent. The LLM is the "brain" that decides *what* needs to be done, and tools are *how* it gets done in the real world.

Common examples:

- **Weather tool** — fetches current weather for a city
- **Calculator tool** — performs precise math
- **Search tool** — looks up current information on the web
- **Database tool** — reads or writes records in a database

Each tool does one narrow job well, and the agent picks the right one when it's needed.

## 2. Why Do Agents Need Tools?

An LLM is trained on a fixed dataset up to a certain point in time, and it generates text by predicting likely words — it does not have a live connection to the world or a built-in calculator. This means an LLM, by itself, cannot reliably:

- Tell you today's **weather** (it has no live data feed)
- Report **current news** or events after its training cutoff
- Look up a record in **your database**
- Do precise **calculations** (it may "guess" at arithmetic instead of computing it)
- Call **external APIs** (payment systems, email services, calendars, etc.)

Tools close this gap. They give the LLM a way to reach outside its own text-generation process and get real, current, or precise information.

## 3. Important Concept

This is the single most important idea in this document, so read it carefully:

> **The LLM does NOT directly execute the Python function.**

The LLM cannot run code. It cannot reach into your codebase and call `get_weather()`. All it can do is generate text. So when an agent "uses a tool," what actually happens is a structured hand-off between the LLM and your application code.

The flow looks like this:

```
LLM
 ↓
Tool call request   (LLM outputs structured text: "call this tool with these arguments")
 ↓
Application          (your code reads that request)
 ↓
Tool execution       (your code actually runs the Python function)
 ↓
Tool result          (your code captures the output)
 ↓
LLM                   (the result is sent back into the conversation)
```

The LLM only ever *asks* for a tool to be run. It never runs anything itself. Your application is the one that trusts (or doesn't trust) that request, executes the real function, and reports back what happened. This separation is what keeps agents safe and predictable — the LLM proposes, the application decides and executes.

## 4. Anatomy of a Tool

Every tool, regardless of framework, is made up of the same core pieces:

- **name** — a short identifier the LLM uses to refer to the tool (e.g. `get_weather`)
- **description** — a plain-English explanation of what the tool does, so the LLM knows *when* to use it
- **input schema** — the structure of the arguments the tool expects (names, types)
- **function** — the actual Python code that runs when the tool is called
- **output** — the result returned after execution, which gets passed back to the LLM

A simple example:

```python
def get_weather(city: str) -> str:
    """Returns the current weather for a given city."""
    # In a real tool, this would call a weather API
    return f"It's 25°C and sunny in {city}."

tool_definition = {
    "name": "get_weather",
    "description": "Get the current weather for a given city.",
    "input_schema": {
        "type": "object",
        "properties": {
            "city": {"type": "string", "description": "Name of the city"}
        },
        "required": ["city"]
    },
    "function": get_weather
}
```

Notice that the `name`, `description`, and `input_schema` are what the LLM sees. The `function` is what your application runs. The LLM never sees the Python code itself.

## 5. Tool Schema

LLMs communicate using text, not typed function calls — so we need a way to make sure the LLM provides arguments in a predictable, structured format. This is what a **schema** does.

Instead of hoping the LLM writes something like:

> "the weather in Lahore please"

...a schema tells the LLM exactly what shape of input is expected:

```
weather(city: str)
```

This means: "call the `weather` tool with one argument, `city`, which must be a string."

If the agent needs to check the weather in Lahore, it doesn't generate free-form text — it generates a structured request like:

```json
{
  "tool": "weather",
  "arguments": { "city": "Lahore" }
}
```

Your application can then parse this reliably, because it knows exactly what fields to expect. Without a schema, you'd have to guess how to extract "Lahore" from arbitrary sentences — schemas remove that ambiguity.

## 6. Tool Calling Flow

Here's a more detailed view of the full round-trip:

```
┌─────────────┐
│    User     │  "What is the weather in Lahore?"
└──────┬──────┘
       ↓
┌─────────────┐
│     LLM     │  Decides a tool is needed
└──────┬──────┘
       ↓
┌─────────────────────┐
│ Tool call request    │  { "tool": "weather", "arguments": {"city": "Lahore"} }
└──────┬───────────────┘
       ↓
┌─────────────┐
│ Application │  Reads the request, validates it
└──────┬──────┘
       ↓
┌─────────────────┐
│ Tool execution   │  weather(city="Lahore") is actually run
└──────┬───────────┘
       ↓
┌─────────────┐
│ Tool result  │  "18°C, partly cloudy"
└──────┬──────┘
       ↓
┌─────────────┐
│     LLM     │  Reads the result, forms a natural-language answer
└──────┬──────┘
       ↓
┌─────────────┐
│    User     │  "It's currently 18°C and partly cloudy in Lahore."
└─────────────┘
```

Note that the LLM appears **twice**: once to *request* the tool, and once again *after* execution to turn the raw result into a natural answer.

## 7. Example

Let's trace one concrete request end-to-end.

**User:** "What is the weather in Lahore?"

```
User
 ↓  "What is the weather in Lahore?"
LLM
 ↓  Decides: I need the weather tool
Tool selection
 ↓  Tool = "weather"
Arguments
 ↓  { "city": "Lahore" }
weather(city="Lahore")
 ↓  Application calls the real function
API
 ↓  Function calls an external weather API
Result
 ↓  "18°C, partly cloudy"
LLM
 ↓  Turns the raw result into natural language
Answer
    "It's currently 18°C and partly cloudy in Lahore."
```

At every arrow, control passes between the LLM and the application — the LLM never skips a step to talk to the API directly.

## 8. Multiple Tools

Real agents usually have more than one tool available, for example:

- `weather` — for weather questions
- `calculator` — for math questions
- `search` — for general knowledge or current events

When multiple tools are registered, the LLM is shown all of their names, descriptions, and schemas at once. Based on the user's message, it decides **which one (if any) fits best**.

For example:
- "What's 245 * 12?" → the LLM picks `calculator`
- "What's the weather in Karachi?" → the LLM picks `weather`
- "Who won the last election in France?" → the LLM picks `search`

If no tool is relevant, the LLM simply answers directly without calling anything. Choosing the right tool is a judgment call made by the LLM based on the descriptions you provide — which is why writing clear, distinct tool descriptions matters a lot.

## 9. Tool Errors

Tool execution happens in the real world, so things can and do go wrong. Common failure cases include:

- **Invalid arguments** — the LLM provides a city name that doesn't exist, or forgets a required field
- **API failure** — the external service the tool depends on is down or returns an error
- **Timeout** — the tool takes too long to respond
- **Missing API key** — the tool needs credentials that haven't been configured
- **Invalid response** — the tool returns data in a format the application doesn't expect

A well-built agent application catches these errors and reports them back to the LLM as a structured result (e.g. `"error": "City not found"`), rather than crashing. This lets the LLM decide how to recover — for example, asking the user to clarify, or trying a different approach.

## 10. Security

Because tools let an LLM trigger real actions — reading databases, calling paid APIs, sending emails — they must be carefully controlled by the application, not left entirely up to the LLM's judgment.

Some basic precautions:
- Validate all arguments before executing a tool (never trust LLM output blindly)
- Limit what each tool is allowed to do (least privilege)
- Avoid exposing tools that can perform destructive or irreversible actions without confirmation
- Log tool calls so unexpected behavior can be reviewed

Remember: the LLM only *requests* a tool call — your application always has the final say on whether to actually execute it.

## 11. Simple Python Example

Here's a minimal example with no framework at all, just to show the core mechanism:

```python
import json

# Step 1: Define the actual function
def calculator(expression: str) -> str:
    try:
        result = eval(expression, {"__builtins__": {}})
        return str(result)
    except Exception as e:
        return f"Error: {e}"

# Step 2: Pretend this is what the LLM generated as a "tool call request"
llm_output = json.dumps({
    "tool": "calculator",
    "arguments": {"expression": "12 * 8"}
})

# Step 3: The application parses the request
request = json.loads(llm_output)

# Step 4: The application executes the real function
if request["tool"] == "calculator":
    result = calculator(**request["arguments"])

# Step 5: The result would now be sent back to the LLM
print(result)  # "96"
```

This is the entire mechanism, stripped down. Frameworks like LangChain don't change this flow — they just provide convenient abstractions on top of it: automatically generating schemas from Python type hints, automatically parsing the LLM's tool call output, and automatically routing execution to the right function. Once you understand the raw flow above, framework code becomes much easier to read, because you can always mentally map it back to these same five steps.

## 12. Key Takeaways

- A tool is just a function with a name, description, and input schema attached, so the LLM knows it exists and how to use it.
- The LLM never executes code directly — it only requests a tool call; your application performs the actual execution.
- Structured input schemas (like `weather(city: str)`) remove ambiguity and let your code reliably parse what the LLM wants.
- The full loop is: **LLM → tool call request → application → tool execution → tool result → LLM**.
- With multiple tools, the LLM chooses the best fit based on tool descriptions.
- Tool execution can fail — handle errors gracefully and report them back to the LLM.
- Tools can trigger real-world actions, so applications must validate and control what they're allowed to do.
- Frameworks like LangChain only add convenience around this same underlying mechanism — they don't replace it.