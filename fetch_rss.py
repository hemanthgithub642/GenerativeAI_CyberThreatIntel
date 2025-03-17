import feedparser
import json

rss_feeds = [
    "https://www.darkreading.com/rss.xml",
    "https://threatpost.com/feed/"
]

data = []

for url in rss_feeds:
    feed = feedparser.parse(url)
    for entry in feed.entries[:10]:  # Fetch only latest 10 news items
        data.append({"title": entry.title, "link": entry.link, "summary": entry.summary})

with open("data/cyber_rss.json", "w") as f:
    json.dump(data, f, indent=4)

print("✅ Cybersecurity RSS feeds saved to data/cyber_rss.json")

