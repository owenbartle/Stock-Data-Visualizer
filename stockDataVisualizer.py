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
print("-------------------------")

# Main While Loop
loop = True
while (loop == True):
    # Get Stock Option - Complete
    symbol = input("Enter the stock symbol to search for: ")
    
    # Select Chart Type - Complete
    print("Chart Types:\n---------------------\n\t1. Bar\n\t2. Line")
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
    
    bool = True
    while(bool):
        tsChoice = input("Enter time series option (1, 2, 3, 4): ")
        if tsChoice == '1':
            interval = input("Enter time interval (1min, 5min, 15min, 30min, 60min): ")
        try:
            tsChoice = int(tsChoice)
            if(tsChoice == 1 or tsChoice == 2 or tsChoice == 3 or tsChoice == 4):
                bool = False
            else:
                raise Exception("Not a valid choice. Enter only a '1', '2', '3', or '4', Exception")
        except:
            print("Not a valid choice. Enter only a '1', '2', '3', or '4'.", Exception)
    
    tsString = ' '
        
    ##Convert user time series type to api url parameter
    if(tsChoice == 1):
        tsString = "TIME_SERIES_INTRADAY"
        fetch_intraday_data(symbol, api_key, tsString, interval)
    elif(tsChoice == 2):
        tsString = "TIME_SERIES_DAILY"
        fetch_stock_data(symbol, api_key, tsString)
    elif(tsChoice == 3):
        tsString = "TIME_SERIES_WEEKLY"
        fetch_stock_data(symbol, api_key, tsString)
    else:
        tsString = "TIME_SERIES_MONTHLY"
        fetch_stock_data(symbol, api_key, tsString)
        
       
        
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
            
    
    
    ##change user choices to api parameters
    ##variables tsString for time series option,
    ##symbol={option}
    
    ##url now queries our api using our key, searching for ouyr given symbol, and using our time series option
    
    ##this is just so we can check to see if our program will develop the correct url for querying the api
    #print(url)

    # Generate Graph and Open in Users Default Browser - In Progress
    
    #Data keys
    #Time Series (interval)
    #Time Series (Daily)
    #Weekly Time Series
    #Monthly Time Series
    
    
    
    if stockData:
        if (chartType == 1):
            barChart = pygal.Bar()
            barChart.title = f'Bar Char for {symbol} between {startDate} and {endDate}'
            dates = []
            openPrices = []
            highPrices = []
            lowPrices = []
            closePrices = []
            for date, data in stockData[tsString].items():
                dates.append(date)
                openPrices.append(float(data['1. open']))
                highPrices.append(float(data['2. high']))
                lowPrices.append(float(data['3. low']))
                closePrices.append(float(data['4. close']))
                
            barChart.x_labels = dates
            barChart.add('Opening Prices', openPrices)
            barChart.add('High Prices', highPrices)
            barChart.add('Low Prices', lowPrices)
            barChart.add('Closing Prices', closePrices)
            barChart.render_in_browser()
        elif (chartType == 2):
            lineChart = pygal.Line()
            lineChart.title = 'Line Chart'
        else:
            print("Chart type invalid.")

    # Find another stock - Complete
    while(True):
        visualizeAnother = input("Would you like to view more stock data? Press 'y' to continue : ")
        if (visualizeAnother == 'y'):
            break
        else:
            loop = False
            break