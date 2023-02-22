from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from django.views.generic import ListView, DetailView


class ProductListView(ListView):
    model = Product
    template_name = 'market/market_list.html'


class ProductDetailView(DetailView):
    model = Product

