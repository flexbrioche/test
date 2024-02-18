import requests
import matplotlib.pyplot as plt
import json

fig, ax = plt.subplots()

url = "https://live.trading212.com/api/v0/equity/portfolio"

headers = {"Authorization": "1442967ZvodHjowzEtivuAZbeqiwHKrCxIiM"}

response = requests.get(url, headers=headers)

data = response.json()

#def ticker():
 
average_prices, current_prices, tickers = [], [], []

for tick in data:
    print(f"You own: {tick['quantity']} units of {tick['ticker']}")
    ticker = tick['ticker']
    tickers.append(ticker)
    average_price = float(tick['averagePrice'])
    print(f"Average Price: {average_price}")
    average_prices.append(average_price)
    current_price = float(tick['currentPrice'])
    print(f"Current Price: {current_price}\n")
    current_prices.append(current_price)

fig, ax = plt.subplots()
ax.plot(tickers, average_prices, c='red', alpha=0.5)
ax.plot(tickers, current_prices, c='green', alpha=0.5)
# plt.fill_between(tickers, average_price, current_prices, facecolor='blue', alpha=0.1)

plt.title("Portfolio", fontsize=24)
plt.xlabel("Ticker symbol", fontsize=10)
plt.ylabel("Avg vs Current Price", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

   
plt.show()

#ticker()

#print(data)