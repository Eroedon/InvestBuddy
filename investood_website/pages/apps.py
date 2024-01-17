from django.apps import AppConfig
# from pages.getCryptoData import getCrypto
# from pages.getStockData import getStocks


class PagesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pages'
    # def ready(self):
    #     getStocks()
    #     print('stock data is uploaded to database')

    #     getCrypto()
    #     print('crypto data is uploaded to database')