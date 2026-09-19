# Streamlit UI for CineSage — Movie Paragraph Extractor (Formatted)

# A simple web UI that mirrors the CLI app: paste a movie paragraph,
# send it to the Groq model, and display the extracted information
# in a clean, properly formatted layout.

# Setup:
#     uv add streamlit langchain-groq python-dotenv

# Run:
#     streamlit run app.py

# Environment (.env):
#     GROQ_API_KEY=your_key_here

# Load Environment Variables
from dotenv import load_dotenv

# Read .env and load GROQ_API_KEY into os.environ
load_dotenv()

# Imports
# Import streamlit for the web UI
import streamlit as st

# Import ChatGroq to connect to Groq's chat models
from langchain_groq import ChatGroq

# Import ChatPromptTemplate to define the extraction prompt
from langchain_core.prompts import ChatPromptTemplate

# Import Pydantic for structured output schema
from pydantic import BaseModel, Field

# PAGE CONFIG
st.set_page_config(
    page_title="CineSage — Movie Paragraph Extractor",
    page_icon="🎬",
    layout="centered",
    initial_sidebar_state="expanded",
)

# TITLE & RULES
st.title("🎬 CineSage")
st.caption("Extract structured movie information from any paragraph using Groq.")

with st.expander("📖 How to use", expanded=False):
    st.markdown(
        """
        **Rules:**
        - Paste a paragraph about a movie into the text box.
        - Click **Extract Information** to send it to the model.
        - The model returns a clean, structured breakdown.
        - Missing fields are marked as `NULL`.
        - Click **Clear** to reset the input and result.
        """
    )


# STRUCTURED OUTPUT SCHEMA
# Define the exact fields we want back from the model
class MovieInfo(BaseModel):
    # Each field maps to one line of the extraction prompt
    movie_title: str = Field(description="Title of the movie, or NULL if unknown")
    release_year: str = Field(description="Release year, or NULL if unknown")
    genre: str = Field(description="Genre(s) of the movie, or NULL if unknown")
    director: str = Field(description="Director's name, or NULL if unknown")
    main_cast: str = Field(description="Comma-separated list of main cast, or NULL")
    setting_location: str = Field(description="Where the movie takes place, or NULL")
    plot: str = Field(description="Short plot description, or NULL")
    themes: str = Field(description="Comma-separated themes, or NULL")
    ratings: str = Field(description="Ratings like IMDb score, or NULL")
    notable_features: str = Field(description="Notable features, or NULL")
    short_summary: str = Field(description="2-3 line summary, or NULL")


# MODEL (CACHED)
@st.cache_resource(show_spinner=False)
def load_model():
    # Load the Groq chat model once and reuse it across reruns
    base_model = ChatGroq(model="openai/gpt-oss-120b")
    # Force the model to return a MovieInfo object instead of free text
    return base_model.with_structured_output(MovieInfo)


# PROMPT TEMPLATE (CACHED)
@st.cache_resource(show_spinner=False)
def load_prompt() -> ChatPromptTemplate:
    # Build the extraction prompt — the schema is enforced by the model wrapper
    return ChatPromptTemplate.from_messages([
        (
            "system",
            """
You are a professional Movie Information Extraction Assistant.

Extract the requested fields from the movie paragraph.
If a field is missing from the paragraph, set it to "NULL".
Do not guess unknown facts.
Keep the short summary to 2-3 lines max.
"""
        ),
        (
            "human",
            "{paragraph}"
        )
    ])


model = load_model()
prompt = load_prompt()

# SIDEBAR
with st.sidebar:
    st.header("⚙️ Settings")
    st.write("**Model:** `openai/gpt-oss-120b`")
    st.write("**Provider:** Groq (free tier)")
    st.write("**Output:** Structured JSON")
    st.divider()
    st.caption("CineSage · FastAPI + Next.js ready")

# SESSION STATE
# Track the current result so it survives reruns
if "result" not in st.session_state:
    st.session_state.result = None

# MAIN INPUT AREA
paragraph: str = st.text_area(
    "Paste your movie paragraph below:",
    height=220,
    placeholder="Interstellar is a visually stunning science fiction epic...",
)

# ACTION BUTTONS
col1, col2 = st.columns([1, 1])

with col1:
    # Trigger extraction
    extract_clicked = st.button(
        "🚀 Extract Information",
        use_container_width=True,
        type="primary",
    )

with col2:
    # Clear input and result
    clear_clicked = st.button("🧹 Clear", use_container_width=True)

if clear_clicked:
    # Reset the stored result; rerun refreshes the UI
    st.session_state.result = None
    st.rerun()

# EXTRACTION LOGIC
if extract_clicked:
    # Guard against empty input
    if not paragraph.strip():
        st.warning("Please paste a movie paragraph first.")
    else:
        # Format the prompt with the user's paragraph
        messages = prompt.format_messages(paragraph=paragraph)

        # Call the model with a spinner so the user sees progress
        with st.spinner("Analyzing paragraph with Groq..."):
            try:
                result: MovieInfo = model.invoke(messages)
                st.session_state.result = result
            except Exception as exc:
                st.session_state.result = None
                st.error(f"Something went wrong: `{exc}`")

# RESULT DISPLAY
if st.session_state.result is not None:
    r: MovieInfo = st.session_state.result

    st.divider()
    st.subheader("📄 Extracted Information")

    # Top row: title + year as highlighted metrics
    top_col1, top_col2, top_col3 = st.columns([3, 1, 1])
    with top_col1:
        st.markdown(f"### 🎬 {r.movie_title}")
    with top_col2:
        st.metric("Year", r.release_year)
    with top_col3:
        st.metric("Rating", r.ratings)

    # Two-column grid for the rest of the fields
    left, right = st.columns(2)

    with left:
        st.markdown(f"**🎭 Genre**  \n{r.genre}")
        st.markdown(f"**🎥 Director**  \n{r.director}")
        st.markdown(f"**👥 Main Cast**  \n{r.main_cast}")
        st.markdown(f"**📍 Setting**  \n{r.setting_location}")

    with right:
        st.markdown(f"**🎨 Themes**  \n{r.themes}")
        st.markdown(f"**⭐ Notable Features**  \n{r.notable_features}")

    # Full-width sections
    st.markdown("---")
    st.markdown("**📖 Plot**")
    st.info(r.plot)

    st.markdown("**📝 Short Summary**")
    st.success(r.short_summary)

    # Raw JSON view for developers + download
    with st.expander("🔍 View raw JSON"):
        st.json(r.model_dump())

    st.download_button(
        "⬇️ Download result as .json",
        data=r.model_dump_json(indent=2),
        file_name=f"cinesage_{r.movie_title.replace(' ', '_')}.json",
        mime="application/json",
        use_container_width=True,
    )