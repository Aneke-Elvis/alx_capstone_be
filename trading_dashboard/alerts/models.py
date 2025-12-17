from django.db import models
from django.contrib.auth.models import User
from trading.models import Asset

class Alert(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    target_price = models.FloatField()
    condition = models.CharField(max_length=10)
    is_triggered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

