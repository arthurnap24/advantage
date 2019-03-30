from flask import Flask, request, session
from stock import Stock
import json

app = Flask(__name__)

# ghetto database
users = [ "ADragon", "Sampaguita" ]

# Don't prioritize sessions, implement buys and sells on client side
@app.route( "/login/<user>" )
def login( user ):
    if user in users:
        # buys is a list of ( share price, # of shares) bought
        # sells is a list of ( share price, # of shares) sold
        session[ "user" ] = {
            "symbol": "",
            "dateRequested": ""
            "buys": []
            "sells": []
        }
        return ( "Hi %s" % user )
    return "Not a valid user"

@app.route( "/logoff/<user>" )
def logout( user ):
    if user in users:
        session.pop( user, None )
        return ( "Bye %s" % user )
    return "Not a valid user" 

@app.route( "/stock/<symbol>" )
def request_stock( symbol ):
    date = request.args.get( "date" )
    stock = Stock( symbol=symbol, date=date )
    stock.fetch_chart()
    bars = create_bars( stock )
    result = json.dumps( bars )

    return result

def create_bars( stock ):
    opens = stock.get_open_prices()
    closes = stock.get_close_prices()
    lows = stock.get_low_prices()
    highs = stock.get_high_prices()

    bars = []

    lim = len( opens )
    for i in range( lim ):
        bar = create_bar( opens[ i ], closes[ i ], lows[ i ], highs[ i ] )
        bars.append( bar )
    
    return bars

def create_bar( open, close, low, high ):
    bar = {
        'open': open,
        'close': close,
        'low': low,
        'hight': high
    }
    return bar