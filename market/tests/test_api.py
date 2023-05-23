from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from django.contrib.auth.models import User
from market.models import Product, Category
from market.serializers import ProductSerializer


class MarketApiTestCase(APITestCase):
    def test_get(self):
        category = Category.objects.create(title='food', slug='food')
        user = User.objects.create_user('stupk')
        product_1 = Product.objects.create(name='Test Product 1', text='Test text', price=24.5,
                                           slug='slug1', category=category, owner=user
                                           )
        url = reverse('product-list')
        response = self.client.get(url)
        serializer_data = ProductSerializer(product_1).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)

