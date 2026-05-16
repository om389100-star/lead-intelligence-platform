import streamlit as st
import requests

API_URL = st.text_input("Backend URL", "http://127.0.0.1:8000")

st.title("Lead Intelligence SaaS")

if st.button("Run Lead Sprint"):
    res = requests.post(f"{API_URL}/run-sprint")
    st.success(res.json()["message"])