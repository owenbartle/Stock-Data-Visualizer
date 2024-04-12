"""Form class decleration"""
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import (
    DateField, 
    PasswordField,
    SelectField,
    StringField,
    SubmitField,
    TextAreaField,
)
from datetime import date
from wtforms.fields import DateField
from wtforms.validators import URL, DataRequired, Email, EqualTo, Length
import csv

##holds stock symbols from csv, so program doesnt have to dedicate memory to 
##getting tickers each time, tickers preloaded into app
tickers = []


with open('symbols.csv', newline='') as symbols:
    reader = csv.reader(symbols)
    next(reader)
    for row in reader:
        tickers.append(row[0])
        

class Stockform(FlaskForm): 
    """Generate Your Graph."""


    """A quick copy and paste of this code below into chatgpt could and should possible 
    help us figure out how to populate the field how he wants it to be"""

    #This is where we will implement code to populate the symbol field with stock options
    ##implements tickers array so symbol field can be chosen among the ticker options
    symbol = SelectField("Choose Stock Symbol", [DataRequired()],
        choices=[(ticker, ticker) for ticker in tickers]
    )


    chart_type = SelectField("Select Chart Type", [DataRequired()],
        choices=[
            ("1", "1. Bar"),
            ("2", "2. Line"),
        ], 
    )
        
    time_series = SelectField("Select Time Series", [DataRequired()],
        choices=[
            ("1", "1. Intraday"),
            ("2", "2. Daily"),
            ("3", "3. Weekly"),
            ("4", "4. Monthly")
        ]
    )

    start_date = DateField("Enter Start Date")
    end_date = DateField("Enter End Date")
    submit = SubmitField("Submit")
