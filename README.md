# Vigil Insurance: Proactive Safety Agent Ecosystem

> **Traditional insurance is reactive. Vigil is proactive.**  
> Built with the **Google Agent Development Kit (ADK)** and **Gemini 2.5 Pro**, this ecosystem detects vehicle safety risks and autonomously coordinates transport and repairs via Agent-to-Agent (A2A) protocols.

[![Documentation](https://img.shields.io/badge/docs-GitHub%20Pages-blue)](https://couchrishi.github.io/vigil-insurance-agent/)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-green.svg)](https://www.python.org/)
[![React](https://img.shields.io/badge/frontend-React%20%2F%20Tailwind-blue)](https://react.dev/)

---

## ⚡ The Vision

Vigil Insurance doesn't wait for a claim. Our autonomous agent team continuously monitors global safety databases (NHTSA) to protect our policyholders. When a critical recall is detected, the agents don't just send an email—they coordinate a solution:

1.  **Autonomous Detection**: Scans for recalls and matches them to our 25 policyholders.
2.  **AI-Driven Triage**: Analyzes the severity (e.g., airbag fragments) and determines the risk level.
3.  **Waymo A2A Dispatch**: If the car is unsafe to drive, the AI autonomously requests a self-driving Waymo to transport the customer.
4.  **Priority Repair**: Negotiates with dealerships to secure immediate service slots.
5.  **Escalation**: Follows up after 30 days and escalates stalled repairs to human safety officers.

---

## 🏗️ Architecture

The system uses a multi-agent orchestration pattern powered by ADK:

- **MonitorAgent**: The "Eyes" — Scans NHTSA APIs and detects matches.
- **TriageAgent**: The "Brains" — Performs RAG searches over safety manuals to assess risk.
- **OutreachAgent**: The "Arms" — Executes A2A protocols with **Waymo** and **AutoNation**.
- **FollowUpAgent**: The "Safety Net" — Monitors completion and handles escalations.

---

## 🖥️ Command Center Dashboard

The project includes a high-fidelity "Safety Control Room" for Insurance Officers.
- **Live Telemetry**: Real-time scrolling feed of agent "thoughts" and tool calls.
- **Action Stepper**: Visual tracking of the AI lifecycle for every policyholder.
- **Time Simulation**: "Fast Forward 30 Days" to trigger escalation logic.

---

## 🚀 Quick Start

### 1. Prerequisites
- Python 3.11+
- Node.js 18+
- Google Cloud SDK authenticated for Vertex AI.

### 2. Installation
```bash
# Clone the repo
git clone https://github.com/couchrishi/vigil-insurance-agent.git
cd vigil-insurance-agent

# Setup Backend
source venv/bin/activate
pip install -r requirements.txt

# Setup Frontend
cd safety-command-center-main && npm install && cd ..
```

### 3. Run the Demo
```bash
# Optional: Clear previous state
python3 reset_demo.py

# Launch the full ecosystem (Port 8080)
python3 start_dashboard.py
```

---

## 📖 Documentation
Full architecture diagrams, tool definitions, and setup guides are available at our [Documentation Site](https://couchrishi.github.io/vigil-insurance-agent/).

---

*This project is a demonstration of the power of autonomous agent teams in the insurance and automotive safety sectors.*
