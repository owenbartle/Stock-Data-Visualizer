from flask import Flask
from flask import current_app as app
from flask import redirect, render_template, url_for, request, flash

from user_input import Stockform
from chart_create import ChartMaker
from ourAPI import DataFetching

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
@app.route("/stocks", methods=['GET', 'POST'])
def stocks():

    form = Stockform()
    if request.method == 'POST':

        if form.validate_on_submit():

            #Get the form data from the user
            #Then use it to query the API
            symbol = request.form['symbol']
            chart_type = request.form['chart_type']
            time_series = request.form['time_series']
            start_date = ChartMaker.convert_date(request.form['start_date'])
            end_date = ChartMaker.convert_date(request.form['end_date'])

            if end_date <= start_date:
                #Generate error message as past to the page
                err = "ERROR: End date cannot be earlier thatn start date."
                chart = None
            else: 
                #Query our api with the form data
                if time_series == 1:
                    data = DataFetching.fetch_intraday_data(symbol, 'JLFXYX4J4I20CF8E', time_series, '60min')
                else:
                    data = DataFetching.fetch_stock_data(symbol, 'JLFXYX4J4I20CF8E', time_series)
                """Insert API call code"""

                err = None
                chart = ChartMaker.chartMaker(data, chart_type, symbol, time_series, start_date, end_date)
            
            return render_template("index.html", form=form, template="form-template", err = err, chart = chart)
    
    return render_template("index.html", form = form, template="form-template")


if __name__ == '__main__':
    app.run(debug=True)