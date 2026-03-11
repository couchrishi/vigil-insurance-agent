# Agents & Tools

The core of the system is composed of four specialized agents, each with a specific mission and set of capabilities.

## 1. MonitorAgent
**Mission**: The "Eyes" of the system.
- **Tools**:
    - `fetch_recalls`: Simulated scan of NHTSA database.
    - `get_affected_policyholders`: Cross-references VINs with the policy database.
    - `update_crm_dashboard`: Marks vehicles as "Recall Detected".

## 2. TriageAgent
**Mission**: The "Brains" of the system.
- **Tools**:
    - `search_safety_manual`: Performs a RAG-style search over vehicle manuals to understand specific risks (e.g., "Airbag inflator rupture").
    - `update_crm_dashboard`: Upgrades status to "Critical" or "High Risk".

## 3. OutreachAgent
**Mission**: The "Arms" of the system (Action-oriented).
- **Tools**:
    - `dispatch_uber_a2a` (Rebranded as **Waymo**): Triggers an Agent-to-Agent protocol to send an autonomous vehicle.
    - `book_dealer_repair_a2a`: Coordinates with the Repair Agent to schedule a priority service slot.
    - `update_crm_dashboard`: Sets `ride_booked` and `repair_scheduled` flags.

## 4. FollowUpAgent
**Mission**: The "Safety Net".
- **Trigger**: Activated via the "Fast Forward 30 Days" simulation.
- **Tools**:
    - `check_repair_status`: Verifies service records for completion.
    - `update_crm_dashboard`: Escalates stalled safety tickets to human officers if the vehicle remains unrepaired after 30 days.
