import ccxt
import robin_stocks.robinhood as rh
import UserInfo as UI


##########################################################################################
 ##################################### Limit Orders #####################################
##########################################################################################

def limit_Buy_Order(stock, allowable_holdings, price):
    limit_Buy_price = round((price+0.10), 2)
    limit_Buy = rh.orders.order_buy_limit(symbol=stock, quantity=allowable_holdings, limitPrice=limit_Buy_price, timeInForce='gfd')
    print(f"Made a Order {limit_Buy}")
    
def limit_Sell_Order(stock, pos_Size, price):
    limit_Sell_price = round((price-0.10), 2)
    limit_Sell = rh.orders.order_sell_limit(symbol=stock,quantity=pos_Size, limitPrice=limit_Sell_price, timeInForce='gfd')
    print(f"Made a Order {limit_Sell}")
