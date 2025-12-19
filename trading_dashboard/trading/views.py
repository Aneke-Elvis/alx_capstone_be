from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Asset , Portfolio, Trade
from .serializers import AssetSerializer, PortfolioSerializer, TradeSerializer

class AssetListCreateView(generics.ListCreateAPIView):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer

class PortfolioDetailView(generics.RetrieveAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer


class TradeListCreateView(generics.ListCreateAPIView):
    queryset = Trade.objects.all()
    serializer_class = TradeSerializer