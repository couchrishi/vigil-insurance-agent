# Tutorial: Building the Proactive Safety Agent

In this tutorial, you will learn how to build a next-generation AI agent designed to transform insurance from a reactive claims processor into a proactive partner in customer safety.

## The Business Problem

*   **The Pain Point:** High loss ratios due to preventable, high-cost accidents caused by unaddressed vehicle recalls.
*   **The Objective:** Reduce automotive loss ratio by 5-10% and decrease customer churn by demonstrating tangible value.

## The AI Agent Solution

The **Proactive Safety Agent** is an automated multi-agent system that monitors vehicle safety information and cross-references it with policyholder data to deliver personalized, life-saving alerts.

### High-Level Architecture

The system consists of four specialized agents:

1.  **Monitor Agent**: Continuously scans recall databases (e.g., NHTSA) and identifies affected policyholders.
2.  **Triage Agent**: Analyzes recall notices and safety manuals to prioritize risks (Critical, Urgent, Standard).
3.  **Outreach Agent**: Orchestrates multi-channel outreach (SMS, Email, In-App) with clear repair instructions.
4.  **Follow-up Agent**: Monitors service records to confirm repair completion and sends reminders if necessary.

## Implementation with ADK

### 1. Define the Tools

We define tools to interact with our data sources:

```python
@tool
def fetch_recalls():
    # Fetches data from NHTSA-like API
    ...

@tool
def get_affected_policyholders(make, year):
    # Queries internal policy database
    ...

@tool
def search_safety_manual(component):
    # RAG-based search for repair instructions
    ...
```

### 2. Configure the Agents

Each agent is given a specific role and set of tools:

```python
monitor_agent = Agent(
    name="MonitorAgent",
    tools=[fetch_recalls, get_affected_policyholders],
    instruction="Identify new recalls and find affected customers."
)

# ... define other agents ...
```

### 3. Orchestrate the Team

The `ProactiveSafetyTeam` agent coordinates the flow between sub-agents:

```python
safety_team = Agent(
    name="ProactiveSafetyTeam",
    sub_agents=[monitor_agent, triage_agent, outreach_agent, follow_up_agent],
    instruction="Coordinate the end-to-end safety process."
)
```

### 4. Enable Proactive Follow-ups

By using ADK's **Session State**, the agent can remember which customers have been notified and track their repair status over time.

```python
# In OutreachAgent tool:
context.state[f"notification_sent:{vin}"] = True
```

## Running the Agent

You can interact with the Proactive Safety Agent using the ADK Web UI:

```console
adk web proactive_safety_agent/agent.py
```

This allows you to see the real-time collaboration between the Monitor, Triage, and Outreach agents as they work to keep policyholders safe.
