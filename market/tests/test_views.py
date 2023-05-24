from django.urls import reverse

from .test_settings import Settings
from market.models import Product


class MarketViewTest(Settings):
    def test_product_list_view(self):
        response = self.client.get(reverse('market:product_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'market/market_list.html')
        self.assertQuerysetEqual(response.context.get('product_list'), Product.objects.all())
        # print(response.context.get('form'))
        # print(response.context.get('product_list'))
        # print(dir(response))

    def test_product_category_list(self):
        response = self.client.get(reverse('market:product_category_list',
                                           args=['electronics']))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context.get('product_list'),
                                 Product.objects.filter(category=self.category))
        self.assertTemplateUsed(response, 'market/market_list.html')

    def test_owner_list_view(self):
        # before logging in
        response = self.client.get(reverse('market:owner_list'))
        self.assertNotEqual(response.status_code, 200)
        # after
        self.client.login(username=self.login, password=self.password)
        response = self.client.get(reverse('market:owner_list'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context.get('product_list'),
                                 Product.objects.filter(owner=self.owner))
        self.assertTemplateUsed(response, 'market/owner_list.html')

    def test_user_profile_view(self):
        # before logging in
        response = self.client.get(reverse('market:user_profile',
                                           kwargs={'slug': self.owner.username,
                                                   'pk': self.owner.pk}))
        self.assertEqual(response.status_code, 404)
        # after logging in
        self.client.login(username=self.login, password=self.password)
        response = self.client.get(reverse('market:user_profile',
                                           kwargs={'slug': self.owner.username,
                                                   'pk': self.owner.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context.get('user'), self.owner)
        self.assertTemplateUsed(response, 'market/profile.html')

    def test_product_create_view(self):
        # not logged in
        response = self.client.get(reverse('market:product_create'))
        self.assertNotEqual(response.status_code, 200)
        response = self.client.post(reverse('market:product_create'))
        self.assertNotEqual(response.status_code, 200)

        # logged in
        self.client.login(username=self.login, password=self.password)
        response = self.client.get(reverse('market:product_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'market/product_form.html')
        response = self.client.post(reverse('market:product_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'market/product_form.html')

    def test_product_detail_view(self):
        response = self.client.get(reverse('market:product_detail',
                                           kwargs={'slug': self.product.slug,
                                                   'id': self.product.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'market/product_detail.html')
        self.assertEqual(response.context.get('product'), self.product)

    def test_product_update_view(self):
        def get():
            return self.client.get(reverse('market:product_update',
                                           kwargs={'slug': self.product.slug}))

        def post():
            return self.client.post(reverse('market:product_update',
                                            kwargs={'slug': self.product.slug}))

        # not logged in
        response = get()
        self.assertNotEqual(response.status_code, 200)
        response = post()
        self.assertNotEqual(response.status_code, 200)

        # logged in but has no permission
        self.client.login(username=self.login2, password=self.password)
        response = get()
        self.assertNotEqual(response.status_code, 200)
        response = post()
        self.assertNotEqual(response.status_code, 200)

        # logged in & being owner
        self.client.login(username=self.login, password=self.password)
        response = get()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context.get('product'), self.product)
        self.assertTemplateUsed(response, 'market/product_form.html')
        response = post()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context.get('product'), self.product)
        self.assertTemplateUsed(response, 'market/product_form.html')

    def test_product_delete(self):
        def get():
            return self.client.get(reverse('market:product_delete',
                                           kwargs={'slug': self.product.slug}))

        def post():
            return self.client.post(reverse('market:product_delete',
                                            kwargs={'slug': self.product.slug}))

        # not logged in
        response = get()
        self.assertNotEqual(response.status_code, 200)
        response = post()
        self.assertNotEqual(response.status_code, 200)

        # logged in but has no permission
        self.client.login(username=self.login2, password=self.password)
        response = get()
        self.assertNotEqual(response.status_code, 200)
        response = post()
        self.assertNotEqual(response.status_code, 200)

        # logged in & being owner
        self.client.login(username=self.login, password=self.password)
        response = get()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context.get('product'), self.product)
        self.assertTemplateUsed(response, 'market/product_confirm_delete.html')
        response = post()
        self.assertEqual(response.status_code, 302)
        self.assertFalse(response.context)
        self.assertRedirects(response, reverse('market:product_list'))
