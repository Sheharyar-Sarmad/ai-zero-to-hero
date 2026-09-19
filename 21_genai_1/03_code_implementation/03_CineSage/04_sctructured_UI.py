# Streamlit UI for CineSage — Movie Paragraph Extractor (JSON First)

# Setup:
#     uv add streamlit langchain-groq python-dotenv

# Run:
#     python -m streamlit run app.py

# Load environment variables from .env (GROQ_API_KEY)
from dotenv import load_dotenv
load_dotenv()

# Import streamlit for the web UI
import streamlit as st

# Import ChatGroq to talk to Groq's LLM API
from langchain_groq import ChatGroq

# Import BaseModel and Field to define the JSON schema
from pydantic import BaseModel, Field

# Import Optional and List for typing
from typing import Optional, List

# Import ChatPromptTemplate to build a reusable prompt
from langchain_core.prompts import ChatPromptTemplate

# Page config
st.set_page_config(
    page_title="CineSage — Movie Extractor",
    page_icon="🎬",
    layout="centered",
)

# Title
st.title("🎬 CineSage")
st.caption("Extract structured movie info as JSON using Groq.")

# Movie schema — defines the JSON shape we want back
class Movie(BaseModel):
    title: str = Field(description="Movie title")
    release_year: Optional[int] = Field(description="Year released")
    genre: List[str] = Field(description="List of genres")
    director: Optional[str] = Field(description="Director's name")
    cast: List[str] = Field(description="Main cast members")
    setting: Optional[str] = Field(description="Where it takes place")
    plot: Optional[str] = Field(description="Short plot description")
    themes: List[str] = Field(description="Themes explored")
    rating: Optional[float] = Field(description="IMDb or similar rating")
    notable_features: Optional[str] = Field(description="Standout features")
    summary: str = Field(description="Short 2-3 line summary")

# Load model + wrap with structured output (cached)
@st.cache_resource(show_spinner=False)
def load_model():
    model = ChatGroq(model="openai/gpt-oss-120b")
    return model.with_structured_output(Movie)

# Load prompt template (cached)
@st.cache_resource(show_spinner=False)
def load_prompt() -> ChatPromptTemplate:
    return ChatPromptTemplate.from_messages([
        (
            "system",
            """
You are a professional Movie Information Extraction Assistant.

Your task:
Extract structured information from a movie paragraph and return it as JSON.

Rules:
- Return ONLY valid JSON that matches the given schema
- Do NOT add explanations or extra commentary
- If information is missing, use null (or an empty list for arrays)
- Keep the summary short (2-3 lines max)
- Do NOT guess unknown facts
"""
        ),
        ("human", "{paragraph}")
    ])

model = load_model()
prompt = load_prompt()

# Session state for the result
if "movie" not in st.session_state:
    st.session_state.movie = None

# Input area
paragraph: str = st.text_area(
    "Paste your movie paragraph below:",
    height=220,
    placeholder="Interstellar is a visually stunning science fiction epic...",
)

# Buttons
col1, col2 = st.columns(2)
with col1:
    extract = st.button("🚀 Extract", use_container_width=True, type="primary")
with col2:
    clear = st.button("🧹 Clear", use_container_width=True)

if clear:
    st.session_state.movie = None
    st.rerun()

# Extraction logic
if extract:
    if not paragraph.strip():
        st.warning("Please paste a movie paragraph first.")
    else:
        messages = prompt.format_messages(paragraph=paragraph)
        with st.spinner("Extracting with Groq..."):
            try:
                st.session_state.movie = model.invoke(messages)
            except Exception as exc:
                st.session_state.movie = None
                st.error(f"Something went wrong: `{exc}`")

# Display result — JSON first, then summary, then actions
if st.session_state.movie is not None:
    m: Movie = st.session_state.movie
    json_str: str = m.model_dump_json(indent=2)

    st.divider()

    # 1) JSON VIEW FIRST — this is the main output
    st.subheader("🧾 JSON Output")
    st.code(json_str, language="json")

    # 2) SUMMARY — plain text summary under the JSON
    st.subheader("📝 Summary")
    st.write(m.summary)

    # 3) ACTIONS — download + copy buttons side by side
    st.divider()
    dl_col, copy_col = st.columns(2)

    with dl_col:
        st.download_button(
            "⬇️ Download JSON",
            data=json_str,
            file_name=f"{m.title.replace(' ', '_')}.json",
            mime="application/json",
            use_container_width=True,
        )

    with copy_col:
        # st.code gives a built-in copy button; clicking it copies the JSON
        st.caption("Copy the JSON:")
        with st.expander("📋 Click to reveal copyable JSON"):
            st.code(json_str, language="json")