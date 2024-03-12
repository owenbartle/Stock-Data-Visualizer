#import all tools
import pygal
from datetime import datetime
import requests

#add api key
api_key = 'JLFXYX4J4I20CF8E'

#method for fetching stock date - In Progress
def fetch_stock_date(symbol, api_key, url):
    #url
    #response
    #data
    return #data

# Title
print("Stock Data Visualizer")
print("-------------------------")

# Main While Loop
loop = True
while (loop == True):
    # Get Stock Option - Incomplete
    option = input("Enter the stock symbol to search for: ")
    
    # Select Chart Type - Complete
    print("Chart Types:\n---------------------\n\t1. Bar\n\t2. Line")
    while (True):
        chartType = input("Enter the type (1, 2)")
        if (chartType == '1' or chartType == '2'):
            chartType = int(chartType)
            break
        else:
            print("Must choose a valid type (1. Bar Graph | 2. Line Graph)")

    # Select Time Series Type - Complete
    print("Select the Time Series of the chart you want to Generate:")
    print("----------------------------")
    print("1. Intraday")
    print("2. Daily")
    print("3. Weekly")
    print("4. Monthly\n")
    
    bool = True
    while(bool):
        tsChoice = input("Enter time series option (1, 2, 3, 4): ")
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
        tsString = "function=TIME_SERIES_INTRADAY"
    elif(tsChoice == 2):
        tsString = "function=TIME_SERIES_DAILY"
    elif(tsChoice == 3):
        tsString = "function=TIME_SERIES_WEEKLY"
    else:
        tsString = "function=TIME_SERIES_MONTHLY"
        
       
        
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
    
    url = f"https://www.alphavantage.co/query?{tsString}&symbol={option}&apikey={api_key}"
    
    ##this is just so we can check to see if our program will develop the correct url for querying the api
    print(url)

    # Generate Graph and Open in Users Default Browser - In Progress
    if (chartType == 1):
        barChart = pygal.Bar()
        barChart.title = 'Bar Chart'
    elif (chartType == 2):
        lineChart = pygal.Line()
        lineChart.title = 'Line Chart'

    # Find another stock - Complete
    while(True):
        visualizeAnother = input("Would you like to view more stock data? Press 'y' to continue : ")
        if (visualizeAnother == 'y'):
            break
        else:
            loop = False
            break