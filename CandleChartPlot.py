def CandleChart(data):

    import mplfinance as mpf
    import matplotlib.pyplot as plt

    #ticker = "QQQM"
    #data = yf.download(ticker, start="2024-03-08", end="2024-04-25",auto_adjust=False)
    #data.columns = data.columns.droplevel(1)

    mc = mpf.make_marketcolors(
        up='red',  # 양봉(상승) → 빨강
        down='blue',  # 음봉(하락) → 파랑
        edge='black',  # 캔들 테두리는 기본값 유지
        wick='black',  # 심지는 기본값 유지
        volume='inherit'  # 거래량 색상은 기본값 유지
    )
    custom_style = mpf.make_mpf_style(marketcolors=mc)

    fig, _ = mpf.plot(
        data,
        type="candle",
        volume=True,
        title="QQQM Candlestick Chart",
        style=custom_style,
        returnfig = True
    )
    plt.figure(num=1)
    plt.show(block=False)
    #plt.pause(3600)


def CandleChart_buyMarking(data,buy_signals):

    import mplfinance as mpf
    import matplotlib.pyplot as plt

    mc = mpf.make_marketcolors(
        up='red',  # 양봉(상승) → 빨강
        down='blue',  # 음봉(하락) → 파랑
        edge='black',  # 캔들 테두리는 기본값 유지
        wick='black',  # 심지는 기본값 유지
        volume='inherit'  # 거래량 색상은 기본값 유지
    )
    custom_style = mpf.make_mpf_style(marketcolors=mc)

    ap_buy = mpf.make_addplot(
        buy_signals,
        scatter=True,
        marker="^",
        markersize=75,
        color="blue",
        label="Buy Signal"
    )

    fig, _ = mpf.plot(
        data,
        type="candle",
        volume=True,
        title="QQQM Candlestick Chart",
        style=custom_style,
        returnfig = True,
        addplot=ap_buy
    )
    plt.figure(num=1)
    plt.show(block=False)
    #plt.pause(3600)
    ap_buy = mpf.make_addplot(buy_signals, scatter=True, marker="^", markersize=100, color="blue", label="Buy Signal")
