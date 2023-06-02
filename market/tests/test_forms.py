from django.urls import reverse

from .test_settings import Settings
from market.models import Product


class MarketFormTest(Settings):

    def test_valid_product_form(self):
        product_count = Product.objects.count()
        self.assertEqual(product_count, 1)
        form_data = {
            'name': 'ball',
            'text': 'a ball for basketball game',
            'price': 14,
            'category': self.category,
        }
        response = self.client.post(reverse('market:product_create'),
                                    data=form_data, follow=True)

        # We can't create new objects without being logged in
        self.assertEqual(response.status_code, 404)

        self.client.login(username=self.login, password=self.password)
        response = self.client.post(reverse('market:product_create'),
                                    data=form_data, follow=True)
        print(response)
        print(Product.objects.all())
        product_count = Product.objects.count()
        self.assertEqual(product_count, 2)

