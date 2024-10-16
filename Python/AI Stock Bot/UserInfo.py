import ccxt
import robin_stocks.robinhood as rh
import config as configs
import pyotp




##########################################################################################
 ################################ Logging In To Robinhood ###############################
##########################################################################################

# Login To Robinhood
def Newlogin(days):
    time_logged_in = 60*60*24*days
    totp  = pyotp.TOTP("SFLN62VANICJJSCQ").now()
    print("Current OTP:", totp)
    log = rh.login( configs.login_User, configs.login_Password, expiresIn= time_logged_in, scope='internal', mfa_code=totp, store_session=True)
def regularLogin(days):
    time_logged_in = 60*60*24*days
    log = rh.login( configs.login_User, configs.login_Password, expiresIn= time_logged_in, scope='internal', store_session=True)




##########################################################################################
 ################################ Checking User Positions ###############################
##########################################################################################

# Check holdings
def userHoldings():
    user_stocks = rh.build_holdings()
    for key,value in user_stocks.items():
        print(key,value)

# Check Positions
def positions():
    cash_info = rh.profiles.load_account_profile()
    pos_info = rh.profiles.load_portfolio_profile()
    cash_balance = float(cash_info['cash'])
    pos_balance = float(pos_info['equity'])
    return (cash_balance, pos_balance)

def get_holdings_and_bought_price(stocks):
    holdings = {stocks[i]: 0 for i in range(0, len(stocks))}
    bought_price = {stocks[i]: 0 for i in range(0, len(stocks))}
    rh_holdings = rh.account.build_holdings()

    for stock in stocks:
        try:
            holdings[stock] = int(float((rh_holdings[stock]['quantity'])))
            bought_price[stock] = float((rh_holdings[stock]['average_buy_price']))
        except:
            holdings[stock] = 0
            bought_price[stock] = 0

    return(holdings, bought_price)
    #...
