import requests
from pprint import pprint
import json

def getGoogleData(isbn):
    res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "i8iZFHFqdnKzXDrfgTLQ", "isbns": isbn})
    if res.status_code is 200:
        json_format = json.loads(res.text)
        for book in json_format['books']:
            avgrating = (book['average_rating'])
            rcount = (book['ratings_count'])
        return avgrating, rcount
    return 0, 0

def getIsbns(isbns):
    res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "i8iZFHFqdnKzXDrfgTLQ", "isbns": isbns})


# Values from google
#review_count = 
#average_score =


#parsed_json = (json.loads(str(res)))
#print(json.dumps(parsed_json, indent=4, sort_keys=True))

#https://www.goodreads.com/api