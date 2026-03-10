import os
import asyncio
import pandas as pd
import json
import random
from datetime import datetime
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

# Load .env with override to ensure Vertex/API settings are picked up
load_dotenv(override=True)

# Force Vertex AI settings (matching run_agent.py)
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "TRUE"
os.environ["GOOGLE_CLOUD_PROJECT"] = "saib-ai-playground"
os.environ["GOOGLE_CLOUD_LOCATION"] = "us-central1"

from google.adk.runners import InMemoryRunner
from proactive_safety_agent.agent import app as agent_app
from proactive_safety_agent.tools import direct_log

app = FastAPI()

# Enable CORS for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

CRM_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "crm", "state.csv")
POLICYHOLDERS_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "policyholders.csv")
LOG_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "crm", "activity.json")

def get_current_status(row):
    if row['fixed']: return "Safe — Repair Complete"
    if row['repair_scheduled']: return "Dealer Appointment Set"
    if row['ride_booked']: return "Waymo Dispatched"
    if row['notification_sent']: return "Notification Sent"
    if row['status'] == "Standard": return "Outreach not required"
    return "Outreach Required"

@app.get("/api/data")
def get_crm_data():
    if not os.path.exists(CRM_FILE):
        return []
    
    state_df = pd.read_csv(CRM_FILE)
    holders_df = pd.read_csv(POLICYHOLDERS_FILE)
    
    # Join on policy_id
    df = pd.merge(state_df, holders_df, on="policy_id", how="left")
    
    # Clean up NaN values for JSON compliance
    df = df.fillna("")
    
    # Add calculated fields for frontend
    df['vehicle'] = df['year'].astype(str) + " " + df['make'] + " " + df['model']
    df['current_status'] = df.apply(get_current_status, axis=1)
    
    # Cast booleans to proper JSON bools
    bool_cols = ['notification_sent', 'ride_booked', 'repair_scheduled', 'fixed']
    for col in bool_cols:
        df[col] = df[col].astype(bool)
        
    return df.to_dict(orient="records")

@app.get("/api/logs")
def get_logs():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            return json.load(f)
    return []

async def run_agent_task(prompt, job_id):
    try:
        runner = InMemoryRunner(app=agent_app)
        direct_log("Orchestrator", f"Agent team is planning workflow...", job_id=job_id)
        # run_debug provides more verbose logs in the terminal
        await runner.run_debug(prompt)
        direct_log("System", f"Safety Audit Job #{job_id} sequence completed.", job_id=job_id)
    except Exception as e:
        error_msg = str(e)
        if "401" in error_msg or "403" in error_msg:
            error_msg = "Authentication Error: Please run 'gcloud auth application-default login'"
        direct_log("Error", f"Job #{job_id} failed: {error_msg}", job_id=job_id)
        print(f"❌ [AGENT ERROR] {e}")

@app.post("/api/trigger")
async def trigger_audit():
    job_id = random.randint(1000, 9999)
    direct_log("System", f"Initializing Global Safety Audit...", job_id=job_id)
    prompt = f"Initialize safety audit for job #{job_id}. Coordinate with Waymo and Dealership partners for any affected customers."
    asyncio.create_task(run_agent_task(prompt, job_id))
    return {"status": "started", "job_id": job_id}

@app.post("/api/simulate/30days")
async def simulate_time():
    job_id = random.randint(1000, 9999)
    direct_log("System", "Fast-forwarding 30 days... checking for stalled repairs.", job_id=job_id)
    prompt = "30 days have passed. Run the FollowUpAgent to check for any customers who still haven't fixed their cars and escalate them."
    asyncio.create_task(run_agent_task(prompt, job_id))
    return {"status": "simulating", "job_id": job_id}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8081)
