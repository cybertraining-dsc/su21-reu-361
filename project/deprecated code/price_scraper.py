#This code was taken from a medium article found here
#https://bryanf.medium.com/web-scraping-crypto-prices-with-python-41072ea5b5bf
#It does not work because coinmarketcap's website has changed




from bs4 import BeautifulSoup
import requests
import pandas as pd
import json
import time
cmc = requests.get('https://coinmarketcap.com/')
soup = BeautifulSoup(cmc.content, 'html.parser')
print(soup.title)

#<title class="next-head">Cryptocurrency Market Capitalizations | CoinMarketCaps/title>
print(soup.prettify())
data = soup.find('script', id="__NEXT_DATA__",type="application/json")

coins = {}

#using data.contents[0] to remove script tags
coin_data = json.loads(data.contents[0])
listings = coin_data['props']['initialState']['cryptocurrency']['listingLatest']['data']

for i in listings:
    coins[str(i['id'])] = i['slug']

for i in coins:
    page = requests.get(
        f'https://coinmarketcap.com/currencies/{coins[i]}/historical-data/?start=20170701&end=20210628')
    soup = BeautifulSoup(page.content, 'html.parser')
    data = soup.find('script', id="__NEXT_DATA__", type="application/json")
    historical_data = json.loads(data.contents[0])

quotes = historical_data['props']['initialState']['cryptocurrency']['ohlcvHistorical'][i]['quotes']
info = historical_data['props']['initialState']['cryptocurrency']['ohlcvHistorical'][i]

market_cap = []
volume = []
timestamp = []
name = []
symbol = []
slug = []

for j in quotes:
    market_cap.append(j['quote']['USD']['market_cap'])
    volume.append(j['quote']['USD']['volume'])
    timestamp.append(j['quote']['USD']['timestamp'])
    name.append(j['name'])
    symbol.append(j['symbol'])
    slug.append(coins[i])

df = pd.DataFrame(columns = ['marketcap', 'volume', 'timestamp', 'name', 'symbol', 'slug'])
df['marketcap'] = market_cap
df['volume'] = volume
df['timestamp'] = timestamp
df['name'] = name
df['symbol'] = symbol
df['slug'] = slug

df.to_csv('cryptos.csv', index = False)