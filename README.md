# AI-Powered Lead Intelligence Platform

An end-to-end automated system for identifying, scoring, and analyzing high-intent B2B technical prospects using hiring signals.

## Features

### Data Acquisition
Scrapes public job listings for technical hiring signals.

### Lead Scoring Engine
Ranks prospects based on role relevance.

### AI Insight Generation
Generates business opportunity analysis.

### Interactive Dashboard
Visualizes and filters scored leads.

## Tech Stack

- Python
- Playwright
- Pandas
- Streamlit
- OpenAI-ready AI layer

## Workflow

Data Collection → Scoring → AI Analysis → Dashboard

## Run Project

### Install
pip install -r requirements.txt

playwright install

### Scrape
python scraper/job_scraper.py

### Score
python scoring/score_leads.py

### Generate Insights
python ai_analysis/generate_insights.py

### Launch Dashboard
streamlit run dashboard/app.py

## Business Use Case

Automates B2B lead intelligence discovery by identifying organizations showing technical growth signals.