import csv
import pandas as pd
import glob

def getData(filename):
    #df = pd.read_csv(filename, parse_dates=["Date"], skiprows=2)
    df = pd.read_csv(filename, parse_dates=["Date"])
    df = df.iloc[:, [0, -1]]
    return df

def getAllFiles():
    filelist = glob.glob("csv/"+"*.csv")
        # print(file)
    out = [getData(file) for file in filelist]
<<<<<<< HEAD
=======
    # print(out)
>>>>>>> 1abcd333db6ba286203a1dabb8a40449f6d850da
    return out


#getAllFiles()
getData("csv/IGGBR10D.csv")

