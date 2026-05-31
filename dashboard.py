import streamlit as st
import pandas as pd

def show_dashboard(df):

    st.subheader("👤 Your Job Profile")

    col1,col2,col3,col4 = st.columns(4)

    col1.metric("Total Jobs", len(df))
    col2.metric("Interviews", len(df[df["status"]=="Interview"]))
    col3.metric("Offers", len(df[df["status"]=="Offer"]))
    col4.metric("Rejections", len(df[df["status"]=="Rejected"]))

    st.markdown("---")

    st.subheader("💼 Job Cards (LinkedIn Style)")

    for i,row in df.tail(6).iterrows():

        with st.container():

            st.markdown(f"""
            ### 🏢 {row['company']}
            **Role:** {row['role']}  
            **Status:** {row['status']}  
            **Location:** {row['location']}  
            """)
            st.progress(min(100, i*10+20))

            st.markdown("---")