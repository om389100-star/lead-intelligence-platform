import pandas as pd

INPUT_FILE = "data/scored/scored_leads.csv"
OUTPUT_FILE = "data/scored/enriched_leads.csv"


def generate_insight(title, score):
    title_lower = str(title).lower()

    if score >= 80:
        return "Strong consulting opportunity: likely scaling critical data infrastructure."

    elif score >= 50:
        return "Moderate opportunity: technical growth suggests possible modernization needs."

    return "Low urgency signal."


def generate_outreach(title, score):
    if score >= 80:
        return "Position distributed data platform optimization and cloud cost reduction."

    elif score >= 50:
        return "Offer infrastructure assessment and analytics pipeline review."

    return "Monitor for stronger future intent signals."


df = pd.read_csv(INPUT_FILE)

df["ai_insight"] = df.apply(
    lambda row: generate_insight(row["title"], row["score"]),
    axis=1
)

df["outreach_recommendation"] = df.apply(
    lambda row: generate_outreach(row["title"], row["score"]),
    axis=1
)

df.to_csv(OUTPUT_FILE, index=False)

print("Insights + outreach recommendations generated.")
print(df.head())