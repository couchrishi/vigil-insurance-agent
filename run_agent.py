import asyncio
import os
from dotenv import load_dotenv

# Load .env first
load_dotenv(override=True)

# Force Vertex AI settings in the environment
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "TRUE"
os.environ["GOOGLE_CLOUD_PROJECT"] = "saib-ai-playground"
os.environ["GOOGLE_CLOUD_LOCATION"] = "us-central1"

from google.adk.runners import InMemoryRunner
from proactive_safety_agent.agent import app

async def main():
    if not os.getenv("GOOGLE_API_KEY"):
        print("Error: GOOGLE_API_KEY environment variable not set.")
        return

    runner = InMemoryRunner(app=app)
    
    print("Starting Proactive Safety Agent on Vertex AI (gemini-3.0-pro)...")
    
    prompt = "Check for new recalls and start the outreach process for any affected customers."
    
    try:
        # run_debug allows us to see the internal agent conversations
        response = await runner.run_debug(prompt)
        print("\n=== FINAL AGENT RESPONSE ===\n")
        print(response)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    asyncio.run(main())
