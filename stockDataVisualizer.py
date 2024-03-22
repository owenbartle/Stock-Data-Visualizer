#import all tools
import pygal
from datetime import datetime
import requests

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


# Title
print("Stock Data Visualizer")
print("-------------------------\n")



# Main While Loop
loop = True
while (loop == True):
    # Get Stock Option - Complete
    symbol = input("Enter the stock symbol to search for: ")

    #Function that checks stock ticker validity
    def check_stock(symbol):

        response = requests.get(url='https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=' + symbol + '&interval=5min&apikey=' + api_key)
        data = response.json()

        if 'Error Message' in data:
            return False
        else: 
            return True
    
    #Check that the given stock ticker is valid
    if check_stock(symbol) == False:
        print("It does not seem that this ticker symbol points to an existing stock. Please try again")
        loop = True
        continue
    else:
        print('The ticker symbol ' + symbol + ' is valid')


    # Select Chart Type - Complete
    print("\nChart Types:\n---------------------\n\t1. Bar\n\t2. Line")
    while (True):
        chartType = input("Enter the type (1, 2): ")
        if (chartType == '1' or chartType == '2'):
            chartType = int(chartType)
            break
        else:
            print("Must choose a valid type (1. Bar Graph | 2. Line Graph)")

    # Select Time Series Type - Complete
    print("Select the Time Series of the chart you want to Generate:")
    print("----------------------------")
    print("\t1. Intraday")
    print("\t2. Daily")
    print("\t3. Weekly")
    print("\t4. Monthly\n")
    
    
    timeSeriesKey = {}
    
    bool = True
    while(bool):
        tsChoice = input("Enter time series option (1, 2, 3, 4): ")
        if tsChoice == '1':
            interval = input("Enter time interval (1. 1min, 2. 5min, 3. 15min, 4. 30min, 5. 60min): ")
            if (interval == '1'):
                interval = "1min"
            elif (interval == '2'):
                interval = "5min"
            elif (interval == '3'):
                interval = "15min"
            elif (interval == '4'):
                interval = "30min"
            elif (interval == '5'):
                interval = "60min"
            else:
                print("Invalid input. Must enter a number 1-5.")
                continue
            tsString = "TIME_SERIES_INTRADAY"
            stockData = fetch_intraday_data(symbol, api_key, tsString, interval)
            timeSeriesKey = {1: f"Time Series ({interval})"}
            break        
        elif(tsChoice == '2'):
            tsString = "TIME_SERIES_DAILY"
            stockData = fetch_stock_data(symbol, api_key, tsString)
            timeSeriesKey = {2: "Time Series (Daily)"}
            break
        elif(tsChoice == '3'):
            tsString = "TIME_SERIES_WEEKLY"
            stockData = fetch_stock_data(symbol, api_key, tsString)
            timeSeriesKey = {3: "Weekly Time Series"}
            break
        elif (tsChoice == '4'):
            tsString = "TIME_SERIES_MONTHLY"
            stockData = fetch_stock_data(symbol, api_key, tsString)
            timeSeriesKey = {4: "Monthly Time Series"}
            break
        else:
            print("Invalid choice. Must enter 1. (Intraday), 2. (Daily) 3. (Weekly) 4. (Monthly)")
            continue
       
       
    #Time Series Keys
        
    # Select Start Date - Complete
    # Select End Date - Complete
    while (True):
        startDate = input("\nEnter the desired Start Date (YYYY-MM-DD): ")
        endDate = input("Enter the desired End Date (YYYY-MM-DD): ")
        try:
            parsedStartDate = datetime.strptime(startDate, "%Y-%m-%d")
            parsedEndDate = datetime.strptime(endDate, "%Y-%m-%d")
            if (parsedEndDate > parsedStartDate):
                break
            else:
                print("The end date must be after the start date.")
        except ValueError:
            print("Must input a valid date format. Ex: (YYYY-MM-DD)")
            
    
    
    if stockData:
        if (chartType == 1):
            barChart = pygal.Bar()
            barChart.title = f'Bar Char for {symbol} between {startDate} and {endDate}'
            
            dates = []
            openPrices = []
            highPrices = []
            lowPrices = []
            closePrices = []
            
            for date, data in stockData[timeSeriesKey[int(tsChoice)]].items():
                dates.append(date)
                openPrices.append(float(data['1. open']))
                highPrices.append(float(data['2. high']))
                lowPrices.append(float(data['3. low']))
                closePrices.append(float(data['4. close']))
                
            barChart.x_labels = map(str, dates)
            barChart.add('Opening Prices', openPrices)
            barChart.add('High Prices', highPrices)
            barChart.add('Low Prices', lowPrices)
            barChart.add('Closing Prices', closePrices)
            barChart.render_in_browser()
            
        elif (chartType == 2):
            lineChart = pygal.Line()
            lineChart.title = f'Line Chart for {symbol} between {startDate} and {endDate}'
            
            
            dates = []
            openPrices = []
            highPrices = []
            lowPrices = []
            closePrices = []
            for date, data in stockData[timeSeriesKey[int(tsChoice)]].items():
                dates.append(date)
                openPrices.append(float(data['1. open']))
                highPrices.append(float(data['2. high']))
                lowPrices.append(float(data['3. low']))
                closePrices.append(float(data['4. close']))
                
            lineChart.x_labels = map(str, dates)
            lineChart.add('Opening Prices', openPrices)
            lineChart.add('High Prices', highPrices)
            lineChart.add('Low Prices', lowPrices)
            lineChart.add('Closing Prices', closePrices)
            lineChart.render_in_browser()
        else:
            print("Chart type invalid.")

    # Find another stock - Complete
    while(True):
        visualizeAnother = input("Would you like to view more stock data? Press 'y' to continue, or any key to exit: ")
        if (visualizeAnother == 'y'):
            break
        else:
            loop = False
            break