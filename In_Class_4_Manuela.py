import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np
import pandas as pd
import yfinance as yf


DEFAULT_START = dt.date.isoformat(dt.date.today() - dt.timedelta(365))
DEFAULT_END = dt.date.isoformat(dt.date.today())

class Stock:
    def __init__(self, symbol, start=DEFAULT_START, end=DEFAULT_END):
        self.symbol = symbol
        self.start = start
        self.end = end
        self.data = self.get_data()

    def get_data(self):
        data = yf.download(self.symbol, start=self.start, end=self.end)
        data.index = pd.DatetimeIndex(data.index)
        self.calc_returns(data)
        return data

    def calc_returns(self, data):
        data["Change"] = data["Close"].diff()
        data["Instant Return"] = np.log(data["Close"]).diff().round(4)

    def plot_return_dist(self):
        plt.hist(self.data["Instant Return"] * 100, bins=30, color="pink", edgecolor="white")
        plt.show()

    def plot_performance(self):
        self.data["Percent Gain/Loss"] = (self.data["Close"] / self.data["Close"].iloc[0]) - 1
        plt.plot(self.data.index, self.data["Percent Gain/Loss"] * 100, color="pink")
        plt.show()

def main():
    test = Stock("MSFT", "2023-01-01", "2023-06-30")
    print(test.data)
    test.plot_return_dist()
    test.plot_performance()

if __name__ == '__main__':
    main()