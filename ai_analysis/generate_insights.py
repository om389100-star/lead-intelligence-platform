import pandas as pd
import os

INPUT_FILE = "data/scored/scored_leads.csv"
OUTPUT_FILE = "data/scored/enriched_leads.csv"


def generate_insight(title, score):
    if score >= 60:
        return "High likelihood of active data infrastructure scaling. Strong consulting opportunity."

    elif score >= 30:
        return "Moderate technical hiring activity. Worth monitoring for engagement."

    return "Low urgency signal."


df = pd.read_csv(INPUT_FILE)

df["ai_insight"] = df.apply(
    lambda row: generate_insight(row["title"], row["score"]),
    axis=1
)

df.to_csv(OUTPUT_FILE, index=False)

print("AI insights generated.")
print(df.head())