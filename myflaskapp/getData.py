import csv
import pandas as pd
import glob

def getData(filename):
    #df = pd.read_csv(filename, parse_dates=["Date"], skiprows=2)
    df = pd.read_csv(filename, parse_dates=["Date"])
    df = df.iloc[:, [0, -1]]
    return df

def getAllFiles():
    filelist = glob.glob("csv-test/"+"*.csv")
    # print(getData(file))
    
    out = [getData(file) for file in filelist]
    # for file in filelist:
    #     print(file, getData(file).shape)
    # print(out)
    return out

#getAllFiles()
# getData("csv/IGGBR10D.csv")

