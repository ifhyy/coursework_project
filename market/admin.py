from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'created_at', 'picture', 'owner', 'is_published')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'content')
    list_editable = ('is_published',)
    list_filter = ('created_at', 'is_published')
    prepopulated_fields = {'slug': ('name', )}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)

