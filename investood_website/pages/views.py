from django.shortcuts import render,redirect
from pages.models import User, Crypto, Stocks, Portfolio, Wallet
from pages.getCryptoData import getCrypto
from  pages.getStockData import getStocks
from heapq import nlargest
import datetime
from datetime import timedelta, date
import pandas as pd
from binance import Client
client = Client("","")



class Authentication:
    def __init__(self):
        self.user_email = ''
        self.authenticate = 'false'

    def setEmail(self,email):
        self.user_email = email

    def setAuthenticate(self,value):
        self.authenticate = value

    
authentication = Authentication()

class HomeClass:
    def __init__(self):
        print('Home object')
        global authentication

    def home(self,request):
        cryptolist = self.getTop5('crypto')
        stocklist = self.getTop5('stock')

        if 'signup_user' in request.POST:
            user_email = request.POST.get('user_email')
            user_password1 = request.POST.get('user_password1')
            user_password2 = request.POST.get('user_password2')
            check_email = User.objects.filter(email=user_email)
            print('check_email',check_email)
            print('user_email',user_email)
            print('user_password1',user_password1)
            print('user_password2',user_password2)
            if check_email:
                print('user exists')
                authentication.setAuthenticate('false') 
                authentication.setEmail('')
                return render(request, "pages/home.html", {'authenticate':authentication.authenticate,'user_email': authentication.user_email,'cryptos':cryptolist,'stocks':stocklist})
            if user_password1 != user_password2:
                print('passwords are not equal')
                authentication.setAuthenticate('false') 
                authentication.setEmail('')
                return render(request, "pages/home.html", {'authenticate':authentication.authenticate,'user_email': authentication.user_email,'cryptos':cryptolist,'stocks':stocklist})
            new_user = User(email=user_email, password=user_password1)
            new_user.save()
            authentication.setAuthenticate('true') 
            authentication.setEmail(user_email)
            print('user saved successfully')
            return render(request, "pages/home.html", {'authenticate':authentication.authenticate,'user_email': authentication.user_email,'cryptos':cryptolist,'stocks':stocklist})
        

        elif 'login_user' in request.POST:
            if request.method == 'POST':
                user_email = request.POST.get('user_email')
                user_email = user_email.replace('%40','@')
                print('user_email',user_email)
                user_password = request.POST.get('user_password')
                check_email = User.objects.filter(email=user_email,password=user_password)
                authentication.setAuthenticate('false') 
                authentication.setEmail('')
                if check_email:
                    print('userfound')
                    authentication.setAuthenticate('true') 
                    authentication.setEmail(user_email)
                    return render(request, 'pages/home.html', {'authenticate':authentication.authenticate ,'user_email': authentication.user_email,'cryptos':cryptolist,'stocks':stocklist})
                print('usernotfound')
                return render(request, 'pages/home.html', {'authenticate':authentication.authenticate,'user_email': authentication.user_email,'cryptos':cryptolist,'stocks':stocklist})
        return render(request, "pages/home.html", {'authenticate':authentication.authenticate,'user_email': authentication.user_email,'cryptos':cryptolist,'stocks':stocklist})



    def getTop5(self,type):
        if type == 'crypto':
            crypto_list = Crypto.objects.all()
            cryptolist = [] 
            for crypto in crypto_list:
                crypto_dict = {}
                crypto_dict['crypto_id'] = crypto.crypto_id
                crypto_dict['crypto_name'] = crypto.crypto_name
                crypto_dict['crypto_symbol'] = crypto.crypto_symbol
                crypto_dict['crypto_value'] = float(crypto.crypto_value.replace('$',''))
                crypto_dict['crypto_value_tl'] = crypto.crypto_value_TL
                crypto_dict['percent_change_7d'] = crypto.percent_change_7d
                crypto_dict['arrow'] = "up" if float(crypto.percent_change_7d) >= 0  else "down" 
                crypto_dict['crypto_date'] = crypto.crypto_date
                cryptolist.append(crypto_dict)
            return nlargest(5, cryptolist, key=lambda item: item["crypto_value"])
        else:
            stocks_list = Stocks.objects.all()
            stocklist = [] 
            for stocks in stocks_list:
                stock_dict = {}
                stock_dict['stock_id'] = stocks.stock_id
                stock_dict['stock_name'] = stocks.stock_name
                stock_dict['stock_value'] = float(stocks.stock_value.replace('₺',''))
                stock_dict['stock_volume'] = stocks.stock_volume
                stock_dict['stock_min'] = stocks.stock_min
                stock_dict['stock_max'] = stocks.stock_max
                stock_dict['stock_rate'] = stocks.stock_rate
                stock_dict['stock_date'] = stocks.stock_date
                stock_dict['arrow'] = "up" if float(stocks.stock_rate) >= 0  else "down" 
                stocklist.append(stock_dict)
            return nlargest(5, stocklist, key=lambda item: item["stock_value"])

    def getData(self,request):

        getStocks()
        print('stock data is uploaded to database')

        getCrypto()
        print('crypto data is uploaded to database')
        return self.home(request)
    
    # signup page
    def user_signup(self,request):
        authentication.authenticate = 'false'
        authentication.user_email = ''
        if request.method == 'POST':
            user_email = request.POST.get('user_email')
            user_password1 = request.POST.get('user_password1')
            user_password2 = request.POST.get('user_password2')
            check_email = User.objects.filter(email=user_email)
            print('check_email',check_email)
            print('user_email',user_email)
            print('user_password1',user_password1)
            print('user_password2',user_password2)
            if check_email:
                print('user exists')
                authentication.authenticate = 'false'
                authentication.user_email = ''
                return render(request, "pages/signup.html", {'authenticate':authentication.authenticate,'user_email': authentication.user_email})
            if user_password1 != user_password2:
                print('passwords are not equal')
                authentication.authenticate = 'false'
                authentication.user_email = ''
                return render(request, "pages/signup.html", {'authenticate':authentication.authenticate,'user_email': authentication.user_email})
            new_user = User(email=user_email, password=user_password1)
            new_user.save()
            authentication.authenticate = 'true'
            authentication.setEmail(user_email)
            print('user saved successfully')
            return render(request, "pages/signup.html", {'authenticate':authentication.authenticate,'user_email': authentication.user_email})
        return render(request, "pages/signup.html", {'authenticate':authentication.authenticate,'user_email': authentication.user_email})


    # login page
    def user_login(self,request):
        authentication.authenticate = 'false'
        authentication.user_email = ''
        if request.method == 'POST':
            user_email = request.POST.get('user_email')
            user_email = user_email.replace('%40','@')
            print('user_email',user_email)
            user_password = request.POST.get('user_password')
            check_email = User.objects.filter(email=user_email,password=user_password)
            authentication.authenticate = 'false'
            if check_email:
                print('userfound')
                authentication.authenticate = 'true'
                authentication.setEmail(user_email)
                return render(request, 'pages/home.html', {'authenticate':authentication.authenticate ,'user_email': authentication.user_email})
            print('usernotfound')
            return render(request, 'pages/login.html', {'authenticate':authentication.authenticate,'user_email': authentication.user_email})
        return render(request, "pages/login.html", {'authenticate':authentication.authenticate,'user_email': authentication.user_email})


    # logout page
    def user_logout(self,request):
        authentication.setAuthenticate("false") 
        authentication.setEmail("")       
        return self.home(request)

            




class CrpytoClass:
    def __init__(self):
        global authentication
        print('Crypto object')

    def crypto(self,request):
        crypto_list = Crypto.objects.all()
        cryptolist = [] 
        for crypto in crypto_list:
            crypto_dict = {}
            crypto_dict['crypto_id'] = crypto.crypto_id
            crypto_dict['crypto_name'] = crypto.crypto_name
            crypto_dict['crypto_symbol'] = crypto.crypto_symbol
            crypto_dict['crypto_value'] = crypto.crypto_value
            crypto_dict['crypto_value_tl'] = crypto.crypto_value_TL
            crypto_dict['percent_change_7d'] = crypto.percent_change_7d
            crypto_dict['arrow'] = "up" if float(crypto.percent_change_7d) >= 0  else "down" 
            crypto_dict['crypto_date'] = crypto.crypto_date
            cryptolist.append(crypto_dict)
            
        return render(request, "pages/cryptohome.html", {'authenticate':authentication.authenticate,'user_email': authentication.user_email,'cryptos':cryptolist})

    
    def getHistoryData(self,symbol, day, month,year):

        current_datetime = datetime.date(int(year),int(month),int(day))

        second_day = current_datetime + timedelta(1)

        current_date_time = current_datetime.strftime("%d-%m-%Y")
        second_day = second_day.strftime("%d-%m-%Y")


        klines = client.get_historical_klines(symbol+"USDC", Client.KLINE_INTERVAL_1DAY, current_date_time,second_day)

        hist_df = pd.DataFrame(klines)
        if hist_df.empty == False:
            print('hist_df',hist_df)

            hist_df.columns = ['Open Time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close Time', 'Quote Asset Volume', 
                                'Number of Trades', 'TB Base Volume', 'TB Quote Volume', 'Ignore']

            hist_df = hist_df[["Open Time","Low"]]
            hist_df[["Low"]] = hist_df[["Low"]].apply(pd.to_numeric, axis=1)

            hist_df['Open Time'] = pd.to_datetime(hist_df['Open Time']/1000, unit='s')

            hist_df = hist_df.iloc[0]
            return hist_df['Low']
        
        
        return "No history data for this coin"


class StockClass:
    def __init__(self):
        global authentication
        print('Stock object')

    def stocks(self,request):
        stocks_list = Stocks.objects.all()
        stocklist = [] 
        for stocks in stocks_list:
            stock_dict = {}
            stock_dict['stock_id'] = stocks.stock_id
            stock_dict['stock_name'] = stocks.stock_name
            stock_dict['stock_value'] = stocks.stock_value
            stock_dict['stock_volume'] = stocks.stock_volume
            stock_dict['stock_min'] = stocks.stock_min
            stock_dict['stock_max'] = stocks.stock_max
            stock_dict['stock_rate'] = stocks.stock_rate
            stock_dict['stock_date'] = stocks.stock_date
            stock_dict['arrow'] = "up" if float(stocks.stock_rate) >= 0  else "down" 
            stocklist.append(stock_dict)

        return render(request, "pages/stockshome.html", {'authenticate':authentication.authenticate,'user_email': authentication.user_email, 'stocks':stocklist})







class PortfolioClass:
    def __init__(self):
        global authentication
        print('Portfolio object')
        self.stocks = StockClass()
        self.crypto = CrpytoClass()


    def add_portfolio_stocks(self,request):
        
        if request.method == 'POST':
            stock_id = request.POST.get('stock')
            if authentication.authenticate == 'true':
                found_user = User.objects.get(email=authentication.user_email)
                found_portfolio = Portfolio.objects.filter(user_id=found_user.user_id)
                if found_portfolio:
                    found_portfolio = Portfolio.objects.get(user_id=found_user.user_id)
                    if  hasattr(found_portfolio, "stock_id"):
                        found_stocks = found_portfolio.stock_id
                        found_stocks = found_stocks + ' ' + str(stock_id)
                    else:
                        found_stocks = str(stock_id)
                    found_portfolio.stock_id = found_stocks
                    found_portfolio.save()
                    print('added to list : stocks')
                else:
                    print(found_user.user_id)
                    print(stock_id)
                    new_portfolio = Portfolio(user_id=found_user.user_id,stock_id = stock_id)
                    new_portfolio.save()
                    print('added stocks')

    
        return self.stocks.stocks(request)

    def remove_stockportfolio(self,request):
        if request.method == 'POST':
            stock_id = request.POST.get('remove_stock')
            found_user = User.objects.get(email=authentication.user_email)
            found_portfolio = Portfolio.objects.filter(user_id=found_user.user_id)
            if found_portfolio:
                found_portfolio = Portfolio.objects.get(user_id=found_user.user_id)
                found_stock = found_portfolio.stock_id
                found_stock = found_stock.replace(str(stock_id),'')
                found_portfolio.stock_id = found_stock
                found_portfolio.save()
                print('removed stock :',stock_id )

        # return render(request, "pages/portfoliohome.html", {'authenticate':authenticate,'user_email': user_email})
        return self.portfoliopage(request)


    def add_portfolio_crypto(self,request):
        
        if request.method == 'POST':
            crypto_id = request.POST.get('crypto')
            if authentication.authenticate == 'true':
                found_user = User.objects.get(email=authentication.user_email)
                found_portfolio = Portfolio.objects.filter(user_id=found_user.user_id)
                if found_portfolio:
                    found_portfolio = Portfolio.objects.get(user_id=found_user.user_id)
                    if  hasattr(found_portfolio, "crypto_id"):
                        found_crypto = found_portfolio.crypto_id
                        found_crypto = found_crypto + ' ' + str(crypto_id)
                    else:
                        found_crypto = str(crypto_id)
                    found_portfolio.crypto_id = found_crypto
                    found_portfolio.save()
                    print('added to list : crpyto')
                else:
                    new_portfolio = Portfolio(user_id=found_user.user_id,crypto_id = crypto_id)
                    new_portfolio.save()
                    print('added crypto')

        return self.crypto.crypto(request)


    def remove_cryptoportfolio(self,request):
        if request.method == 'POST':
            crypto_id = request.POST.get('remove_crypto')
            found_user = User.objects.get(email=authentication.user_email)
            found_portfolio = Portfolio.objects.filter(user_id=found_user.user_id)
            if found_portfolio:
                found_portfolio = Portfolio.objects.get(user_id=found_user.user_id)
                found_crypto = found_portfolio.crypto_id
                found_crypto = found_crypto.replace(str(crypto_id),'')
                found_portfolio.crypto_id = found_crypto
                found_portfolio.save()
                print('removed crypto:',crypto_id)

        #return render(request, "pages/portfoliohome.html", {'authenticate':authenticate,'user_email': user_email})
        return self.portfoliopage(request)


    def portfoliopage(self,request):
        history_result = ""
        found_user = User.objects.get(email=authentication.user_email)
        found_portfolio = Portfolio.objects.filter(user_id=found_user.user_id)
        stocklist = []
        cryptolist = [] 
        if found_portfolio:
            found_portfolio = Portfolio.objects.get(user_id=found_user.user_id)
            if hasattr(found_portfolio, "stock_id"):
                stock_id_list = found_portfolio.stock_id
                stock_id_list = set(stock_id_list.split())
                stocklist = []
                for stock_id in stock_id_list:
                    found_stock = Stocks.objects.filter(stock_id=stock_id)
                    if found_stock:
                        found_stock = Stocks.objects.get(stock_id=stock_id)
                        stock_dict = {}
                        stock_dict['stock_id'] = found_stock.stock_id
                        stock_dict['stock_name'] = found_stock.stock_name
                        stock_dict['stock_value'] = found_stock.stock_value
                        stock_dict['stock_volume'] = found_stock.stock_volume
                        stock_dict['stock_min'] = found_stock.stock_min
                        stock_dict['stock_max'] = found_stock.stock_max
                        stock_dict['stock_rate'] = found_stock.stock_rate
                        stock_dict['stock_date'] = found_stock.stock_date
                        stock_dict['arrow'] = "up" if float(found_stock.stock_rate) >= 0  else "down" 
                        stocklist.append(stock_dict)

            if hasattr(found_portfolio, "crypto_id"):
                crypto_id_list = found_portfolio.crypto_id
                crypto_id_list = set(crypto_id_list.split())
                cryptolist = [] 
                for crypto_id in crypto_id_list:
                    found_crypto = Crypto.objects.filter(crypto_id=crypto_id)
                    if found_crypto:
                        found_crypto = Crypto.objects.get(crypto_id=crypto_id)
                        crypto_dict = {}
                        crypto_dict['crypto_id'] = found_crypto.crypto_id
                        crypto_dict['crypto_name'] = found_crypto.crypto_name
                        crypto_dict['crypto_symbol'] = found_crypto.crypto_symbol
                        crypto_dict['crypto_value'] = found_crypto.crypto_value
                        crypto_dict['crypto_value_tl'] = found_crypto.crypto_value_TL
                        crypto_dict['percent_change_7d'] = found_crypto.percent_change_7d
                        crypto_dict['arrow'] = "up" if float(found_crypto.percent_change_7d) >= 0  else "down" 
                        crypto_dict['crypto_date'] = found_crypto.crypto_date
                        cryptolist.append(crypto_dict)
            
        if 'addwallet' in request.POST:
            found_wallet = Wallet.objects.filter(user_id=found_user.user_id)
            item_type = request.POST.get('type_to_add')
            item_id = request.POST.get('item_id')
            item_amount = request.POST.get('amount')
            if item_type == 'Cryptocurrency':
                crypto_check = Crypto.objects.get(crypto_id=item_id)
                if crypto_check:
                    if found_wallet:
                        found_wallet = Wallet.objects.get(user_id=found_user.user_id)
                        if  hasattr(found_wallet, "crypto_id"):
                            found_crypto = found_wallet.crypto_id
                            crypto_id_list = found_crypto.split()
                            found_crypto_amount = found_wallet.crypto_amount
                            if item_id in crypto_id_list:
                                index = crypto_id_list.index(item_id)
                                amount_list = found_crypto_amount.split()
                                amount_list[index] = str(float(amount_list[index]) + float(item_amount))
                                found_crypto_amount = ' '.join(amount_list)
                            else:
                                found_crypto = found_crypto + ' ' + str(item_id)
                                found_crypto_amount = found_crypto_amount + ' ' + str(item_amount)
                        else:
                            found_crypto = str(item_id)
                            found_crypto_amount = str(item_amount)
                        found_wallet.crypto_id = found_crypto
                        found_wallet.crypto_amount = found_crypto_amount
                        found_wallet.save()
                        print('added to list : crpyto')
                    else:
                        new_wallet = Wallet(user_id=found_user.user_id,crypto_id = str(item_id),crypto_amount=str(item_amount))
                        new_wallet.save()
            else:
                stock_check = Stocks.objects.get(stock_id=item_id)
                if stock_check:
                    if found_wallet:
                        found_wallet = Wallet.objects.get(user_id=found_user.user_id)
                        if  hasattr(found_wallet, "stock_id"):
                            found_stock = found_wallet.stock_id
                            stock_id_list = found_stock.split()
                            found_stock_amount = found_wallet.stock_amount
                            if item_id in stock_id_list:
                                index = stock_id_list.index(item_id)
                                amount_list = found_stock_amount.split()
                                amount_list[index] = str(float(amount_list[index]) + float(item_amount))
                                found_stock_amount = ' '.join(amount_list)
                            else:
                                found_stock = found_stock + ' ' + str(item_id)
                                found_stock_amount = found_stock_amount + ' ' + str(item_amount)
                        else:
                            found_stock = str(item_id)
                            found_stock_amount = str(item_amount)
                        found_wallet.stock_id = found_stock
                        found_wallet.stock_amount = found_stock_amount
                        found_wallet.save()
                        print('added to list : crpyto')
                    else:
                        new_wallet = Wallet(user_id=found_user.user_id,stock_id = str(item_id),stock_amount=str(item_amount))
                        new_wallet.save()




        found_wallet = Wallet.objects.filter(user_id=found_user.user_id)
        wallet_stocklist = []
        wallet_cryptolist = [] 
        if found_wallet:
            found_wallet = Wallet.objects.get(user_id=found_user.user_id)
            if hasattr(found_wallet, "crypto_id"):
                crypto_id_list = found_wallet.crypto_id
                crypto_id_list = crypto_id_list.split()
                amount_list = found_wallet.crypto_amount.split()
                wallet_cryptolist = [] 
                for (crypto_id,amount) in zip(crypto_id_list,amount_list):
                    found_crypto = Crypto.objects.filter(crypto_id=crypto_id)
                    if found_crypto:
                        found_crypto = Crypto.objects.get(crypto_id=crypto_id)
                        wallet_crypto_dict = {}
                        wallet_crypto_dict['crypto_id'] = found_crypto.crypto_id
                        wallet_crypto_dict['crypto_name'] = found_crypto.crypto_name
                        wallet_crypto_dict['crypto_symbol'] = found_crypto.crypto_symbol
                        wallet_crypto_dict['crypto_value'] = str(float(amount)/ float(found_crypto.crypto_value_TL.replace('₺','')))
                        wallet_crypto_dict['crypto_value_tl'] = '₺' + amount
                        wallet_cryptolist.append(wallet_crypto_dict)

            if hasattr(found_portfolio, "stock_id"):
                stock_id_list = found_wallet.stock_id
                stock_id_list = stock_id_list.split()
                wallet_stocklist = []
                amount_list = found_wallet.stock_amount.split()
                for (stock_id,amount) in zip(stock_id_list,amount_list):
                    print('STOCKID',stock_id)
                    found_stock = Stocks.objects.filter(stock_id=stock_id)
                    if found_stock:
                        found_stock = Stocks.objects.get(stock_id=stock_id)
                        stock_dict = {}
                        stock_dict['stock_id'] = found_stock.stock_id
                        stock_dict['stock_name'] = found_stock.stock_name
                        stock_dict['stock_value'] =  str(float(amount)/ float(found_stock.stock_value.replace('₺','')))
                        stock_dict['stock_value_tl'] = '₺' + amount
                        wallet_stocklist.append(stock_dict)

        if 'crypto_symbol' in request.POST:
            crypto_symbol = request.POST.get('crypto_symbol')
            crypto_date = str(request.POST.get('crypto_date')) #2022-06-08

            year = crypto_date[:4]
            month = crypto_date[5:7]
            day = crypto_date[8:]

            history_result = str(self.crypto.getHistoryData(crypto_symbol,day,month,year))
            print('crypto_symbol',crypto_symbol)
            print('crypto_date',crypto_date)
            print('history_result',history_result)


        return render(request, "pages/portfoliohome.html", {'authenticate':authentication.authenticate,'user_email': authentication.user_email,'stocks':stocklist,'cryptos':cryptolist,'wallet_stocklist':wallet_stocklist,'wallet_cryptolist':wallet_cryptolist,'history_result':history_result})
    


    ####

    def add_stock_to_wallet(self,request):
        found_user = User.objects.get(email=authentication.user_email)
        found_wallet = Wallet.objects.filter(user_id=found_user.user_id)
        item_id = request.POST.get('add_stock')
        item_amount = request.POST.get('amount')
        print('itemid',item_id)
        print('item_amount',item_amount)

        if found_wallet and item_id and item_amount:
            found_wallet = Wallet.objects.get(user_id=found_user.user_id)
            if  hasattr(found_wallet, "stock_id"):
                found_stock = found_wallet.stock_id
                stock_id_list = found_stock.split()
                found_stock_amount = found_wallet.stock_amount
                if item_id in stock_id_list:
                    index = stock_id_list.index(item_id)
                    amount_list = found_stock_amount.split()
                    amount_list[index] = str(float(amount_list[index]) + float(item_amount))
                    found_stock_amount = ' '.join(amount_list)
                else:
                    found_stock = found_stock + ' ' + str(item_id)
                    found_stock_amount = found_stock_amount + ' ' + str(item_amount)
            else:
                found_stock = str(item_id)
                found_stock_amount = str(item_amount)
            found_wallet.stock_id = found_stock
            found_wallet.stock_amount = found_stock_amount
            found_wallet.save()
            print('added to list : crpyto')
        else:
            new_wallet = Wallet(user_id=found_user.user_id,stock_id = str(item_id),stock_amount=str(item_amount))
            new_wallet.save()
        return redirect("http://localhost:8000/portfolio")

    def remove_stock_wallet(self,request):
        if request.method == 'POST':
            stock_id = request.POST.get('remove_stock_wallet')
            if stock_id:
                found_user = User.objects.get(email=authentication.user_email)
                found_wallet = Wallet.objects.filter(user_id=found_user.user_id)
                if found_wallet:
                    found_wallet = Wallet.objects.get(user_id=found_user.user_id)
                    found_stock = found_wallet.stock_id
                    stocko_id_list = found_stock.split()
                    index = stocko_id_list.index(stock_id)
                    found_stock = found_stock.replace(str(stock_id),'')
                    found_wallet.stock_id = found_stock
                    stock_amount_list = found_wallet.stock_amount.split()
                    stock_amount_list.pop(index)
                    amount = ' '.join(stock_amount_list)
                    found_wallet.stock_amount = amount
                    found_wallet.save()
                    print('removed stock:',stock_id)

        return redirect("http://localhost:8000/portfolio")
    

    ###

    def add_crypto_to_wallet(self,request):
        found_user = User.objects.get(email=authentication.user_email)
        found_wallet = Wallet.objects.filter(user_id=found_user.user_id)
        item_id = request.POST.get('add_crypto')
        item_amount = request.POST.get('amount')
        if found_wallet and item_id and item_amount:
            found_wallet = Wallet.objects.get(user_id=found_user.user_id)
            if  hasattr(found_wallet, "crypto_id"):
                found_crypto = found_wallet.crypto_id
                crypto_id_list = found_crypto.split()
                found_crypto_amount = found_wallet.crypto_amount
                if item_id in crypto_id_list:
                    index = crypto_id_list.index(item_id)
                    amount_list = found_crypto_amount.split()
                    amount_list[index] = str(float(amount_list[index]) + float(item_amount))
                    found_crypto_amount = ' '.join(amount_list)
                else:
                    found_crypto = found_crypto + ' ' + str(item_id)
                    found_crypto_amount = found_crypto_amount + ' ' + str(item_amount)
            else:
                found_crypto = str(item_id)
                found_crypto_amount = str(item_amount)
            found_wallet.crypto_id = found_crypto
            found_wallet.crypto_amount = found_crypto_amount
            found_wallet.save()
            print('added to list : crpyto')
        else:
            new_wallet = Wallet(user_id=found_user.user_id,crypto_id = str(item_id),crypto_amount=str(item_amount))
            new_wallet.save()

        # return self.portfoliopage(request)
        return redirect("https://investood.onrender.com/portfolio")


    def remove_crypto_wallet(self,request):
        if request.method == 'POST':
            crypto_id = request.POST.get('remove_crypto_wallet')
            if crypto_id:
                found_user = User.objects.get(email=authentication.user_email)
                found_wallet = Wallet.objects.filter(user_id=found_user.user_id)
                if found_wallet:
                    found_wallet = Wallet.objects.get(user_id=found_user.user_id)
                    found_crypto = found_wallet.crypto_id
                    crypto_id_list = found_crypto.split()
                    index = crypto_id_list.index(crypto_id)
                    found_crypto = found_crypto.replace(str(crypto_id),'')
                    found_wallet.crypto_id = found_crypto
                    crypto_amount_list = found_wallet.crypto_amount.split()
                    crypto_amount_list.pop(index)
                    amount = ' '.join(crypto_amount_list)
                    found_wallet.crypto_amount = amount
                    found_wallet.save()
                    print('removed crypto:',crypto_id)

        return redirect("https://investood.onrender.com/portfolio")
