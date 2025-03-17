import json

# Load local MITRE ATT&CK data
with open("data/mitre_attack.json", "r") as f:
    data = json.load(f)

# Extract techniques
techniques = [item for item in data["objects"] if item["type"] == "attack-pattern"]

# Save extracted techniques
with open("data/mitre_attack_filtered.json", "w") as f:
    json.dump(techniques, f, indent=4)

print("✅ MITRE ATT&CK data processed and saved to data/mitre_attack_filtered.json")

