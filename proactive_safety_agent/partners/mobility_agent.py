from google.adk.agents import Agent
from google.adk.a2a.utils.agent_to_a2a import to_a2a
from google.adk.tools import tool

@tool
def book_safety_ride(customer_name: str, pickup_location: str):
    """
    Books a complementary Uber ride for a customer whose car is unsafe to drive.
    """
    print(f"🚖 [A2A UBER] Dispatching ride for {customer_name} at {pickup_location}...")
    return {"status": "success", "driver": "Gemini Driver", "eta": "5 mins"}

mobility_agent = Agent(
    name="UberMobilityAgent",
    model="gemini-2.0-flash",
    instruction="You provide mobility solutions for insurance partners. Use book_safety_ride when requested.",
    tools=[book_safety_ride]
)

# This would normally run on port 8001
a2a_mobility_app = to_a2a(mobility_agent, port=8001)
