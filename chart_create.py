#import all tools
import pygal
from datetime import datetime


#Chart creation class

class ChartMaker():

    def chartMaker(stockData, chartType, symbol, tsChoice, startDate, endDate):

        if stockData:

            timeSeriesKey = {}
            if tsChoice == 1:
                timeSeriesKey = {1: f"Time Series ({"60min"})"}
            elif tsChoice == 2: 
                timeSeriesKey = {2: "Time Series (Daily)"}
            elif tsChoice == 3:
                timeSeriesKey = {3: "Weekly Time Series"}
            else:
                timeSeriesKey = {4: "Monthly Time Series"}

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

                lineChart.x_labels = dates
                lineChart.add('Opening Prices', openPrices)
                lineChart.add('High Prices', highPrices)
                lineChart.add('Low Prices', lowPrices)
                lineChart.add('Closing Prices', closePrices)
                lineChart.render_in_browser()
            else:
                print("Chart type invalid.")

