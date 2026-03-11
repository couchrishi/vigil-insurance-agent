# Setup Guide

Follow these steps to get the Proactive Safety Agent and Command Center running on your local machine.

## Prerequisites

- **Python 3.11+**
- **Node.js 18+** & **npm**
- **Google Cloud SDK (gcloud)** authenticated with Vertex AI permissions.

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/couchrishi/vigil-insurance-agent.git
cd vigil-insurance-agent
```

### 2. Backend Setup
Create a virtual environment and install the required Python packages:
```bash
python3 -m venv venv
source venv/bin/activate
pip install pandas uvicorn fastapi google-adk google-genai python-dotenv
```

### 3. Frontend Setup
Install the dashboard dependencies:
```bash
cd safety-command-center-main
npm install
cd ..
```

### 4. Configuration
Create a `.env` file in the root directory:
```env
GOOGLE_API_KEY=your_api_key_here
GOOGLE_CLOUD_PROJECT=your_project_id
GOOGLE_CLOUD_LOCATION=us-central1
```

## Running the Demo

### 1. Reset Data (Optional)
To start with a clean slate (clears CRM and activity logs):
```bash
python3 reset_demo.py
```

### 2. Start the Ecosystem
This command launches both the FastAPI backend (port 8081) and the Vite frontend (port 8080):
```bash
python3 start_dashboard.py
```

Open [http://localhost:8080](http://localhost:8080) in your browser to view the Command Center.
