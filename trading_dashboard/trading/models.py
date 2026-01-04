from django.db import models
from django.contrib.auth.models import User


class Asset (models.Model):
    symbol = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    asset_type = models.CharField(max_length=50)

    def __str__(self):
        return self.symbol


class Portfolio(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_value = models.FloatField(default=0)

    def __str__(self):
        return f"{self.user.username} Portfolio"
    
class Trade(models.Model):
    BUY = "BUY"
    SELL = "SELL"

    TRADE_TYPE_CHOICES = [
        (BUY, "Buy"),
        (SELL, "Sell"),
    ]
    portfolio = models.ForeignKey(Portfolio,on_delete=models.CASCADE )
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE )
    trade_type = models.CharField(
        max_length=10, 
        choices=TRADE_TYPE_CHOICES )
    entry_price = models.FloatField()
    exit_price = models.FloatField(null=True, blank=True)
    quantity = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)
