import robin_stocks.robinhood as rh
import time
import pandas as pd

import StockTradeStratRSI as RSI
import stockTradeStratSMA as STS

import StockInfo as si
import UserInfo as ui

import ordering as o
import grapher as g

if __name__ == "__main__":

    #Logging Into Robinhood
    ui.Newlogin(days=1)


    #Get Stock Symbols.
    stocks = si.get_stocks()


    #Setting Up Strats
    ts = STS.trader(stocks)
    tsRSI = RSI.RSITrader(stocks)


    #populate Graph
    trade_dict = {stocks[i]: 0 for i in range(0, len(stocks))}
    price_dict = {stocks[i]: 0 for i in range(0, len(stocks))}
    df_trades = pd.DataFrame(columns=stocks)
    df_prices = pd.DataFrame(columns=stocks)
    

    #Bot Loops Until The Market Closes.
    while si.open_market():


         #get Account worth and Equity
        cash, equity = ui.positions()


        #Stock Price
        prices = rh.stocks.get_latest_price(stocks)


        #User Holdings and Bought At Price
        holdings, bought_price = ui.get_holdings_and_bought_price(stocks)

        count = 0
        #For Each Stock In Sotcks
        for i, stock in enumerate(stocks):
            price = float(prices[i])
            print()
                count += 1
                print(count)
                #Do Trade Tests
                tradeRSI =  tsRSI.trade_option(stock, price)
                tradeSMA = ts.trade_option(stock, price)


                #Check if Each Tests have the same Signals
                if tradeRSI != tradeSMA:
                    trade = 'WAIT'
                elif tradeSMA == tradeRSI:
                    if tradeSMA == "BUY":
                        trade = 'BUY'
                    else:
                        trade = 'SELL'


                #Buy and Sell Functions
                if trade == "BUY":
                    allowable_holdings = int((cash/10)/price)
                    print(cash)
                    if allowable_holdings > 5 and holdings[stock] == 0:
                        #o.limit_Buy_Order(stock, allowable_holdings, price)
                        print('### Trying to BUY {} with {} amount at ${}.'.format(stock, allowable_holdings, price))
                    elif allowable_holdings < 5:
                        print('### Trying to BUY {} with {} amount at ${}, but failed.'.format(stock, allowable_holdings, price))
                elif trade == "SELL":
                    if holdings[stock] > 0:
                        #o.limit_Sell_Order(stock, holdings[stock], price)
                        print('### Trying to SELL {} at ${}.'.format(stock, price))
                
            


                #Getting Hold or Wait signals.
                price_dict[stock] = price
                if holdings[stock] > 0 and trade != "SELL":
                    trade = "HOLD"
                elif holdings[stock] == 0 and trade != "BUY":
                    trade = 'WAIT'
                trade_dict[stock] = trade

        #Building Graph
        df_trades, df_prices = g.build_dataframes(df_trades, trade_dict, df_prices, price_dict)
        g.active_graph(g.normlize(df_prices), df_trades)
        

        #Refreash Each min
        time.sleep(60)


    #logout of Robinhood
    rh.logout()

