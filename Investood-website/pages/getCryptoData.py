import pandas as pd
import json
from pages.models import Crypto
from requests import Session


def getCrypto():
    Crypto.objects.all().delete()

    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'c11a8cf5-0aa5-4d74-8762-acc1497aacd3',
    }

    session = Session()
    session.headers.update(headers)
    response = session.get(url)
    data = json.loads(response.text)

    dataframe = pd.json_normalize(data['data'])[['name','symbol','date_added','total_supply']]
    dataframe['total_supply'] = dataframe['total_supply'].astype(str)
    seq = 1
    for index, row in dataframe.iterrows():
        new_record = Crypto(crypto_id=seq,crypto_name=row['name'], crypto_symbol=row['symbol'],crypto_value=row['total_supply'], crypto_date=row['date_added'])
        new_record.save()
        seq+=1
