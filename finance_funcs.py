import pandas as pd
import numpy as np
import pandas_datareader.data as wb

# all figures returned are percentages

# global variable to indicate the start date we are grabbing the financial data
# along with where the data is coming from. 
start = '2010-1-1'
yahoo = 'yahoo'

# all data is gathered from the Yahoo Finance through the pandas_datareader package.
# sec stands for security. finance term for a tradeable asset. a stock is a security. 
# need to pass in the stocks "ticker" aka the abbrevaition on pretty much all trading platforms. 
def data_reader(*securities):
    data = pd.DataFrame()
    for item in securities:
        data[item] = wb.DataReader(item,start=start,data_source=yahoo)['Adj Close']
    return data

# function to get rid of some typing. 
def shifted(data):
    return (data / data.shift(1))


# annual simple return of the passed in security. 
def simple_return(sec):
    # simple returns on stocks are better for looking at multiple stocks over the same timeframe. 
    data = data_reader(sec)
    simple_return = shifted(data) - 1
    simple_annual_return = simple_return.mean() * 250
    return print(simple_annual_return[sec] * 100)

simple_return('MSFT')
def log_return(sec):
    # log returns are better for looking at one security over a period of time.
    data = data_reader(sec)
    log_return = np.log(shifted(data))
    log_annual_return = log_return.mean() * 250
    return print(log_annual_return[sec] * 100)

# indices are clusters of securities in one place that are usually market indicators.
# 3 most heard of index funds are dowjones, s&p 500, & nasdaq. 
# you can pass in any index fund that is valid on Yahoo. (Including foreign indices.)
# function to calculate the return of however many indices you would like. 
# you can tell an index from a stock usually by the little carrot. AAPL vs ^GSCP (Apple vs S&P 500)

def market_indicators(*indices):
    data = data_reader(*indices)
    id_return = (shifted(data)-1)
    annual_id_return = id_return.mean() * 250
    return print(f'{annual_id_return * 100}')

# function calculates the return of your portfolio based on the stocks you pass in
# along with the weights in your portfolio. 
def portfolio_return(weights,*stocks):
    data = data_reader(*stocks)
    if len(weights) == len(stocks) and sum(weights) == 1:
        p_return= (shifted(data) - 1)
        annual_returns = p_return.mean() * 250
        folio_return = np.dot(annual_returns,weights)
        return print(f'{folio_return * 100:.3f}')
    else:
        print('Make sure your weights add to 1 and the lengths of stocks and weights you are passing in are the same. ')
    

weights = [.5,.5]
portfolio_return(weights,'PG','MSFT')


        




