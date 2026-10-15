import requests
import pandas as pd

# Replace BTC with whatever stock you're looking to track
url = 'https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol=BTC&market=USD&apikey=ALPHAVANTAGE'
r = requests.get(url)
data = r.json()


df = pd.DataFrame.from_dict(data["Time Series (Digital Currency Daily)"], orient="index")
df.index = pd.to_datetime(df.index)
df = df.sort_index(ascending = True)
filtered_df = df[df.index >= "2016-06-01"]
filtered_df.to_csv("BTC_data.csv", index=True)