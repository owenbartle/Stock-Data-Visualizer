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
from wtforms.fields.html5 import DateField
from wtforms.validators import URL, DataRequired, Email, Equalto, Length

class Stockform(FlaskForm): 
    """Generate Your Graph."""


    """A quick copy and paste of this code below into chatgpt could and should possible 
    help us figure out how to populate the field how he wants it to be"""

    #This is where we will implement code to populate the symbol field with stock options
    symbol = SelectField("Choose Stock Symboo", [DataRequired()],
        choices=[
            ("IBM", "IBM"),
            ("GOOGL", "GOOGL")
        ],
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
