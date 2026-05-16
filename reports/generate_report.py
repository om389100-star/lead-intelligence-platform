import pandas as pd

INPUT_FILE = "data/scored/enriched_leads.csv"
OUTPUT_FILE = "reports/client_report.csv"

df = pd.read_csv(INPUT_FILE)

high_priority = df[df["priority"] == "High"]

report = high_priority[[
    "company",
    "title",
    "score",
    "ai_insight"
]]

report.to_csv(OUTPUT_FILE, index=False)

print(f"Client report generated: {OUTPUT_FILE}")
print(report.head(10))