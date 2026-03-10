from google.adk.agents import Agent
from google.adk.a2a.utils.agent_to_a2a import to_a2a
from google.adk.tools import tool

@tool
def schedule_repair_appointment(vin: str, dealer_name: str):
    """
    Schedules a priority repair slot for a specific VIN at a dealership.
    """
    print(f"🔧 [A2A REPAIR] Scheduling slot for VIN {vin} at {dealer_name}...")
    return {"status": "success", "appointment_id": "REPAIR-99", "time": "Tomorrow 10:00 AM"}

repair_agent = Agent(
    name="AutoNationRepairAgent",
    model="gemini-2.0-flash",
    instruction="You manage service schedules for dealership networks. Use schedule_repair_appointment to book slots.",
    tools=[schedule_repair_appointment]
)

# This would normally run on port 8002
a2a_repair_app = to_a2a(repair_agent, port=8002)
