import pandas as pd
import robin_stocks.robinhood as rh
import StockInfo as SI

class trader():

    def __init__(self, stocks):
        self.stocks = stocks
        self.run_time = 0
        self.buffer = 0.005
        self.sma_hour = {stocks[i]: 0 for i in range(0, len(stocks))}
        self.price_sma_hour = {stocks[i]: 0 for i in range(0, len(stocks))}

    def get_sma(self, stock, df_prices, window=9):
        sma = df_prices.rolling(window=window, min_periods = window).mean()
        sma = round(float(sma[stock].iloc[-1]),4)
        return(sma)
    
    def get_price_sma(self, price, sma):
        #print(f"Price: {price}")
        #print(f"SMA: {sma}")
        price_sma = round(price/sma, 4)
        return(price_sma)
        
    def trade_option(self, stock, price):
        if self.run_time % (5) == 0:
            df_hist_prices = SI.get_historical_prices(stock,span='day')
            #print(df_hist_prices)
            self.sma_hour[stock] = self.get_sma(stock, df_hist_prices[-9:], window=9)
            #print(f"Price: {price}")
            #print(f"SMA HOUR: {self.sma_hour[stock]}")
        self.price_sma_hour[stock] = self.get_price_sma(price, self.sma_hour[stock])
    
        i1 = "BUY" if self.price_sma_hour[stock] < (1.0 - self.buffer) else 'SELL' if self.price_sma_hour[stock] > (1.0 + self.buffer) else "NONE"
        if i1 == "BUY":
            trade="BUY"
            self.run_time += 1
        elif i1 == "SELL":
            trade = "SELL"
            if self.run_time >= 1:
                self.run_time -=1
        else:
            trade = "HOLD"
        return(trade)
        