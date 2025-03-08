from typing import Any
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import CandleChartPlot
import matplotlib.dates as mdates

# ticker select and data crawling
ticker = "QQQM"
data = yf.download(ticker, start="2024-01-01", end="2025-01-01",auto_adjust=False)
data.columns = data.columns.droplevel(1)

# data input
data_open = data.iloc[:]["Open"]
data_close = data.iloc[:]["Close"]
data_High = data.iloc[:]["High"]
data_Low = data.iloc[:]["Low"]

# 1-3 Algorithm
N = data.shape[0]
UpDn = np.zeros(N)
buySignal = np.zeros(N)
num_stock = 0
num_stock_ary = np.zeros(N)
buy_price = 0
buy_price_ary = np.zeros(N)
appraised_price_ary = np.zeros(N)
for i in range(4):
    UpDn[i] = data_close.iloc[i] > data_open.iloc[i]
for i in range(4, N):
    UpDn[i] = data_close.iloc[i] > data_open.iloc[i]
    if (UpDn[i - 4] == 1) and (UpDn[i - 3] == 0) and (UpDn[i - 2] == 0) and (UpDn[i - 1] == 0):
        buySignal[i] = 1
        num_stock += 1
        buy_price += data_open.iloc[i]
        num_stock_ary[i] = num_stock
    buy_price_ary[i] = buy_price
    appraised_price_ary[i] = num_stock * data_open.iloc[i]
appraised_price = num_stock * data_open.iloc[N - 1]

# profit calculation
deter = 0
RateOfProfit_ary = np.zeros(N)
for i in range(N):
    if buySignal[i] == 1:
        deter = 1
    if deter == 1:
        RateOfProfit_ary[i] = 100 * (appraised_price_ary[i] - buy_price_ary[i]) / buy_price_ary[i]

# buy signal generate
formatted_dates = data.index.strftime('%Y-%m-%d')
buy_day = [None] * num_stock
cnt = 0
for i in range(N):
    if buySignal[i] == 1:
        buy_day[cnt] = formatted_dates[i]
        cnt += 1
buy_signals = pd.Series(index=data.index, data=np.nan)
for date in buy_day:
    if date in buy_signals.index:
        buy_signals[date] = data.loc[date, "Close"]
# candle Chart plot
CandleChartPlot.CandleChart_buyMarking(data,buy_signals)

# My Asset plot
plt.figure(num=2)
plt.plot(data.index,RateOfProfit_ary,label='FTT')
plt.xticks(rotation=45)
plt.title("Algorithm of FridayTheThirteenth")
ax = plt.gca()
ax.xaxis.set_major_locator(mdates.AutoDateLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %d"))
plt.ylabel("The Rate of Profit [%]")
plt.grid(True)
plt.show(block=False)

# print
print("Buying Price is ", round(buy_price,2), "$")
print("appraised Price is ", round(appraised_price,2), "$")
My_RateOfProfit = 100*(appraised_price-buy_price)/buy_price
print("My rate of profit is ", round(My_RateOfProfit,2), "%")
QQQM_RateOfProfit = 100*(data_open.iloc[N-1] - data_open.iloc[0])/data_open.iloc[0]
print("QQQM's rate of profit is ", round(QQQM_RateOfProfit,2), "%")



plt.pause(3600)
