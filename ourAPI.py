import requests

class DataFetching: 

    # Add api key
    api_key = 'WQ7ZBXJ13TX4DPY5'

    # Method for fetching stock data - In Progress
    def fetch_stock_data(self, symbol, tsString):
        url = f"https://www.alphavantage.co/query?function={tsString}&symbol={symbol}&apikey={self.api_key}"
        r = requests.get(url)
        data = r.json()
        return data

    def fetch_intraday_data(self, symbol, tsString, interval):
        url = f"https://www.alphavantage.co/query?function={tsString}&symbol={symbol}&interval={interval}&apikey={self.api_key}"
        r = requests.get(url)
        data = r.json()
        return data
    
