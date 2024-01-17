import pandas as pd
import http.client
import json
from pages.models import Stocks
from datetime import datetime


def getStocks():
    Stocks.objects.all().delete()

    conn = http.client.HTTPSConnection("api.collectapi.com")

    headers = {
        'content-type': "application/json",
        'authorization': "apikey 0rYHXRqFCAwjgYv0Kh0A6N:0GXunmYu67ZIz1ElTu2EGN"
        }

    conn.request("GET", "/economy/hisseSenedi", headers=headers)

    res = conn.getresponse()
    data = res.read()
    data = str(data, encoding='utf-8')
    json_object = json.loads(data)

    dataframe = pd.json_normalize(json_object['result'])
    dataframe = dataframe[['rate','lastprice','hacimstr','code','min','max']]
    dataframe['lastprice'] =  (round(dataframe['lastprice'].astype(float),3)).astype(str) 
    today = datetime.today().strftime('%Y-%m-%d')
    seq = 1
    for index, row in dataframe.iterrows():
        new_record = Stocks(stock_id=seq,stock_name=row['code'], stock_value=row['lastprice'],stock_volume=row['hacimstr'], stock_rate=row['rate'],stock_min=row['min'],stock_max=row['max'],stock_date = str(today))
        new_record.save()
        seq +=1



