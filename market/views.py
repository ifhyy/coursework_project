from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from .forms import *

from .models import Product, Category
from django.views.generic import ListView, DetailView, CreateView


class ProductListView(ListView):
    model = Product
    template_name = 'market/market_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        context['categories'] = categories
        return context


class ProductDetailView(DetailView):
    model = Product


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'market/register.html'
    success_url = reverse_lazy('market:login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('market:product_list')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'market/login.html'
    success_url = reverse_lazy('market:product_list')

    def get_success_url(self):
        return reverse_lazy('market:product_list')


def logout_user(request):
    logout(request)
    return redirect('market:login')
