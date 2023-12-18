from django.db import models
from django.core.validators import MinLengthValidator


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField()
    password = models.TextField(validators=[MinLengthValidator(8, 'the field must contain at least 50 characters')],max_length=12)

class Crypto(models.Model):
    crypto_id = models.IntegerField(primary_key=True)
    crypto_name = models.TextField(max_length=100)
    crypto_symbol = models.TextField(max_length=100)
    crypto_value = models.FloatField()
    crypto_date = models.TextField()

class Portfolio(models.Model):
    portfolio_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    crypto_id = models.TextField()
    stock_id = models.TextField()

class Stocks(models.Model):
    stock_id = models.AutoField(primary_key=True)
    stock_name = models.TextField(max_length=100)
    stock_value = models.TextField(max_length=100)
    stock_volume = models.TextField(max_length=100)
    stock_rate = models.TextField(max_length=100)
    stock_date = models.DateField()
