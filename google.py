import requests
import json


res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "i8iZFHFqdnKzXDrfgTLQ", "isbns": "9781632168146"})
print(res.json())
parsed_json = (json.loads(str(res)))
print(json.dumps(parsed_json, indent=4, sort_keys=True))

#https://www.goodreads.com/api