import requests
import json

# Fetch MITRE ATT&CK data
mitre_url = "https://cti-taxii.mitre.org/stix2"
response = requests.get(mitre_url)

if response.status_code == 200:
    data = response.json()
    techniques = [item for item in data["objects"] if item["type"] == "attack-pattern"]

    with open("data/mitre_attack.json", "w") as f:
        json.dump(techniques, f, indent=4)

    print("✅ MITRE ATT&CK data saved to data/mitre_attack.json")

else:
    print(f"❌ Failed to fetch MITRE data: HTTP {response.status_code}")

