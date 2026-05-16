import pandas as pd
import json

def load_icp():
    with open("icp_profile.json", "r") as f:
        return json.load(f)


def score_lead(row, icp):
    score = 0
    text = str(row["title"]).lower()

    for signal in icp["signals"]:
        if signal in text:
            score += 20

    for role in icp["target_roles"]:
        if role.lower() in text:
            score += 30

    return score


def run_engine(input_file, output_file):
    icp = load_icp()
    df = pd.read_csv(input_file)

    df["score"] = df.apply(lambda row: score_lead(row, icp), axis=1)

    df["priority"] = df["score"].apply(
        lambda x: "High" if x >= 60 else "Medium" if x >= 30 else "Low"
    )

    df.to_csv(output_file, index=False)

    print("Intelligence engine complete.")