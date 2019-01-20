import plotly

import plotly.plotly as py
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
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


def getSeries():
    df = getData.getData("csv/IGGBR10D.csv")
    #data = list_of_df[0]
    date = df.iloc[:, [0]]
    returns = df.iloc[:, [1]]
    vis(df, date, returns)

getSeries()