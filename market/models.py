from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('market:product_category_list', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['id']


class Product(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField(max_length=400)
    price = models.FloatField(max_length=20)
    picture = models.ImageField(upload_to="photos/%Y/%m/%d/")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='URL')
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Listing'
        verbose_name_plural = 'Listings'
        ordering = ['-created_at', 'name']

    def get_absolute_url(self):
        return reverse('market:product_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name




