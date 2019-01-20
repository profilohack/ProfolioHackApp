import plotly
import plotly.graph_objs as go
import plotly.tools as tls
import cufflinks as cf
tls.embed('https://plot.ly/~cufflinks/8')

import getData

def vis(df, date, returns):
    print(plotly.__version__)
    df = cf.datagen.lines()
    df.iplot(kind='scatter', filename='cufflinks/cf-simple-line')


def getSeries():
    df = getData.getData("csv/IGGBR10D.csv")
    #data = list_of_df[0]
    date = df.iloc[:, [0]]
    returns = df.iloc[:, [1]]
    vis(df, date, returns)

getSeries()