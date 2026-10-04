# Its created by claude i didnt right anything i just copy and paste the 03_project.py
# file to claude and say create the ui for this CLI base code in to streamlit UI.
# You should also use ai for this kind of workflows


import uuid
from typing import TypedDict

import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import END, START, StateGraph

load_dotenv()

st.set_page_config(page_title="Hinglish Script Studio", page_icon="🎬", layout="centered")


# ---------------------------------------------------------------- State
class PipelineState(TypedDict):
    raw_input: str
    edited_text: str
    script_text: str
    final_output: str


# ---------------------------------------------------------------- Graph
@st.cache_resource(show_spinner=False)
def build_graph(model: str, temperature: float, max_tokens: int):
    """Build the graph once per settings combo (cached across reruns)."""
    llm = ChatGroq(model=model, max_tokens=max_tokens, temperature=temperature)

    def editor_node(state: PipelineState) -> dict[str, str]:
        prompt = (
            "You are an expert copyeditor. Clean up the following raw text. "
            "Fix any grammatical errors, spelling mistakes, and smooth out the transitions "
            "while keeping the core message intact. Return only the edited text.\n\n"
            f"Text:\n{state['raw_input']}"
        )
        return {"edited_text": llm.invoke(prompt).content.strip()}

    def scriptwriter_node(state: PipelineState) -> dict[str, str]:
        prompt = (
            "You are a charismatic YouTube content creator. Take this edited text and transform "
            "it into a highly engaging, punchy, conversational video script hook. Make it sound "
            "like a real person speaking passionately. Return only the script content.\n\n"
            f"Edited Text:\n{state['edited_text']}"
        )
        return {"script_text": llm.invoke(prompt).content.strip()}

    def translator_node(state: PipelineState) -> dict[str, str]:
        prompt = (
            "You are an expert content localizer for a young, tech-savvy audience. Take the following script "
            "and convert it into natural, conversational 'Roman Hinglish' (written strictly in English/Latin alphabets, "
            "exactly like how people text and chat on WhatsApp, e.g., 'Bhai yeh code dekho, mast chal raha hai'). "
            "Do NOT use Devanagari script; use Roman letters only. Blend Hindi and English seamlessly just like "
            "a modern tech YouTuber or developer explaining things on a live stream. Keep the energy high! "
            "Return only the final Roman Hinglish text.\n\n"
            f"Script:\n{state['script_text']}"
        )
        return {"final_output": llm.invoke(prompt).content.strip()}

    graph = StateGraph(PipelineState)
    graph.add_node("editor", editor_node)
    graph.add_node("scriptwriter", scriptwriter_node)
    graph.add_node("translator", translator_node)
    graph.add_edge(START, "editor")
    graph.add_edge("editor", "scriptwriter")
    graph.add_edge("scriptwriter", "translator")
    graph.add_edge("translator", END)
    return graph.compile(checkpointer=InMemorySaver())


STAGES = {
    "editor": ("✏️ Editor", "edited_text", "Edited text"),
    "scriptwriter": ("🎙️ Scriptwriter", "script_text", "Video script"),
    "translator": ("🌐 Hinglish Translator", "final_output", "Roman Hinglish"),
}

# ---------------------------------------------------------------- Sidebar
with st.sidebar:
    st.header("⚙️ Settings")
    model = st.text_input("Groq model", value="openai/gpt-oss-20b")
    temperature = st.slider("Temperature", 0.0, 1.5, 0.7, 0.1)
    max_tokens = st.slider(
        "Max tokens", 256, 4096, 2048, 128,
        help="Reasoning models like gpt-oss spend tokens on thinking, so keep this generous.",
    )
    show_steps = st.checkbox("Show intermediate stages", value=True)
    if st.button("🗑️ Clear history", use_container_width=True):
        st.session_state.history = []
        st.rerun()

# ---------------------------------------------------------------- Main UI
st.title("🎬 Hinglish Script Studio")
st.caption("Transform your raw idea into an engaging Roman Hinglish video script.")

if "history" not in st.session_state:
    st.session_state.history = []

raw_input = st.text_area(
    "Your raw idea",
    height=180,
    placeholder="e.g. langgraph lets you build agent workflows as graphs, its pretty cool and easy to learn...",
)

run = st.button("🚀 Generate script", type="primary", use_container_width=True)

if run:
    if not raw_input.strip():
        st.warning("Please enter some text first.")
    else:
        app = build_graph(model, temperature, max_tokens)
        # Fresh thread per run so state never leaks between generations
        config = {"configurable": {"thread_id": str(uuid.uuid4())}}
        results: dict[str, str] = {}

        try:
            with st.status("Running pipeline...", expanded=True) as status:
                for chunk in app.stream(
                    {"raw_input": raw_input}, config=config, stream_mode="updates"
                ):
                    for node_name, update in chunk.items():
                        label, key, _ = STAGES[node_name]
                        results[key] = update[key]
                        st.write(f"✅ {label} done")
                status.update(label="Pipeline complete!", state="complete", expanded=False)

            st.session_state.history.insert(
                0, {"raw": raw_input, **results}
            )
        except Exception as err:
            st.error(f"Pipeline failed: {err}")

# ---------------------------------------------------------------- Results
for i, item in enumerate(st.session_state.history):
    st.divider()
    if i == 0:
        st.subheader("Latest result")
    with st.container(border=True):
        st.markdown("**🗣️ Roman Hinglish script**")
        st.write(item["final_output"])
        st.code(item["final_output"], language=None)  # handy copy button

    if show_steps:
        with st.expander("See intermediate stages"):
            st.markdown("**Original input**")
            st.write(item["raw"])
            st.markdown("**✏️ Edited text**")
            st.write(item["edited_text"])
            st.markdown("**🎙️ Video script**")
            st.write(item["script_text"])