# Streamlit Chatbot with Groq — SaaS Edition (Dark Theme)

# A polished, responsive, dark-only web chatbot UI that talks to Groq's free API.

# Setup:
#     uv add streamlit langchain-groq python-dotenv

# Run:
#     streamlit run app.py

# Environment (.env):
#     GROQ_API_KEY=your_key_here

# Imports — Standard Library
# Import os module for environment variable access
import os
# Import time module to measure response latency
import time
# Import base64 module to encode SVG icons as data URIs
import base64
# Import datetime to timestamp exported chat files
from datetime import datetime

# Imports — Third Party
# Import load_dotenv to read environment variables from a .env file
from dotenv import load_dotenv

# Import streamlit for building the web UI
import streamlit as st
# Import ChatGroq to connect to Groq's chat models
from langchain_groq import ChatGroq
# Import the base chat model class for type hinting
from langchain_core.language_models import BaseChatModel
# Import message types used to structure the conversation
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

# Environment
# Load environment variables from the .env file into os.environ
load_dotenv()


# CONSTANTS
# Title shown in the browser tab and header
APP_TITLE = "Groq Chatbot"
# Short tagline displayed beneath the title
APP_TAGLINE = "Fast, free, and open-weight LLMs — served instantly by Groq"
# Default persona used if the user does not override it
DEFAULT_SYSTEM_PROMPT = "You are a helpful, friendly, and concise assistant."

# Mapping of model IDs to human-friendly labels shown in the sidebar
MODEL_OPTIONS = {
    "openai/gpt-oss-120b": "GPT-OSS 120B — Best quality",
    "openai/gpt-oss-20b": "GPT-OSS 20B — Fastest",
    "llama-3.3-70b-versatile": "Llama 3.3 70B — Versatile",
    "mixtral-8x7b-32768": "Mixtral 8x7B — Long context",
}

# Inline SVG icons (no external deps, no emoji)
# Dictionary holding all SVG icon markup used throughout the UI
ICONS = {
    "logo": """
        <svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <linearGradient id="lg" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#FB923C"/>
              <stop offset="100%" stop-color="#EF4444"/>
            </linearGradient>
          </defs>
          <circle cx="50" cy="50" r="46" fill="url(#lg)"/>
          <circle cx="35" cy="45" r="7" fill="#0E1117"/>
          <circle cx="65" cy="45" r="7" fill="#0E1117"/>
          <path d="M30 65 Q50 82 70 65" stroke="#0E1117" stroke-width="6"
                fill="none" stroke-linecap="round"/>
          <rect x="46" y="10" width="8" height="14" rx="4" fill="#0E1117"/>
        </svg>
    """,
    "chat": """
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor"
             stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>
        </svg>
    """,
    "settings": """
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor"
             stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <circle cx="12" cy="12" r="3"/>
          <path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 1 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 1 1-4 0v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 1 1-2.83-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 1 1 0-4h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 1 1 2.83-2.83l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 1 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 1 1 2.83 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 1 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1z"/>
        </svg>
    """,
    "info": """
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor"
             stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <circle cx="12" cy="12" r="10"/>
          <line x1="12" y1="16" x2="12" y2="12"/>
          <line x1="12" y1="8" x2="12.01" y2="8"/>
        </svg>
    """,
    "reset": """
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor"
             stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M3 12a9 9 0 1 0 3-6.7L3 8"/>
          <polyline points="3 3 3 8 8 8"/>
        </svg>
    """,
    "download": """
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor"
             stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/>
          <polyline points="7 10 12 15 17 10"/>
          <line x1="12" y1="15" x2="12" y2="3"/>
        </svg>
    """,
    "save": """
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor"
             stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M19 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11l5 5v11a2 2 0 0 1-2 2z"/>
          <polyline points="17 21 17 13 7 13 7 21"/>
          <polyline points="7 3 7 8 15 8"/>
        </svg>
    """,
    "trash": """
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor"
             stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <polyline points="3 6 5 6 21 6"/>
          <path d="M19 6l-1 14a2 2 0 0 1-2 2H8a2 2 0 0 1-2-2L5 6"/>
          <path d="M10 11v6M14 11v6"/>
        </svg>
    """,
    "bot": """
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor"
             stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <rect x="3" y="11" width="18" height="10" rx="2"/>
          <circle cx="12" cy="5" r="2"/>
          <path d="M12 7v4"/>
          <line x1="8" y1="16" x2="8" y2="16"/>
          <line x1="16" y1="16" x2="16" y2="16"/>
        </svg>
    """,
    "user": """
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor"
             stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/>
          <circle cx="12" cy="7" r="4"/>
        </svg>
    """,
    "key": """
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor"
             stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M21 2l-2 2m-7.61 7.61a5.5 5.5 0 1 1-7.778 7.778 5.5 5.5 0 0 1 7.777-7.777zm0 0L15.5 7.5m0 0l3 3L22 7l-3-3m-3.5 3.5L19 4"/>
        </svg>
    """,
    "sparkles": """
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor"
             stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M12 3l1.9 5.6L19 10l-5.1 1.4L12 17l-1.9-5.6L5 10l5.1-1.4z"/>
          <path d="M5 18l.7 2.1L8 21l-2.3.9L5 24"/>
        </svg>
    """,
    "layers": """
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor"
             stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <polygon points="12 2 2 7 12 12 22 7 12 2"/>
          <polyline points="2 17 12 22 22 17"/>
          <polyline points="2 12 12 17 22 12"/>
        </svg>
    """,
    "package": """
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor"
             stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <line x1="16.5" y1="9.4" x2="7.5" y2="4.21"/>
          <path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/>
          <polyline points="3.27 6.96 12 12.01 20.73 6.96"/>
          <line x1="12" y1="22.08" x2="12" y2="12"/>
        </svg>
    """,
    "check": """
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor"
             stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
          <polyline points="20 6 9 17 4 12"/>
        </svg>
    """,
    "x": """
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor"
             stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
          <line x1="18" y1="6" x2="6" y2="18"/>
          <line x1="6" y1="6" x2="18" y2="18"/>
        </svg>
    """,
}


def icon(name: str, size: int = 16, color: str = "currentColor") -> str:
    # Return an inline SVG icon as a string sized and coloured on demand
    svg = ICONS[name]
    svg = svg.replace("<svg ", f'<svg width="{size}" height="{size}" '
                               f'style="color:{color};vertical-align:middle;" ')
    return svg


def svg_to_data_uri(svg: str) -> str:
    # Encode an SVG string as a data URI for use in <img src
    b64 = base64.b64encode(svg.encode("utf-8")).decode("utf-8")
    return f"data:image/svg+xml;base64,{b64}"


# Convert the logo SVG into a data URI so it can be embedded anywhere
LOGO_URI = svg_to_data_uri(ICONS["logo"])


# PAGE CONFIG
# Configure the Streamlit page title, icon, layout, and sidebar state
st.set_page_config(
    page_title=APP_TITLE,
    page_icon=LOGO_URI,
    layout="centered",
    initial_sidebar_state="expanded",
)


# GLOBAL STYLES — Dark theme only, Inter + JetBrains Mono
def inject_styles() -> None:
    # Inject custom CSS into the app to style every component
    st.markdown(
        f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');

        :root {{
            --bg-primary: #0b0e14;
            --bg-secondary: #11151d;
            --bg-elevated: #161b24;
            --bg-hover: #1b212c;
            --text-primary: #e8eaed;
            --text-secondary: #8b929e;
            --text-muted: #5f6673;
            --border-color: rgba(255,255,255,0.07);
            --border-strong: rgba(255,255,255,0.12);
            --accent: #fb923c;
            --accent-hover: #fdba74;
            --accent-soft: rgba(251,146,60,0.12);
            --accent-glow: rgba(251,146,60,0.35);
            --success: #22c55e;
            --success-soft: rgba(34,197,94,0.12);
            --danger: #ef4444;
            --danger-soft: rgba(239,68,68,0.12);
            --bubble-user: #1a2130;
            --bubble-assistant: #171b24;
            --shadow-sm: 0 1px 2px rgba(0,0,0,0.4);
            --shadow-md: 0 4px 16px rgba(0,0,0,0.45);
            --shadow-lg: 0 12px 32px rgba(0,0,0,0.55);
            --radius-sm: 8px;
            --radius-md: 12px;
            --radius-lg: 16px;
            --radius-xl: 20px;
        }}

        /* ---- Base reset ---- */
        html, body, [class*="css"], .stApp {{
            font-family: 'Inter', -apple-system, BlinkMacSystemFont,
                         'Segoe UI', sans-serif !important;
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: grayscale;
        }}
        .stApp {{
            background:
                radial-gradient(ellipse 80% 50% at 50% -20%,
                    rgba(251,146,60,0.08), transparent),
                var(--bg-primary) !important;
            color: var(--text-primary) !important;
        }}
        code, pre, kbd, samp, .mono {{
            font-family: 'JetBrains Mono', ui-monospace, SFMono-Regular,
                         Menlo, monospace !important;
        }}
        #MainMenu, footer {{ visibility: hidden; }}
        [data-testid="stHeader"] {{ background: transparent !important; }}
        [data-testid="stToolbar"] {{ right: 1rem; }}

        /* ---- Sidebar ---- */
        [data-testid="stSidebar"] {{
            background-color: var(--bg-secondary) !important;
            border-right: 1px solid var(--border-color);
        }}
        [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {{
            color: var(--text-secondary);
        }}

        /* ---- Tabs (top nav) ---- */
        .stTabs [data-baseweb="tab-list"] {{
            gap: 4px;
            background: var(--bg-secondary);
            padding: 6px;
            border-radius: var(--radius-md);
            border: 1px solid var(--border-color);
            box-shadow: var(--shadow-sm);
        }}
        .stTabs [data-baseweb="tab"] {{
            height: 42px;
            border-radius: var(--radius-sm);
            color: var(--text-secondary);
            font-weight: 600;
            font-size: 0.9rem;
            letter-spacing: 0.01em;
            padding: 0 18px;
            transition: all 0.18s cubic-bezier(0.4, 0, 0.2, 1);
        }}
        .stTabs [data-baseweb="tab"]:hover {{
            color: var(--text-primary);
            background: var(--bg-hover);
        }}
        .stTabs [aria-selected="true"] {{
            background: var(--accent-soft) !important;
            color: var(--accent) !important;
            box-shadow: inset 0 0 0 1px var(--accent-glow);
        }}
        .stTabs [data-baseweb="tab-highlight"],
        .stTabs [data-baseweb="tab-border"] {{
            display: none !important;
        }}

        /* ---- Hero header ---- */
        .app-header {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 16px;
            padding: 0.85rem 1.15rem;
            border-radius: var(--radius-lg);
            background:
                linear-gradient(180deg, rgba(255,255,255,0.02), transparent),
                var(--bg-secondary);
            border: 1px solid var(--border-color);
            box-shadow: var(--shadow-md);
            margin-bottom: 1.2rem;
            flex-wrap: wrap;
            animation: slideDown 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        }}
        .app-header-left {{
            display: flex; align-items: center; gap: 14px;
        }}
        .app-header img {{
            border-radius: var(--radius-md);
            box-shadow: 0 2px 12px var(--accent-glow);
        }}
        .app-header h1 {{
            margin: 0;
            font-size: 1.45rem;
            font-weight: 700;
            line-height: 1.2;
            letter-spacing: -0.02em;
            color: var(--text-primary);
        }}
        .app-header p {{
            margin: 2px 0 0 0;
            color: var(--text-secondary);
            font-size: 0.85rem;
            font-weight: 400;
        }}

        /* ---- Cards ---- */
        .saas-card {{
            background: var(--bg-elevated);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-lg);
            padding: 1.1rem 1.25rem;
            box-shadow: var(--shadow-sm);
            margin-bottom: 1rem;
            transition: border-color 0.2s ease, transform 0.2s ease;
        }}
        .saas-card:hover {{
            border-color: var(--border-strong);
        }}
        .saas-card h4 {{
            margin: 0 0 0.35rem 0;
            color: var(--text-primary);
            font-size: 0.98rem;
            font-weight: 600;
            letter-spacing: -0.01em;
            display: flex; align-items: center; gap: 8px;
        }}
        .saas-card p.sub {{
            color: var(--text-secondary);
            font-size: 0.83rem;
            margin: 0 0 0.4rem 0;
            line-height: 1.5;
        }}
        .saas-card code {{
            background: var(--bg-secondary);
            border: 1px solid var(--border-color);
            padding: 2px 7px;
            border-radius: 6px;
            font-size: 0.8rem;
            color: var(--accent);
        }}

        /* ---- Chat messages ---- */
        [data-testid="stChatMessage"] {{
            border-radius: var(--radius-lg);
            padding: 0.55rem 0.75rem;
            border: 1px solid var(--border-color);
            background: var(--bg-elevated);
            margin-bottom: 10px;
            animation: fadeUp 0.28s cubic-bezier(0.4, 0, 0.2, 1);
            transition: border-color 0.18s ease, transform 0.18s ease;
        }}
        [data-testid="stChatMessage"]:hover {{
            border-color: var(--border-strong);
            transform: translateY(-1px);
        }}
        [data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) {{
            background: var(--bubble-user);
        }}
        [data-testid="stChatMessageContent"] {{
            font-size: 0.94rem;
            line-height: 1.65;
            color: var(--text-primary);
        }}
        [data-testid="stChatMessageContent"] p {{ margin: 0.2rem 0; }}
        [data-testid="stChatMessageAvatarUser"],
        [data-testid="stChatMessageAvatarAssistant"] {{
            border-radius: 10px !important;
            overflow: hidden;
        }}

        /* ---- Status pill ---- */
        .status-pill {{
            display: inline-flex;
            align-items: center;
            gap: 7px;
            padding: 5px 12px;
            border-radius: 999px;
            background: var(--success-soft);
            color: var(--success);
            font-size: 0.75rem;
            font-weight: 600;
            letter-spacing: 0.01em;
            border: 1px solid rgba(34,197,94,0.25);
        }}
        .status-pill.offline {{
            background: var(--danger-soft);
            color: var(--danger);
            border-color: rgba(239,68,68,0.25);
        }}
        .status-dot {{
            width: 7px; height: 7px; border-radius: 50%;
            background: var(--success);
            animation: pulse 2s infinite;
        }}
        .status-dot.offline {{ background: var(--danger); animation: none; }}

        /* ---- Buttons ---- */
        .stButton > button,
        .stDownloadButton > button {{
            border-radius: var(--radius-sm) !important;
            font-weight: 600 !important;
            font-size: 0.86rem !important;
            letter-spacing: 0.01em;
            border: 1px solid var(--border-strong) !important;
            background: var(--bg-elevated) !important;
            color: var(--text-primary) !important;
            transition: all 0.18s cubic-bezier(0.4, 0, 0.2, 1) !important;
            display: inline-flex !important;
            align-items: center !important;
            justify-content: center !important;
            gap: 8px !important;
            padding: 0.5rem 1rem !important;
        }}
        .stButton > button:hover,
        .stDownloadButton > button:hover {{
            border-color: var(--accent) !important;
            color: var(--accent) !important;
            background: var(--accent-soft) !important;
            transform: translateY(-1px);
            box-shadow: 0 4px 14px rgba(0,0,0,0.35),
                        0 0 0 1px var(--accent-glow) !important;
        }}
        .stButton > button:active,
        .stDownloadButton > button:active {{
            transform: translateY(0);
        }}
        .stButton > button[kind="primary"],
        .stDownloadButton > button[kind="primary"] {{
            background: linear-gradient(180deg, #fb923c, #ea580c) !important;
            border-color: #ea580c !important;
            color: #0b0e14 !important;
            box-shadow: 0 4px 14px rgba(251,146,60,0.3) !important;
        }}
        .stButton > button[kind="primary"]:hover,
        .stDownloadButton > button[kind="primary"]:hover {{
            background: linear-gradient(180deg, #fdba74, #f97316) !important;
            color: #0b0e14 !important;
            box-shadow: 0 6px 20px rgba(251,146,60,0.45) !important;
        }}

        /* ---- Inputs / selects / sliders ---- */
        .stTextInput input,
        .stTextArea textarea,
        [data-baseweb="select"] > div {{
            background: var(--bg-secondary) !important;
            border: 1px solid var(--border-color) !important;
            border-radius: var(--radius-sm) !important;
            color: var(--text-primary) !important;
            font-family: 'Inter', sans-serif !important;
            transition: border-color 0.18s ease, box-shadow 0.18s ease;
        }}
        .stTextInput input:focus,
        .stTextArea textarea:focus,
        [data-baseweb="select"] > div:focus-within {{
            border-color: var(--accent) !important;
            box-shadow: 0 0 0 3px var(--accent-soft) !important;
        }}
        [data-testid="stSlider"] [data-baseweb="slider"] div[role="slider"] {{
            background: var(--accent) !important;
            box-shadow: 0 0 0 4px var(--accent-soft) !important;
        }}

        /* ---- Chat input ---- */
        [data-testid="stChatInput"] {{
            border-radius: var(--radius-md) !important;
            border: 1px solid var(--border-strong) !important;
            background: var(--bg-elevated) !important;
            transition: border-color 0.2s ease, box-shadow 0.2s ease;
        }}
        [data-testid="stChatInput"]:focus-within {{
            border-color: var(--accent) !important;
            box-shadow: 0 0 0 3px var(--accent-soft),
                        0 4px 16px rgba(0,0,0,0.35) !important;
        }}
        [data-testid="stChatInput"] textarea {{
            color: var(--text-primary) !important;
            font-family: 'Inter', sans-serif !important;
        }}

        /* ---- Metrics / captions ---- */
        [data-testid="stMetricValue"] {{
            font-family: 'JetBrains Mono', monospace !important;
            font-size: 1.35rem !important;
            font-weight: 600 !important;
            color: var(--text-primary) !important;
        }}
        [data-testid="stMetricLabel"] {{
            color: var(--text-secondary) !important;
            font-size: 0.78rem !important;
            font-weight: 500 !important;
        }}
        .stCaption, [data-testid="stCaptionContainer"] {{
            color: var(--text-muted) !important;
            font-size: 0.78rem !important;
        }}

        /* ---- Divider ---- */
        hr, [data-testid="stDivider"] {{
            border-color: var(--border-color) !important;
            margin: 0.75rem 0 !important;
        }}

        /* ---- Alerts ---- */
        [data-testid="stAlert"] {{
            border-radius: var(--radius-md) !important;
            border: 1px solid var(--border-color) !important;
            background: var(--bg-elevated) !important;
        }}

        /* ---- Animations ---- */
        @keyframes fadeUp {{
            from {{ opacity: 0; transform: translateY(8px); }}
            to   {{ opacity: 1; transform: translateY(0); }}
        }}
        @keyframes slideDown {{
            from {{ opacity: 0; transform: translateY(-10px); }}
            to   {{ opacity: 1; transform: translateY(0); }}
        }}
        @keyframes pulse {{
            0%   {{ box-shadow: 0 0 0 0 rgba(34,197,94,0.5); }}
            70%  {{ box-shadow: 0 0 0 8px rgba(34,197,94,0); }}
            100% {{ box-shadow: 0 0 0 0 rgba(34,197,94,0); }}
        }}
        @keyframes blink {{
            0%, 100% {{ opacity: 1; }}
            50%      {{ opacity: 0.15; }}
        }}
        .cursor-blink {{
            display: inline-block;
            width: 7px; height: 1.05em;
            background: var(--accent);
            vertical-align: text-bottom;
            margin-left: 2px;
            border-radius: 1px;
            animation: blink 1s steps(2, start) infinite;
        }}

        /* ---- Responsiveness ---- */
        @media (max-width: 640px) {{
            .app-header {{ flex-direction: column; align-items: flex-start; }}
            .app-header h1 {{ font-size: 1.2rem; }}
            .app-header p  {{ font-size: 0.78rem; }}
            .app-header img {{ width: 34px; height: 34px; }}
            [data-testid="stChatMessageContent"] {{ font-size: 0.9rem; }}
            .saas-card {{ padding: 0.9rem 1rem; }}
        }}

        /* ---- Scrollbar ---- */
        ::-webkit-scrollbar {{ width: 8px; height: 8px; }}
        ::-webkit-scrollbar-track {{ background: transparent; }}
        ::-webkit-scrollbar-thumb {{
            background: rgba(255,255,255,0.12);
            border-radius: 8px;
        }}
        ::-webkit-scrollbar-thumb:hover {{
            background: rgba(255,255,255,0.2);
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )


# Call the style injection function to apply CSS to the app
inject_styles()


# SESSION STATE INIT
def init_state() -> None:
    # Set default values for all session state keys used by the app
    defaults = {
        "messages": [SystemMessage(content=DEFAULT_SYSTEM_PROMPT)],
        "model_name": "openai/gpt-oss-120b",
        "temperature": 0.7,
        "system_prompt": DEFAULT_SYSTEM_PROMPT,
    }
    # Only set each key if it hasn't been set before
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


# Initialize session state on first run
init_state()


# MODEL LOADER
# Cache the model instance so it isn't rebuilt on every rerun
@st.cache_resource(show_spinner=False)
def load_model(model_name: str, temperature: float) -> BaseChatModel:
    return ChatGroq(model=model_name, temperature=temperature)


def get_model() -> BaseChatModel | None:
    # Return None if the API key is missing so the UI can warn the user
    if not os.getenv("GROQ_API_KEY"):
        return None
    # Otherwise return the cached model instance
    return load_model(st.session_state.model_name, st.session_state.temperature)


# Check whether the API key exists so the UI can reflect connection status
api_key_present = bool(os.getenv("GROQ_API_KEY"))


# HEADER
# Render the hero header with logo, title, tagline, and status pill
st.markdown(
    f"""
    <div class="app-header">
        <div class="app-header-left">
            <img src="{LOGO_URI}" width="44" height="44" alt="logo" />
            <div>
                <h1>{APP_TITLE}</h1>
                <p>{APP_TAGLINE}</p>
            </div>
        </div>
        <span class="status-pill{' offline' if not api_key_present else ''}">
            <span class="status-dot{' offline' if not api_key_present else ''}"></span>
            {'Connected' if api_key_present else 'No API Key'}
        </span>
    </div>
    """,
    unsafe_allow_html=True,
)


# SIDEBAR — Controls
with st.sidebar:
    # Sidebar header with logo and title
    st.markdown(
        f"""
        <div style="display:flex;align-items:center;gap:10px;
                    padding:0.25rem 0 0.75rem 0;">
            <img src="{LOGO_URI}" width="32" height="32" alt="logo" />
            <span style="font-weight:700;font-size:1rem;
                         letter-spacing:-0.01em;color:var(--text-primary);">
                Control Panel
            </span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Show an error if the API key is missing
    if not api_key_present:
        st.error("GROQ_API_KEY not found. Add it to your `.env` file.")

    # Section label for the model dropdown
    st.markdown(
        f'<div style="display:flex;align-items:center;gap:8px;'
        f'font-size:0.82rem;font-weight:600;color:var(--text-secondary);'
        f'margin:0.4rem 0 0.5rem 0;">'
        f'{icon("bot", 15)} Model</div>',
        unsafe_allow_html=True,
    )
    # Let the user pick a model by its human-friendly label
    selected_label = st.selectbox(
        "Model",
        options=list(MODEL_OPTIONS.values()),
        index=list(MODEL_OPTIONS.keys()).index(st.session_state.model_name),
        label_visibility="collapsed",
    )
    # Translate the selected label back into its model ID
    new_model = [k for k, v in MODEL_OPTIONS.items() if v == selected_label][0]
    # If the model changed, clear the cache and rerun so it reloads
    if new_model != st.session_state.model_name:
        st.session_state.model_name = new_model
        load_model.clear()
        st.rerun()

    # Slider to adjust the model's temperature
    st.session_state.temperature = st.slider(
        "Temperature",
        min_value=0.0,
        max_value=1.5,
        value=st.session_state.temperature,
        step=0.05,
        help="Higher = more creative, lower = more focused.",
    )

    # Expandable section to edit the system prompt
    with st.expander("System Prompt"):
        # Text area pre-filled with the current system prompt
        new_prompt = st.text_area(
            "Persona / instructions",
            value=st.session_state.system_prompt,
            height=100,
            label_visibility="collapsed",
        )
        # Apply the new prompt when the user clicks the button
        if st.button("Apply prompt", use_container_width=True):
            st.session_state.system_prompt = new_prompt
            st.session_state.messages[0] = SystemMessage(content=new_prompt)
            st.toast("System prompt updated", icon=":material/check_circle:")

    # Visual separator
    st.divider()

    # Button to wipe the conversation history
    if st.button("Reset chat", use_container_width=True):
        st.session_state.messages = [
            SystemMessage(content=st.session_state.system_prompt)
        ]
        st.rerun()

    # Count non-system messages to show in metrics and export
    chat_count = len(st.session_state.messages) - 1
    if chat_count > 0:
        # Build a plain-text transcript of the conversation
        export_text = "\n\n".join(
            f"{'You' if isinstance(m, HumanMessage) else 'Assistant'}: {m.content}"
            for m in st.session_state.messages
            if not isinstance(m, SystemMessage)
        )
        # Download button to export the chat as a text file
        st.download_button(
            "Export chat",
            data=export_text,
            file_name=f"chat_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
            mime="text/plain",
            use_container_width=True,
        )

    # Visual separator
    st.divider()
    # Small captions summarizing current session info
    st.caption(f"Messages · {chat_count}")
    st.caption(f"Model · `{st.session_state.model_name}`")
    st.caption("Provider · Groq (free tier)")


# MAIN — Tabs
# Create the three main tabs of the app
tab_chat, tab_settings, tab_about = st.tabs(["Chat", "Settings", "About"])



# TAB 1 — CHAT
with tab_chat:
    # Render every non-system message in the conversation
    for msg in st.session_state.messages:
        if isinstance(msg, SystemMessage):
            continue
        if isinstance(msg, HumanMessage):
            with st.chat_message("user"):
                st.write(msg.content)
        elif isinstance(msg, AIMessage):
            with st.chat_message("assistant", avatar=LOGO_URI):
                st.write(msg.content)

    # Show a friendly hint when the chat is empty
    if len(st.session_state.messages) == 1:
        st.info("Say hello to get started. Ask anything below.")

    # Text input at the bottom for the user's next message
    user_input: str | None = st.chat_input("Type your message...")

    if user_input:
        # Load the model, or fail early if the API key is missing
        model = get_model()
        if model is None:
            st.error("No GROQ_API_KEY found. Set it in your `.env` file.")
            st.stop()

        # Append the user's message to the conversation history
        st.session_state.messages.append(HumanMessage(content=user_input))
        with st.chat_message("user"):
            st.write(user_input)

        # Stream the assistant's reply token by token
        with st.chat_message("assistant", avatar=LOGO_URI):
            placeholder = st.empty()
            full_response = ""

            try:
                # Track how long the response takes to generate
                start = time.time()
                for chunk in model.stream(st.session_state.messages):
                    full_response += chunk.content or ""
                    # Show the growing response with a blinking cursor
                    placeholder.markdown(
                        full_response + '<span class="cursor-blink"></span>',
                        unsafe_allow_html=True,
                    )
                elapsed = time.time() - start

                # Replace the streaming placeholder with the final text
                placeholder.markdown(full_response)
                st.caption(f"Responded in {elapsed:.2f}s")

            except Exception as exc:
                # Surface any error nicely in the chat bubble
                full_response = f"Something went wrong: `{exc}`"
                placeholder.error(full_response)

        # Append the assistant's reply to the conversation history
        st.session_state.messages.append(AIMessage(content=full_response))

# TAB 2 — SETTINGS
with tab_settings:
    # Card describing the API connection section
    st.markdown(
        f"""
        <div class="saas-card">
            <h4>{icon("key", 16, "#fb923c")} API Connection</h4>
            <p class="sub">Manage how this app talks to Groq.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    # Two-column layout for the key display and connection metric
    col1, col2 = st.columns(2)
    with col1:
        # Read-only masked API key field
        st.text_input(
            "GROQ_API_KEY",
            value="•" * 12 if api_key_present else "",
            type="password",
            disabled=True,
            help="Set this in your .env file — not editable here for security.",
        )
    with col2:
        # Quick glance at whether the key is detected
        st.metric(
            "Connection status",
            "Online" if api_key_present else "Offline",
        )

    # Card describing the model preferences section
    st.markdown(
        f"""
        <div class="saas-card">
            <h4>{icon("sparkles", 16, "#fb923c")} Model Preferences</h4>
            <p class="sub">Fine-tune the behavior of your assistant.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    # Two-column layout for model info and temperature visualization
    c1, c2 = st.columns(2)
    with c1:
        st.write("**Current model**")
        st.code(st.session_state.model_name, language="text")
    with c2:
        st.write("**Temperature**")
        # Progress bar scaled to the slider's max value
        st.progress(min(st.session_state.temperature / 1.5, 1.0))
        st.caption(f"{st.session_state.temperature:.2f} / 1.50")

    # Card describing the data management section
    st.markdown(
        f"""
        <div class="saas-card">
            <h4>{icon("layers", 16, "#fb923c")} Data</h4>
            <p class="sub">Manage your conversation history.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    # Two-column layout for clearing the chat and showing message count
    colA, colB = st.columns(2)
    with colA:
        if st.button("Clear conversation", use_container_width=True):
            st.session_state.messages = [
                SystemMessage(content=st.session_state.system_prompt)
            ]
            st.toast("Conversation cleared", icon=":material/delete:")
            st.rerun()
    with colB:
        # Show how many messages are in the current session
        st.metric("Total messages", len(st.session_state.messages) - 1)


# TAB 3 — ABOUT
with tab_about:
    # Render informational cards describing the app, stack, and setup
    st.markdown(
        f"""
        <div class="saas-card">
            <h4>{icon("info", 16, "#fb923c")} About this app</h4>
            <p class="sub">{APP_TAGLINE}</p>
            <p style="color:var(--text-secondary); font-size:0.88rem;
                      line-height:1.6; margin:0;">
                This chatbot streams responses in real time from Groq's
                LPU-powered inference engine using open-weight models via
                LangChain. Fully configurable model, temperature, and persona —
                all running on Streamlit with zero external image or CSS
                dependencies.
            </p>
        </div>
        <div class="saas-card">
            <h4>{icon("package", 16, "#fb923c")} Tech stack</h4>
            <p class="sub">
                Streamlit · LangChain · langchain-groq · python-dotenv
            </p>
        </div>
        <div class="saas-card">
            <h4>{icon("check", 16, "#fb923c")} Setup</h4>
            <p class="sub" style="margin:0;">
                <code>uv add streamlit langchain-groq python-dotenv</code><br/>
                <code>streamlit run app.py</code>
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )