import pandas as pd
import json
import os
import shutil

CRM_FILE = "proactive_safety_agent/crm/state.csv"
LOG_FILE = "proactive_safety_agent/crm/activity.json"
ADK_DIR = "proactive_safety_agent/.adk"

def reset():
    print("🧹 Resetting Proactive Safety Demo...")

    # 1. Reset CRM State
    if os.path.exists(CRM_FILE):
        df = pd.read_csv(CRM_FILE)
        df['status'] = 'Standard'
        df['notification_sent'] = False
        df['ride_booked'] = False
        df['repair_scheduled'] = False
        df['fixed'] = False
        df.to_csv(CRM_FILE, index=False)
        print("✅ CRM State cleared (25 records reset).")

    # 2. Clear Activity Logs
    # Ensure directory exists before writing logs
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    with open(LOG_FILE, "w") as f:
        json.dump([], f)
    print("✅ Activity Feed cleared.")

    # 3. Wipe ADK Session (Optional but recommended for fresh start)
    if os.path.exists(ADK_DIR):
        shutil.rmtree(ADK_DIR)
        print("✅ ADK Session history wiped.")

    print("\n✨ Demo is now fresh and ready for Job #1001!")

if __name__ == "__main__":
    reset()
