from django.utils.text import slugify

from market.models import Product, Category
from django.contrib.auth.models import User
from .test_settings import Settings


class ProductModelTest(Settings):

    def test_product_name(self):
        name_label = self.product._meta.get_field('name').verbose_name
        self.assertEqual(name_label, 'name')
        self.assertEqual(self.product.name, 'Car')
        self.assertEqual(self.product._meta.get_field('name').max_length, 100)

    def test_product_text(self):
        text_label = self.product._meta.get_field('text').verbose_name
        self.assertEqual(text_label, 'text')
        self.assertEqual(self.product.text, 'some text')
        self.assertEqual(self.product._meta.get_field('text').max_length, 400)

    def test_product_price(self):
        price_label = self.product._meta.get_field('price').verbose_name
        self.assertEqual(price_label, 'price')
        self.assertEqual(self.product.price, 14.52)
        self.assertEqual(self.product._meta.get_field('price').max_length, 20)

    def test_product_picture(self):
        picture_label = self.product._meta.get_field('picture').verbose_name
        self.assertEqual(picture_label, 'picture')
        self.assertTrue('media/' in self.product.picture.url)

    def test_product_owner(self):
        self.assertEqual(self.owner.id, self.product.owner_id)
        self.assertEqual(self.owner, self.product.owner)
        self.assertEqual(self.product._meta.get_field('owner').related_model, User)

    def test_product_slug(self):
        field = self.product._meta.get_field('slug')
        self.assertEqual(field.populate_from, 'name')
        self.assertEqual(self.product.slug, slugify(self.product.name))

    def test_product_category(self):
        self.assertEqual(self.category.id, self.product.category_id)
        self.assertEqual(self.category, self.product.category)
        self.assertEqual(self.product._meta.get_field('category').related_model, Category)

    def test_product_other(self):
        self.assertTrue(self.product.is_published)
        self.assertTrue(self.product.created_at)
        self.assertTrue(self.product.updated_at)

    def test_product_meta(self):
        meta = self.product._meta
        self.assertEqual(meta.verbose_name, 'Listing')
        self.assertEqual(meta.verbose_name_plural, 'Listings')
        self.assertEqual(meta.ordering, ['-created_at', 'name'])

    def test_product_get_absolute_url(self):
        self.assertURLEqual(self.product.get_absolute_url(), '/product/3/car/')


class CategoryModelTest(Settings):

    def test_category_title(self):
        title = self.category._meta.get_field('title')
        self.assertEqual(title.verbose_name, 'title')
        self.assertEqual(title.max_length, 100)
        self.assertEqual(self.category.title, 'electronics')

    def test_category_slug(self):
        slug = self.category._meta.get_field('slug')
        self.assertEqual(slug.verbose_name, 'URL')
        self.assertEqual(slug.max_length, 100)
        self.assertEqual(self.category.slug, slugify(self.category.title))

    def test_category_str_(self):
        self.assertEqual(str(self.category), self.category.title)

    def test_category_get_absolute_url(self):
        self.assertURLEqual(self.category.get_absolute_url(), '/category/electronics')

    def test_category_meta(self):
        meta = self.category._meta
        self.assertEqual(meta.verbose_name, 'Category')
        self.assertEqual(meta.verbose_name_plural, 'Categories')
        self.assertEqual(meta.ordering, ['id'])


class UserModelTest(Settings):
    def test_get_absolute_url(self):
        self.assertURLEqual(self.owner.get_absolute_url(), '/profile/user/stupk/4/')

    def test_user_image(self):
        image = self.owner._meta.get_field('image')
        self.assertEqual(image.verbose_name, 'image')
        self.assertTrue('media/' in self.owner.image.url)

