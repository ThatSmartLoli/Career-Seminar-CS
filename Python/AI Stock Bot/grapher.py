import matplotlib.pyplot as plt
import pandas as pd
import datetime as dt
import matplotlib.dates as mdates

def build_dataframes(df_trades, trade_dict, df_prices, price_dict):
    time_now = str(dt.datetime.now().time())[:8]
    df_trades.loc[time_now] = trade_dict
    df_prices.loc[time_now] = price_dict
    return df_trades, df_prices

def normlize(df):
    if len(df.shape) == 1 or df.shape[1] == 1:
        return df / df.iloc[0]
    else:
        dfNORMALIZED = pd.DataFrame()
        trading_days = df.index
        for stock in df.columns.values.tolist():
            dfNORMALIZED[stock] = pd.Series(df[stock] / df[stock].iloc[0], index=trading_days)
        return dfNORMALIZED

def active_graph(df, df_trades, ax, pause=1):
    ax.clear()
    ax.set_title('Active Graph')
    ax.set_xlabel('Time')
    ax.set_ylabel('Normalized Price')
    
    # Time formatting for the x-axis
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
    ax.xaxis.set_major_locator(mdates.MinuteLocator(interval=1))
    plt.xticks(rotation=45)
    
    # Plot each stock with its corresponding transparency based on the trade signal
    for stock in df.columns.values.tolist():
        alpha_value = 1.0 if df_trades[stock].iloc[-1] in ['HOLD', 'BUY'] else 0.2
        ax.plot(df[stock], label=stock, alpha=alpha_value)
    
    # Adding buy/sell annotations
    for day, order in df_trades.iterrows():
        for stock in df.columns.values.tolist():
            if order[stock] == 'BUY':
                ax.axvline(day, color='g', alpha=0.25)
            elif order[stock] == 'SELL':
                ax.axvline(day, color='r', alpha=0.25)
    
    # Draw and pause
    ax.legend(df.columns.values.tolist(), loc='upper left')
    plt.draw()
    plt.pause(pause)
    plt.savefig(str(dt.date.today()))