from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.urls import reverse
from autoslug import AutoSlugField


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
    picture = models.ImageField(upload_to="photos/%Y/%m/%d/", null=True,
                                default='no-photo-available.png')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                              related_name='products')
    slug = AutoSlugField(populate_from='name', unique=True, editable=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Listing'
        verbose_name_plural = 'Listings'
        ordering = ['-created_at', 'name']
        indexes = [
            models.Index(fields=['-created_at', 'name']),
            models.Index(fields=['id', 'slug'])
        ]

    def get_absolute_url(self):
        return reverse('market:product_detail', kwargs={'id': self.id,
                                                        'slug': self.slug})

    def __str__(self):
        return self.name


def user_absolute_url(self):
    return reverse('market:user_profile', kwargs={'slug': self.username, 'pk': self.pk})


user_model = get_user_model()
user_model.add_to_class('get_absolute_url', user_absolute_url)
user_model.add_to_class('image', models.ImageField(upload_to='users/%Y/%m/%d/', null=True,
                                                   default='istockphoto-1337144146-612x612.jpg'))


