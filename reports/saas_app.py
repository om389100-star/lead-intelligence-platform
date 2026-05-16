import streamlit as st
import requests

st.title("Lead Intelligence SaaS")
st.write("Generate high-intent B2B leads in minutes")

API_URL = "https://your-api.onrender.com"

if st.button("Run Lead Sprint"):
    try:
        res = requests.post(f"{API_URL}/run-sprint", timeout=30)
        data = res.json()

        st.success(data.get("message", "Sprint completed"))
        st.write(data)

    except requests.exceptions.RequestException as e:
        st.error("Backend not reachable")
        st.write(str(e))