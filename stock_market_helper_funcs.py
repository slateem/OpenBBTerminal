
from pytz import timezone
from holidays import US as holidaysUS
from datetime import datetime, time as Time
import matplotlib
import matplotlib.pyplot as plt

# -----------------------------------------------------------------------------------------------------------------------
def check_positive(value):
    ivalue = int(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError(f"{value} is an invalid positive int value")
    return ivalue


# -----------------------------------------------------------------------------------------------------------------------
def valid_date(s):
    try:
        return datetime.strptime(s, "%Y-%m-%d")
    except ValueError:
        raise argparse.ArgumentTypeError("Not a valid date: {s}")


# -----------------------------------------------------------------------------------------------------------------------
def plot_view_stock(df, symbol):
    pfig, axVolume = plt.subplots()
    plt.bar(df.index, df.iloc[:, -1], color='k', alpha=0.8, width=.3)
    plt.ylabel('Volume')
    axPrice = axVolume.twinx()
    plt.plot(df.index, df.iloc[:, :-1])
    plt.title(symbol + ' (Time Series)')
    plt.xlim(df.index[0], df.index[-1])
    plt.xlabel('Time')
    plt.ylabel('Share Price ($)')
    plt.legend(df.columns)
    plt.grid(b=True, which='major', color='#666666', linestyle='-')
    plt.minorticks_on()
    plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
    plt.show()
    print("")


# -----------------------------------------------------------------------------------------------------------------------
def plot_stock_ta(df_stock, s_ticker, df_ta, s_ta):
    plt.plot(df_stock.index, df_stock.values)
    plt.plot(df_ta.index, df_ta.values)
    plt.title(f"{s_ta} on {s_ticker}")
    plt.xlim(df_stock.index[0], df_stock.index[-1])
    plt.xlabel('Time')
    plt.ylabel('Share Price ($)')
    plt.legend([s_ticker, s_ta])
    plt.grid(b=True, which='major', color='#666666', linestyle='-')
    plt.minorticks_on()
    plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
    plt.show()
    print("")


# -----------------------------------------------------------------------------------------------------------------------
def plot_ta(s_ticker, df_ta, s_ta):
    plt.plot(df_ta.index, df_ta.values)
    plt.title(f"{s_ta} on {s_ticker}")
    plt.xlim(df_ta.index[0], df_ta.index[-1])
    plt.xlabel('Time')
    #plt.ylabel('Share Price ($)')
    #if isinstance(df_ta, pd.DataFrame):
    #    plt.legend(df_ta.columns)
    plt.grid(b=True, which='major', color='#666666', linestyle='-')
    plt.minorticks_on()
    plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
    plt.show()
    print("")


# -----------------------------------------------------------------------------------------------------------------------
def b_is_stock_market_open():
    ''' checks if the stock market is open '''
    # Get current US time
    now = datetime.now(timezone('US/Eastern'))
    # Check if it is a weekend
    if now.date().weekday() > 4:
        return False
    # Check if it is a holiday
    if now.strftime('%Y-%m-%d') in holidaysUS():
        return False
    # Check if it hasn't open already
    if now.time() < Time(hour=9, minute=30, second=0):
        return False
    # Check if it has already closed
    if now.time() > Time(hour=16, minute=0, second=0):
        return False
    # Otherwise, Stock Market is open!
    return True

