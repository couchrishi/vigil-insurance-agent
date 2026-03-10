# Lovable App Specification: Proactive Safety Command Center

## Project Goal
Create a professional, high-fidelity "Safety Control Room" dashboard for Insurance Officers to manage the **Proactive Safety Agent** ecosystem. The UI should look like a modern enterprise risk management tool (think dark mode, glassmorphism, and live telemetry).

## App Persona: The Insurance Safety Officer
The user needs to see "Safety Exposure" in their territory and monitor the AI-driven A2A dispatches (Uber and Dealership bookings) in real-time.

---

## 1. Design Aesthetic
- **Theme**: Dark Mode (Deep Navy/Charcoal).
- **Style**: Modern, clean, enterprise-grade.
- **Accents**: 
  - #38bdf8 (Sky Blue) for Active/AI actions.
  - #fbbf24 (Amber) for High-Risk/Urgent cases.
  - #10b981 (Emerald) for Resolved/Safe cases.

---

## 2. Page Structure

### Header
- **Title**: Proactive Safety Command Center
- **System Status**: "Background Agent: Active" (with a pulsing green dot).
- **Primary Action**: "🚀 Run Global Safety Audit" (Large, high-contrast button).

### Hero Metrics (Top Row)
1. **Current Exposure**: Total policyholders affected by active recalls.
2. **Active Dispatches**: Number of A2A Uber rides currently in progress.
3. **Negotiated Repairs**: Number of dealership appointments booked by the AI.
4. **Resolved Risks**: Number of vehicles confirmed fixed this week.

### The "Lifecycle" Table (Main View)
A table showing all affected policyholders. Columns:
- **Policyholder**: (Name & ID)
- **Vehicle Info**: (Make, Model, VIN)
- **Recall Severity**: (Critical, Urgent, Standard) - with colored badges.
- **AI Action Status**: A progress-stepper or set of icons showing:
  - 📩 Notification Sent
  - 🚖 Uber Dispatched
  - 🔧 Dealer Booked
- **Current Status**: (e.g., "En Route to Dealer", "Awaiting Parts", "Safe").

### Real-Time Activity Feed (Sidebar/Drawer)
A rolling log of the AI Agent's work:
- "09:41 AM: MonitorAgent detected new Takata Airbag recall."
- "09:42 AM: TriageAgent flagged P001 as High Risk."
- "09:43 AM: OutreachAgent dispatched A2A Uber ride for John Doe."

---

## 3. Data Integration (API Contract)
The app should expect a JSON array from the backend (`/api/data`):
```json
[
  {
    "policy_id": "P001",
    "vin": "VIN123TOYOTA",
    "status": "High Risk",
    "notification_sent": true,
    "ride_booked": true,
    "repair_scheduled": true,
    "fixed": false
  }
]
```

## 4. Interaction Logic
1. **On Load**: Fetch data from `http://localhost:8080/api/data`.
2. **Click "Run Audit"**: 
   - Call `POST http://localhost:8080/api/trigger`.
   - Show a "Scanning NHTSA API..." loading animation.
   - Poll for updates every 3 seconds to show icons flipping from gray to active blue.
