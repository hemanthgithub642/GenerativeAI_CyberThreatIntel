import requests
import json

# AlienVault API
api_url = "https://otx.alienvault.com/api/v1/pulses/subscribed"

# Replace with your AlienVault API key
headers = {"X-OTX-API-KEY": "1096178ea98713c92129b419cf655115ae50ec8aa504f40b6c5a35b2d9e591fa"}

response = requests.get(api_url, headers=headers)

if response.status_code == 200:
    data = response.json()

    with open("data/alienvault.json", "w") as f:
        json.dump(data, f, indent=4)

    print("✅ AlienVault OTX data saved to data/alienvault.json")
else:
    print(f"❌ Failed to fetch AlienVault data: HTTP {response.status_code}")

