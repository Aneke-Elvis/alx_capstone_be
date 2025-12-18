from django.shortcuts import render

# Create your views here.
from .models import Asset , Portforlio, Trade
from .serializers import AssetSerializer, PortforlioSerializer, TradeSerializer

class AssetListCreateView(generics.ListCreateAPIView):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer

class PortfolioListCreateView(generics.ListCreateAPIView):
    queryset = Portforlio.objects.all()
    serializer_class = PortforlioSerializer


class TradeListCreateView(generics.ListCreateAPIView):
    queryset = Trade.objects.all()
    serializer_class = TradeSerializer