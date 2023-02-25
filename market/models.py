from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.urls import reverse


class Product(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField(max_length=400)
    price = models.FloatField(max_length=20)
    picture = models.ImageField(upload_to="photos/%Y/%m/%d/")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('market:product_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class Category(models.Model):
    title = models.CharField(max_length=100)
    product = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Categories'

