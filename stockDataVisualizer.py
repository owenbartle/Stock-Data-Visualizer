#import all tools
import pygal
from datetime import datetime
import requests

#add api key
api_key = 'JLFXYX4J4I20CF8E'

#method for fetching stock date - In Progress
def fetch_stock_date(symbol, api_key):
    #url
    #response
    #data
    return #data

# Title
print("Stock Data Visualizer")
print("---------------------")

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

    # Select Time Series Type - Incomplete

    # Select Start Date - Complete
    # Select End Date - Complete
    while (True):
        startDate = input("Enter the desired Start Date (YYYY-MM-DD): ")
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