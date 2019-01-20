from __future__ import division
import pandas as pd
import numpy as np
from decimal import Decimal


def convert(s):
    a = Decimal(s[1:-1])
    return -a


def suggest(df, customer_name):
    net_income = df[df.loc[:, "Account"] == customer_name].loc[:, "Total Amount"].sum()
    suggested_amount = (Decimal(0.5) * net_income / Decimal(12))
    print("{}, I suggest you invest ${:2f} per month".format(customer_name, suggested_amount))
    return suggested_amount, net_income

if __name__ == "__main__":
    df = pd.read_csv("SampleTransactionDataset.csv",  converters={
            "Spending": convert,
            "Income": Decimal
        }
        )
    df = df.iloc[:, :-2]
    # df.loc[:, "Spending"] = df.loc[:, "Spending"][1:-1]
    df.loc[:, "Total Amount"] = df.loc[:, "Spending"] + df.loc[:, "Income"]
    # df.to_csv("df.csv")
    # print(df)
    # print(df[df.loc[:, "Account"] == "Bat Man"])
    pt = pd.pivot_table(df, values=["Income", "Spending", "Total Amount"], index=["Account", "Month"], aggfunc=np.sum)
    print(pt)
    suggest(df, "Bat Man")
    suggest(df, "Bob The Builder")
    suggest(df, "Jerry Maguire")
