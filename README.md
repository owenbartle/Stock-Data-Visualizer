# Project 3 : Stock-Data-Visualizer

## Description: 
- Group project building a web app that displays real-time stock data/trends for INFOTC 4320 - Software Engineering.

## Group Members:
- Owen Bartle
- Sean Moser
- Connor VanTress
- Grant Eckhardt

## Project Requirements:
- A professor in your department is interested in tracking stock data trends and recently found the Alpha Vantage website. This site offers an api that returns historical stock data from the past 20 years. The data is returned in json and other formats. There is no way to visualize the data or choose a date range to view the data. The api, by default, returns 20 years of data for all but one of its functions.

- Your team’s job is to create a python application that queries the Alpha Vantage api, and allows the user to select a date range to view the data, and the type of chart they want to view the data in. Your team should use git and GitHub as a means of version control for the project.

## The application should:

1. Ask the user to enter the stock symbol for the company they want data for.
2. Ask the user for the chart type they would like.
3. Ask the user for the time series function they want the api to use.
4. Ask the user for the beginning date in YYYY-MM-DD format.
5. Ask the user for the end date in YYYY-MM-DD format.
    - The end date should not be before the begin date
6. Generate a graph and open in the user’s default browser.
