from rest_framework import serializers
from .models import Asset, Portfolio, Trade

class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        models = Asset
        fields = '__all__'

class PortfolioSerializer(serializers.ModelSerializer):
    class meta:
        models = Portfolio
        fields = '__all__'

class TradeSerializer(serializers.ModelSerializer):
    class meta:
        models = Trade
        fields = '__all__'