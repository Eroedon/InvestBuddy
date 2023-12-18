from django.shortcuts import render,redirect
from pages.models import User, Crypto, Stocks, Portfolio
from pages.getCryptoData import getCrypto
from  pages.getStockData import getStocks
user_email = ''
authenticate = 'false'

def home(request):
    global authenticate, user_email
    return render(request, "pages/home.html", {'authenticate':authenticate,'user_email': user_email})

def getData(request):
    global authenticate, user_email

    getStocks()
    print('stock data is uploaded to database')

    getCrypto()
    print('crypto data is uploaded to database')
    return render(request, "pages/home.html", {'authenticate':authenticate,'user_email': user_email})




# signup page
def user_signup(request):
    global authenticate, user_email
    authenticate = 'false'
    user_email = ''
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
            authenticate = 'false'
            user_email = ''
            return render(request, "pages/signup.html", {'authenticate':authenticate,'user_email': user_email})
        if user_password1 != user_password2:
            print('passwords are not equal')
            authenticate = 'false'
            user_email = ''
            return render(request, "pages/signup.html", {'authenticate':authenticate,'user_email': user_email})
        new_user = User(email=user_email, password=user_password1)
        new_user.save()
        authenticate = 'true'
        print('user saved successfully')
        return render(request, "pages/signup.html", {'authenticate':authenticate,'user_email': user_email})
    return render(request, "pages/signup.html", {'authenticate':authenticate,'user_email': user_email})


# login page
def user_login(request):
    global authenticate, user_email
    authenticate = 'false'
    user_email = ''
    if request.method == 'POST':
        user_email = request.POST.get('user_email')
        user_email = user_email.replace('%40','@')
        print('user_email',user_email)
        user_password = request.POST.get('user_password')
        check_email = User.objects.filter(email=user_email,password=user_password)
        authenticate = 'false'
        if check_email:
            print('userfound')
            authenticate = 'true'
            return render(request, 'pages/home.html', {'authenticate':authenticate ,'user_email': user_email})
        print('usernotfound')
        return render(request, 'pages/login.html', {'authenticate':authenticate,'user_email': user_email})
    return render(request, "pages/login.html", {'authenticate':authenticate,'user_email': user_email})



# logout page
def user_logout(request):
    # logout(request)
    global authenticate, user_email
    authenticate = 'false'
    user_email = ''
    return render(request, 'pages/login.html', {'authenticate':authenticate,'user_email': user_email})

def add_portfolio_stocks(request):
    global authenticate, user_email
    
    if request.method == 'POST':
        stock_id = request.POST.get('stock')
        if authenticate == 'true':
            found_user = User.objects.get(email=user_email)
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

 
    return stocks(request)



def add_portfolio_crypto(request):
    global authenticate, user_email
    
    if request.method == 'POST':
        crypto_id = request.POST.get('crypto')
        if authenticate == 'true':
            found_user = User.objects.get(email=user_email)
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

 
    return crypto(request)

def crypto(request):
    global authenticate, user_email
    crypto_list = Crypto.objects.all()
    cryptolist = [] 
    for crypto in crypto_list:
        crypto_dict = {}
        crypto_dict['crypto_id'] = crypto.crypto_id
        crypto_dict['crypto_name'] = crypto.crypto_name
        crypto_dict['crypto_symbol'] = crypto.crypto_symbol
        crypto_dict['crypto_value'] = crypto.crypto_value
        crypto_dict['crypto_date'] = crypto.crypto_date
        cryptolist.append(crypto_dict)
        
    return render(request, "pages/cryptohome.html", {'authenticate':authenticate,'user_email': user_email,'cryptos':cryptolist})







def stocks(request):
    global authenticate, user_email
    stocks_list = Stocks.objects.all()
    stocklist = [] 
    for stocks in stocks_list:
        stock_dict = {}
        stock_dict['stock_id'] = stocks.stock_id
        stock_dict['stock_name'] = stocks.stock_name
        stock_dict['stock_value'] = stocks.stock_value
        stock_dict['stock_volume'] = stocks.stock_volume
        stock_dict['stock_rate'] = stocks.stock_rate
        stock_dict['stock_date'] = stocks.stock_date
        stocklist.append(stock_dict)

    return render(request, "pages/stockshome.html", {'authenticate':authenticate,'user_email': user_email, 'stocks':stocklist})

def portfolio(request):
    global authenticate, user_email
    if authenticate == 'true':
        found_user = User.objects.get(email=user_email)
        found_portfolio = Portfolio.objects.filter(user_id=found_user.user_id)
        if found_portfolio:
            found_portfolio = Portfolio.objects.get(user_id=found_user.user_id)
            if hasattr(found_portfolio, "stock_id"):
                stock_id_list = found_portfolio.stock_id
                stock_id_list = set(stock_id_list.split())
                stocklist = []
                print('stock_id_list',stock_id_list)
                for stock_id in stock_id_list:
                    found_stock = Stocks.objects.filter(stock_id=stock_id)
                    if found_stock:
                        found_stock = Stocks.objects.get(stock_id=stock_id)
                        stock_dict = {}
                        stock_dict['stock_id'] = found_stock.stock_id
                        stock_dict['stock_name'] = found_stock.stock_name
                        stock_dict['stock_value'] = found_stock.stock_value
                        stock_dict['stock_volume'] = found_stock.stock_volume
                        stock_dict['stock_rate'] = found_stock.stock_rate
                        stock_dict['stock_date'] = found_stock.stock_date
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
                        crypto_dict['crypto_date'] = found_crypto.crypto_date
                        cryptolist.append(crypto_dict)
            
            print('cryptolist',cryptolist)
            print('stocklist',stocklist)

            return render(request, "pages/portfoliohome.html", {'authenticate':authenticate,'user_email': user_email,'stocks':stocklist,'cryptos':cryptolist})
        else:
            return render(request, "pages/portfoliohome.html", {'authenticate':authenticate,'user_email': user_email})
    return render(request, "pages/portfoliohome.html", {'authenticate':authenticate,'user_email': user_email})
