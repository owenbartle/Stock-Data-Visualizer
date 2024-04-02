import requests

class DataFetching: 

    #add api key
    api_key = 'JLFXYX4J4I20CF8E'

    #method for fetching stock date - In Progress
    def fetch_stock_data(symbol, api_key, tsString):
        url = f"https://www.alphavantage.co/query?function={tsString}&symbol={symbol}&apikey={api_key}"
        r = requests.get(url)
        data = r.json()
        return data

    def fetch_intraday_data(symbol, api_key, tsString, interval):
        url = f"https://www.alphavantage.co/query?function={tsString}&symbol={symbol}&interval={interval}&apikey={api_key}"
        r = requests.get(url)
        data = r.json()
        return data