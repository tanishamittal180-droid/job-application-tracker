import streamlit as st

def apply_ui():

    st.markdown("""
    <style>

    /* ===== BACKGROUND IMAGE ===== */
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1521737604893-d14cc237f11d");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    /* ===== MAIN CONTAINER (GLASS EFFECT) ===== */
    .block-container {
        background: rgba(255, 255, 255, 0.92);
        padding: 2rem;
        border-radius: 15px;
        margin-top: 20px;
        margin-bottom: 20px;
    }

    /* ===== TEXT FIX ===== */
    h1, h2, h3, h4, p, span, label {
        color: #111827 !important;
    }

    /* ===== CARDS ===== */
    .card {
        background: rgba(255, 255, 255, 0.95);
        border: 1px solid #e5e7eb;
        padding: 16px;
        border-radius: 12px;
        margin-bottom: 10px;
        box-shadow: 0px 2px 10px rgba(0,0,0,0.08);
    }

    /* ===== SIDEBAR ===== */
    section[data-testid="stSidebar"] {
        background-color: rgba(17, 24, 39, 0.95);
    }

    section[data-testid="stSidebar"] * {
        color: white !important;
    }

    /* ===== BUTTONS ===== */
    button {
        border-radius: 8px !important;
    }

    </style>
    """, unsafe_allow_html=True)