import requests
import pandas as pd
import os
from datetime import datetime

OUTPUT_DIR = "data/raw"
os.makedirs(OUTPUT_DIR, exist_ok=True)

url = "https://remoteok.com/api"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

jobs = response.json()

filtered_jobs = []

for job in jobs[1:]:
    position = str(job.get("position", "")).lower()

    if any(keyword in position for keyword in [
        "data engineer",
        "machine learning",
        "data platform",
        "cloud"
    ]):
        filtered_jobs.append({
            "company": job.get("company"),
            "title": job.get("position"),
            "location": job.get("location"),
            "scraped_at": datetime.now().isoformat()
        })

df = pd.DataFrame(filtered_jobs)

filename = f"{OUTPUT_DIR}/remoteok_jobs.csv"

df.to_csv(filename, index=False)

print(f"Saved {len(df)} jobs")
print(df.head())