from django.contrib.auth import logout, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from .forms import *

from .models import Product, Category
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class ProductListView(ListView):
    paginate_by = 6
    model = Product
    template_name = 'market/market_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        context['categories'] = categories
        context['cat_selected'] = 0
        return context

    def get_queryset(self):
        return Product.objects.filter(is_published=True)


class ProductCategoryView(ListView):
    paginate_by = 3
    model = Product
    template_name = 'market/market_list.html'

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['cat_slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        context['categories'] = categories
        context['cat_selected'] = self.kwargs['cat_slug']
        return context


class OwnerListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'market/owner_list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(owner=self.request.user)


class ProductDetailView(DetailView):
    model = Product

    def get_queryset(self):
        return Product.objects.all().select_related('owner', 'category')


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'market/product_form.html'

    def form_valid(self, form):
        f = form.save(commit=False)
        f.owner = self.request.user
        f.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'market/product_form.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(owner=self.request.user)


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('market:product_list')

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(owner=self.request.user)


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
