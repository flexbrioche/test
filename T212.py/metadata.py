import requests
import json

url = "https://live.trading212.com/api/v0/equity/portfolio"

headers = {"Authorization": "1442967ZvodHjowzEtivuAZbeqiwHKrCxIiM"}

response = requests.get(url, headers=headers)

data = response.json()

def ticker():
    for tick in data:
        print(f"You own: {tick['quantity']} units of {tick['ticker']}")
        average_price = float(tick['averagePrice'])
        print(f"Average Price: {average_price}")
        current_price = float(tick['currentPrice'])
        print(f"Current Price: {current_price}\n")
      
ticker()

#print(data)