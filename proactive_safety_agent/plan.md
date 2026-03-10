# Proactive Safety Agent: Pitch & MVP Plan

This plan transforms a simple notification tool into a full **Safety Ecosystem** using ADK's A2A protocol.

## Phase 1-3: Core Infrastructure (Complete)
- [x] **Hybrid Data Layer**: NHTSA for detection, Mock CRM for state tracking.
- [x] **Agent Team**: Monitor, Triage, Outreach, and FollowUp agents.
- [x] **ADK Web UI**: Ready for visual demonstration.

## Phase 4: The A2A Partnership Ecosystem (Pitch Value)
- [x] **Mobility Partner (Uber)**: Implemented `dispatch_uber_a2a` to provide rides for critical hazards.
- [x] **Service Partner (AutoNation)**: Implemented `book_dealer_repair_a2a` to remove friction for the customer.
- [x] **CRM Dashboard Simulation**: Implemented `update_crm_dashboard` using `pandas` to track the lifecycle in `crm/state.csv`.

## The Pitch Narrative (Hackathon Ready)
1. **The Human Agent Experience**: The insurance officer logs in and sees a **comprehensive view** of safety exposure via the CRM dashboard.
2. **The Background Engine**: The agent runs silently, pushes detected risks through a triage pipe, and triggers the partners.
3. **The Magic Moment**: The judge sees the logs: *"Proactively booked an Uber for John Doe (Airbag Hazard) and scheduled a repair slot at AutoNation for 10AM tomorrow."*

## Final Steps for Demo
- [ ] Run `adk web proactive_safety_agent/`
- [ ] Send: `"Initialize the daily safety audit and coordinate with partners."`
- [ ] Open `proactive_safety_agent/crm/state.csv` during the demo to show real-time state changes.
