from django.db import models
from django.conf import settings


class Product(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField(max_length=400)
    price = models.FloatField(max_length=20)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
