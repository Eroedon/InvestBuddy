from django.urls import path
from pages import views

urlpatterns = [
    path("", views.home, name='home'),
    path('signup/', views.user_signup, name ='signup'),
    path('signin/', views.user_login, name = 'login'),
    path('logout/', views.user_logout, name = 'logout'),
    path("crypto/", views.crypto, name='crypto'),
    path("crypto/addportfolio", views.add_portfolio_crypto, name='add_portfolio_crypto'),
    path("portfolio/", views.portfolio, name='portfolio'),
    path("stocks/addportfolio", views.add_portfolio_stocks, name='add_portfolio_stocks'),
    path("stocks/", views.stocks, name='stocks'),
    path("getData/", views.getData, name='getData'),
]