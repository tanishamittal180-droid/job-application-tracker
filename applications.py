import streamlit as st

def show_applications(df, delete_app, update_status):

    st.title("📋 Applications")

    # ================= TABLE =================
    st.dataframe(df, use_container_width=True, height=350)

    st.markdown("---")

    # ================= ACTION PANEL =================
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("❌ Delete Application")
        del_id = st.number_input("Enter ID", min_value=1)

        if st.button("Delete"):
            delete_app(del_id)
            st.success("Deleted")

    with col2:
        st.subheader("🔄 Update Status")

        up_id = st.number_input("Enter ID ", min_value=1)
        new_status = st.selectbox(
            "Status",
            ["Saved","Applied","Interview","Offer","Rejected"]
        )

        if st.button("Update"):
            update_status(up_id, new_status)
            st.success("Updated")