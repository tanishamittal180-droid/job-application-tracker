import streamlit as st

def load_theme():

    dark = st.sidebar.toggle("🌙 Dark Mode", value=True)

    if dark:

        st.markdown("""
        <style>

        .stApp {
            background-color: #0f172a;
            color: #e5e7eb;
        }

        section[data-testid="stSidebar"] {
            background-color: #111827;
        }

        section[data-testid="stSidebar"] * {
            color: #e5e7eb !important;
        }

        /* Fix ALL text visibility */
        h1, h2, h3, h4, p, span, label {
            color: #e5e7eb !important;
        }

        /* Metric cards */
        div[data-testid="stMetric"] {
            background-color: #1f2937;
            border-radius: 12px;
            padding: 12px;
            color: white !important;
            box-shadow: 0px 4px 12px rgba(0,0,0,0.4);
        }

        /* Dataframe fix */
        table {
            color: black !important;
            background-color: white;
            border-radius: 10px;
        }

        /* Job cards */
        .card {
            background-color: #1e293b;
            padding: 15px;
            border-radius: 12px;
            margin-bottom: 10px;
            border: 1px solid #334155;
            color: #e5e7eb;
        }

        /* Buttons */
        button {
            border-radius: 8px !important;
        }

        </style>
        """, unsafe_allow_html=True)

    else:

        st.markdown("""
        <style>

        .stApp {
            background-color: #f8fafc;
            color: #0f172a;
        }

        h1, h2, h3, h4, p, span, label {
            color: #0f172a !important;
        }

        .card {
            background-color: white;
            padding: 15px;
            border-radius: 12px;
            margin-bottom: 10px;
            box-shadow: 0px 2px 10px rgba(0,0,0,0.08);
            color: #0f172a;
        }

        div[data-testid="stMetric"] {
            background-color: white;
            border-radius: 12px;
            padding: 12px;
            box-shadow: 0px 2px 10px rgba(0,0,0,0.1);
        }

        table {
            color: black !important;
        }

        </style>
        """, unsafe_allow_html=True)