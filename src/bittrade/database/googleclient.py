from datetime import datetime

import pandas as pd
import requests


def get_price_data(query):
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
