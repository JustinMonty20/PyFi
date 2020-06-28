import pandas as pd
import numpy as np
from pandas_datareader import data as wb

# global variable to indicate the start date we are grabbing the financial data
# along with where the data is coming from. 
start = '2010-1-1'
yahoo = 'yahoo'

# all data is gathered from the Yahoo Finance through the pandas_datareader package.
# sec stands for security. finance term for a tradeable asset. a stock is a security. 
# need to pass in the stocks "ticker" aka the abbrevaition on pretty much all trading platforms. 

def single_adj_close(sec):
    # this functions returns the Adj Close column of the security you pass in.
    # the Adj Close column is the data we need for all of the financial calculations we will be doing. 
    data = wb.DataReader(sec,start=start,data_source=yahoo)['Adj Close']
    return data



    
# annual simple return of the passed in security. 
def simple_return(sec):
    data = single_adj_close(sec)
    simple_return = data / data.shift(1) - 1
    stock_annual_return = simple_return.mean() * 250
    return print(f'Annual simple return {stock_annual_return * 100 :.3f}%')

simple_return('MSFT')
