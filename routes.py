from flask import flask
from flask import current_app as app
from flask import redirect, render_template,url_for, request, flash

from .user_input import Stockform
from. chart_create import ChartMaker


from .forms import StockForm
from.charts import *

@app.route("/", methods=['GET', 'Post'])
@app.route("/stocks", methods=['GET', 'POST'])
def stocks():

    form = StockForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            symbol = request.form['symbole']
            chart_type = request.form['chart_type']
            time_series = request.form['time_series']
            start_date = convert_date(request.form['start_date'])
            end_date = convert_date(request.form['end_date'])

            if end_date <= start_date:
                err = "Error: End date cannot be earlier than Start Date"
                chart = None
            else:
                err = None

                #This is where we need to call the methods from Charts.py file and implement our code

                #This chart variable is passed to index.html to render the returned chart

                chart = "ASSIGN CHART TO THIS VARIABLE"
            return render_template("index.html", form=form, template="form-template", err = err, chart = chart)
        
        return render_template("index.html", form=form, template="form-template")