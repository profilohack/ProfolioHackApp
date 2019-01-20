from __future__ import division
import pandas as pd
import numpy as np
import datetime
from dateutil.relativedelta import relativedelta


def mean_std_year(df, num_years):
    now = datetime.datetime.today()
    years = df.loc[:, "Date"].apply(lambda x: x.year)
    years_diff = now.year - years
    return float(df[years_diff <= num_years].mean()), float(df[years_diff <= num_years].std())


def mean_std_month(df, num_months):
    now = datetime.datetime.today()
    # years = df.loc[:, "Date"].apply(lambda x: x.year)
    # months = df.loc[:, "Date"].apply(lambda x: x.month)
    # months_diff = now.month - months
    # years_equal = (years == now.year)
    # time_diff = 
    # time_diff = (now - df.loc[:, "Date"]).apply(lambda x: x.months)
    time_diff = now <= (df.loc[:, "Date"] + pd.Timedelta(days=num_months * 30))
    return float(df[time_diff].mean()), float(df[time_diff].std())

if __name__ == "__main__":
    df = pd.read_csv("IGGBR10D.csv", parse_dates=["Date"], skiprows=2)
    df = df.iloc[:, [0, 5]]
      
    
    # print(df[years_equal])
    # print(years_equal)
    # print(months)
     
    print([mean_std_year(df, num_years) for num_years in [10, 5, 3, 1]])
    print([mean_std_month(df, num_months) for num_months in [6, 3, 1]])
    # print(last_10_years, last_5_years, last_3_years, last_year, last_6_months, last_3_months, last_month)
    # pt = pd.pivot_table(df, values=["Date", "Close"], aggfunc=np.mean, columns="Date")
    # print(pt)
    # print(df[years_equal & months_diff <= 1])
