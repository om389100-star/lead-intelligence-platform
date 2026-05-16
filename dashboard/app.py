import streamlit as st
import pandas as pd

st.set_page_config(page_title="Lead Intelligence Dashboard")

df = pd.read_csv("data/scored/enriched_leads.csv")

st.title("AI-Powered Lead Intelligence Platform")

st.subheader("Lead Overview")

col1, col2, col3 = st.columns(3)

col1.metric("Total Leads", len(df))
col2.metric("High Priority", len(df[df["priority"] == "High"]))
col3.metric("Medium Priority", len(df[df["priority"] == "Medium"]))

st.subheader("Filter Leads")

priority_filter = st.selectbox(
    "Select Priority",
    ["All", "High", "Medium", "Low"]
)

if priority_filter != "All":
    filtered_df = df[df["priority"] == priority_filter]
else:
    filtered_df = df

st.dataframe(filtered_df)

st.subheader("Top Leads")

top_leads = df.sort_values(by="score", ascending=False)

st.table(top_leads.head(10))