import pandas as pd
import os
import glob

RAW_DIR = "data/raw"
SCORED_DIR = "data/scored"

os.makedirs(SCORED_DIR, exist_ok=True)


def score_job(title):
    score = 0
    title_lower = str(title).lower()

    if "data engineer" in title_lower:
        score += 40

    if "senior" in title_lower:
        score += 20

    if "cloud" in title_lower:
        score += 20

    if "spark" in title_lower:
        score += 10

    if "architect" in title_lower:
        score += 25

    return score


files = glob.glob(f"{RAW_DIR}/*.csv")

latest_file = max(files, key=os.path.getctime)

df = pd.read_csv(latest_file)

df["score"] = df["title"].apply(score_job)


def classify(score):
    if score >= 60:
        return "High"
    elif score >= 30:
        return "Medium"
    return "Low"


df["priority"] = df["score"].apply(classify)

output_file = f"{SCORED_DIR}/scored_leads.csv"

df.to_csv(output_file, index=False)

print(f"Scored leads saved to {output_file}")
print(df.head(10))