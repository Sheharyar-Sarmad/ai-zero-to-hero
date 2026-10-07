import os 
from typing import TypedDict, Annotated, Literal, Any
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.runnables import Runnable
from langchain_core.messages import BaseMessage, AIMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.types import interrupt, Command

load_dotenv()

search_tool = TavilySearchResults(max_results=3)
tools: list[Any] = [search_tool]

writer_llm: ChatGroq = ChatGroq(
    model="openai/gpt-oss-120b",
    max_tokens=2048,
    temperature=0.8
)

writer_llm_with_tools: Runnable = writer_llm.bind_tools(tools)

reviewer_llm: ChatGroq = ChatGroq(
    model="openai/gpt-oss-20b",
    max_tokens=1024,
    temperature=0.3
)

class State(TypedDict):
    topic: str 
    messages: Annotated[list[BaseMessage], add_messages]
    draft: str 
    content_feedback: str
    compliance_feedback: str
    review_feedback: str 
    content_approved: bool
    compliance_approved: bool
    is_approved: bool 
    attempts: int 

WRITER_SYSTEM_PROMPT: str = (
    "You are an expert LinkedIn content writer. Your job is to write "
    "engaging, professional LinkedIn posts about the given topic. "
    "If the topic requires up-to-date information, statistics, or "
    "current trends, use the web search tool to gather fresh context "
    "before writing. If you have already received feedback on a "
    "previous draft, carefully address every point in the new draft. "
    "Rules for good LinkedIn posts: strong hook in the first line, "
    "1 clear takeaway, easy to skim (short paragraphs), around "
    "150–200 words, ends with a question or call-to-action to invite "
    "engagement. Do not use hashtags."
)

def writer_node(state: State) -> dict: 
    try:
        attempts: int = state.get("attempts", 0) + 1
        topic: str = state.get("topic", "")
        previous_feedback: str = state.get("review_feedback", "")

        if attempts == 1: 
            user_message: str = (
                f"Write a Linkedin post on this topic: {topic}. "
                f"If you need current info search the web first!"
            )
        else: 
            user_message = (
                f"Your previous draft on '{topic}' was rejected.\n"
                f"Here is the reviewer's feedback:\n{previous_feedback}\n\n"
                f"Write a new, improved draft that fixes every issue mentioned. "
                f"Do not repeat the same mistake."
            )

        messages = [
            ("system", WRITER_SYSTEM_PROMPT),
            ("human", user_message)
        ]

        response: AIMessage = writer_llm_with_tools.invoke(messages)

        return {
            "messages": [response],
            "attempts": attempts
        }

    except Exception as err:
        raise Exception(f"Error coming in writer node due to: {err}")

tool_node: ToolNode = ToolNode(tools)

def extract_draft_node(state: State) -> dict:
    try:
        last_message: BaseMessage = state['messages'][-1]
        draft: str = getattr(last_message, 'content', '')
        return {"draft": draft}
    except Exception as err:
        raise Exception(f"Error coming in extracting draft node due to: {err}")

REVIEWER_SYSTEM_PROMPT = (
    "You are a strict LinkedIn content reviewer. You judge whether a "
    "post is publish-ready. Evaluate against these criteria:\n"
    "1. Strong hook in the first line\n"
    "2. One clear, valuable takeaway\n"
    "3. Easy to skim — uses short paragraphs\n"
    "4. Roughly 150-200 words\n"
    "5. Ends with an engaging question or CTA\n"
    "6. Professional but human tone (not corporate-robotic)\n"
    "7. No hashtags\n\n"
    "Respond in exactly this format:\n"
    "VERDICT: APPROVED or REJECTED\n"
    "FEEDBACK: <one short paragraph explaining why>\n\n"
    "Be strict but fair. Approve only if the post genuinely meets all "
    "criteria. Reject if even one criterion is clearly missing."
)

def content_reviewer_node(state: State) -> dict:
    try: 
        draft: str = state.get('draft', '')
        prompt: str = f"Review this LinkedIn post draft:\n{draft}\nGive your reviews."

        response: AIMessage = reviewer_llm.invoke(
            [("system", REVIEWER_SYSTEM_PROMPT), ("human", prompt)]
        )

        review_text: str = response.content.strip()
        is_approved: bool = "APPROVED" in review_text.upper().split("FEEDBACK")[0]
        
        if "FEEDBACK:" in review_text:
            feedback = review_text.split("FEEDBACK:", 1)[1].strip()
        else:
            feedback = review_text
        
        return {
            "content_feedback": f"Content Review: {feedback}",
            "content_approved": is_approved,
        }
    except Exception as err: 
        raise Exception(f"Error coming in content reviewer node due to: {err}")

COMPLIANCE_SYSTEM_PROMPT = (
    "You are a strict compliance checker. Check if post contains no hashtags "
    "and adheres to standard formatting constraints.\n"
    "Respond strictly in format:\nVERDICT: APPROVED or REJECTED\nFEEDBACK: <reason>"
)

def compliance_reviewer_node(state: State) -> dict:
    try:
        draft: str = state.get('draft', '')
        response: AIMessage = reviewer_llm.invoke(
            [("system", COMPLIANCE_SYSTEM_PROMPT), ("human", f"Check format:\n{draft}")]
        )

        review_text: str = response.content.strip()
        is_approved: bool = "APPROVED" in review_text.upper().split("FEEDBACK")[0]
        
        if "FEEDBACK:" in review_text:
            feedback = review_text.split("FEEDBACK:", 1)[1].strip()
        else:
            feedback = review_text

        return {
            "compliance_feedback": f"Compliance Review: {feedback}",
            "compliance_approved": is_approved,
        }
    except Exception as err:
        raise Exception(f"Error coming in compliance reviewer node due to: {err}")

def aggregate_reviews_node(state: State) -> dict:
    try:
        c_app: bool = state.get("content_approved", False)
        m_app: bool = state.get("compliance_approved", False)
        
        c_fb: str = state.get("content_feedback", "")
        m_fb: str = state.get("compliance_feedback", "")

        automated_approved: bool = c_app and m_app
        combined_feedback: str = f"{c_fb}\n{m_fb}"

        return {
            "is_approved": automated_approved,
            "review_feedback": combined_feedback
        }
    except Exception as err:
        raise Exception(f"Error coming in aggregate reviews node due to: {err}")

# Human-in-the-Loop Node using the LangGraph interrupt primitive
def human_review_node(state: State) -> dict:
    draft: str = state.get("draft", "")
    feedback: str = state.get("review_feedback", "")
    
    # Pauses graph execution and surfaces payload to the CLI user interface
    human_input = interrupt({
        "draft": draft,
        "feedback": feedback,
        "message": "Review the draft and feedback above. Type 'approve' to accept or provide revision notes:"
    })
    
    if isinstance(human_input, str) and human_input.lower().strip() in ["approve", "yes", "y"]:
        return {"is_approved": True}
    else:
        return {
            "is_approved": False,
            "review_feedback": f"Human Override Feedback: {human_input}"
        }

def should_use_tool(state: State) -> str: 
    last_message: BaseMessage = state['messages'][-1]
    tool_calls_count = sum(1 for msg in state.get('messages', []) if getattr(msg, 'tool_calls', None))
    if getattr(last_message, 'tool_calls', None) and tool_calls_count < 2: 
        return "tools"
    return "extract_draft"

def should_stop_looping(state: State) -> Literal["writer", "__end__"]: 
    if state.get('is_approved', False): 
        return END

    if state.get('attempts', 0) >= 3: 
        return END

    return "writer"

workflow = StateGraph(State)

workflow.add_node("writer", writer_node)
workflow.add_node("tools", tool_node)
workflow.add_node("extract_draft", extract_draft_node)
workflow.add_node("content_reviewer", content_reviewer_node)
workflow.add_node("compliance_reviewer", compliance_reviewer_node)
workflow.add_node("aggregate_reviews", aggregate_reviews_node)
workflow.add_node("human_review", human_review_node)

workflow.add_edge(START, "writer")

workflow.add_conditional_edges(
    "writer",
    should_use_tool,
    {
        "tools": "tools",
        "extract_draft": "extract_draft"
    }
)
workflow.add_edge("tools", "writer")

workflow.add_edge("extract_draft", "content_reviewer")
workflow.add_edge("extract_draft", "compliance_reviewer")

workflow.add_edge("content_reviewer", "aggregate_reviews")
workflow.add_edge("compliance_reviewer", "aggregate_reviews")

workflow.add_edge("aggregate_reviews", "human_review")

workflow.add_conditional_edges(
    "human_review",
    should_stop_looping,
    {
        "writer": "writer",
        END: END
    }
)

checkpointer = MemorySaver()
app = workflow.compile(checkpointer=checkpointer)

if __name__ == "__main__":
    print("LinkedIn Agentic Engine with HITL Initialized")
    config = {"configurable": {"thread_id": "cli_session_hitl_1"}}

    while True:
        topic_input = input("\nEnter post topic (or type 'exit' to stop): ").strip()
        if topic_input.lower() in ["exit", "quit"]:
            print("Exiting application.")
            break

        if not topic_input:
            continue

        initial_state = {
            "topic": topic_input,
            "messages": [],
            "draft": "",
            "content_feedback": "",
            "compliance_feedback": "",
            "review_feedback": "",
            "content_approved": False,
            "compliance_approved": False,
            "is_approved": False,
            "attempts": 0
        }

        print(f"Executing workflow for topic: '{topic_input}'")

        current_input: Any = initial_state
        while True:
            has_interrupted = False
            for output in app.stream(current_input, config=config):
                if "__interrupt__" in output:
                    has_interrupted = True
                    interrupt_payload = output["__interrupt__"][0].value
                    print("\n--- HUMAN REVIEW REQUIRED ---")
                    print(f"Draft:\n{interrupt_payload.get('draft')}")
                    print(f"Feedback:\n{interrupt_payload.get('feedback')}")
                    
                    user_decision = input("\nType 'approve' to publish, or type revision instructions: ").strip()
                    current_input = Command(resume=user_decision)
                    break
                else:
                    for node_name in output.keys():
                        print(f"Executed node: {node_name}")
            
            if not has_interrupted:
                break

        final_state = app.get_state(config)
        final_draft = final_state.values.get("draft", "No draft generated.")

        print("\nFinal LinkedIn Post Draft:")
        print("--------------------------")
        print(final_draft)
        print("--------------------------")