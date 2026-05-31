import streamlit as st
import pandas as pd

from auth import register, login
from crud import add_app, get_apps, update_status
from ui import apply_ui
from utils import init_session

# ---------------- UI ----------------
apply_ui()
init_session()

st.set_page_config(page_title="Job Tracker Pro", layout="wide")

# ---------------- SESSION ----------------
if "user" not in st.session_state:
    st.session_state.user = None

# =================================================
# 🏠 HOME PAGE (LOGIN / REGISTER)
# =================================================
if not st.session_state.user:

    st.title("🚀 Job Application Tracker")

    col1, col2 = st.columns(2)

    # ---------------- LOGIN ----------------
    with col1:
        st.subheader("🔐 Login")

        email = st.text_input("Email", key="login_email")
        password = st.text_input("Password", type="password", key="login_pass")

        if st.button("Login"):

            user = login(email, password)

            if user:
                st.session_state.user = user[2]  # email column
                st.success("Login successful 🚀")
                st.rerun()
            else:
                st.error("Invalid email or password")

    # ---------------- REGISTER ----------------
    with col2:
        st.subheader("🆕 Register")

        name = st.text_input("Name", key="reg_name")
        email_r = st.text_input("Email", key="reg_email")
        password_r = st.text_input("Password", type="password", key="reg_pass")

        if st.button("Register"):

            if register(name, email_r, password_r):
                st.success("Account created 🚀")
            else:
                st.error("User already exists")

# =================================================
# 🚀 MAIN APP (AFTER LOGIN)
# =================================================
else:

    st.sidebar.success(f"Logged in: {st.session_state.user}")

    menu = st.sidebar.radio(
        "Navigation",
        ["Dashboard", "Add Job", "Applications", "Kanban Board", "Logout"]
    )

    # ---------------- LOGOUT ----------------
    if menu == "Logout":
        st.session_state.user = None
        st.rerun()

    # =================================================
    # 📊 DASHBOARD
    # =================================================
    elif menu == "Dashboard":

        data = get_apps(st.session_state.user)

        if data:

            df = pd.DataFrame(data, columns=[
                "id","user","company","role","status",
                "location","salary","apply","interview",
                "resume","cover","notes","keywords"
            ])

            st.title("📊 Dashboard")

            col1, col2, col3, col4 = st.columns(4)

            col1.metric("Total", len(df))
            col2.metric("Interview", len(df[df["status"]=="Interview"]))
            col3.metric("Offer", len(df[df["status"]=="Offer"]))
            col4.metric("Rejected", len(df[df["status"]=="Rejected"]))

            st.markdown("---")

            st.subheader("💼 Recent Applications")

            for _, row in df.tail(5).iterrows():

                st.markdown(f"""
                <div style="
                    background:#ffffff;
                    padding:15px;
                    border-radius:12px;
                    margin-bottom:10px;
                    border:1px solid #e5e7eb;
                ">
                    <h4>🏢 {row['company']}</h4>
                    <p><b>Role:</b> {row['role']}</p>
                    <p><b>Status:</b> {row['status']}</p>
                    <p><b>Location:</b> {row['location']}</p>
                </div>
                """, unsafe_allow_html=True)

        else:
            st.info("No applications yet")

    # =================================================
    # ➕ ADD JOB (FIXED 12 VALUES ONLY)
    # =================================================
    elif menu == "Add Job":

        st.title("➕ Add Job Application")

        company = st.text_input("Company")
        role = st.text_input("Role")

        status = st.selectbox(
            "Status",
            ["Saved","Applied","Interview","Offer","Rejected"]
        )

        location = st.text_input("Location")

        if st.button("Save Job"):

            add_app((
                st.session_state.user,
                company,
                role,
                status,
                location,
                "N/A",   # salary
                "N/A",   # apply
                "N/A",   # interview
                "N/A",   # resume
                "N/A",   # cover
                "N/A",   # notes
                "N/A"    # keywords
            ))

            st.success("Job added successfully 🚀")

    # =================================================
    # 📋 APPLICATIONS
    # =================================================
    elif menu == "Applications":

        data = get_apps(st.session_state.user)

        df = pd.DataFrame(data, columns=[
            "id","user","company","role","status",
            "location","salary","apply","interview",
            "resume","cover","notes","keywords"
        ])

        st.title("📋 All Applications")

        st.dataframe(df, use_container_width=True)

    # =================================================
    # 📌 KANBAN BOARD
    elif menu == "Kanban Board":
    
        data = get_apps(st.session_state.user)

    df = pd.DataFrame(data, columns=[
        "id","user","company","role","status",
        "location","salary","apply","interview",
        "resume","cover","notes","keywords"
    ])

    st.title("📌 Kanban Board")

    stages = ["Saved","Applied","Interview","Offer","Rejected"]

    cols = st.columns(5)

    for i, stage in enumerate(stages):

        with cols[i]:

            st.subheader(stage)

            filtered = df[df["status"] == stage]

            for _, row in filtered.iterrows():

                company = row['company']

                # 👉 AUTO IMAGE (no backend change needed)
                img_url = f"https://ui-avatars.com/api/?name={company}&background=random&color=fff&size=128"

                st.markdown(f"""
                <div style="
                    background:#ffffff;
                    padding:12px;
                    border-radius:12px;
                    margin-bottom:10px;
                    border:1px solid #e5e7eb;
                    text-align:center;
                ">

                    <img src="{img_url}" width="50" style="border-radius:50%;"><br>

                    <b>{company}</b><br>
                    <small>{row['role']}</small>

                </div>
                """, unsafe_allow_html=True)

                if stage != "Rejected":

                    if st.button("➡ Move", key=row["id"]):

                        next_stage = stages[min(i+1, len(stages)-1)]
                        update_status(row["id"], next_stage)
                        st.rerun()