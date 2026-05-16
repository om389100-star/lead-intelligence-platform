import streamlit as st
import requests

API_URL = st.text_input(
    "Backend URL",
    "http://127.0.0.1:8000"
)

st.title("Lead Intelligence SaaS")

st.write("Generate high-intent B2B leads in minutes")

if st.button("Run Lead Sprint"):
    try:
        res = requests.post(f"{API_URL}/run-sprint")

        if res.status_code == 200:
            st.success(res.json()["message"])
        else:
            st.error(f"Backend error: {res.text}")

    except Exception as e:
        st.error(f"Connection failed: {e}")