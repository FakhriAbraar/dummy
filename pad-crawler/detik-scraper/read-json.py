import json
import re

with open("detik-scraper\data\detik_12.json", "r") as file:
    data = json.load(file)

# print(data)
# print(data["unique_id"])
for item in data:
    # print(item["unique_id"], item["related_link"])
    # match = re.search(r"d-(\d+)", url)
    # print(match.group(1))
    raw = item["related_link"]
    text = re.search(r"d-(\d+)", raw)
    print(item["unique_id"], text.group(1))