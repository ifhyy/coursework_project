from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name= 'market'
urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
