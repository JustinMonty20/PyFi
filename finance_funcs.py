import pandas as pd
import pprint
import numpy as np
from iexfinance.stocks import get_historical_data
from iexfinance.stocks import Stock
import os
from datetime import datetime

# global variables one for the start and end parameters as well as the auth token needed to make API calls. 
beginning = datetime(2015,1,1)
finish = datetime.now()
access = os.getenv('IEX_Token')


# sec stands for security. finance term for a tradeable asset. a stock is a security. 
# need to pass in the stocks "ticker" aka the abbrevaition on trading platforms. 
def single_adj_close(sec):
    data = get_historical_data(sec, start=beginning,end=finish, output_format='pandas',token=access,)['close']
    return data

    

def simple_return(sec):
    data = single_adj_close(sec)
    simple_return = data / data.shift(1) - 1
    stock_daily_return = simple_return.mean()
    return print(f'Daily return over past 4 months {stock_daily_return * 100 :.3f}%')

print(single_adj_close('AAPL'))
