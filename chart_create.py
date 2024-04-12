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
            date_obj = datetime.strptime(date, '%Y-%m-%d').date()
            print("Processing date:", date_obj)  # Debugging output

            if startDate <= date_obj <= endDate:
                dates.append(date)
                openPrices.append(float(data['1. open']))
                highPrices.append(float(data['2. high']))
                lowPrices.append(float(data['3. low']))
                closePrices.append(float(data['4. close']))
            else:
                print("Date out of range:", date_obj)  # Debugging output

        chart.x_labels = dates
        chart.add('Opening Prices', openPrices)
        chart.add('High Prices', highPrices)
        chart.add('Low Prices', lowPrices)
        chart.add('Closing Prices', closePrices)
        return chart.render()

            


