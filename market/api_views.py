from django.forms import model_to_dict
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *


class MarketViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



