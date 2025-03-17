from transformers import pipeline
import json

# Load Hugging Face Summarization Model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Load threat data
with open("data/cyber_rss.json", "r") as f:
    threats = json.load(f)

summarized_data = []
for threat in threats:
    summary = summarizer(threat["summary"], max_length=100, min_length=30, do_sample=False)
    summarized_data.append({"title": threat["title"], "summary": summary[0]["summary_text"]})

# Save summarized threats
with open("data/summarized_threats.json", "w") as f:
    json.dump(summarized_data, f, indent=4)

print("✅ Summarized threats saved to data/summarized_threats.json")

