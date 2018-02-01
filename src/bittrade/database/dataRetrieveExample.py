# Running regression on daily close price based on four years data, data processing part.
import pandas as pd
from googleclient import get_price_data
# Getting the date we need from google finance API
# currencyTicker represents the bitcoin price, and the most tradable currency include Japanese Yen, Swiss Franc,
# Australian Dollar, Canadian Dollar, Indian Rupee, Euro. The price data for these currency are all quoted in dollar.
currencyTickers = [
    "CURRENCY:BTCUSD", "CURRENCY:GBPUSD", "CURRENCY:JPYUSD", "CURRENCY:CHFUSD",
    "CURRENCY:AUDUSD", "CURRENCY:CADUSD", "CURRENCY:INRUSD", "CURRENCY:EURUSD",
]
# 24 Most Liquid ETFs:
# SPDR S&P 500 (SPY)
# Financial Select Sector SPDR (XLF)
# Russell 2000 Index Fund Profile (IWM)
# MSCI Emerging Markets Index Fund (EEM)
# PowerShares QQQ (QQQ)
# Vanguard MSCI Emerging Markets ETF (VWO)
# MSCI EAFE Index Fund (EFA)
# FTSE China 25 Index Fund (FXI)
# Industrial Select Sector SPDR Fund (XLI)
# Daily Small Cap Bear 3X Shares Fundamentals (TZA)
# Energy Select Sector SPDR Fund (XLE)
# UltraShort S&P500 (SDS)
# Silver Trust ETF (SLV)
# Direxion Daily Financial Bear 3x Shares (FAZ)
# Market Vectors TR Gold Miners ETF (GDX)
# MSCI Japan Index Fund (EWJ)
# UltraPro Short S&P500 (SPXU)
# MSCI Brazil Index Fund (EWZ)
# Daily Financial Bull 3X Shares (FAS)
# VelocityShares Daily 2x VIX Short-Term ETN (TVIX)
# United States Oil Fund (USO)
# SPDR Gold Shares (GLD)
# UltraShort Barclays 20+ Year Treasury (TBT)
# United States Natural Gas Fund (UNG)
etfTickers = [
    "NYSEARCA:XLF", "NYSEARCA:IWM", "NYSEARCA:EEM", "NASDAQ:QQQ", "NYSEARCA:VWO", "NYSEARCA:EFA",
    "NYSEARCA:FXI", "NYSEARCA:XLI", "NYSEARCA:TZA", "NYSEARCA:XLE", "NYSEARCA:SDS", "NYSEARCA:SLV",
    "NYSEARCA:FAZ", "NYSEARCA:GDX", "NYSEARCA:EWJ", "NYSEARCA:SPXU", "NYSEARCA:EWZ", "NYSEARCA:FAS",
    "NASDAQ:TVIX", "NYSEARCA:USO", "NYSEARCA:GLD", "NYSEARCA:TBT", "NYSEARCA:UNG",
]
# Function use to get currency data and major stock index


def getClosePrice(target):
    market, ticker = target.split(':')
    param = {
        'q': ticker,  # Bitcoin price in USD
        'i': "86400",  # Interval size in seconds ("86400" = 1 day intervals)
        'x': market,
        'p': "4Y",  # Period (Ex: "4Y" = 4 year)
    }
    df = get_price_data(param)
    price = df[['Close']]
    price = price.reset_index()
    price['index'] = price['index'].apply(lambda x: x.date())
    price.columns = ['Date', ticker]
    return price


def getClosePriceTable(targetList):
    df_table = pd.DataFrame()
    for target in targetList:
        price = getClosePrice(target)
        if (df_table.shape == (0, 0)):
            df_table = price
        else:
            df_table = pd.merge(df_table, price, how='outer', on='Date')
    return df_table


# Get a joined table of all tickers sharing the same Data index
priceTable = getClosePriceTable(currencyTickers + etfTickers)
# The interpolation method I use here is linear interpolation.
priceTable['Date'] = pd.to_datetime(priceTable.Date)
priceTable = priceTable.sort_values(by='Date')
priceTable = priceTable.interpolate(method='linear', axis=0).ffill().bfill()
priceTable = priceTable.set_index('Date')
priceTable
