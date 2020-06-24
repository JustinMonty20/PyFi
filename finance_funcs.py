import pandas as pd
import pprint
pp=pprint.PrettyPrinter(indent=4)
import numpy as np
from alpha_vantage.timeseries import TimeSeries
import os


def single_adj_close(ticker):
    ts = TimeSeries(key=os.environ['AV_API_KEY'],output_format='pandas', outputsize='full')
    data, meta_data = ts.get_daily_adjusted(ticker)
    return (data['5. adjusted close'])
    

def simple_return(ticker):
    data = single_adj_close(ticker)
    s_return = data / data.shift(1) - 1
    stock_daily_return = s_return.mean()
    return print(f'Daily return over past 4 months {stock_daily_return * 100 :.3f}%')

single_adj_close('MSFT')
