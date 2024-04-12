#import all tools
import pygal
from datetime import datetime


#Chart creation class

class ChartMaker():
    
    @staticmethod
    def convert_date(strDate):
        return datetime.strptime(strDate, '%Y-%m-%d').date()

    @staticmethod
    def chartMaker(stockData, chartType, symbol, time_series, startDate, endDate):

        ## code below is for testing for solving current time series error
        print(stockData)    
        
        if stockData:

            if chartType == "1":
                barChart = pygal.Bar()
                barChart.title = f'Bar Chart for {symbol} between {startDate} and {endDate}'
            elif chartType == "2":
                lineChart = pygal.Line()
                lineChart.title = f'Line Chart for {symbol} between {startDate} and {endDate}'
            else:
                print("Chart type invalid.")
                return

            dates = []
            openPrices = []
            highPrices = []
            lowPrices = []
            closePrices = []

            filtered_data = {}
            for date, data in stockData.get(time_series, {}).items():
                if startDate <= datetime.strptime(date, '%Y-%m-%d').date() <= endDate:
                    filtered_data[date] = data

            print(filtered_data)

            for date, data in stockData.get(time_series, {}).items():
                dates.append(date)
                openPrices.append(float(data['1. open']))
                highPrices.append(float(data['2. high']))
                lowPrices.append(float(data['3. low']))
                closePrices.append(float(data['4. close']))

            if chartType == "1":
                barChart.x_labels = dates
                barChart.add('Opening Prices', openPrices)
                barChart.add('High Prices', highPrices)
                barChart.add('Low Prices', lowPrices)
                barChart.add('Closing Prices', closePrices)
                # return barChart
                barChart.render_in_browser()
            elif chartType == "2":
                lineChart.x_labels = dates
                lineChart.add('Opening Prices', openPrices)
                lineChart.add('High Prices', highPrices)
                lineChart.add('Low Prices', lowPrices)
                lineChart.add('Closing Prices', closePrices)
                # return lineChart
                lineChart.render_in_browser()


