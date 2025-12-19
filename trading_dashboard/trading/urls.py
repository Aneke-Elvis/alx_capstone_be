from django.urls import path
from .views import AssetListCreateView, PortfolioDetailView, TradeListCreateView

urlpatterns = [
    path('assets/', AssetListCreateView.as_view(), name='asset-list'),
    path('portfolio/<int:pk>/', PortfolioDetailView.as_view(), name='portfolio-detail'),
    path('trades/', TradeListCreateView.as_view(), name='trade-list'),
]
