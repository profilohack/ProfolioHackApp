#this module

import plotly
import re
import pandas as pd
import plotly.plotly as py
plotly.tools.set_credentials_file(username='NatashaTing', api_key='D2EsU928WZxYqs9NRPdF')
plotly.tools.set_config_file(world_readable=True,
                             sharing='public')
import plotly.graph_objs as go
import plotly.tools as tls
import cufflinks as cf
tls.embed('https://plot.ly/~cufflinks/8')

import getData

def vis(df, date, returns):
    print(plotly.__version__)
    spendingcategory = date
    amount = returns
    spendingcategory = ['Boat supply', 'eTransfer - Vacation Property rental Total', 'Hotels & Motels Total',
            'Retail - Books & Household items Total','Services - Marketing Total']
    amount = [307.47,45000,2774.79,18867.93,4234.78]

    trace = go.Pie(labels=spendingcategory, values=amount)
    py.iplot([trace], filename='batman_pie_chart')


def linechart(df, date, returns):
    # Add data
    userd = input('input string of date data separated by spaces')
    userdatelist = re.split(r'\t+', userd)
    date = userdatelist
    usere = input('input string of returns data separated by spaces')
    returns = re.split(r'\t+', usere)
    print(date)
    print(returns)
    month = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
             'August', 'September', 'October', 'November', 'December']
    df = pd.read_csv('earnings.csv')

    high_2000 = [32.5, 37.6, 49.9, 53.0, 69.1, 75.4, 76.5, 76.6, 70.7, 60.6, 45.1, 29.3]
    low_2000 = [13.8, 22.3, 32.5, 37.2, 49.9, 56.1, 57.7, 58.3, 51.2, 42.8, 31.6, 15.9]
    high_2007 = [36.5, 26.6, 43.6, 52.3, 71.5, 81.4, 80.5, 82.2, 76.0, 67.3, 46.1, 35.0]
    low_2007 = [23.6, 14.0, 27.0, 36.8, 47.6, 57.7, 58.9, 61.2, 53.3, 48.5, 31.0, 23.6]
    high_2014 = [28.8, 28.5, 37.0, 56.8, 69.7, 79.7, 78.5, 77.8, 74.1, 62.6, 45.3, 39.9]
    low_2014 = [12.7, 14.3, 18.6, 35.5, 49.9, 58.0, 60.0, 58.6, 51.7, 45.2, 32.2, 29.1]

    # Create and style traces

    FTSE = go.Scatter(
        x=date,
        y=returns,
        name='UK FTSE 100 Index w GFD Extension',
        line=dict(
            color=('rgb(205, 12, 24)'),
            width=4)
    )
    trace1 = go.Scatter(
        x=month,
        y=low_2014,
        name='Low 2014',
        line=dict(
            color=('rgb(22, 96, 167)'),
            width=4, )
    )
    trace2 = go.Scatter(
        x=month,
        y=high_2007,
        name='High 2007',
        line=dict(
            color=('rgb(205, 12, 24)'),
            width=4,
            dash='dash')  # dash options include 'dash', 'dot', and 'dashdot'
    )
    trace3 = go.Scatter(
        x=month,
        y=low_2007,
        name='Low 2007',
        line=dict(
            color=('rgb(22, 96, 167)'),
            width=4,
            dash='dash')
    )
    trace4 = go.Scatter(
        x=month,
        y=high_2000,
        name='High 2000',
        line=dict(
            color=('rgb(205, 12, 24)'),
            width=4,
            dash='dot')
    )
    trace5 = go.Scatter(
        x=month,
        y=low_2000,
        name='Low 2000',
        line=dict(
            color=('rgb(22, 96, 167)'),
            width=4,
            dash='dot')
    )
    data = [FTSE]

    # Edit the layout
    layout = dict(title='UK FTSE 100 Index w GFD Extension - monthly returns',
                  xaxis=dict(title='Month'),
                  yaxis=dict(title='Returns'),
                  )

    fig = dict(data=data, layout=layout)
    py.iplot(fig, filename='styled-line')

def getSeries():
    df = getData.getData("csv/IGGBR10D.csv")
    #data = list_of_df[0]
    date = df.iloc[:, [0]]
    returns = df.iloc[:, [1]]
    linechart(df, date, returns)

getSeries()