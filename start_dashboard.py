import subprocess
import os
import time
import sys

def run_dashboard():
    # 1. Start FastAPI Backend in background
    print("🚀 Starting FastAPI Backend on port 8081...")
    env = os.environ.copy()
    env["PYTHONPATH"] = os.getcwd()
    backend_process = subprocess.Popen(
        [sys.executable, "proactive_safety_agent/dashboard/server.py"],
        env=env,
        cwd=os.getcwd()
    )

    # 2. Start Vite Frontend
    print("🚀 Starting Vite Frontend on port 8080...")
    frontend_dir = os.path.join(os.getcwd(), "safety-command-center-main")
    
    # Check if node_modules exists
    if not os.path.exists(os.path.join(frontend_dir, "node_modules")):
        print("📦 node_modules not found. Running npm install...")
        subprocess.run(["npm", "install"], cwd=frontend_dir)

    try:
        subprocess.run(["npm", "run", "dev"], cwd=frontend_dir)
    except KeyboardInterrupt:
        print("\n🛑 Stopping servers...")
        backend_process.terminate()

if __name__ == "__main__":
    run_dashboard()
