import os

print("Starting Lead Intelligence Sprint...")

os.system("python scraper/job_scraper.py")
os.system("python scraper/remoteok_scraper.py")
os.system("python scoring/score_leads.py")
os.system("python ai_analysis\generate_insights.py")
os.system("python reports\sprint_report.py")

print("DONE: Client Sprint Ready.")