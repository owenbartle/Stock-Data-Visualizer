#import all tools
import pygal
from datetime import datetime

# Imports of helper files
import user_input
import ourAPI

#Instantiate helper classes
usrs = user_input.UserInputs
api = ourAPI.DataFetching

# api key
api_key = 'JLFXYX4J4I20CF8E'

# Title
print("Stock Data Visualizer")
print("-------------------------\n")


# Main While Loop
loop = True
while (loop == True):

    # Get Stock Option - Complete
    symbol = input("Enter the stock symbol to search for: ")
    
    #Check that the given stock ticker is valid
    if usrs.check_stock(symbol, api_key) == False:
        print("It does not seem that this ticker symbol points to an existing stock. Please try again")
        loop = True
        continue
    else:
        print('The ticker symbol ' + symbol + ' is valid')


    # Select Chart Type 
    chartType = usrs.selectChartType()


    # Select Time Series Type
    timeSeriesKey = {}
    stockData = None

    stockData, timeSeriesKey, tsChoice = usrs.selectTimeSeries(symbol, api_key)
        

    # Select start and end date
    startDate, endDate, parsedStartDate, parsedEndDate = usrs.getDate()

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
            
            ##same fix for 
            dates = []
            openPrices = []
            highPrices = []
            lowPrices = []
            closePrices = []
            
            for date, data in stockData[timeSeriesKey[int(tsChoice)]].items():
                if parsedStartDate <= datetime.strptime(date, "%Y-%m-%d") <= parsedEndDate:
                    dates.append(date)
                    openPrices.append(float(data['1. open']))
                    highPrices.append(float(data['2. high']))
                    lowPrices.append(float(data['3. low']))
                    closePrices.append(float(data['4. close']))

          
            ##for date, data in stockData[timeSeriesKey[int(tsChoice)]].items():
             ##   dates.append(date)
              ##  openPrices.append(float(data['1. open']))
               ## highPrices.append(float(data['2. high']))
                ##lowPrices.append(float(data['3. low']))
                ##closePrices.append(float(data['4. close']))
                
            barChart.x_labels = dates
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
                if parsedStartDate <= datetime.strptime(date, "%Y-%m-%d") <= parsedEndDate:
                    dates.append(date)
                    openPrices.append(float(data['1. open']))
                    highPrices.append(float(data['2. high']))
                    lowPrices.append(float(data['3. low']))
                    closePrices.append(float(data['4. close']))

            # for date, data in stockData[timeSeriesKey[int(tsChoice)]].items():
            #     dates.append(date)
            #     openPrices.append(float(data['1. open']))
            #     highPrices.append(float(data['2. high']))
            #     lowPrices.append(float(data['3. low']))
            #     closePrices.append(float(data['4. close']))
                
            lineChart.x_labels = dates
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