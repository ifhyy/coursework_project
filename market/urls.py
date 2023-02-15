from django.urls import path
from . import views


app_name= 'market'
urlpatterns = [
    path('', views.MarketListView.as_view(), name='market_list'),
    ]