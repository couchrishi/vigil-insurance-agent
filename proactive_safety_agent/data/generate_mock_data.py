import json
import csv
import os

def generate_data():
    data_dir = "proactive_safety_agent/data"
    
    # 1. Mock Recalls (NHTSA-like)
    recalls = [
        {
            "recall_id": "R001",
            "component": "Airbag",
            "description": "Takata airbag inflator may rupture, sending metal fragments into the cabin.",
            "severity": "Critical",
            "affected_makes": ["Toyota", "Honda"],
            "affected_years": [2015, 2016, 2017]
        },
        {
            "recall_id": "R002",
            "component": "Brakes",
            "description": "Brake fluid leak may increase stopping distance.",
            "severity": "Urgent",
            "affected_makes": ["Ford"],
            "affected_years": [2018, 2019]
        },
        {
            "recall_id": "R003",
            "component": "Software",
            "description": "Infotainment screen may go blank while reversing.",
            "severity": "Standard",
            "affected_makes": ["Tesla"],
            "affected_years": [2021, 2022]
        }
    ]
    with open(os.path.join(data_dir, "recalls.json"), "w") as f:
        json.dump(recalls, f, indent=2)

    # 2. Mock Policyholders
    policyholders = [
        {"policy_id": "P001", "name": "John Doe", "email": "john@example.com", "phone": "555-0101", "vin": "VIN123TOYOTA", "make": "Toyota", "year": 2016, "model": "Camry"},
        {"policy_id": "P002", "name": "Jane Smith", "email": "jane@example.com", "phone": "555-0102", "vin": "VIN456HONDA", "make": "Honda", "year": 2017, "model": "Civic"},
        {"policy_id": "P003", "name": "Bob Brown", "email": "bob@example.com", "phone": "555-0103", "vin": "VIN789FORD", "make": "Ford", "year": 2019, "model": "F-150"},
        {"policy_id": "P004", "name": "Alice Green", "email": "alice@example.com", "phone": "555-0104", "vin": "VIN000TESLA", "make": "Tesla", "year": 2022, "model": "Model 3"}
    ]
    with open(os.path.join(data_dir, "policyholders.csv"), "w", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=policyholders[0].keys())
        writer.writeheader()
        writer.writerows(policyholders)

    # 3. Mock Safety Manuals (Simulating a Knowledge Base)
    manuals = {
        "Airbag": "Repair Instructions: Contact authorized dealer immediately for inflator replacement. Do not allow passengers in the front seat until repaired. Severity: Level 1 (Life-threatening).",
        "Brakes": "Repair Instructions: Check fluid levels and visit a service center within 48 hours. Avoid high-speed driving. Severity: Level 2 (High Risk).",
        "Software": "Repair Instructions: Schedule an Over-the-Air (OTA) update via the vehicle settings menu. Severity: Level 3 (Feature Issue)."
    }
    with open(os.path.join(data_dir, "safety_manuals.json"), "w") as f:
        json.dump(manuals, f, indent=2)

    # 4. Mock Service Records (Empty initially)
    service_records = []
    with open(os.path.join(data_dir, "service_records.json"), "w") as f:
        json.dump(service_records, f, indent=2)

    print("Mock data generated successfully in proactive_safety_agent/data/")

if __name__ == "__main__":
    generate_data()
