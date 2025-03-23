from transformers import pipeline
import json
import os

# Ensure PyTorch is installed: pip install torch
try:
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
except Exception as e:
    print("❌ Error loading summarization model:", str(e))
    print("Ensure you have installed PyTorch (pip install torch).")
    exit()

# Load threat data
rss_file = "data/cyber_rss.json"
output_file = "data/summarized_threats.json"

# Check if the file exists
if not os.path.exists(rss_file):
    print(f"❌ Error: {rss_file} not found!")
    exit()

# Read JSON data safely
try:
    with open(rss_file, "r") as f:
        threats = json.load(f)
        if not isinstance(threats, list):  # Ensure correct format
            raise ValueError("Invalid JSON format: Expected a list.")
except json.JSONDecodeError:
    print(f"❌ Error: {rss_file} is not a valid JSON file.")
    exit()

# Summarize threats
summarized_data = []
for threat in threats:
    summary_text = threat.get("summary", "")
    if summary_text:
        # Ensure the text length does not exceed model input limits
        summary_text = summary_text[:4096]  # Trim text to max length for BART
        
        try:
            summary = summarizer(summary_text, max_length=100, min_length=30, do_sample=False)
            summarized_data.append({
                "title": threat.get("title", "No Title"),
                "summary": summary[0]["summary_text"]
            })
        except Exception as e:
            print(f"❌ Error summarizing threat: {e}")

# Save summarized threats
try:
    with open(output_file, "w") as f:
        json.dump(summarized_data, f, indent=4)
    print(f"✅ Summarized threats saved to {output_file}")
except Exception as e:
    print(f"❌ Error saving summarized data: {e}")
