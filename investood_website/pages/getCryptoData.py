import pandas as pd
import json
from pages.models import Crypto
import requests
import datetime
 
def getTL():
    url = "https://min-api.cryptocompare.com/data/price?fsym=TRY&tsyms=USD"
    responseUSD = requests.request("POST", url, headers={'Content-Type': 'application/json'})
    TRYtoUSD = float(responseUSD.json()['USD'])
    return TRYtoUSD

def getCrypto():
    Crypto.objects.all().delete()

    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'c11a8cf5-0aa5-4d74-8762-acc1497aacd3',
    }

    session = requests.Session()
    session.headers.update(headers)
    response = session.get(url)
    data = json.loads(response.text)

    TLtoUSD = getTL()

    dataframe = pd.json_normalize(data['data'])[['name','symbol','last_updated','quote.USD.price','quote.USD.percent_change_7d']]
    # import pdb;pdb.set_trace()
    dataframe['quote.TL'] = '₺'+dataframe['quote.USD.price'].div(TLtoUSD).round(2).astype(str)
    dataframe['quote.USD.price'] = round(dataframe['quote.USD.price'],3).astype(str)+ '$'   

    seq = 1
    for index, row in dataframe.iterrows():
        new_record = Crypto(crypto_id=seq,crypto_name=row['name'], crypto_symbol=row['symbol'],crypto_value=row['quote.USD.price'],crypto_value_TL=row['quote.TL'],percent_change_7d=row['quote.USD.percent_change_7d'],  crypto_date=datetime.datetime.strptime(row['last_updated'][:10],'%Y-%m-%d') )
        new_record.save()
        seq+=1


