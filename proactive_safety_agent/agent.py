from google.adk.agents import Agent
from google.adk.apps import App, ResumabilityConfig
from proactive_safety_agent.tools import (
    fetch_recalls,
    get_affected_policyholders,
    search_safety_manual,
    update_crm_dashboard,
    dispatch_uber_a2a,
    book_dealer_repair_a2a,
    check_repair_status
)

# Shared model string
MODEL_ID = "gemini-2.5-pro"

# 1. Monitor Agent: Constantly checks for new recalls
monitor_agent = Agent(
    name="MonitorAgent",
    description="Identifies new vehicle recalls and finds affected policyholders.",
    instruction=(
        "1. Call 'fetch_recalls' to get the latest list of recalls.\n"
        "2. For each recall, call 'get_affected_policyholders' using the make and year from the recall.\n"
        "3. For every policyholder ID found, call 'update_crm_dashboard' to set status='Recall Detected'.\n"
        "4. Provide the list of IDs and components (e.g. Airbag) to the orchestrator for triage."
    ),
    tools=[fetch_recalls, get_affected_policyholders, update_crm_dashboard],
    model=MODEL_ID
)

# 2. Triage Agent: Analyzes severity and repair instructions
triage_agent = Agent(
    name="TriageAgent",
    description="Analyzes recall severity and provides repair instructions.",
    instruction=(
        "1. Use 'search_safety_manual' to understand the recall risk.\n"
        "2. If the recall is 'Critical' or 'Urgent', call 'update_crm_dashboard' to set status to 'Critical' or 'High Risk' accordingly.\n"
        "3. Provide a brief repair instruction and pass to OutreachAgent."
    ),
    tools=[search_safety_manual, update_crm_dashboard],
    model=MODEL_ID
)

# 3. Outreach Agent: Orchestrates personalized notifications and A2A partnerships
outreach_agent = Agent(
    name="OutreachAgent",
    description="Sends personalized safety alerts and coordinates partner actions.",
    instruction=(
        "For each policyholder provided:\n"
        "1. Send a safety notification via 'update_crm_dashboard' (notification_sent=True).\n"
        "2. If their status is 'Critical' or 'High Risk', you MUST call 'dispatch_uber_a2a' to send a Waymo and set 'ride_booked=True' in the CRM.\n"
        "3. Call 'book_dealer_repair_a2a' for every affected customer and set 'repair_scheduled=True'.\n"
        "DO NOT skip the Waymo tool call; it is a vital part of our premium safety service."
    ),
    tools=[dispatch_uber_a2a, book_dealer_repair_a2a, update_crm_dashboard],
    model=MODEL_ID
)

# 4. Follow-up Agent: Checks for completed repairs
follow_up_agent = Agent(
    name="FollowUpAgent",
    description="Checks if notified customers have completed their repairs.",
    instruction=(
        "Check service records using check_repair_status(vin). "
        "If True, call update_crm_dashboard to set status to 'Safe' and fixed=True."
    ),
    tools=[check_repair_status, update_crm_dashboard],
    model=MODEL_ID
)

# 5. Proactive Safety Team (Orchestrator)
safety_team = Agent(
    name="ProactiveSafetyTeam",
    description="A team that proactively manages vehicle safety for insurance policyholders.",
    instruction=(
        "CRITICAL: You MUST follow these steps in order for every job. Do not skip steps.\n"
        "1. Start by calling MonitorAgent to run 'fetch_recalls'. You cannot proceed without the recall data.\n"
        "2. Once recalls are found, delegate to MonitorAgent to 'get_affected_policyholders' for each affected make/year.\n"
        "3. Pass those specific policyholders to TriageAgent to assess severity via 'search_safety_manual'.\n"
        "4. ONLY after triage is complete, delegate to OutreachAgent to coordinate Waymo and Dealer bookings.\n"
        "Do not use any placeholder IDs like '78901'. Only use IDs (e.g., P001) returned by the tools."
    ),
    sub_agents=[monitor_agent, triage_agent, outreach_agent, follow_up_agent],
    model=MODEL_ID
)

# 6. The ADK App (Resumability disabled for clean demo runs)
app = App(
    name="proactive_safety_agent",
    root_agent=safety_team,
    resumability_config=ResumabilityConfig(is_resumable=False)
)

