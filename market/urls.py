from django.urls import path
from . import views

app_name = 'market'
urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),
    path('category/<int:cat_id>', views.ProductCategoryView.as_view(), name='product_category_list'),
    path('my_listings/', views.OwnerListView.as_view(), name='owner_list'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('product/update/<int:pk>', views.ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>', views.ProductDeleteView.as_view(), name='product_delete'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    ]
