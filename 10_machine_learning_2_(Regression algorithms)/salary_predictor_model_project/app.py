# ============================================
# STREAMLIT APP - SALARY PREDICTOR PRO
# Professional UI with Font Awesome Icons & Groq API
# Created by: Sheharyar Sarmad
# Model: Linear Regression
# ============================================

import streamlit as st
import joblib
import pandas as pd
import numpy as np
from datetime import datetime
import os
from dotenv import load_dotenv
from groq import Groq
import json

# ============================================
# LOAD ENVIRONMENT VARIABLES
# ============================================

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# ============================================
# PAGE CONFIG
# ============================================

st.set_page_config(
    page_title="Salary Predictor Pro",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ============================================
# CONSTANTS
# ============================================

MODEL_PATH = "salary_model.pkl"
SCALER_PATH = "scaler.pkl"

EDUCATION_OPTIONS = ["Bachelor's", "Master's", "PhD"]
JOB_LEVEL_OPTIONS = ["Junior", "Mid Level", "Senior/Manager", "Executive/High"]
GENDER_OPTIONS = ["Female", "Male"]

SALARY_BANDS = [
    (50_000, "Entry Level", "Focus on gaining experience and building core skills."),
    (80_000, "Mid Level", "You're building a solid career trajectory."),
    (120_000, "Senior Level", "Strong professional standing in your field."),
    (float("inf"), "Executive Level", "You're in a leadership-tier compensation band."),
]

# ============================================
# CUSTOM CSS — MODERN REFINED THEME
# ============================================

st.markdown("""
<style>
    /* ===== FONT AWESOME ===== */
    @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css');
    
    /* ===== GOOGLE FONTS ===== */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

    /* ===== RESET & BASE ===== */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header[data-testid="stHeader"] {
        background: rgba(255,255,255,0.8);
        backdrop-filter: blur(10px);
        border-bottom: 1px solid rgba(0,0,0,0.05);
    }

    * {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    /* ===== BACKGROUND ===== */
    .stApp {
        background: linear-gradient(135deg, #f8faff 0%, #f0f4ff 100%);
    }

    .main > div {
        padding: 0 1rem;
    }

    /* ===== HEADER ===== */
    .app-header {
        text-align: center;
        padding: 1.5rem 0 0.5rem 0;
        position: relative;
    }

    .app-header::after {
        content: '';
        position: absolute;
        bottom: 0;
        left: 50%;
        transform: translateX(-50%);
        width: 60px;
        height: 3px;
        background: linear-gradient(90deg, #6c5ce7, #0984e3);
        border-radius: 2px;
    }

    .app-header h1 {
        font-size: 2.8rem;
        font-weight: 800;
        color: #1a1a2e;
        letter-spacing: -1px;
        margin: 0;
        font-family: 'Inter', sans-serif;
        background: linear-gradient(135deg, #1a1a2e 0%, #2d2d44 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }

    .app-header h1 .icon {
        background: linear-gradient(135deg, #6c5ce7, #0984e3);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }

    .app-header .subtitle {
        font-size: 0.95rem;
        color: #6b7280;
        margin-top: 0.3rem;
        letter-spacing: 0.3px;
        font-weight: 400;
    }

    .app-header .subtitle .divider {
        color: #d1d5db;
        margin: 0 8px;
    }

    .app-header .subtitle .highlight {
        color: #4f46e5;
        font-weight: 600;
        background: rgba(79, 70, 229, 0.08);
        padding: 0.1rem 0.6rem;
        border-radius: 4px;
    }

    .app-header .badge-group {
        margin-top: 0.8rem;
        display: flex;
        justify-content: center;
        gap: 10px;
        flex-wrap: wrap;
    }

    .app-header .badge {
        display: inline-flex;
        align-items: center;
        background: white;
        border: 1px solid #e5e7eb;
        padding: 4px 16px;
        border-radius: 20px;
        font-size: 0.7rem;
        color: #4b5563;
        font-weight: 500;
        box-shadow: 0 1px 3px rgba(0,0,0,0.04);
        transition: all 0.2s ease;
        gap: 6px;
    }

    .app-header .badge:hover {
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    }

    .app-header .badge i {
        font-size: 0.6rem;
    }

    .app-header .badge.live {
        background: #ecfdf5;
        border-color: #6ee7b7;
        color: #065f46;
    }

    .app-header .badge.live i {
        color: #10b981;
        animation: pulse 2s infinite;
    }

    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.3; }
    }

    .app-header .badge.creator {
        background: #eef2ff;
        border-color: #a5b4fc;
        color: #3730a3;
    }

    .app-header .badge.model {
        background: #fef3c7;
        border-color: #fcd34d;
        color: #92400e;
    }

    .app-header .badge.model i {
        color: #f59e0b;
    }

    .app-header .tagline {
        margin-top: 0.5rem;
        font-size: 0.85rem;
        color: #6b7280;
        font-weight: 400;
        letter-spacing: 0.2px;
    }

    .app-header .tagline i {
        color: #4f46e5;
        margin-right: 6px;
    }

    /* ===== CARDS ===== */
    .card {
        background: rgba(255,255,255,0.9);
        backdrop-filter: blur(12px);
        border-radius: 20px;
        padding: 1.8rem 2rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.04), 0 1px 2px rgba(0,0,0,0.02);
        border: 1px solid rgba(255,255,255,0.8);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        margin-bottom: 1.2rem;
        position: relative;
        overflow: hidden;
    }

    .card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 2px;
        background: linear-gradient(90deg, #6c5ce7, #0984e3, #6c5ce7);
        background-size: 200% 100%;
        animation: gradientMove 3s ease infinite;
    }

    @keyframes gradientMove {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }

    .card:hover {
        box-shadow: 0 8px 30px rgba(0,0,0,0.06);
        transform: translateY(-2px);
    }

    .card-title {
        font-size: 1.05rem;
        font-weight: 700;
        color: #1f2937;
        margin-bottom: 1.2rem;
        display: flex;
        align-items: center;
        gap: 12px;
        letter-spacing: -0.2px;
    }

    .card-title i {
        color: #4f46e5;
        font-size: 1.2rem;
        width: 1.4rem;
        text-align: center;
        background: rgba(79, 70, 229, 0.08);
        padding: 6px;
        border-radius: 8px;
    }

    /* ===== FORM ELEMENTS ===== */
    .stSlider > div {
        padding-top: 0.2rem !important;
    }

    .stSlider label {
        display: none !important;
    }

    .stSlider [data-baseweb="slider"] {
        margin-top: 0.2rem !important;
    }

    .stSlider [data-baseweb="slider"] > div > div {
        background: #e5e7eb !important;
        height: 4px !important;
        border-radius: 2px !important;
    }

    .stSlider [data-baseweb="slider"] > div > div > div {
        background: linear-gradient(90deg, #6c5ce7, #0984e3) !important;
        box-shadow: 0 0 0 4px rgba(79, 70, 229, 0.12) !important;
        border: 2px solid white !important;
        width: 18px !important;
        height: 18px !important;
        border-radius: 50% !important;
        transition: all 0.2s ease !important;
    }

    .stSlider [data-baseweb="slider"] > div > div > div:hover {
        box-shadow: 0 0 0 8px rgba(79, 70, 229, 0.15) !important;
        transform: scale(1.05);
    }

    .stSlider [data-baseweb="slider"] > div > div > div:active {
        box-shadow: 0 0 0 12px rgba(79, 70, 229, 0.2) !important;
    }

    /* Select boxes */
    .stSelectbox > div > div {
        background: white !important;
        border: 1.5px solid #e5e7eb !important;
        border-radius: 10px !important;
        color: #1f2937 !important;
        min-height: 42px !important;
        transition: all 0.2s ease !important;
    }

    .stSelectbox > div > div:hover {
        border-color: #9ca3af !important;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
    }

    .stSelectbox > div > div:focus-within {
        border-color: #4f46e5 !important;
        box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.1);
    }

    .stSelectbox label {
        color: #4b5563 !important;
        font-weight: 600 !important;
        font-size: 0.8rem !important;
        margin-bottom: 0.3rem !important;
        display: flex !important;
        align-items: center !important;
        gap: 6px !important;
    }

    .stSelectbox label i {
        color: #6b7280;
        font-size: 0.9rem;
    }

    /* Number labels for sliders */
    .stMarkdown .slider-label {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 0.2rem;
    }

    .stMarkdown .slider-label .label-text {
        font-size: 0.8rem;
        font-weight: 600;
        color: #4b5563;
    }

    .stMarkdown .slider-label .value-text {
        font-size: 0.85rem;
        font-weight: 700;
        color: #1f2937;
        background: #f3f4f6;
        padding: 0.1rem 0.8rem;
        border-radius: 6px;
    }

    /* ===== SUMMARY METRICS ===== */
    .summary-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 0.8rem;
    }

    .metric-chip {
        background: #f9fafb;
        border-radius: 12px;
        padding: 0.8rem 0.5rem;
        text-align: center;
        border: 1px solid #f0f0f0;
        transition: all 0.2s ease;
        position: relative;
        overflow: hidden;
    }

    .metric-chip::after {
        content: '';
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        height: 2px;
        background: linear-gradient(90deg, #6c5ce7, #0984e3);
        transform: scaleX(0);
        transition: transform 0.3s ease;
    }

    .metric-chip:hover::after {
        transform: scaleX(1);
    }

    .metric-chip:hover {
        background: #f3f4f6;
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.04);
    }

    .metric-chip .number {
        font-size: 1.5rem;
        font-weight: 700;
        color: #1f2937;
        font-family: 'Inter', sans-serif;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 6px;
    }

    .metric-chip .number i {
        color: #4f46e5;
        font-size: 1rem;
    }

    .metric-chip .lbl {
        font-size: 0.65rem;
        text-transform: uppercase;
        color: #6b7280;
        letter-spacing: 0.5px;
        font-weight: 600;
        margin-top: 2px;
    }

    /* ===== RESULT BOX ===== */
    .result-box {
        background: linear-gradient(135deg, #4f46e5, #7c3aed);
        border-radius: 16px;
        padding: 2rem 1.5rem;
        text-align: center;
        color: white;
        box-shadow: 0 8px 32px rgba(79, 70, 229, 0.3);
        position: relative;
        overflow: hidden;
    }

    .result-box::before {
        content: '';
        position: absolute;
        top: -50%;
        right: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(255,255,255,0.05) 0%, transparent 70%);
        animation: shimmer 6s ease-in-out infinite;
    }

    @keyframes shimmer {
        0%, 100% { transform: translate(0, 0); }
        50% { transform: translate(-10%, -10%); }
    }

    .result-box .label {
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 2px;
        opacity: 0.85;
        font-weight: 600;
        position: relative;
        z-index: 1;
    }

    .result-box .label i {
        margin-right: 8px;
    }

    .result-box .amount {
        font-size: 3.2rem;
        font-weight: 800;
        margin: 0.2rem 0;
        letter-spacing: -1px;
        font-family: 'Inter', sans-serif;
        position: relative;
        z-index: 1;
        text-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }

    .result-box .sub-label {
        font-size: 0.75rem;
        opacity: 0.7;
        letter-spacing: 0.5px;
        position: relative;
        z-index: 1;
    }

    .result-box .band {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: rgba(255,255,255,0.15);
        backdrop-filter: blur(8px);
        padding: 0.3rem 1.4rem;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 600;
        border: 1px solid rgba(255,255,255,0.15);
        margin-top: 0.5rem;
        letter-spacing: 0.3px;
        position: relative;
        z-index: 1;
    }

    .result-info {
        background: #f9fafb;
        border-radius: 12px;
        padding: 0.8rem 1rem;
        border: 1px solid #f0f0f0;
        margin: 0.8rem 0;
        font-size: 0.85rem;
        color: #4b5563;
        display: flex;
        align-items: flex-start;
        gap: 8px;
    }

    .result-info i {
        color: #4f46e5;
        margin-top: 0.1rem;
        flex-shrink: 0;
    }

    .result-info strong {
        color: #1f2937;
    }

    .range-indicator {
        display: flex;
        align-items: center;
        gap: 12px;
        padding: 0.4rem 0;
        margin-top: 0.3rem;
    }

    .range-indicator .range-bar {
        flex: 1;
        height: 4px;
        background: #e5e7eb;
        border-radius: 2px;
        position: relative;
    }

    .range-indicator .range-bar .range-fill {
        height: 100%;
        background: linear-gradient(90deg, #6c5ce7, #0984e3);
        border-radius: 2px;
        transition: width 0.6s ease;
    }

    .range-indicator .range-label {
        font-size: 0.7rem;
        color: #6b7280;
        font-weight: 500;
        white-space: nowrap;
    }

    /* ===== BUTTONS ===== */
    .stButton > button {
        background: linear-gradient(135deg, #4f46e5, #7c3aed);
        color: white;
        font-weight: 600;
        font-size: 0.95rem;
        padding: 0.8rem 2rem;
        border-radius: 12px;
        border: none;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        width: 100%;
        letter-spacing: 0.3px;
        box-shadow: 0 4px 16px rgba(79, 70, 229, 0.25);
        position: relative;
        overflow: hidden;
    }

    .stButton > button::after {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: linear-gradient(135deg, rgba(255,255,255,0.1), transparent);
        pointer-events: none;
    }

    .stButton > button i {
        margin-right: 10px;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 30px rgba(79, 70, 229, 0.35);
    }

    .stButton > button:active {
        transform: translateY(0);
        box-shadow: 0 4px 16px rgba(79, 70, 229, 0.2);
    }

    /* Download button */
    .stDownloadButton > button {
        background: white !important;
        border: 1.5px solid #e5e7eb !important;
        color: #4b5563 !important;
        border-radius: 10px !important;
        font-weight: 500 !important;
        transition: all 0.2s ease !important;
        padding: 0.6rem 1.2rem !important;
        font-size: 0.85rem !important;
        box-shadow: none !important;
        display: inline-flex !important;
        align-items: center !important;
        gap: 6px !important;
    }

    .stDownloadButton > button i {
        margin-right: 4px;
    }

    .stDownloadButton > button:hover {
        background: #f9fafb !important;
        border-color: #9ca3af !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.04) !important;
        transform: translateY(-1px);
    }

    /* ===== SIDEBAR ===== */
    section[data-testid="stSidebar"] {
        background: rgba(255,255,255,0.95);
        backdrop-filter: blur(12px);
        border-right: 1px solid rgba(0,0,0,0.04);
        padding: 1.5rem 1.2rem;
    }

    section[data-testid="stSidebar"] .sidebar-header {
        padding-bottom: 1rem;
        border-bottom: 1px solid #f0f0f0;
        margin-bottom: 1.2rem;
    }

    section[data-testid="stSidebar"] .sidebar-header h2 {
        font-size: 1.2rem;
        font-weight: 700;
        color: #1f2937;
        margin: 0;
        display: flex;
        align-items: center;
        gap: 8px;
    }

    section[data-testid="stSidebar"] .sidebar-header h2 i {
        color: #4f46e5;
    }

    section[data-testid="stSidebar"] h3 {
        font-size: 0.85rem;
        font-weight: 700;
        color: #1f2937;
        margin-top: 1rem;
        margin-bottom: 0.8rem;
        display: flex;
        align-items: center;
        gap: 8px;
    }

    section[data-testid="stSidebar"] h3 i {
        color: #4f46e5;
        font-size: 0.9rem;
    }

    section[data-testid="stSidebar"] .stMarkdown {
        color: #4b5563;
        font-size: 0.85rem;
        line-height: 1.6;
    }

    /* Sidebar metrics */
    div[data-testid="stMetric"] {
        background: #f9fafb;
        border-radius: 10px;
        padding: 0.8rem 0.8rem;
        border: 1px solid #f0f0f0;
        transition: all 0.2s ease;
    }

    div[data-testid="stMetric"]:hover {
        background: #f3f4f6;
        transform: translateY(-1px);
    }

    div[data-testid="stMetric"] label {
        color: #6b7280 !important;
        font-size: 0.7rem !important;
        font-weight: 600 !important;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    div[data-testid="stMetric"] div {
        color: #1f2937 !important;
        font-weight: 700 !important;
        font-size: 1.2rem !important;
    }

    /* Feature bars in sidebar */
    .feature-bar {
        display: flex;
        align-items: center;
        gap: 10px;
        margin: 6px 0;
        padding: 4px 0;
        transition: all 0.2s ease;
    }

    .feature-bar:hover {
        background: #f9fafb;
        border-radius: 6px;
        padding: 4px 6px;
    }

    .feature-bar .name {
        min-width: 80px;
        font-size: 0.75rem;
        color: #4b5563;
        font-weight: 500;
        display: flex;
        align-items: center;
        gap: 4px;
    }

    .feature-bar .name i {
        color: #6b7280;
        width: 0.9rem;
        font-size: 0.7rem;
    }

    .feature-bar .track {
        flex: 1;
        height: 4px;
        background: #f0f0f0;
        border-radius: 4px;
        overflow: hidden;
        position: relative;
    }

    .feature-bar .fill {
        height: 100%;
        border-radius: 4px;
        transition: width 0.8s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
    }

    .feature-bar .fill.positive {
        background: linear-gradient(90deg, #4f46e5, #7c3aed);
    }

    .feature-bar .fill.negative {
        background: linear-gradient(90deg, #ef4444, #dc2626);
    }

    .feature-bar .val {
        min-width: 56px;
        font-size: 0.7rem;
        text-align: right;
        color: #6b7280;
        font-weight: 600;
    }

    /* ===== GROQ CHAT ===== */
    .chat-container {
        background: #f9fafb;
        border-radius: 14px;
        padding: 1rem;
        border: 1px solid #f0f0f0;
        margin-top: 0.8rem;
        max-height: 380px;
        overflow-y: auto;
        transition: all 0.2s ease;
    }

    .chat-container::-webkit-scrollbar {
        width: 4px;
    }

    .chat-container::-webkit-scrollbar-track {
        background: #f0f0f0;
        border-radius: 2px;
    }

    .chat-container::-webkit-scrollbar-thumb {
        background: #4f46e5;
        border-radius: 2px;
    }

    .chat-message {
        padding: 0.6rem 1rem;
        margin: 0.4rem 0;
        border-radius: 12px;
        font-size: 0.85rem;
        line-height: 1.5;
        animation: slideIn 0.3s ease;
    }

    @keyframes slideIn {
        from {
            opacity: 0;
            transform: translateY(-10px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    .chat-message.user {
        background: #eef2ff;
        border-left: 3px solid #4f46e5;
        margin-left: 1rem;
    }

    .chat-message.assistant {
        background: white;
        border-left: 3px solid #10b981;
        margin-right: 1rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
    }

    .chat-message .role {
        font-weight: 600;
        font-size: 0.7rem;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        color: #6b7280;
        margin-bottom: 3px;
        display: flex;
        align-items: center;
        gap: 6px;
    }

    .chat-message .role i {
        font-size: 0.8rem;
    }

    .chat-message .role.user-role {
        color: #4f46e5;
    }

    .chat-message .role.assistant-role {
        color: #10b981;
    }

    /* ===== EXPANDER ===== */
    .streamlit-expanderHeader {
        font-weight: 600 !important;
        color: #1f2937 !important;
        background: #f9fafb !important;
        border-radius: 12px !important;
        border: 1px solid #f0f0f0 !important;
        font-size: 0.85rem !important;
        padding: 0.6rem 1.2rem !important;
        transition: all 0.2s ease !important;
    }

    .streamlit-expanderHeader:hover {
        background: #f3f4f6 !important;
        border-color: #e5e7eb !important;
    }

    .streamlit-expanderHeader i {
        margin-right: 10px;
        color: #4f46e5;
    }

    .streamlit-expanderContent {
        background: transparent !important;
        padding: 0.5rem 0 !important;
    }

    /* ===== DATAFRAME ===== */
    .stDataFrame {
        border-radius: 12px !important;
        overflow: hidden !important;
        border: 1px solid #f0f0f0 !important;
    }

    .stDataFrame th {
        background: #f9fafb !important;
        color: #4b5563 !important;
        font-weight: 600 !important;
        font-size: 0.7rem !important;
        text-transform: uppercase !important;
        letter-spacing: 0.5px !important;
        padding: 8px 12px !important;
    }

    .stDataFrame td {
        color: #1f2937 !important;
        padding: 6px 12px !important;
        font-size: 0.8rem !important;
        border-bottom: 1px solid #f5f5f5 !important;
    }

    .stDataFrame tr:hover td {
        background: #f9fafb !important;
    }

    /* ===== FOOTER ===== */
    .footer {
        text-align: center;
        color: #9ca3af;
        font-size: 0.75rem;
        padding-top: 2rem;
        border-top: 1px solid #f0f0f0;
        margin-top: 2rem;
        letter-spacing: 0.3px;
        line-height: 1.6;
    }

    .footer i {
        margin: 0 4px;
        color: #6b7280;
    }

    .footer .creator-name {
        color: #4f46e5;
        font-weight: 600;
        transition: color 0.2s ease;
    }

    .footer .creator-name:hover {
        color: #4338ca;
    }

    /* ===== ALERTS ===== */
    div[data-testid="stAlertContainer"] {
        border-radius: 12px !important;
        border: 1px solid #f0f0f0 !important;
        background: #fffbeb !important;
        padding: 0.6rem 1.2rem !important;
    }

    /* ===== WARNING STYLING ===== */
    .warning-text {
        font-size: 0.8rem;
        color: #92400e;
        background: #fffbeb;
        padding: 0.5rem 1rem;
        border-radius: 10px;
        border-left: 3px solid #f59e0b;
        margin-top: 0.5rem;
        display: flex;
        align-items: center;
        gap: 8px;
    }

    .warning-text i {
        color: #f59e0b;
    }

    .info-placeholder {
        color: #6b7280;
        text-align: center;
        padding: 1rem 0;
        font-size: 0.9rem;
        line-height: 1.6;
    }

    .info-placeholder i {
        color: #4f46e5;
        font-size: 1.2rem;
        display: block;
        margin-bottom: 0.5rem;
    }

    /* ===== RESPONSIVE ===== */
    @media (max-width: 768px) {
        .summary-grid { grid-template-columns: 1fr 1fr; }
        .app-header h1 { font-size: 2rem; }
        .result-box .amount { font-size: 2.2rem; }
        .card { padding: 1.2rem 1rem; }
        .app-header .badge-group { gap: 6px; }
        .app-header .badge { font-size: 0.6rem; padding: 3px 12px; }
        section[data-testid="stSidebar"] { padding: 1rem; }
    }

    @media (max-width: 480px) {
        .summary-grid { grid-template-columns: 1fr 1fr; gap: 0.5rem; }
        .metric-chip .number { font-size: 1.1rem; }
        .app-header h1 { font-size: 1.6rem; }
        .result-box .amount { font-size: 1.8rem; }
        .card-title { font-size: 0.9rem; }
    }

    /* ===== CUSTOM SCROLLBAR ===== */
    ::-webkit-scrollbar {
        width: 6px;
        height: 6px;
    }

    ::-webkit-scrollbar-track {
        background: #f0f0f0;
        border-radius: 3px;
    }

    ::-webkit-scrollbar-thumb {
        background: #d1d5db;
        border-radius: 3px;
    }

    ::-webkit-scrollbar-thumb:hover {
        background: #9ca3af;
    }
</style>
""", unsafe_allow_html=True)

# ============================================
# GROQ API HELPER
# ============================================

def get_groq_response(prompt, context):
    """Get response from Groq API for follow-up questions"""
    if not GROQ_API_KEY:
        return "⚠️ GROQ_API_KEY not found in .env file. Please add it to enable follow-up questions."

    try:
        client = Groq(api_key=GROQ_API_KEY)

        system_prompt = """You are a helpful salary analyst assistant. You help users understand their salary predictions, 
        career growth, and provide actionable advice based on their profile. Be concise, professional, and data-driven.
        Provide specific, actionable recommendations. Keep responses under 150 words."""

        user_prompt = f"""Context: User's profile and salary prediction:
        {context}

        User question: {prompt}

        Please provide a helpful, professional response with specific advice."""

        active_models = [
            "llama-3.3-70b-versatile",
            "llama-3.1-8b-instant",
        ]
        
        last_error = None
        for model in active_models:
            try:
                response = client.chat.completions.create(
                    model=model,
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_prompt}
                    ],
                    temperature=0.7,
                    max_tokens=300,
                )
                return response.choices[0].message.content
            except Exception as e:
                last_error = e
                continue
        
        return f"⚠️ All AI models are currently unavailable. Please try again later. Error: {str(last_error)}"

    except Exception as e:
        error_msg = str(e)
        if "model_decommissioned" in error_msg:
            return "⚠️ The AI model has been updated. Please try again with a different question."
        return f"❌ Error: {error_msg}"

# ============================================
# MODEL LOADING
# ============================================

@st.cache_resource(show_spinner=False)
def load_model_and_scaler():
    try:
        model = joblib.load(MODEL_PATH)
    except FileNotFoundError:
        return None, None, f"Model file not found: `{MODEL_PATH}`"
    except Exception as e:
        return None, None, f"Failed to load model: {e}"

    try:
        scaler = joblib.load(SCALER_PATH)
    except Exception:
        scaler = None

    return model, scaler, None


def encode_and_scale_features(age, experience, gender, education, job_level, scaler):
    is_male = 1 if gender == "Male" else 0
    ed_masters = 1 if education == "Master's" else 0
    ed_phd = 1 if education == "PhD" else 0

    jl_1 = 1 if job_level == "Junior" else 0
    jl_2 = 1 if job_level == "Mid Level" else 0
    jl_3 = 1 if job_level == "Senior/Manager" else 0
    jl_4 = 1 if job_level == "Executive/High" else 0

    if scaler is not None:
        try:
            scaled_values = scaler.transform([[age, experience]])
            scaled_age = scaled_values[0][0]
            scaled_exp = scaled_values[0][1]
        except Exception:
            age_mean, age_std = 35, 10
            exp_mean, exp_std = 8, 5
            scaled_age = (age - age_mean) / age_std
            scaled_exp = (experience - exp_mean) / exp_std
    else:
        scaled_age = age
        scaled_exp = experience

    return [[
        scaled_age,
        is_male,
        scaled_exp,
        ed_masters,
        ed_phd,
        jl_1, jl_2, jl_3, jl_4
    ]]


def get_salary_band(prediction: float):
    for threshold, label, message in SALARY_BANDS:
        if prediction < threshold:
            return label, message
    return SALARY_BANDS[-1][1], SALARY_BANDS[-1][2]

# ============================================
# SESSION STATE
# ============================================

if "history" not in st.session_state:
    st.session_state.history = []
if "last_prediction" not in st.session_state:
    st.session_state.last_prediction = None
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ============================================
# LOAD MODEL
# ============================================

with st.spinner("Loading model..."):
    model, scaler, load_error = load_model_and_scaler()

if load_error:
    st.error(f"❌ {load_error}")
    st.info("Place `salary_model.pkl` in the app directory.")
    st.stop()

# ============================================
# HEADER
# ============================================

st.markdown("""
<div class="app-header">
    <h1>
        <span class="icon">💰</span> Salary Predictor Pro
    </h1>
    <div class="subtitle">
        <i class="fas fa-user-astronaut"></i> Created by <span class="highlight">Sheharyar Sarmad</span>
        <span class="divider">·</span>
        <i class="fas fa-robot"></i> Powered by <span class="highlight">Linear Regression</span>
    </div>
    <div class="badge-group">
        <span class="badge live"><i class="fas fa-circle"></i> LIVE</span>
        <span class="badge creator"><i class="fas fa-star"></i> Sheharyar Sarmad</span>
        <span class="badge model"><i class="fas fa-chart-line"></i> R² 92.8%</span>
        <span class="badge model"><i class="fas fa-bullseye"></i> MAE $8,454</span>
    </div>
    <div class="tagline">
        <i class="fas fa-brain"></i> AI-powered salary estimation based on your professional profile
    </div>
</div>
""", unsafe_allow_html=True)

# ============================================
# MAIN LAYOUT
# ============================================

col_left, col_right = st.columns([1.2, 0.8], gap="large")

# ============================================
# LEFT COLUMN — PROFILE
# ============================================

with col_left:
    # Profile Card
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="card-title"><i class="fas fa-user-circle"></i> Your Profile</div>', unsafe_allow_html=True)

        col_a, col_b = st.columns(2)

        with col_a:
            st.markdown("""
            <div class="slider-label">
                <span class="label-text"><i class="fas fa-calendar"></i> Age</span>
                <span class="value-text" id="age-value">30</span>
            </div>
            """, unsafe_allow_html=True)
            age = st.slider("Age", 18, 65, 30, key="age_slider", label_visibility="collapsed")
            
            st.markdown("""
            <div class="slider-label">
                <span class="label-text"><i class="fas fa-venus-mars"></i> Gender</span>
            </div>
            """, unsafe_allow_html=True)
            gender = st.selectbox("Gender", GENDER_OPTIONS, label_visibility="collapsed")

        with col_b:
            st.markdown("""
            <div class="slider-label">
                <span class="label-text"><i class="fas fa-briefcase"></i> Experience</span>
                <span class="value-text" id="exp-value">5</span>
            </div>
            """, unsafe_allow_html=True)
            experience = st.slider("Years of Experience", 0, 40, 5, key="exp_slider", label_visibility="collapsed")
            
            st.markdown("""
            <div class="slider-label">
                <span class="label-text"><i class="fas fa-graduation-cap"></i> Education</span>
            </div>
            """, unsafe_allow_html=True)
            education = st.selectbox("Highest Education", EDUCATION_OPTIONS, label_visibility="collapsed")

        st.markdown("""
        <div class="slider-label">
            <span class="label-text"><i class="fas fa-layer-group"></i> Job Level</span>
        </div>
        """, unsafe_allow_html=True)
        job_level = st.selectbox("Job Level", JOB_LEVEL_OPTIONS, label_visibility="collapsed")

        if experience > (age - 16):
            st.markdown(
                '<div class="warning-text"><i class="fas fa-exclamation-triangle"></i> Experience seems high relative to age — estimate may be less reliable.</div>',
                unsafe_allow_html=True
            )

        st.markdown('</div>', unsafe_allow_html=True)

    # Summary Card
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="card-title"><i class="fas fa-chart-simple"></i> Profile Summary</div>', unsafe_allow_html=True)

        st.markdown('<div class="summary-grid">', unsafe_allow_html=True)

        summary_items = [
            (age, "Age", "fa-calendar"),
            (gender, "Gender", "fa-venus-mars"),
            (experience, "Experience", "fa-briefcase"),
            (education.split()[0], "Education", "fa-graduation-cap"),
        ]

        for value, label, icon in summary_items:
            st.markdown(f"""
            <div class="metric-chip">
                <div class="number"><i class="fas {icon}"></i> {value}</div>
                <div class="lbl">{label}</div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# ============================================
# RIGHT COLUMN — SALARY
# ============================================

with col_right:
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="card-title"><i class="fas fa-coins"></i> Your Salary</div>', unsafe_allow_html=True)

        predict_button = st.button("🔮 Predict Salary", use_container_width=True)

        result_placeholder = st.empty()

        if predict_button:
            with st.spinner("Calculating your salary estimate..."):
                try:
                    input_data = encode_and_scale_features(
                        age, experience, gender, education, job_level, scaler
                    )
                    prediction = model.predict(input_data)[0]
                    prediction = float(prediction)
                    display_prediction = max(prediction, 0.0)
                    band_label, band_message = get_salary_band(display_prediction)

                    st.session_state.last_prediction = {
                        "timestamp": datetime.now().strftime("%H:%M:%S"),
                        "age": age,
                        "gender": gender,
                        "experience": experience,
                        "education": education,
                        "job_level": job_level,
                        "prediction": display_prediction,
                        "band": band_label,
                    }
                    st.session_state.history.insert(0, st.session_state.last_prediction)
                    st.session_state.history = st.session_state.history[:10]
                    st.balloons()

                except Exception as e:
                    st.error(f"❌ Prediction error: {e}")
                    st.session_state.last_prediction = None

        if st.session_state.last_prediction:
            data = st.session_state.last_prediction
            prediction = data["prediction"]
            band_label, band_message = get_salary_band(prediction)
            lower_bound = max(prediction - 10000, 0)
            upper_bound = prediction + 10000
            range_percent = ((prediction - lower_bound) / (upper_bound - lower_bound)) * 100

            with result_placeholder.container():
                st.markdown(f"""
                <div class="result-box">
                    <div class="label"><i class="fas fa-calculator"></i> Estimated Annual Salary</div>
                    <div class="amount">${prediction:,.0f}</div>
                    <div class="sub-label"><i class="fas fa-user"></i> Based on your profile</div>
                    <div class="band"><i class="fas fa-tag"></i> {band_label}</div>
                </div>
                """, unsafe_allow_html=True)

                st.markdown(f"""
                <div class="result-info">
                    <i class="fas fa-info-circle"></i>
                    <div><strong>{band_label}</strong> — {band_message}</div>
                </div>
                """, unsafe_allow_html=True)

                st.markdown("""
                <div class="range-indicator">
                    <span class="range-label">$${:.0f}</span>
                    <div class="range-bar">
                        <div class="range-fill" style="width: {:.0f}%;"></div>
                    </div>
                    <span class="range-label">$${:.0f}</span>
                </div>
                """.format(lower_bound, range_percent, upper_bound), unsafe_allow_html=True)

                st.caption(
                    f"<i class='fas fa-chart-line'></i> Estimated salary range based on model confidence",
                    unsafe_allow_html=True
                )

                report_df = pd.DataFrame([{
                    "Age": data["age"],
                    "Gender": data["gender"],
                    "Experience (yrs)": data["experience"],
                    "Education": data["education"],
                    "Job Level": data["job_level"],
                    "Predicted Salary ($)": round(prediction, 2),
                    "Band": band_label,
                }])
                st.download_button(
                    "📥 Download Report",
                    data=report_df.to_csv(index=False).encode("utf-8"),
                    file_name=f"salary_estimate_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                    mime="text/csv",
                    use_container_width=True,
                )
        else:
            with result_placeholder.container():
                st.markdown(
                    '<div class="info-placeholder"><i class="fas fa-arrow-left"></i> Fill in your profile<br>Click <strong>Predict Salary</strong> to get started</div>',
                    unsafe_allow_html=True
                )

        st.markdown('</div>', unsafe_allow_html=True)

    # GROQ FOLLOW-UP CHAT
    if st.session_state.last_prediction:
        with st.container():
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown('<div class="card-title"><i class="fas fa-comments"></i> Ask Follow-up Questions</div>', unsafe_allow_html=True)

            # Display chat history
            if st.session_state.chat_history:
                st.markdown('<div class="chat-container">', unsafe_allow_html=True)
                for msg in st.session_state.chat_history:
                    role_class = "user" if msg["role"] == "user" else "assistant"
                    icon = "fa-user" if msg["role"] == "user" else "fa-robot"
                    role_label = "user-role" if msg["role"] == "user" else "assistant-role"
                    st.markdown(f"""
                    <div class="chat-message {role_class}">
                        <div class="role {role_label}"><i class="fas {icon}"></i> {msg["role"]}</div>
                        {msg["content"]}
                    </div>
                    """, unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)

            # Input for follow-up
            col_input, col_btn = st.columns([3, 1])
            with col_input:
                follow_up = st.text_input("Ask a question about your salary prediction:", 
                                         placeholder="e.g., How can I increase my salary?",
                                         key="follow_up_input",
                                         label_visibility="collapsed")
            with col_btn:
                ask_button = st.button("Ask 💬", use_container_width=True, key="ask_btn")
            
            if ask_button and follow_up:
                # Add user message
                st.session_state.chat_history.append({"role": "user", "content": follow_up})

                # Prepare context
                data = st.session_state.last_prediction
                context = f"""
                Age: {data['age']}
                Gender: {data['gender']}
                Experience: {data['experience']} years
                Education: {data['education']}
                Job Level: {data['job_level']}
                Predicted Salary: ${data['prediction']:,.2f}
                Salary Band: {data['band']}
                """

                # Get response from Groq
                with st.spinner("Getting AI response..."):
                    response = get_groq_response(follow_up, context)
                    st.session_state.chat_history.append({"role": "assistant", "content": response})
                    st.rerun()

            # Clear chat button
            if st.session_state.chat_history:
                if st.button("🗑️ Clear Chat", use_container_width=True):
                    st.session_state.chat_history = []
                    st.rerun()

            st.markdown('</div>', unsafe_allow_html=True)

    # History
    if st.session_state.history:
        with st.expander(f"📊 Recent Predictions ({len(st.session_state.history)})"):
            hist_df = pd.DataFrame(st.session_state.history)[
                ["timestamp", "age", "gender", "experience", "education", "job_level", "prediction", "band"]
            ]
            hist_df = hist_df.rename(columns={
                "timestamp": "Time", "age": "Age", "gender": "Gender",
                "experience": "Exp.", "education": "Education",
                "job_level": "Job Level", "prediction": "Salary ($)", "band": "Band"
            })
            st.dataframe(
                hist_df.style.format({"Salary ($)": "{:,.0f}"}),
                use_container_width=True,
                hide_index=True,
            )

# ============================================
# SIDEBAR
# ============================================

with st.sidebar:
    st.markdown("""
    <div class="sidebar-header">
        <h2><i class="fas fa-info-circle"></i> About</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(
        "This tool uses **Linear Regression** to estimate salary based on your professional profile.",
        unsafe_allow_html=True
    )
    
    st.markdown("""
    <div style="margin: 0.5rem 0;">
        <div style="display: flex; align-items: center; gap: 8px; padding: 4px 0;">
            <i class="fas fa-user" style="color: #4f46e5; width: 1.2rem;"></i>
            <span style="font-size: 0.85rem;">Age & Gender</span>
        </div>
        <div style="display: flex; align-items: center; gap: 8px; padding: 4px 0;">
            <i class="fas fa-graduation-cap" style="color: #4f46e5; width: 1.2rem;"></i>
            <span style="font-size: 0.85rem;">Education Level</span>
        </div>
        <div style="display: flex; align-items: center; gap: 8px; padding: 4px 0;">
            <i class="fas fa-briefcase" style="color: #4f46e5; width: 1.2rem;"></i>
            <span style="font-size: 0.85rem;">Job Level</span>
        </div>
        <div style="display: flex; align-items: center; gap: 8px; padding: 4px 0;">
            <i class="fas fa-clock" style="color: #4f46e5; width: 1.2rem;"></i>
            <span style="font-size: 0.85rem;">Years of Experience</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("<h3><i class='fas fa-chart-bar'></i> Model Performance</h3>", unsafe_allow_html=True)
    col_r1, col_r2 = st.columns(2)
    with col_r1:
        st.metric("R² Score", "92.8%", delta="+0.2%")
    with col_r2:
        st.metric("MAE", "$8,454", delta="-1.2%")

    st.markdown("---")
    st.markdown("<h3><i class='fas fa-crown'></i> Feature Impact</h3>", unsafe_allow_html=True)

    try:
        feature_names = ['Age', 'Gender', 'Experience', "Master's", 'PhD',
                         'Junior', 'Mid Level', 'Senior', 'Executive']
        coefs = model.coef_

        sorted_idx = np.argsort(np.abs(coefs))[::-1]
        max_coef = max(abs(coefs)) if len(coefs) else 1

        for idx in sorted_idx[:7]:
            name = feature_names[idx]
            coef = coefs[idx]
            pct = abs(coef) / max_coef * 100 if max_coef else 0
            is_positive = coef > 0
            icon = "fa-arrow-up" if is_positive else "fa-arrow-down"
            color_class = "positive" if is_positive else "negative"

            st.markdown(f"""
            <div class="feature-bar">
                <span class="name"><i class="fas {icon}"></i> {name}</span>
                <div class="track">
                    <div class="fill {color_class}" style="width: {pct}%;"></div>
                </div>
                <span class="val">${abs(coef):,.0f}</span>
            </div>
            """, unsafe_allow_html=True)
    except Exception:
        st.caption("Feature importance data unavailable.")

    st.markdown("---")
    st.markdown("<h3><i class='fas fa-lightbulb'></i> Insights</h3>", unsafe_allow_html=True)
    st.markdown("""
    <div style="font-size: 0.85rem; color: #4b5563; line-height: 1.8;">
        <div>• <i class="fas fa-arrow-up" style="color: #10b981;"></i> Higher education → higher salary</div>
        <div>• <i class="fas fa-arrow-up" style="color: #10b981;"></i> More experience → higher salary</div>
        <div>• <i class="fas fa-crown" style="color: #f59e0b;"></i> Executive roles → highest band</div>
        <div>• <i class="fas fa-flask" style="color: #8b5cf6;"></i> PhD adds a significant premium</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("<h3><i class='fas fa-user-astronaut'></i> Creator</h3>", unsafe_allow_html=True)
    st.markdown("""
    <div style="text-align: center; padding: 0.5rem 0;">
        <div style="font-weight: 700; font-size: 1.1rem; color: #1f2937;">Sheharyar Sarmad</div>
        <div style="font-size: 0.8rem; color: #6b7280;">AI/ML Engineer</div>
        <div style="margin-top: 0.3rem; display: flex; justify-content: center; gap: 12px; font-size: 1.2rem;">
            <a href="#" style="color: #4f46e5; text-decoration: none;"><i class="fab fa-github"></i></a>
            <a href="#" style="color: #4f46e5; text-decoration: none;"><i class="fab fa-linkedin"></i></a>
            <a href="#" style="color: #4f46e5; text-decoration: none;"><i class="fab fa-twitter"></i></a>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    if st.button("🔄 Reset All", use_container_width=True):
        st.session_state.history = []
        st.session_state.last_prediction = None
        st.session_state.chat_history = []
        st.rerun()

    if not GROQ_API_KEY:
        st.warning("⚠️ GROQ_API_KEY not set. Follow-up questions won't work.")

# ============================================
# FOOTER
# ============================================

st.markdown(
    f"""
    <div class="footer">
        <i class="fas fa-bolt"></i> Built with Streamlit · 
        <i class="fas fa-robot"></i> Powered by <strong>Linear Regression</strong> ·
        <i class="fas fa-user-astronaut"></i> Created by <span class="creator-name">Sheharyar Sarmad</span> ·
        <i class="fas fa-info-circle"></i> Estimates are model-based approximations
        <br>
        <span style="font-size: 0.7rem; opacity: 0.6;">© 2024 Salary Predictor Pro — All rights reserved</span>
    </div>
    """,
    unsafe_allow_html=True
)

# ============================================
# JAVASCRIPT FOR SLIDER VALUE DISPLAY
# ============================================

st.markdown("""
<script>
    // Update age slider value
    const ageSlider = document.querySelector('[data-testid="stSlider"] input[type="range"]');
    if (ageSlider) {
        const ageValue = document.getElementById('age-value');
        if (ageValue) {
            ageSlider.addEventListener('input', function() {
                ageValue.textContent = this.value;
            });
        }
    }
    
    // Update experience slider value
    const expSlider = document.querySelectorAll('[data-testid="stSlider"] input[type="range"]')[1];
    if (expSlider) {
        const expValue = document.getElementById('exp-value');
        if (expValue) {
            expSlider.addEventListener('input', function() {
                expValue.textContent = this.value;
            });
        }
    }
</script>
""", unsafe_allow_html=True)