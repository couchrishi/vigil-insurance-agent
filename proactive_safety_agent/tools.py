import json
import csv
import os
import pandas as pd
import time
from datetime import datetime
from google.adk.tools import ToolContext

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
CRM_FILE = os.path.join(os.path.dirname(__file__), "crm", "state.csv")
LOG_FILE = os.path.join(os.path.dirname(__file__), "crm", "activity.json")

def direct_log(agent, action, job_id=None):
    """Helper to write logs directly to file to avoid circular imports."""
    try:
        logs = []
        if os.path.exists(LOG_FILE):
            with open(LOG_FILE, "r") as f:
                logs = json.load(f)
        
        prefix = f"[Job #{job_id}] " if job_id else ""
        logs.append({
            "timestamp": datetime.now().strftime("%H:%M:%S"),
            "agent": agent,
            "action": f"{prefix}{action}"
        })
        
        # Keep last 50 to allow for more scrolling
        with open(LOG_FILE, "w") as f:
            json.dump(logs[-50:], f)
    except Exception as e:
        print(f"Log Error: {e}")

def fetch_recalls():
    """Fetches the latest vehicle recalls."""
    direct_log("MonitorAgent", "Scanning NHTSA database for new recalls...")
    time.sleep(1)
    path = os.path.join(DATA_DIR, "recalls.json")
    with open(path, "r") as f:
        return json.load(f)

def get_affected_policyholders(make: str, year: int):
    """Finds matching policyholders."""
    time.sleep(1)
    path = os.path.join(DATA_DIR, "policyholders.csv")
    affected = []
    with open(path, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["make"].lower() == make.lower() and int(row["year"]) == year:
                affected.append(row)
    
    if affected:
        direct_log("MonitorAgent", f"Detected {len(affected)} policyholders affected by {make} recall.")
    return affected

def search_safety_manual(component: str):
    """RAG-style manual search."""
    direct_log("TriageAgent", f"Searching safety manuals for: {component}")
    time.sleep(1.5)
    path = os.path.join(DATA_DIR, "safety_manuals.json")
    with open(path, "r") as f:
        manuals = json.load(f)
    return manuals.get(component, "No manual found.")

def update_crm_dashboard(policy_id: str, field: str, value: str):
    """
    Updates the Insurance Officer's CRM dashboard with the current lifecycle status.
    """
    time.sleep(0.5)
    df = pd.read_csv(CRM_FILE)
    
    # Handle boolean strings from LLM
    if str(value).lower() == 'true': val = True
    elif str(value).lower() == 'false': val = False
    else: val = value

    df.loc[df['policy_id'] == policy_id, field] = val
    df.to_csv(CRM_FILE, index=False)
    
    direct_log("CRM", f"Updated {policy_id}: {field} -> {value}")
    print(f"📊 [CRM UPDATE] Policy {policy_id}: {field} -> {value}")
    return {"status": "updated"}

def dispatch_uber_a2a(customer_name: str, location: str):
    """
    Simulates an A2A call to the WaymoMobilityAgent.
    """
    direct_log("A2A Partner", f"Waymo Mobility: Requesting autonomous ride for {customer_name}...")
    time.sleep(2)
    direct_log("A2A Partner", f"Waymo Mobility: Vehicle dispatched for {customer_name}")
    print(f"📡 [A2A] Requesting Waymo for {customer_name} via MobilityAgent...")
    return {"status": "success", "msg": "Waymo is on the way!"}

def book_dealer_repair_a2a(vin: str):
    """
    Simulates an A2A call to the AutoNationRepairAgent.
    """
    direct_log("A2A Partner", f"Repair Agent: Finding nearest service center for {vin}...")
    time.sleep(2)
    direct_log("A2A Partner", f"Repair Agent: priority service slot booked for {vin}")
    print(f"📡 [A2A] Requesting repair slot for {vin} via RepairAgent...")
    return {"status": "success", "msg": "Repair scheduled for tomorrow 10AM."}

def check_repair_status(vin: str):
    """Checks service records."""
    time.sleep(1)
    path = os.path.join(DATA_DIR, "service_records.json")
    with open(path, "r") as f:
        records = json.load(f)
    for record in records:
        if record["vin"] == vin:
            return True
    return False
