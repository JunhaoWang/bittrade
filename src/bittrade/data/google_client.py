"""Module to retrieves Google Finance data.

This module contains various price for stocks and crypto.

Todo:
    * EMPTY
    * You have to also use ``sphinx.ext.todo`` extension
"""
from datetime import datetime

import pandas as pd
import requests


def get_price_data(query):
    """
    Use Google Finance to get data.

    Args:
        query (str): EMPTY

    Returns:
        pandas.DataFrame: EMPTY
    """
    r = requests.get(
        "https://finance.google.com/finance/getprices", params=query,
    )
    lines = r.text.splitlines()
    data = []
    index = []
    basetime = 0
    for price in lines:
        cols = price.split(",")
        if cols[0][0] == 'a':
            basetime = int(cols[0][1:])
            index.append(datetime.fromtimestamp(basetime))
            data.append([
                float(cols[4]), float(cols[2]), float(
                    cols[3],
                ), float(cols[1]), int(cols[5]),
            ])
        elif cols[0][0].isdigit():
            date = basetime + (int(cols[0])*int(query['i']))
            index.append(datetime.fromtimestamp(date))
            data.append([
                float(cols[4]), float(cols[2]), float(
                    cols[3],
                ), float(cols[1]), int(cols[5]),
            ])
    return pd.DataFrame(data, index=index, columns=['Open', 'High', 'Low', 'Close', 'Volume'])


def get_close_price(target, period='1Y'):
    """
    Get the close price, for every target ticker.

    Args:
        target (EMPTY): EMPTY
        period (str): EMPTY

    Returns:
        EMPTY: EMPTY
    """
    market, ticker = target.split(':')
    param = {
        'q': ticker,  # Bitcoin price in USD
        'i': "86400",  # Interval size in seconds ("86400" = 1 day intervals)
        'x': market,
        'p': period,  # Period (Ex: "4Y" = 4 year)
    }
    df = get_price_data(param)
    price = df[['Close']]
    price = price.reset_index()
    price['index'] = price['index'].apply(lambda x: x.date())
    price.columns = ['Date', ticker]
    return price


def get_close_price_table(targetList, interpolation=True, period='1Y'):
    """
    EMPTY
    """
    df_table = pd.DataFrame()
    for target in targetList:
        price = get_close_price(target, period)
        if (df_table.shape == (0, 0)):
            df_table = price
        else:
            df_table = pd.merge(df_table, price, how='outer', on='Date')
    if (not interpolation):
        return df_table
    else:
        priceTable = df_table
        # linear interpolation is applied.
        priceTable['Date'] = pd.to_datetime(priceTable.Date)
        priceTable = priceTable.sort_values(by='Date')
        priceTable = priceTable.interpolate(
            method='linear', axis=0,
        ).ffill().bfill()
        priceTable = priceTable.set_index('Date')
        return priceTable
