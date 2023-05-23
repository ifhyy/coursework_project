from django.urls import path
from . import views

app_name = 'market'
urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),
    path('category/<slug:cat_slug>', views.ProductCategoryView.as_view(), name='product_category_list'),
    path('profile/user/<slug:slug>/<int:pk>/', views.UserProfileView.as_view(), name='user_profile'),
    path('my_listings/', views.OwnerListView.as_view(), name='owner_list'),
    path('product/create/', views.ProductCreateView.as_view(), name='product_create'),
    path('product/<int:id>/<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('product/update/<slug:slug>', views.ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<slug:slug>', views.ProductDeleteView.as_view(), name='product_delete'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    ]
