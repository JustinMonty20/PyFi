import pandas as pd
import numpy as np
import pandas_datareader.data as wb
import requests
from bs4 import BeautifulSoup

# some figures are returned as percentages. But other values are not because the return values are needed to calcuate other functions. 
# everything is calculated yearly. multiple by 250 because on average thats how many days the markets are open. 


# global variable to indicate the start date we are grabbing the financial data
# along with where the data is coming from. 
start = '2010-1-1'
yahoo = 'yahoo'

# all data is gathered from the Yahoo Finance through the pandas_datareader package.
# sec stands for security. finance term for a tradeable asset. a stock is a security. 
# need to pass in the stocks "ticker" aka the abbrevaition on pretty much all trading platforms. 
"""Helper functions for calculations"""

def data_reader(*securities):
    data = pd.DataFrame()
    for item in securities:
        data[item] = wb.DataReader(item,start=start,data_source=yahoo)['Adj Close']
    return data

def logged(shifted_data):
    return np.log(shifted_data)
def shifted(data):
    # divides each entry in the dataframe by the next entry.
    return (data / data.shift(1))
def error(str):
    return RuntimeError(str)

"""Financial Functions"""

# annual simple return of the passed in security. 
def simple_return(sec):
    # simple returns on stocks are better for looking at multiple stocks over the same timeframe. 
    data = data_reader(sec)
    simple_return = shifted(data) - 1
    simple_annual_return = simple_return.mean() * 250
    return f'{simple_annual_return[sec] * 100:.4f}%'

def log_return(sec):
    # log returns are better for looking at one security over a period of time.
    data = data_reader(sec)
    log_return = logged(shifted(data))
    log_annual_return = log_return.mean() * 250
    return f'{log_annual_return[sec] * 100:.4f}%'


# function that checks how volatile a security is.
# volatility is calculated through standard deviation. 
# Volatility shows how often a security goes above or below its standard deviation. 
def sec_volatility(sec):
    data = data_reader(sec)
    sec_returns = logged(shifted(data))
    annual_volatility = sec_returns.std() * 250 ** .5
    return f'{annual_volatility * 100}'

# indices are clusters of securities in one place that are usually market indicators.
# 3 most heard of index funds are dowjones, s&p 500, & nasdaq. 
# you can pass in any index fund that is valid on Yahoo. (Including foreign indices.)
# you can tell an index from a stock usually by the little carrot. AAPL vs ^GSCP (Apple vs S&P 500)

def market_indicators(*indices):
    # function to calculate the return of however many indices you would like. 
    data = data_reader(*indices)
    id_return = (shifted(data)-1)
    annual_id_return = id_return.mean() * 250
    return f'{annual_id_return * 100}'

def portfolio_return(weights,*stocks):
    # function calculates the return of your portfolio based on the stocks you pass in
    # along with the weights in your portfolio. 
    data = data_reader(*stocks)
    if len(weights) == len(stocks) and sum(weights) == 1:
        p_return= (shifted(data) - 1)
        annual_returns = p_return.mean() * 250
        folio_return = np.dot(annual_returns,weights)
        return f'{folio_return * 100:.4f}%'
    else:
       raise RuntimeError('Make sure your weights add to 1 and the lengths of stocks and weights you are passing in are the same.')
# weights = [.5,.4]
# portfolio_return(weights,'PG','MSFT')

# function that takes the securites in your portfolio by the weight they hold in your portfolio.
# returns the volatility of your whole portfolio. 
def portfolio_volatility(weights,secs):
    data = data_reader(secs)
    sec_returns = logged(shifted(data))
    if len(weights) == len(secs) and sum(weights) == 1.0:
        annual_covariance = sec_returns.cov() * 250
        array_weights = np.array(weights)
        pfolio_volatilty = (np.dot(array_weights.T, np.dot(sec_returns.cov() * 250, array_weights))) ** 0.5
        return f'{pfolio_volatilty * 100:.4f} %'
    else:
         raise error('Make sure your weights add to 1 and the lengths of sec and weights you are passing in are the same.')

# weights = [.5,.5,]
# print(portfolio_volatility(weights,'AAPL','MSFT'))



""" Capital Asset Pricing Model Calculations"""
""" CAPM describes the realtionship between systematic risk and the expected return for their assets particulary stocks"""

# calculates the beta of a single security. need to pass in an index to compare with.
# use one of the three major indices in the U.S. Dow Jones, NASDAQ, or S&P 500 depending on the sec.
# Beta is a measure of the volatility of a security or a portfolio comapred tho the market as a whole.
# Beta describes the activity of a security's returns as it responds to swings in the market. 
def beta(sec,index):
    if index not in ['^GSPC','^IXIC','^DJI']:
        raise error('use one of the three major indices in the US')
    else:
        data = data_reader(sec,index)
        returns = logged(shifted(data))
        cov = returns.cov() * 250
        cov_with_mkt = cov.iloc[0,1]
        market_var = returns[index].var() * 250
        sec_beta = cov_with_mkt / market_var
    return sec_beta

# function to webscrape the ten year bond yield and use it as the risk free rate in the beta calculation. 
def get_risk_free_rate():
    URL = 'https://fred.stlouisfed.org/series/DGS10'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content,'html.parser')
    results = soup.find(id='meta-left-col')
    yield_span = results.find(class_='series-meta-observation-value')
    for rate in yield_span:
       ten_year_bond_yield = float(rate)
    return (ten_year_bond_yield / 100)


# calculates the expected return of a stock. 
# for this function it calculates the beta of the stock based off of one of the three major indicies in the US. 
def expected_return(sec,index):
    if index not in ['^GSPC','^IXIC','^DJI']:
        raise error('use one of the three major indices in the US')
    else:
        risk_free_rate = get_risk_free_rate()
        sec_beta = float(beta(sec,index))
    return risk_free_rate + sec_beta * .05

def sharpe_ratio(sec,index):
    if index not in ['^GSPC','^IXIC','^DJI']:
       raise error('use one of the three major indices in the US')
    else:
        data = data_reader(sec,index)
        returns = logged(shifted(data))
        sharpe = (expected_return(sec,index) - get_risk_free_rate()) / (returns[sec].std() * 250 ** .05)
    return sharpe    





