from django.urls import path
from pages.views import HomeClass,Authentication,StockClass,CrpytoClass,PortfolioClass


home = HomeClass()
stocks = StockClass()
crptos = CrpytoClass()
portfolios = PortfolioClass()


urlpatterns = [
    path("", home.home, name='home'),
    path('signup/', home.user_signup, name ='signup'),
    path('signin/', home.user_login, name = 'login'),
    path('logout/', home.user_logout, name = 'logout'),
    path("crypto/", crptos.crypto, name='crypto'),
    path("crypto/addportfolio", portfolios.add_portfolio_crypto, name='add_portfolio_crypto'),
    path("portfolio/", portfolios.portfoliopage, name='portfoliopage'),
    path("stocks/addportfolio", portfolios.add_portfolio_stocks, name='add_portfolio_stocks'),
    path("stocks/", stocks.stocks, name='stocks'),
    path("getData/", home.getData, name='getData'),
    path("portfolio/remove_stockportfolio", portfolios.remove_stockportfolio, name='remove_stockportfolio'),
    path("portfolio/remove_cryptoportfolio", portfolios.remove_cryptoportfolio, name='remove_cryptoportfolio'),
    path("portfolio/remove_stock_wallet", portfolios.remove_stock_wallet, name='remove_stock_wallet'),
    path("portfolio/remove_crypto_wallet", portfolios.remove_crypto_wallet, name='remove_crypto_wallet'),
    path("portfolio/add_stock_to_wallet", portfolios.add_stock_to_wallet, name='add_stock_to_wallet'),
    path("portfolio/add_crypto_to_wallet", portfolios.add_crypto_to_wallet, name='add_crypto_to_wallet'),
    # path("portfolio/crypto_history", crptos.crypto_history, name='crypto_history'),

]