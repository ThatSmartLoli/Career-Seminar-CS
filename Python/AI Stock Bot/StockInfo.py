import robin_stocks.robinhood as rh
import datetime as dt
import pandas as pd


##########################################################################################
 ################################## Getting Market Time ##################################
##########################################################################################

#Finding Market Hours.
def open_market():
    market = True
    time_now = dt.datetime.now().time()
    market_open = dt.time(8,30,0)
    market_close = dt.time(15,59,0)

    if time_now > market_open and time_now < market_close:
        market = True
    else:
        print('market close')
    return(market)




##########################################################################################
 ############################# Getting and Filtering Symbols #############################
##########################################################################################

#Get Crypto Symbols
def get_crypto():
    cryptoAll = list(rh.crypto.get_crypto_currency_pairs(info="symbol"))
    cleaned_prices = [price.replace("-usd", "") for price in cryptoAll]
    return(cleaned_prices)

#Get Stocks Symbols
def get_stocks():
    stocks = list(rh.get_top_100(info='symbol'))
    filtered_stocks = filter_stocks(stocks, 10)
    #filtered_stocks = filter_25_dollar_and_under_stocks(stocks)
    #filtered_stocks = filter_50_dollar_and_under_stocks(stocks)
    #filtered_stocks = filter_100_dollar_and_under_stocks(stocks)
    #filtered_stocks = filter_150_dollar_and_under_stocks(stocks)
    #filtered_stocks = stocks
    print(filtered_stocks)
    return(filtered_stocks)

#filter Stocks Symbols
def filter_stocks(stock, price_limit):
    def filter_150_dollar_and_under_stocks(stocks, prices, filtered_stocks):
        for stock in stocks:
            current_price = prices[stock]
            if current_price <= 150:
                filtered_stocks.append(stock)

        return filtered_stocks

    def filter_100_dollar_and_under_stocks(stocks, prices, filtered_stocks):
        for stock in stocks:
            current_price = prices[stock]
            if current_price <= 100:
                filtered_stocks.append(stock)

        return filtered_stocks

    def filter_50_dollar_and_under_stocks(stocks, prices, filtered_stocks):
        for stock in stocks:
            current_price = prices[stock]
            if current_price <= 50:
                filtered_stocks.append(stock)

        return filtered_stocks

    def filter_25_dollar_and_under_stocks(stocks, prices, filtered_stocks):
        for stock in stocks:
            current_price = prices[stock]
            if current_price <= 25:
                filtered_stocks.append(stock)

        return filtered_stocks

    def filter_10_dollar_and_under_stocks(stocks, prices, filtered_stocks):
        for stock in stocks:
            current_price = prices[stock]
            if current_price <= 10:
                filtered_stocks.append(stock)

        return filtered_stocks
    
    filtered_stocks = []
    prices = get_stock_prices(stock)

    if price_limit == 150:
        return filter_150_dollar_and_under_stocks(stock, prices, filtered_stocks)
    elif price_limit == 100:
        return filter_100_dollar_and_under_stocks(stock, prices, filtered_stocks)
    elif price_limit == 50:
        return filter_50_dollar_and_under_stocks(stock, prices, filtered_stocks)
    elif price_limit == 25:
        return filter_25_dollar_and_under_stocks(stock, prices, filtered_stocks)
    elif price_limit == 10:
        return filter_10_dollar_and_under_stocks(stock, prices, filtered_stocks)
    else:
        return []

def get_stock_prices(stocks):
    prices = {}

    for stock in stocks:
        stock_info = rh.stocks.get_stock_quote_by_symbol(stock)
        current_price = float(stock_info['last_trade_price'])
        prices[stock] = current_price

    return prices

def get_historical_prices(stock, span):
        span_interval = {'day': '5minute', 'week': '10minute', 'month': 'hour'}
        interval = span_interval[span]

        historical_data = rh.stocks.get_stock_historicals(stock, interval=interval, span=span, bounds='regular')

        df = pd.DataFrame(historical_data)

        dates_times = pd.to_datetime(df.loc[:, 'begins_at'])
        close_prices = df.loc[:, 'close_price'].astype('float')

        df_price = pd.concat([close_prices, dates_times], axis=1)
        df_price = df_price.rename(columns={'close_price': stock})
        df_price = df_price.set_index('begins_at')

        return(df_price)



##########################################################################################
############################## Extra Unused Code #########################################
##########################################################################################
#Extra Code
#Pulling Current Bid And Ask From Robinhood.
def get_bid_ask(symbol):
    ph_book = rh.stocks.get_quotes(symbol)[0]
    bid_price = float(ph_book['bid_price'])
    ask_price = float(ph_book['ask_price'])
    return bid_price, ask_price

#Pulling All Stocks Symbols.
def get_all_stock_symbols(tag):
    all_stocks = rh.get_all_stocks_from_market_tag(tag)
    stock_symbols = [stock['symbol'] for stock in all_stocks if 'symbol' in stock]
    return stock_symbols
#...
