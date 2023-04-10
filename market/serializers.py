from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from .models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

