from playwright.sync_api import sync_playwright
import pandas as pd
import os
from datetime import datetime

OUTPUT_DIR = "data/raw"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def scrape_jobs():
    jobs = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.indeed.com/jobs?q=data+engineer", timeout=60000)

        page.wait_for_timeout(5000)

        cards = page.locator("div.job_seen_beacon").all()

        for card in cards[:20]:
            try:
                title = card.locator("h2").inner_text()
                company = card.locator('[data-testid="company-name"]').inner_text()

                jobs.append({
                    "title": title,
                    "company": company,
                    "scraped_at": datetime.now().isoformat()
                })

            except Exception as e:
                print(f"Skipping card: {e}")

        browser.close()

    return jobs


if __name__ == "__main__":
    jobs = scrape_jobs()

    df = pd.DataFrame(jobs)

    filename = f"{OUTPUT_DIR}/jobs_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

    df.to_csv(filename, index=False)

    print(f"Saved {len(df)} jobs to {filename}")
    print(df.head())