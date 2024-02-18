import requests
import json

url = "https://live.trading212.com/api/v0/equity/portfolio"

headers = {"Authorization": "1442967ZvodHjowzEtivuAZbeqiwHKrCxIiM"}

response = requests.get(url, headers=headers)

def ticker():
    data = response.json()
    for tick in data:
        print(f"You own: {tick['ticker']}")
        print(f"Average Price: {tick['averagePrice']}")

ticker()
