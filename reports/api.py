from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def home():
    return {"status": "Lead Intelligence SaaS Running"}

@app.post("/run-sprint")
def run_sprint():
    os.system("python run_sprint.py")
    return {"message": "Sprint executed. Report generated."}