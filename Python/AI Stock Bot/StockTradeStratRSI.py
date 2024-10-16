import StockInfo as SI
import robin_stocks.robinhood as rh


class RSITrader:
    
    def __init__(self, stocks, rsi_period=14, rsi_overbought=70, rsi_oversold=30):
        self.stocks = stocks
        self.rsi_period = rsi_period
        self.rsi_overbought = rsi_overbought
        self.rsi_oversold = rsi_oversold
        
        self.rsi_values = {stock: 0 for stock in stocks}
        self.prev_rsi_values = {stock: None for stock in stocks}
        self.price_rsi = {stock: 0 for stock in stocks}

    def calculate_rsi(self, stock, df_prices):
        delta = df_prices.diff()
        gain = delta.where(delta > 0, 0).rolling(window=self.rsi_period).mean()
        loss = -delta.where(delta < 0, 0).rolling(window=self.rsi_period).mean()
        
        rs = gain / loss
        rsi = 100 - (100 / (1 + rs))
        
        rsi_value = rsi.iloc[-1]
        return round(rsi_value, 2)
    
    def check_rsi_crossing(self, stock, current_rsi):
        prev_rsi = self.prev_rsi_values[stock]
        
        if prev_rsi is None:
            return
    
        if prev_rsi < 50 and current_rsi > 50:
            print(f"{stock} RSI crossed above 50! Current RSI: {current_rsi}")
        elif prev_rsi > 50 and current_rsi < 50:
            print(f"{stock} RSI crossed below 50! Current RSI: {current_rsi}")
        
        self.prev_rsi_values[stock] = current_rsi
    
    def trade_option(self, stock, price):
        df_hist_prices = SI.get_historical_prices(stock, span='day')
        self.rsi_values[stock] = self.calculate_rsi(stock, df_hist_prices[stock])
        
        rsi = self.rsi_values[stock]
        
        if rsi < self.rsi_oversold:
            trade = "BUY"
        elif rsi > self.rsi_overbought:
            trade = "SELL"
        else:
            trade = "HOLD"
        
        return trade