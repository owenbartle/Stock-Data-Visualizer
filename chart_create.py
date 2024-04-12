#import all tools
import pygal
from datetime import datetime


#Chart creation class

class ChartMaker():
    
    @staticmethod
    def convert_date(strDate):
        if isinstance(strDate, str):
            return datetime.strptime(strDate, '%Y-%m-%d').date()
        return strDate

    @staticmethod
    def chartMaker(stockData, chartType, symbol, time_series, startDate, endDate):

        startDate = ChartMaker.convert_date(startDate) 
        endDate = ChartMaker.convert_date(endDate)    
        
        if stockData:
            chart = pygal.Bar() if chartType == "1" else pygal.Line() if chartType == "2" else None
            if not chart:
                raise ValueError("Invalid chart type")

            chart.title = f'{("Bar" if chartType == "1" else "Line")} Chart for {symbol} between {startDate} and {endDate}'
            
            dates, openPrices, highPrices, lowPrices, closePrices = [], [], [], [], []
            
            print("Stock Data:", stockData) #print statement to test if data is passed 

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


