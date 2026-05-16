import pandas as pd

def generate_report():
    df = pd.read_csv("data/scored/enriched_leads.csv")

    high = df[df["priority"] == "High"]

    report = high[[
        "company",
        "title",
        "score",
        "ai_insight",
        "outreach_recommendation"
    ]]

    report.to_csv("reports/FINAL_CLIENT_SPRINT_REPORT.csv", index=False)

    print("Client Sprint Report generated.")


if __name__ == "__main__":
    generate_report()