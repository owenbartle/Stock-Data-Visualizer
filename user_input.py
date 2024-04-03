import requests
from datetime import datetime

import ourAPI

# Instantiate the ourAPI class object
api = ourAPI.DataFetching

class UserInputs:

    #Function that checks stock ticker validity
    def check_stock(symbol, apiKey):

        response = requests.get(url='https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=' + symbol + '&interval=5min&apikey=' + apiKey)
        data = response.json()

        if 'Error Message' in data:
            return False
        else: 
            return True

    # Select Chart Type - Complete
    def selectChartType():

        print("\nChart Types:\n---------------------\n\t1. Bar\n\t2. Line")

        while (True):

            chartType = input("Enter the type (1, 2): ")

            if (chartType == '1' or chartType == '2'):
                chartType = int(chartType)
                return chartType
            
            else:
                print("Must choose a valid type (1. Bar Graph | 2. Line Graph)")


    # Select Time Series Type - Complete
    def selectTimeSeries(symbol, api_key):

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
                return api.fetch_intraday_data(symbol, api_key, tsString, interval), {1: f"Time Series ({interval})"}, tsChoice

            elif(tsChoice == '2'):
                tsString = "TIME_SERIES_DAILY"
                return api.fetch_stock_data(symbol, api_key, tsString), {2: "Time Series (Daily)"}, tsChoice

            elif(tsChoice == '3'):
                tsString = "TIME_SERIES_WEEKLY"
                return api.fetch_stock_data(symbol, api_key, tsString), {3: "Weekly Time Series"}, tsChoice

            elif (tsChoice == '4'):
                tsString = "TIME_SERIES_MONTHLY"
                return api.fetch_stock_data(symbol, api_key, tsString), {4: "Monthly Time Series"}, tsChoice
        
            else:
                print("Invalid choice. Must enter 1. (Intraday), 2. (Daily) 3. (Weekly) 4. (Monthly)"), tsChoice
                continue


    def getDate():

        while (True):
            startDate = input("\nEnter the desired Start Date (YYYY-MM-DD): ")
            endDate = input("Enter the desired End Date (YYYY-MM-DD): ")
            try:
                parsedStartDate = datetime.strptime(startDate, "%Y-%m-%d")
                parsedEndDate = datetime.strptime(endDate, "%Y-%m-%d")
                if (parsedEndDate > parsedStartDate):
                    return startDate, endDate, parsedStartDate, parsedEndDate
                else:
                    print("The end date must be after the start date.")
            except ValueError:
                print("Must input a valid date format. Ex: (YYYY-MM-DD)")