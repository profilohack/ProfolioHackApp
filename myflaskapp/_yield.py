from __future__ import division
import pandas as pd
import numpy as np
from getData import getAllFiles
import datetime
from dateutil.relativedelta import relativedelta

df = pd.read_csv("IGGBR10D.csv", parse_dates=["Date"], skiprows=2)
df = df.iloc[:, [0, 5]]
returns = getAllFiles()

def mean_var_year(df, num_years):
    now = datetime.datetime.today()
    years = df.loc[:, "Date"].apply(lambda x: x.year)
    years_diff = now.year - years
    return float(df[years_diff <= num_years].mean()), float(df[years_diff <= num_years].var())


def mean_var_month(df, num_months):
    now = datetime.datetime.today()
    # years = df.loc[:, "Date"].apply(lambda x: x.year)
    # months = df.loc[:, "Date"].apply(lambda x: x.month)
    # months_diff = now.month - months
    # years_equal = (years == now.year)
    # time_diff = 
    # time_diff = (now - df.loc[:, "Date"]).apply(lambda x: x.months)
    time_diff = now <= (df.loc[:, "Date"] + pd.Timedelta(days=num_months * 30))
    return float(df[time_diff].mean()), float(df[time_diff].var())

def covar(returns):
    
    # print(len(returns)) 11 20
    # np_returns = [ret.iloc[:, -1].values for ret in list(returns[11]) + list(returns[20])]
    # TODO
    if len(returns) == 1:
        return np.asarray([1])
    # a1 = returns[11].iloc[:, -1].values
    # a2 = returns[20].iloc[:, -1].values
    # np_returns = np.asarray([a1, a2])
    np_returns = [ret.iloc[:, -1].values for ret in returns]
    # for ret in np_returns:
    #     print(ret.shape)
    omega = np.cov(np_returns)
    mu = np.array(np.mean(np_returns, axis=1))
    # print(omega.shape, mu.shape, mu.T @ omega)

    #
    a = np.ones(mu.shape).T @ np.linalg.solve(omega, np.ones(mu.shape))
    b = np.ones(mu.shape).T @ np.linalg.solve(omega, mu)
    c = mu.T @ np.linalg.solve(omega, mu)
    delta = a * c - b * b
    # TODO what is mu_p?
    mu_p = b / a
    lambda_1 = (c - b * mu_p) / delta
    lambda_2 = (a * mu_p - b) / delta

    weights = np.linalg.solve(omega, lambda_1 * np.ones(mu.shape) + lambda_2 * mu)
    # print(sum(weights)
    return weights

if __name__ == "__main__":
    # print(df[years_equal])
    # print(years_equal)
    # print(months)
    
    # print([mean_var_year(df, num_years) for num_years in [10, 5, 3, 1]])
    # print([mean_var_month(df, num_months) for num_months in [6, 3, 1]])
    covar(returns)
    # print(last_10_years, last_5_years, last_3_years, last_year, last_6_months, last_3_months, last_month)
    # pt = pd.pivot_table(df, values=["Date", "Close"], aggfunc=np.mean, columns="Date")
    # print(pt)
    # print(df[years_equal & months_diff <= 1])
